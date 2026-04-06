from __future__ import annotations

import sys
from pathlib import Path


LABELS = {
    "cmd": ("CMD / Terminal", "text"),
    "bash": ("Bash / Terminal", "text"),
    "sh": ("Bash / Terminal", "text"),
    "powershell": ("PowerShell", "text"),
    "r": ("R", "r"),
    "yaml": ("YAML", "yaml"),
    "gitignore": (".gitignore", "gitignore"),
}


def prepare_markdown(source: str) -> str:
    lines = source.splitlines()
    output: list[str] = []
    in_fence = False
    current_lang = ""

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("```"):
            if not in_fence:
                current_lang = stripped[3:].strip().lower()
                label_info = LABELS.get(current_lang)
                if label_info:
                    label, render_lang = label_info
                    output.append(f'<div class="code-caption">{label}</div>')
                    output.append("")
                    output.append(f"```{render_lang}")
                else:
                    output.append(line)
                in_fence = True
            else:
                output.append("```")
                in_fence = False
                current_lang = ""
            continue

        output.append(line)

    return "\n".join(output) + "\n"


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python prepare_markdown_for_pdf.py input.md output.md")
        return 1

    input_path = Path(sys.argv[1]).resolve()
    output_path = Path(sys.argv[2]).resolve()

    if not input_path.exists():
        print(f"Markdown tidak ditemukan: {input_path}")
        return 1

    prepared = prepare_markdown(input_path.read_text(encoding="utf-8"))
    output_path.write_text(prepared, encoding="utf-8", newline="\n")
    print(f"Prepared markdown: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
