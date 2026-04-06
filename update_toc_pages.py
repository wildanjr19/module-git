from __future__ import annotations

import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path

from pypdf import PdfReader

AUTO_TOC_START = "<!-- AUTO-TOC:START -->"
AUTO_TOC_END = "<!-- AUTO-TOC:END -->"


@dataclass
class Section:
    number: str
    title: str
    anchor: str
    page: int | None = None


def slugify_heading(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    normalized = normalized.lower()
    normalized = normalized.replace("&", " dan ")
    normalized = re.sub(r"[`'\".:/(),?]", "", normalized)
    normalized = re.sub(r"[^a-z0-9\s-]", "", normalized)
    normalized = re.sub(r"\s+", "-", normalized)
    normalized = re.sub(r"-{2,}", "-", normalized)
    return normalized.strip("-")


def parse_sections(markdown_text: str) -> list[Section]:
    sections: list[Section] = []
    in_fence = False

    for raw_line in markdown_text.splitlines():
        stripped = raw_line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue

        if in_fence:
            continue

        match = re.match(r"^##\s+(\d+)\.\s+(.+?)\s*$", raw_line)
        if not match:
            continue

        number, title = match.groups()
        full_heading = f"{number}. {title}"
        sections.append(Section(number=number, title=title, anchor=slugify_heading(full_heading)))

    return sections


def extract_page_map(pdf_path: Path) -> dict[str, int]:
    reader = PdfReader(str(pdf_path))
    page_map: dict[str, int] = {}

    for name, destination in reader.named_destinations.items():
        page_map[str(name).lstrip("/")] = reader.get_destination_page_number(destination) + 1

    return page_map


def render_toc_plain(sections: list[Section]) -> str:
    rows = [AUTO_TOC_START]

    for section in sections:
        page_text = f" (hal. {section.page})" if section.page is not None else ""
        rows.append(f"[{section.title}](#{section.anchor}){page_text}  ")

    rows.append(AUTO_TOC_END)
    return "\n".join(rows)


def replace_toc_block(markdown_text: str, toc_block: str) -> str:
    if AUTO_TOC_START in markdown_text and AUTO_TOC_END in markdown_text:
        pattern = re.compile(
            rf"{re.escape(AUTO_TOC_START)}.*?{re.escape(AUTO_TOC_END)}",
            re.DOTALL,
        )
        return pattern.sub(toc_block, markdown_text, count=1)

    pattern = re.compile(r"(## Daftar Isi\s*\n)(.*?)(\n---\s*\n)", re.DOTALL)
    replacement = rf"\1\n{toc_block}\n\3"
    new_text, replacements = pattern.subn(replacement, markdown_text, count=1)

    if replacements == 0:
        raise ValueError("Bagian 'Daftar Isi' tidak ditemukan untuk diperbarui.")

    return new_text


def sync_toc(markdown_path: Path, pdf_path: Path) -> bool:
    markdown_text = markdown_path.read_text(encoding="utf-8")
    sections = parse_sections(markdown_text)
    page_map = extract_page_map(pdf_path)

    for section in sections:
        section.page = page_map.get(section.anchor)

    toc_block = render_toc_plain(sections)
    new_markdown_text = replace_toc_block(markdown_text, toc_block)
    changed = new_markdown_text != markdown_text

    if changed:
        markdown_path.write_text(new_markdown_text, encoding="utf-8", newline="\n")

    return changed


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python update_toc_pages.py path/to/file.md path/to/file.pdf")
        return 1

    markdown_path = Path(sys.argv[1]).resolve()
    pdf_path = Path(sys.argv[2]).resolve()

    if not markdown_path.exists():
        print(f"Markdown tidak ditemukan: {markdown_path}")
        return 1

    if not pdf_path.exists():
        print(f"PDF tidak ditemukan: {pdf_path}")
        return 1

    changed = sync_toc(markdown_path, pdf_path)
    print(f"CHANGED={1 if changed else 0}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
