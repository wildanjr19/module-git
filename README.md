# Build PDF Modul Git

Folder ini berisi modul Git berbasis Markdown yang diekspor ke PDF dengan daftar isi klikable, nomor halaman otomatis, dan styling yang lebih rapi untuk blok command.

## File Penting

- `draft_Module_Git.md`
  Sumber utama modul yang kamu edit.
- `export-pdf.ps1`
  Perintah utama untuk membangun ulang PDF.
- `md-to-pdf.config.js`
  Konfigurasi `md-to-pdf`, termasuk footer nomor halaman.
- `pdf-style.css`
  Styling PDF, termasuk tampilan daftar isi dan label kecil untuk blok command seperti `CMD`, `Bash`, `R`, dan `YAML`.
- `prepare_markdown_for_pdf.py`
  Menyiapkan versi markdown khusus untuk PDF, termasuk caption kecil di atas blok command agar command lebih mudah dibaca dan disalin.
- `update_toc_pages.py`
  Menyinkronkan nomor halaman daftar isi berdasarkan hasil PDF terbaru.
- `fix_pdf_links.py`
  Memperbaiki link internal PDF dan menambahkan bookmark/sidebar outline.

## Cara Build

Jalankan dari folder ini:

```powershell
powershell -ExecutionPolicy Bypass -File .\export-pdf.ps1
```

Kalau file input berbeda, gunakan:

```powershell
powershell -ExecutionPolicy Bypass -File .\export-pdf.ps1 -InputFile "nama_file.md"
```

## Yang Dilakukan Script Build

1. Render Markdown ke PDF dengan `md-to-pdf`.
2. Siapkan versi markdown sementara khusus PDF.
3. Baca posisi halaman tiap bab dari PDF hasil render.
4. Perbarui bagian `Daftar Isi` di markdown secara otomatis.
5. Render ulang sampai nomor halaman daftar isi stabil.
6. Perbaiki link internal PDF agar lebih kompatibel di viewer PDF.
7. Tambahkan bookmark PDF untuk heading utama.

## Kebutuhan

- PowerShell
- Node.js dan `npx`
- Python 3
- Paket Python `pypdf`

## Catatan

- Bagian `Daftar Isi` di `draft_Module_Git.md` memakai marker `<!-- AUTO-TOC:START -->` dan `<!-- AUTO-TOC:END -->`. Jangan hapus marker ini kalau ingin sinkronisasi nomor halaman tetap otomatis.
- File sementara build akan dibersihkan otomatis, sehingga hasil akhirnya cukup satu file PDF utama.
