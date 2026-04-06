from __future__ import annotations

import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import ArrayObject, DictionaryObject, NameObject

from update_toc_pages import extract_page_map, parse_sections


def rewrite_named_dest_links(pdf_path: Path, markdown_path: Path | None = None) -> tuple[int, int]:
    reader = PdfReader(str(pdf_path))
    writer = PdfWriter()
    writer.clone_document_from_reader(reader)

    page_map = extract_page_map(pdf_path)
    named_dest_page_index: dict[str, int] = {}
    for name, destination in reader.named_destinations.items():
        named_dest_page_index[str(name)] = reader.get_destination_page_number(destination)

    updated = 0

    for page in writer.pages:
        annots = page.get("/Annots")
        if not annots:
            continue

        for annot_ref in annots:
            annot = annot_ref.get_object()
            dest_name = annot.get("/Dest")

            if not isinstance(dest_name, NameObject):
                continue

            page_index = named_dest_page_index.get(str(dest_name))
            if page_index is None or page_index < 0 or page_index >= len(writer.pages):
                continue

            # Rebuild destination using page refs owned by the writer output.
            # Keep the original view mode / coordinates (e.g. /XYZ) so clicks
            # land near the section heading instead of forcing full-page fit.
            target_page_ref = writer.pages[page_index].indirect_reference
            if target_page_ref is None:
                continue

            destination = reader.named_destinations.get(str(dest_name))
            if destination and len(destination.dest_array) > 1:
                trailing = list(destination.dest_array[1:])
            else:
                trailing = [NameObject("/Fit")]

            dest_array = ArrayObject([target_page_ref, *trailing])
            annot[NameObject("/A")] = DictionaryObject(
                {
                    NameObject("/S"): NameObject("/GoTo"),
                    NameObject("/D"): dest_array,
                }
            )
            if "/Dest" in annot:
                del annot[NameObject("/Dest")]

            updated += 1

    outline_count = 0
    if markdown_path and markdown_path.exists():
        sections = parse_sections(markdown_path.read_text(encoding="utf-8"))
        for section in sections:
            page_number = page_map.get(section.anchor)
            if page_number is None:
                continue
            writer.add_outline_item(
                title=f"{section.number}. {section.title}",
                page_number=page_number - 1,
                bold=True,
            )
            outline_count += 1

    temp_output_path = pdf_path.with_name(f"{pdf_path.stem}.tmp.pdf")
    legacy_backup_path = pdf_path.with_suffix(".prelinkfix.pdf")

    try:
        with temp_output_path.open("wb") as handle:
            writer.write(handle)

        temp_output_path.replace(pdf_path)
    finally:
        if temp_output_path.exists():
            temp_output_path.unlink()
        if legacy_backup_path.exists():
            legacy_backup_path.unlink()

    return updated, outline_count


def main() -> int:
    if len(sys.argv) not in (2, 3):
        print("Usage: python fix_pdf_links.py path/to/file.pdf [path/to/file.md]")
        return 1

    pdf_path = Path(sys.argv[1]).resolve()
    markdown_path = Path(sys.argv[2]).resolve() if len(sys.argv) == 3 else None
    if not pdf_path.exists():
        print(f"PDF tidak ditemukan: {pdf_path}")
        return 1

    updated, outline_count = rewrite_named_dest_links(pdf_path, markdown_path)
    print(f"Link internal yang diperbarui: {updated}")
    print(f"Bookmark PDF yang ditambahkan: {outline_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
