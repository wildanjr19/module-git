# 🗂️ Modul Git Version Control
### Dari Nol Sampai Mahir

> **Target Pembaca:** Pemula hingga menengah yang ingin menguasai Git dan GitHub untuk proyek individu maupun tim.

---

## 📋 Daftar Isi

1. [Apa Itu Version Control?](#1-apa-itu-version-control)
2. [Mengenal Git](#2-mengenal-git)
3. [Membuat Akun GitHub](#3-membuat-akun-github)
4. [GitHub Student Developer Pack](#4-github-student-developer-pack)
5. [Instalasi Git](#5-instalasi-git)
6. [Konfigurasi Awal Git](#6-konfigurasi-awal-git)
7. [Konsep Dasar Git](#7-konsep-dasar-git)
8. [Perintah Git Dasar](#8-perintah-git-dasar)
9. [Bekerja dengan Remote Repository](#9-bekerja-dengan-remote-repository)
10. [Branching dan Merging](#10-branching-dan-merging)
11. [Menyelesaikan Konflik (Merge Conflict)](#11-menyelesaikan-konflik-merge-conflict)
12. [Stash — Menyimpan Pekerjaan Sementara](#12-stash--menyimpan-pekerjaan-sementara)
13. [Melihat Riwayat dan Membatalkan Perubahan](#13-melihat-riwayat-dan-membatalkan-perubahan)
14. [Tagging dan Versioning](#14-tagging-dan-versioning)
15. [Git Workflow untuk Tim](#15-git-workflow-untuk-tim)
16. [Pull Request dan Code Review](#16-pull-request-dan-code-review)
17. [GitHub Actions — CI/CD Dasar](#17-github-actions--cicd-dasar)
18. [Tips, Trik, dan Best Practice](#18-tips-trik-dan-best-practice)
19. [Referensi dan Sumber Belajar Lanjutan](#19-referensi-dan-sumber-belajar-lanjutan)
20. [Deployment dengan GitHub Pages](#20-deployment-dengan-github-pages)

---

## 1. Apa Itu Version Control?

### Pengertian

**Version Control System (VCS)** adalah sistem yang merekam setiap perubahan pada file atau sekumpulan file dari waktu ke waktu, sehingga kamu bisa kembali ke versi tertentu kapan pun kamu mau.

Bayangkan kamu menulis skripsi dan menyimpan file seperti ini:

```
skripsi_v1.docx
skripsi_v2_final.docx
skripsi_v2_final_REVISI.docx
skripsi_v2_final_REVISI_beneran.docx
```

Inilah masalah yang dipecahkan oleh version control — kamu cukup punya **satu file**, dan sistemnya yang melacak semua perubahan.

### Kegunaan Version Control

| Kegunaan | Penjelasan |
|---|---|
| **Pelacakan Perubahan** | Tahu siapa mengubah apa, kapan, dan kenapa |
| **Pemulihan** | Kembalikan file ke versi sebelumnya jika ada kesalahan |
| **Kolaborasi** | Banyak orang bisa bekerja pada proyek yang sama secara bersamaan |
| **Branching** | Uji coba fitur baru tanpa merusak kode utama |
| **Audit Trail** | Riwayat lengkap seluruh perubahan proyek |

### Jenis-Jenis VCS

- **Local VCS** — Riwayat disimpan di komputer lokal saja (RCS)
- **Centralized VCS** — Satu server pusat, semua klien terhubung ke sana (SVN, CVS)
- **Distributed VCS** — Setiap klien punya salinan penuh repository (Git, Mercurial) ✅

---

## 2. Mengenal Git

### Apa Itu Git?

**Git** adalah sistem version control terdistribusi (*Distributed Version Control System*) yang paling populer di dunia. Git dibuat oleh **Linus Torvalds** pada tahun 2005 untuk mengelola pengembangan kernel Linux.

### Mengapa Git?

- ⚡ **Cepat** — Sebagian besar operasi berjalan secara lokal
- 🔒 **Aman** — Setiap data di-hash menggunakan SHA-1
- 🌿 **Branching yang mudah** — Membuat dan menggabungkan branch sangat ringan
- 🌍 **Terdistribusi** — Setiap developer punya salinan penuh repository
- 🆓 **Gratis dan Open Source**

### Git vs GitHub

> ⚠️ **Git ≠ GitHub!** Ini perbedaan yang sering membingungkan pemula.

| | **Git** | **GitHub** |
|---|---|---|
| **Apa** | Software version control | Platform hosting repository |
| **Di mana** | Berjalan di komputermu | Layanan cloud (website) |
| **Fungsi** | Melacak perubahan kode | Menyimpan & berkolaborasi online |
| **Alternatif** | Mercurial, SVN | GitLab, Bitbucket |

Analoginya: **Git** = Microsoft Word, **GitHub** = Google Drive.

---

## 3. Membuat Akun GitHub

### Langkah-Langkah

1. Buka **[github.com](https://github.com)** di browser
2. Klik **"Sign up"** di pojok kanan atas
3. Masukkan **email** kamu
4. Buat **password** yang kuat
5. Pilih **username** — ini akan menjadi identitasmu di GitHub (pilih yang profesional, misal: `namaKamu-dev`)
6. Selesaikan verifikasi dan klik **"Create account"**
7. Pilih plan **Free** (sudah lebih dari cukup untuk pemula)
8. Verifikasi email yang dikirim ke inbox kamu

### Tips Memilih Username GitHub

- Gunakan nama asli atau nama profesional
- Hindari angka atau karakter acak
- Konsisten dengan platform lain (LinkedIn, dll)
- Contoh bagus: `budi-santoso`, `budidev`, `budisantoso`

### Personalisasi Profil

Setelah akun dibuat, lengkapi profilmu:
- **Avatar** — Foto profesional atau avatar yang konsisten
- **Bio** — Deskripsi singkat (misal: "Statistics Student | Data Science Enthusiast")
- **Location** — Kota/negara
- **Website** — Link portfolio jika ada
- **README Profile** — File khusus yang tampil di halaman profil GitHub-mu

---

## 4. GitHub Student Developer Pack

### Apa Itu GitHub Student Developer Pack?

**GitHub Student Developer Pack** adalah program dari GitHub yang memberikan **akses gratis** ke berbagai tool dan layanan berbayar khusus untuk pelajar/mahasiswa aktif. Nilainya bisa mencapai ribuan dolar!

### Cara Mendaftar

1. Buka **[education.github.com/pack](https://education.github.com/pack)**
2. Klik **"Get student benefits"**
3. Login dengan akun GitHub kamu
4. Pilih **"Student"**
5. Masukkan **email institusi** kamu (misal: `nama@student.uns.ac.id`)
6. Upload **bukti status mahasiswa** (KTM, surat keterangan, atau transkrip)
7. Tunggu verifikasi (biasanya 1–7 hari kerja)

> 💡 **Tips:** Gunakan email kampus jika ada. Jika tidak, upload foto KTM yang jelas.

### Benefit Unggulan

| Tool | Benefit | Nilai |
|---|---|---|
| **GitHub Pro** | Repository private tak terbatas, fitur advanced | Gratis selama kuliah |
| **GitHub Copilot** | AI coding assistant | Gratis selama kuliah |
| **JetBrains IDEs** | PyCharm, IntelliJ, dll | Gratis 1 tahun (renewable) |
| **Namecheap** | Domain `.me` gratis 1 tahun + SSL | ~$13/tahun |
| **Microsoft Azure** | $100 Azure credits | $100 |
| **DigitalOcean** | Cloud server credits | $200 |
| **Canva Pro** | Design tool premium | Gratis |
| **DataCamp** | Kursus data science | Gratis 3 bulan |
| **MongoDB Atlas** | Cloud database | Credits gratis |

---

## 5. Instalasi Git

### Windows

**Cara 1: Download Installer (Direkomendasikan)**

1. Buka **[git-scm.com/download/win](https://git-scm.com/download/win)**
2. Download installer terbaru (64-bit)
3. Jalankan installer dan ikuti wizard:
   - Biarkan semua pengaturan default
   - Pada bagian **"Adjusting your PATH environment"**, pilih **"Git from the command line and also from 3rd-party software"**
   - Pada bagian **"Choosing the default behavior of `git pull`"**, pilih **"Fast-forward or merge"**
4. Klik **Install** lalu **Finish**

**Cara 2: Via winget (Windows Package Manager)**

```cmd
winget install --id Git.Git -e --source winget
```

### Verifikasi Instalasi

Buka **Command Prompt (CMD)** dan jalankan:

```cmd
git --version
```

Output yang diharapkan:

```
git version 2.47.0.windows.1
```

---

## 6. Konfigurasi Awal Git

Sebelum mulai bekerja, kita perlu mengatur identitas di Git. Informasi ini akan muncul di setiap commit yang kamu buat.

### Mengatur Nama dan Email

```cmd
git config --global user.name "Nama Kamu"
git config --global user.email "email@kamu.com"
```

> Gunakan email yang sama dengan akun GitHub-mu.

### Mengatur Default Branch Name

```cmd
git config --global init.defaultBranch main
```

### Mengatur Editor Teks Default (Opsional)

```cmd
:: Menggunakan Notepad (bawaan Windows)
git config --global core.editor notepad

:: Menggunakan VS Code
git config --global core.editor "code --wait"
```

### Mengatur Line Ending (Penting untuk Windows!)

```cmd
git config --global core.autocrlf true
```

> Ini mencegah masalah perbedaan format baris antara Windows dan Linux/Mac.

### Melihat Semua Konfigurasi

```cmd
git config --list
```

### File Konfigurasi

Konfigurasi global tersimpan di `C:\Users\NamaUser\.gitconfig`. Kamu bisa membukanya dengan:

```cmd
notepad C:\Users\%USERNAME%\.gitconfig
```

---

## 7. Konsep Dasar Git

### Tiga Area Kerja Git

```
┌─────────────────────────────────────────────────────────┐
│                    WORKING DIRECTORY                    │
│         (File yang sedang kamu edit sekarang)           │
└──────────────────────┬──────────────────────────────────┘
                       │  git add
                       ▼
┌─────────────────────────────────────────────────────────┐
│                    STAGING AREA (INDEX)                 │
│       (File yang sudah siap untuk di-commit)            │
└──────────────────────┬──────────────────────────────────┘
                       │  git commit
                       ▼
┌─────────────────────────────────────────────────────────┐
│                    REPOSITORY (.git)                    │
│         (Riwayat commit yang sudah tersimpan)           │
└─────────────────────────────────────────────────────────┘
```

| Area | Penjelasan |
|---|---|
| **Working Directory** | Folder proyekmu — tempat kamu membuat dan mengedit file |
| **Staging Area** | "Antrian commit" — file yang sudah dipilih untuk disimpan |
| **Repository** | Database Git — semua riwayat perubahan tersimpan di sini |

### Status File dalam Git

```
Untracked → Tracked (Staged) → Committed → Modified → Staged → Committed
```

- **Untracked** — File baru yang belum dikenal Git
- **Staged** — File sudah ditambahkan ke staging area
- **Committed** — File sudah tersimpan di repository
- **Modified** — File yang sudah di-commit tapi ada perubahan baru

### Apa Itu Commit?

**Commit** adalah snapshot (foto) dari seluruh proyekmu pada suatu titik waktu. Setiap commit memiliki:
- **Hash unik** (misal: `a3f2c1d`) — pengenal commit
- **Pesan** — deskripsi apa yang berubah
- **Timestamp** — kapan commit dibuat
- **Author** — siapa yang membuat commit
- **Parent** — pointer ke commit sebelumnya

---

## 8. Perintah Git Dasar

### Membuat Repository Baru

```cmd
:: Buat folder proyek baru
mkdir nama-proyek
cd nama-proyek

:: Inisialisasi Git repository
git init
```

Output:
```
Initialized empty Git repository in C:/Users/kamu/nama-proyek/.git/
```

### Melihat Status Repository

```cmd
git status
```

### Menambahkan File ke Staging Area

```cmd
:: Tambahkan file tertentu
git add nama-file.txt

:: Tambahkan semua file di folder saat ini
git add .

:: Tambahkan semua file dengan ekstensi tertentu
git add *.py
```

### Membuat Commit

```cmd
:: Commit dengan pesan singkat
git commit -m "Pesan commit yang deskriptif"

:: Contoh pesan commit yang baik
git commit -m "Add login feature with email validation"
git commit -m "Fix bug: null pointer exception on user profile"
git commit -m "Update README with installation instructions"
```

> 💡 **Tips Pesan Commit:** Gunakan present tense dalam bahasa Inggris. Jelaskan **apa** yang berubah, bukan **bagaimana**.

### Shortcut: Add + Commit Sekaligus

```cmd
:: Hanya untuk file yang sudah pernah di-track sebelumnya
git commit -am "Pesan commit"
```

### Melihat Log Commit

```cmd
:: Log lengkap
git log

:: Log ringkas (satu baris per commit)
git log --oneline

:: Log dengan grafik branch
git log --oneline --graph --all

:: Log N commit terakhir
git log --oneline -5
```

### Contoh Alur Kerja Lengkap

```cmd
:: 1. Masuk ke folder proyek
cd C:\Users\kamu\proyek-saya

:: 2. Inisialisasi Git
git init

:: 3. Buat file baru (contoh)
echo. > README.md
notepad README.md

:: 4. Cek status
git status

:: 5. Tambahkan ke staging
git add README.md

:: 6. Commit
git commit -m "Initial commit: add README"

:: 7. Cek log
git log --oneline
```

---

## 9. Bekerja dengan Remote Repository

### Apa Itu Remote?

**Remote** adalah versi repository yang tersimpan di server (seperti GitHub). Ini memungkinkan kolaborasi dan backup kode.

### Membuat Repository di GitHub

1. Login ke **github.com**
2. Klik tombol **"+"** → **"New repository"**
3. Isi **Repository name** (gunakan huruf kecil, pisahkan dengan `-`)
4. Pilih **Public** atau **Private**
5. **Jangan** centang "Initialize this repository" jika sudah punya repo lokal
6. Klik **"Create repository"**

### Menghubungkan Repo Lokal ke GitHub

```cmd
:: Tambahkan remote bernama "origin"
git remote add origin https://github.com/username/nama-repo.git

:: Verifikasi remote
git remote -v

:: Push (kirim) ke GitHub untuk pertama kali
git push -u origin main
```

### Autentikasi GitHub

GitHub tidak lagi menerima password biasa. Gunakan salah satu cara berikut:

**Cara 1: Personal Access Token (PAT)**

1. Buka **GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)**
2. Klik **"Generate new token"**
3. Centang scope **"repo"** (minimal)
4. Copy token yang dihasilkan
5. Gunakan token ini sebagai pengganti password saat diminta

**Cara 2: GitHub CLI (Direkomendasikan)**

```cmd
:: Install GitHub CLI via winget
winget install --id GitHub.cli

:: Login
gh auth login
```

Ikuti instruksi di layar, pilih **GitHub.com** → **HTTPS** → **Login with a web browser**.

### Perintah Remote Penting

```cmd
:: Clone repository dari GitHub ke lokal
git clone https://github.com/username/nama-repo.git

:: Clone ke folder dengan nama berbeda
git clone https://github.com/username/nama-repo.git nama-folder-baru

:: Pull (ambil perubahan terbaru dari remote)
git pull origin main

:: Push (kirim perubahan lokal ke remote)
git push origin main

:: Lihat semua remote
git remote -v

:: Hapus remote
git remote remove origin
```

### Alur Kerja Sehari-Hari

```cmd
:: Setiap mulai kerja — ambil perubahan terbaru
git pull origin main

:: ... kerjakan tugasmu ...

:: Setelah selesai — kirim ke GitHub
git add .
git commit -m "Deskripsi perubahan"
git push origin main
```

---

## 10. Branching dan Merging

### Apa Itu Branch?

**Branch** adalah "jalur pengembangan" yang terpisah dari kode utama. Ibarat pohon: batang utama adalah `main`, dan ranting-rantingnya adalah branch fitur.

```
main:    A --- B --- C --- G --- H
                      \       /
feature:               D --- E --- F
```

### Mengapa Menggunakan Branch?

- Kembangkan fitur baru tanpa mengganggu kode yang sudah stabil
- Beberapa developer bisa kerja paralel tanpa konflik
- Mudah membatalkan fitur yang gagal (tinggal hapus branch-nya)

### Perintah Branch Dasar

```cmd
:: Lihat semua branch
git branch

:: Buat branch baru
git branch nama-branch

:: Pindah ke branch lain
git checkout nama-branch

:: Buat + langsung pindah ke branch baru (shortcut)
git checkout -b nama-branch

:: Cara modern (Git versi 2.23+)
git switch nama-branch
git switch -c nama-branch   :: buat + pindah

:: Hapus branch (setelah di-merge)
git branch -d nama-branch

:: Hapus branch paksa (belum di-merge)
git branch -D nama-branch
```

### Konvensi Penamaan Branch

```
feature/nama-fitur       → untuk fitur baru
bugfix/nama-bug          → untuk perbaikan bug
hotfix/nama-hotfix       → untuk perbaikan darurat di production
release/v1.2.0           → untuk persiapan rilis
```

### Merging (Menggabungkan Branch)

```cmd
:: 1. Kembali ke branch tujuan (biasanya main)
git checkout main

:: 2. Merge branch fitur ke main
git merge nama-branch

:: 3. Hapus branch yang sudah di-merge (opsional)
git branch -d nama-branch
```

### Jenis-Jenis Merge

**Fast-forward merge** — Terjadi ketika tidak ada commit baru di `main` sejak branch dibuat. Git cukup memindahkan pointer.

```
Sebelum:  main: A --- B
                       \
          feature:      C --- D

Sesudah:  main: A --- B --- C --- D
```

**3-way merge** — Terjadi ketika ada commit baru di kedua branch. Git membuat commit merge baru.

```cmd
:: Merge dengan commit message yang jelas
git merge --no-ff nama-branch -m "Merge branch 'feature/login' into main"
```

---

## 11. Menyelesaikan Konflik (Merge Conflict)

### Kapan Konflik Terjadi?

Konflik terjadi ketika **dua branch mengubah baris yang sama** pada file yang sama, dan Git tidak bisa menentukan perubahan mana yang harus dipertahankan.

### Tanda Konflik dalam File

Ketika konflik terjadi, Git menandai bagian yang bertentangan dalam file:

```
<<<<<<< HEAD
Ini perubahan dari branch saat ini (main)
=======
Ini perubahan dari branch yang di-merge (feature)
>>>>>>> feature/nama-branch
```

### Cara Menyelesaikan Konflik

```cmd
:: 1. Cek file mana yang konflik
git status

:: 2. Buka file yang konflik dan edit manual
notepad nama-file.txt

:: 3. Hapus marker konflik, pertahankan kode yang benar
:: (hapus <<<<<, =====, >>>>> dan salah satu versinya)

:: 4. Tambahkan ke staging setelah diselesaikan
git add nama-file.txt

:: 5. Selesaikan merge dengan commit
git commit -m "Resolve merge conflict in nama-file.txt"
```

### Membatalkan Merge yang Bermasalah

```cmd
:: Batalkan merge dan kembali ke kondisi sebelumnya
git merge --abort
```

---

## 12. Stash — Menyimpan Pekerjaan Sementara

### Apa Itu Stash?

**Stash** menyimpan perubahan yang belum siap di-commit ke "laci sementara", sehingga working directory kamu bersih dan kamu bisa ganti branch atau melakukan hal lain.

### Kapan Digunakan?

Skenario: Kamu sedang mengerjakan fitur A, lalu tiba-tiba ada bug urgent di `main` yang harus segera diperbaiki, tapi pekerjaan fitur A belum siap di-commit.

### Perintah Stash

```cmd
:: Simpan perubahan ke stash
git stash

:: Simpan stash dengan nama/deskripsi
git stash save "WIP: sedang mengerjakan fitur login"

:: Lihat daftar stash
git stash list

:: Ambil kembali stash terbaru (dan hapus dari stash list)
git stash pop

:: Ambil kembali stash tertentu (tanpa menghapus dari list)
git stash apply stash@{0}

:: Hapus stash tertentu
git stash drop stash@{0}

:: Hapus semua stash
git stash clear
```

---

## 13. Melihat Riwayat dan Membatalkan Perubahan

### Melihat Perubahan

```cmd
:: Lihat perubahan yang belum di-staging
git diff

:: Lihat perubahan yang sudah di-staging
git diff --staged

:: Lihat perubahan antara dua commit
git diff abc1234 def5678

:: Lihat detail commit tertentu
git show abc1234
```

### Membatalkan Perubahan

```cmd
:: ─── SEBELUM STAGING ────────────────────────────────────

:: Batalkan perubahan pada file (kembalikan ke versi commit terakhir)
git checkout -- nama-file.txt
:: Cara modern:
git restore nama-file.txt


:: ─── SETELAH STAGING (git add), SEBELUM COMMIT ──────────

:: Keluarkan file dari staging (perubahan tetap ada)
git reset HEAD nama-file.txt
:: Cara modern:
git restore --staged nama-file.txt


:: ─── SETELAH COMMIT ──────────────────────────────────────

:: Buat commit baru yang membatalkan commit tertentu (AMAN)
git revert abc1234

:: Hapus commit terakhir, pertahankan perubahan di working dir
git reset --soft HEAD~1

:: Hapus commit terakhir, pertahankan perubahan di staging
git reset --mixed HEAD~1

:: Hapus commit terakhir + semua perubahannya (BERBAHAYA!)
git reset --hard HEAD~1
```

> ⚠️ **Peringatan:** `git reset --hard` menghapus perubahan secara permanen. Hindari menggunakan ini pada commit yang sudah di-push ke remote yang digunakan bersama.

### Memperbaiki Commit Terakhir

```cmd
:: Ubah pesan commit terakhir
git commit --amend -m "Pesan yang sudah diperbaiki"

:: Tambahkan file yang terlupa ke commit terakhir
git add file-yang-terlupa.txt
git commit --amend --no-edit
```

---

## 14. Tagging dan Versioning

### Apa Itu Tag?

**Tag** adalah penanda pada commit tertentu, biasanya digunakan untuk menandai versi rilis.

### Semantic Versioning (SemVer)

Format: `vMAJOR.MINOR.PATCH`

| Bagian | Kapan Naik |
|---|---|
| **MAJOR** | Perubahan yang tidak backward-compatible |
| **MINOR** | Fitur baru yang backward-compatible |
| **PATCH** | Bug fix backward-compatible |

Contoh: `v1.4.2` → MAJOR=1, MINOR=4, PATCH=2

### Perintah Tag

```cmd
:: Buat tag ringan (lightweight)
git tag v1.0.0

:: Buat annotated tag (lebih lengkap, direkomendasikan)
git tag -a v1.0.0 -m "Release versi 1.0.0 - Initial stable release"

:: Tag pada commit tertentu
git tag -a v0.9.0 abc1234 -m "Beta release"

:: Lihat semua tag
git tag

:: Lihat detail tag
git show v1.0.0

:: Push tag ke GitHub
git push origin v1.0.0

:: Push semua tag sekaligus
git push origin --tags

:: Hapus tag lokal
git tag -d v1.0.0

:: Hapus tag remote
git push origin --delete v1.0.0
```

---

## 15. Git Workflow untuk Tim

### Trunk-Based Development

Semua developer commit langsung ke `main` (dengan branch fitur yang umurnya pendek, < 1 hari). Cocok untuk tim kecil dengan CI/CD yang baik.

### Git Flow

Workflow yang paling populer untuk proyek dengan siklus rilis yang terstruktur.

```
main          ──────●──────────────────────●──────
                    │                      │
release/1.0   ──────●──────●               │
                           │               │
develop       ─────────────●───────────────●─────
                     /         \
feature/login ──────●───────────●
                    
hotfix/bug    ──────────────────────●──────●
```

**Branch dalam Git Flow:**

| Branch | Fungsi |
|---|---|
| `main` | Kode production yang selalu stabil |
| `develop` | Branch pengembangan utama |
| `feature/*` | Pengembangan fitur baru |
| `release/*` | Persiapan rilis |
| `hotfix/*` | Perbaikan bug kritis di production |

### GitHub Flow (Direkomendasikan untuk Pemula Tim)

Versi yang lebih sederhana dari Git Flow:

```
1. Buat branch dari main  →  git checkout -b feature/nama
2. Kerjakan fiturnya      →  commit berkali-kali
3. Push ke GitHub         →  git push origin feature/nama
4. Buat Pull Request      →  via GitHub web
5. Code Review            →  tim memberikan feedback
6. Merge ke main          →  setelah disetujui
7. Hapus branch           →  git branch -d feature/nama
```

---

## 16. Pull Request dan Code Review

### Apa Itu Pull Request (PR)?

**Pull Request** adalah permintaan untuk menggabungkan kode dari satu branch ke branch lain. PR adalah jantung dari kolaborasi di GitHub — tempat diskusi, review, dan persetujuan perubahan kode.

### Membuat Pull Request

1. Push branch ke GitHub:
   ```cmd
   git push origin feature/nama-fitur
   ```
2. Buka repository di **github.com**
3. GitHub akan menampilkan banner "Compare & pull request" — klik tombol itu
4. Isi **judul** yang deskriptif
5. Isi **deskripsi** — jelaskan apa yang berubah, kenapa, dan cara testnya
6. Assign **reviewer** (rekan tim yang akan mereview)
7. Klik **"Create pull request"**

### Menulis Deskripsi PR yang Baik

```markdown
## Ringkasan Perubahan
Menambahkan fitur login dengan validasi email dan rate limiting.

## Perubahan yang Dilakukan
- Tambah form login di `pages/login.html`
- Implementasi validasi email di `utils/validator.py`
- Tambah rate limiting 5 percobaan per 15 menit
- Unit test untuk semua fungsi baru

## Cara Pengujian
1. Jalankan `python app.py`
2. Buka `http://localhost:5000/login`
3. Coba login dengan email tidak valid
4. Coba login lebih dari 5 kali

## Screenshot (jika ada perubahan UI)
[screenshot di sini]

## Checklist
- [x] Kode sudah di-test
- [x] Tidak ada console.log yang tertinggal
- [x] Dokumentasi sudah diupdate
```

### Melakukan Code Review

Sebagai reviewer:
- Baca kode dengan teliti
- Berikan komentar yang **konstruktif dan spesifik**
- Gunakan fitur "Suggest changes" untuk perubahan kecil
- Approve jika sudah OK, atau Request changes jika perlu revisi

---

## 17. GitHub Actions — CI/CD Dasar

### Apa Itu GitHub Actions?

**GitHub Actions** adalah platform CI/CD (Continuous Integration/Continuous Deployment) bawaan GitHub. Kamu bisa mengotomasi pengujian, build, dan deployment kode setiap kali ada push atau pull request.

### Konsep Dasar

- **Workflow** — File YAML yang mendefinisikan proses otomatis
- **Job** — Sekumpulan langkah yang berjalan di satu runner
- **Step** — Satu perintah atau action dalam sebuah job
- **Runner** — Server yang menjalankan workflow (GitHub menyediakan gratis)

### Contoh Workflow: Auto-Test Python

Buat file `.github/workflows/test.yml` di repositorimu:

```yaml
name: Python Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Run tests
      run: |
        python -m pytest tests/ -v
```

Setiap kali ada push ke `main` atau ada PR baru, GitHub akan otomatis menjalankan test. Hasilnya terlihat langsung di PR sebagai centang ✅ atau silang ❌.

---

## 18. Tips, Trik, dan Best Practice

### File `.gitignore`

File `.gitignore` memberitahu Git untuk **mengabaikan** file/folder tertentu dan tidak melacak perubahannya.

```cmd
:: Buat file .gitignore
notepad .gitignore
```

Contoh isi `.gitignore` untuk proyek Python:

```gitignore
# File environment Python
__pycache__/
*.py[cod]
*.pyo
.env
venv/
env/

# File IDE
.vscode/
.idea/
*.suo

# File OS
.DS_Store
Thumbs.db

# File output
*.log
dist/
build/
*.egg-info/

# Credentials (PENTING! Jangan pernah commit ini)
secrets.json
config/credentials.py
.env.local
```

> 🔐 **Aturan Emas:** **JANGAN PERNAH** commit password, API key, atau credential apapun ke Git!

Generate `.gitignore` otomatis di **[gitignore.io](https://www.toptal.com/developers/gitignore)**

### Git Aliases — Shortcut Perintah

```cmd
:: Buat alias untuk perintah yang sering dipakai
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.lg "log --oneline --graph --all --decorate"

:: Penggunaan
git st          :: setara dengan git status
git co main     :: setara dengan git checkout main
git lg          :: log visual yang indah
```

### Conventional Commits

Format standar untuk pesan commit:

```
<type>(<scope>): <description>

[optional body]
[optional footer]
```

**Tipe umum:**

| Type | Kapan Digunakan |
|---|---|
| `feat` | Menambah fitur baru |
| `fix` | Memperbaiki bug |
| `docs` | Perubahan dokumentasi |
| `style` | Format kode (bukan logika) |
| `refactor` | Refactor tanpa tambah fitur/fix bug |
| `test` | Menambah atau memperbaiki test |
| `chore` | Update dependencies, konfigurasi, dll |

Contoh:
```
feat(auth): add email verification on signup
fix(api): resolve null pointer in user endpoint
docs(readme): update installation steps for Windows
```

### Perintah Berguna Lainnya

```cmd
:: Lihat siapa yang mengubah baris tertentu dalam file
git blame nama-file.py

:: Cari commit yang menyebabkan bug (binary search)
git bisect start
git bisect bad               :: commit sekarang ada bug
git bisect good v1.0.0       :: versi ini masih oke
:: (Git akan checkout commit di tengah, kamu test)
git bisect good              :: atau: git bisect bad
:: (ulangi sampai Git menemukan commit penyebab bug)
git bisect reset             :: selesai

:: Salin satu commit dari branch lain
git cherry-pick abc1234

:: Lihat semua branch (lokal + remote)
git branch -a

:: Fetch perubahan dari remote tanpa merge
git fetch origin

:: Rebase (alternatif merge yang lebih bersih)
git rebase main
```

### Checklist Sebelum Push

```
□ Semua test lulus?
□ Tidak ada file sensitif (password, API key)?
□ .gitignore sudah benar?
□ Pesan commit sudah deskriptif?
□ Branch sudah up-to-date dengan main?
□ Kode sudah di-review sendiri (self-review)?
```

---

## 19. Referensi dan Sumber Belajar Lanjutan

### Dokumentasi Resmi

- **Git Documentation** — [git-scm.com/doc](https://git-scm.com/doc)
- **Pro Git Book** (gratis) — [git-scm.com/book](https://git-scm.com/book/en/v2)
- **GitHub Docs** — [docs.github.com](https://docs.github.com)

### Latihan Interaktif

- **Learn Git Branching** — [learngitbranching.js.org](https://learngitbranching.js.org) ⭐ Sangat direkomendasikan!
- **GitHub Skills** — [skills.github.com](https://skills.github.com)
- **Oh My Git!** — Game untuk belajar Git

### Cheat Sheet

```cmd
:: ═══ SETUP ════════════════════════════════════════
git config --global user.name "Nama"
git config --global user.email "email@mail.com"

:: ═══ INIT & CLONE ═══════════════════════════════════
git init
git clone <url>

:: ═══ STAGING & COMMIT ═══════════════════════════════
git status
git add <file>
git add .
git commit -m "pesan"
git commit -am "pesan"

:: ═══ BRANCH ══════════════════════════════════════════
git branch
git checkout -b <branch>
git switch -c <branch>
git merge <branch>
git branch -d <branch>

:: ═══ REMOTE ══════════════════════════════════════════
git remote add origin <url>
git push origin <branch>
git pull origin <branch>
git fetch origin
git clone <url>

:: ═══ UNDO ════════════════════════════════════════════
git restore <file>
git restore --staged <file>
git revert <commit>
git reset --soft HEAD~1
git stash
git stash pop

:: ═══ LOG & DIFF ══════════════════════════════════════
git log --oneline --graph --all
git diff
git diff --staged
git blame <file>
```

---

## 20. Deployment dengan GitHub Pages

### Apa Itu GitHub Pages?

**GitHub Pages** adalah layanan hosting gratis dari GitHub yang bisa menampilkan website statis langsung dari repository kamu. Cocok untuk:

- Portfolio pribadi
- Dokumentasi proyek
- **Laporan analisis data (R Markdown / Quarto)** ⭐
- Blog teknis
- Halaman landing proyek

URL default yang kamu dapatkan: `https://username.github.io/nama-repo/`

### Jenis GitHub Pages

| Tipe | Repository | URL |
|---|---|---|
| **User/Org site** | `username.github.io` | `https://username.github.io` |
| **Project site** | Repo mana saja | `https://username.github.io/nama-repo` |

---

### 20.1 GitHub Pages — HTML/Website Biasa

Ini cara paling dasar — deploy website HTML statis.

**Langkah-langkah:**

1. Buat atau buka repository di GitHub
2. Pastikan ada file `index.html` di root folder atau di folder `docs/`
3. Buka **Settings** repository → tab **Pages** (di sidebar kiri)
4. Pada bagian **Source**, pilih branch `main` dan folder `/root` (atau `/docs`)
5. Klik **Save**
6. Tunggu beberapa menit, URL website akan muncul di bagian atas halaman Pages

```cmd
:: Contoh struktur folder untuk GitHub Pages biasa
nama-repo/
├── index.html
├── style.css
├── script.js
└── assets/
    └── gambar.png
```

---

### 20.2 GitHub Pages untuk R Markdown

Ini bagian yang paling relevan untuk data science — deploy hasil analisis R Markdown sebagai website yang bisa diakses siapa saja!

#### Cara Kerja

R Markdown di-render menjadi file HTML, lalu file HTML itu di-hosting di GitHub Pages. Ada dua pendekatan utama:

```
Pendekatan A (Manual):    .Rmd → render di lokal → push .html → GitHub Pages
Pendekatan B (Otomatis):  .Rmd → push → GitHub Actions render → GitHub Pages
```

---

#### Pendekatan A: Manual (Render Lokal, Push HTML)

Paling sederhana untuk pemula.

**Langkah 1 — Setup Proyek R**

Buat struktur folder proyek:

```
proyek-analisis/
├── analisis.Rmd
├── data/
│   └── dataset.csv
└── docs/              ← folder output untuk GitHub Pages
```

**Langkah 2 — Atur Output ke Folder `docs/`**

Tambahkan ini di YAML header file `.Rmd` kamu:

```yaml
---
title: "Judul Analisis"
author: "Namamu"
date: "`r Sys.Date()`"
output:
  html_document:
    theme: flatly
    highlight: tango
    toc: true
    toc_float: true
    code_folding: show
    self_contained: true
---
```

> ⚠️ **`self_contained: true`** sangat penting! Ini memastikan semua gambar, CSS, dan JS tertanam di dalam file HTML sehingga tampil sempurna di GitHub Pages.

**Langkah 3 — Render dari R Console**

```r
# Di R atau RStudio Console
rmarkdown::render(
  input  = "analisis.Rmd",
  output_file = "index.html",
  output_dir  = "docs"
)
```

Atau klik tombol **Knit** di RStudio, lalu pindahkan file HTML ke folder `docs/`.

**Langkah 4 — Push ke GitHub**

```cmd
git add docs/index.html
git commit -m "docs: render analisis ke HTML untuk GitHub Pages"
git push origin main
```

**Langkah 5 — Aktifkan GitHub Pages**

1. Buka **Settings** → **Pages**
2. Source: branch `main`, folder `/docs`
3. Klik **Save**

Selesai! Website kamu akan live di `https://username.github.io/nama-repo/`

---

#### Pendekatan B: Otomatis dengan GitHub Actions

Setiap kali kamu push file `.Rmd`, GitHub Actions akan otomatis me-render dan deploy — tanpa perlu install R di komputer lain.

**Langkah 1 — Buat File Workflow**

Buat file `.github/workflows/render-rmd.yml`:

```yaml
name: Render and Deploy R Markdown

on:
  push:
    branches: [ main ]
    paths:
      - '**.Rmd'
      - '**.R'
      - 'data/**'

jobs:
  render-and-deploy:
    runs-on: ubuntu-latest
    
    permissions:
      contents: write
    
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup R
        uses: r-lib/actions/setup-r@v2
        with:
          r-version: '4.3.0'

      - name: Install pandoc
        uses: r-lib/actions/setup-pandoc@v2

      - name: Install R packages
        uses: r-lib/actions/setup-r-dependencies@v2
        with:
          packages: |
            any::rmarkdown
            any::knitr
            any::tidyverse
            any::ggplot2

      - name: Render R Markdown
        run: |
          Rscript -e "rmarkdown::render('analisis.Rmd', output_file='docs/index.html')"

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./docs
```

**Langkah 2 — Aktifkan GitHub Pages dari Branch `gh-pages`**

Action di atas akan membuat branch `gh-pages` secara otomatis.

1. Buka **Settings** → **Pages**
2. Source: branch `gh-pages`, folder `/root`
3. Klik **Save**

Sekarang setiap kali kamu push `.Rmd` yang berubah, website akan otomatis ter-update!

---

#### Membuat Website Multi-Halaman dengan `rmarkdown::render_site()`

Untuk laporan dengan banyak halaman (misal: EDA, Modeling, Kesimpulan), gunakan fitur **R Markdown Website**.

**Struktur Folder:**

```
proyek-website/
├── _site.yml          ← konfigurasi navigasi website
├── index.Rmd          ← halaman utama (wajib ada)
├── eda.Rmd            ← halaman EDA
├── modeling.Rmd       ← halaman modeling
├── kesimpulan.Rmd     ← halaman kesimpulan
└── data/
    └── dataset.csv
```

**File `_site.yml`:**

```yaml
name: "Analisis Data Klaim Asuransi"
output_dir: docs
navbar:
  title: "Proyek Analisis"
  left:
    - text: "Beranda"
      href: index.html
    - text: "EDA"
      href: eda.html
    - text: "Modeling"
      href: modeling.html
    - text: "Kesimpulan"
      href: kesimpulan.html
  right:
    - icon: fa-github
      href: https://github.com/username/nama-repo

output:
  html_document:
    theme: flatly
    highlight: tango
    toc: true
    toc_float: true
    self_contained: false   # false untuk multi-halaman (lebih efisien)
```

**Render Seluruh Website:**

```r
# Di R Console atau RStudio
rmarkdown::render_site()
```

Ini akan menghasilkan semua file HTML di folder `docs/`, lengkap dengan navigasi antar halaman.

**Push ke GitHub:**

```cmd
git add docs/
git commit -m "docs: update website analisis"
git push origin main
```

---

#### Menggunakan Quarto (Modern, Direkomendasikan)

**Quarto** adalah penerus R Markdown yang lebih modern dan mendukung Python, R, Julia dalam satu dokumen. Sangat cocok untuk data science.

**Instalasi Quarto:**

Download dari **[quarto.org/docs/download](https://quarto.org/docs/download)** dan install seperti biasa.

**Verifikasi instalasi:**

```cmd
quarto --version
```

**Struktur Proyek Quarto:**

```
proyek-quarto/
├── _quarto.yml         ← konfigurasi proyek
├── index.qmd           ← halaman utama
├── eda.qmd
├── modeling.qmd
└── data/
    └── dataset.csv
```

**File `_quarto.yml`:**

```yaml
project:
  type: website
  output-dir: docs

website:
  title: "Analisis Klaim Asuransi"
  navbar:
    left:
      - href: index.qmd
        text: Beranda
      - href: eda.qmd
        text: EDA
      - href: modeling.qmd
        text: Modeling

format:
  html:
    theme: flatly
    toc: true
    code-fold: true
    code-tools: true
```

**Render Quarto Website:**

```cmd
quarto render
```

**GitHub Actions untuk Quarto:**

Buat `.github/workflows/publish-quarto.yml`:

```yaml
name: Publish Quarto Website

on:
  push:
    branches: [ main ]

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    
    permissions:
      contents: write
    
    steps:
      - uses: actions/checkout@v4

      - name: Setup Quarto
        uses: quarto-dev/quarto-actions/setup@v2

      - name: Setup R
        uses: r-lib/actions/setup-r@v2

      - name: Install R dependencies
        uses: r-lib/actions/setup-r-dependencies@v2
        with:
          packages: |
            any::tidyverse
            any::ggplot2
            any::knitr

      - name: Render and Publish
        uses: quarto-dev/quarto-actions/publish@v2
        with:
          target: gh-pages
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

---

### 20.3 Tips dan Troubleshooting GitHub Pages

#### Tips Penting

**Penamaan File:**

```
✅ index.html   ← GitHub Pages otomatis menampilkan ini
✅ index.Rmd    ← jika di-render menjadi index.html
❌ analisis.html ← harus akses manual via URL penuh
```

**Self-contained vs. Tidak:**

| | `self_contained: true` | `self_contained: false` |
|---|---|---|
| **Ukuran file** | Besar (semua tertanam) | Kecil |
| **Kemudahan** | ✅ Satu file, selalu tampil | ⚠️ Perlu folder lib/ ikut di-push |
| **Cocok untuk** | Halaman tunggal | Website multi-halaman |

**Waktu Deploy:**

GitHub Pages butuh 1–5 menit untuk live setelah push. Cek status di **Settings → Pages**.

#### Troubleshooting Umum

| Masalah | Penyebab | Solusi |
|---|---|---|
| Halaman 404 | Tidak ada `index.html` di root/docs | Rename file output menjadi `index.html` |
| Gambar tidak muncul | Path gambar absolut atau `self_contained: false` | Gunakan `self_contained: true` atau path relatif |
| CSS/theme hilang | File lib/ tidak ikut di-push | Gunakan `self_contained: true` atau push seluruh folder `docs/` |
| Actions gagal | Package R tidak terinstall | Tambahkan package di bagian `packages:` di workflow |
| Website tidak update | Cache browser | Tekan `Ctrl + Shift + R` untuk hard refresh |

#### Mengabaikan File yang Tidak Perlu di `.gitignore`

```gitignore
# R specific
.Rhistory
.RData
.Rproj.user/
*.Rproj

# Output sementara (jika pakai Pendekatan B)
# Jangan ignore docs/ jika pakai Pendekatan A!
# docs/

# Cache knitr
*_cache/
*_files/
```

---

### 20.4 Alur Kerja Lengkap: R Markdown → GitHub → GitHub Pages

Berikut alur kerja end-to-end dari nol:

```cmd
:: ── PERSIAPAN (sekali saja) ──────────────────────────

:: 1. Buat folder proyek dan init git
mkdir analisis-klaim-asuransi
cd analisis-klaim-asuransi
git init

:: 2. Buat file .gitignore
notepad .gitignore

:: 3. Buat struktur folder
mkdir data docs

:: ── KERJA SEHARI-HARI ────────────────────────────────

:: 4. Edit file .Rmd di RStudio, lalu render:
::    rmarkdown::render("analisis.Rmd", output_file="docs/index.html")

:: 5. Cek hasilnya di browser lokal dulu
::    (buka docs/index.html di browser)

:: 6. Jika sudah oke, commit dan push
git add .
git commit -m "feat: tambah analisis eksplorasi data klaim"
git push origin main

:: ── HASIL ────────────────────────────────────────────
:: Website live di:
:: https://username.github.io/analisis-klaim-asuransi/
```

---

> 📝 **Catatan Akhir**
> 
> Git adalah skill yang dipelajari dengan **praktik langsung**. Jangan takut membuat kesalahan — hampir semua kesalahan di Git bisa diperbaiki. Mulailah dengan membuat repository untuk proyek yang sedang kamu kerjakan sekarang, dan biasakan diri commit secara teratur.
>
> *"Commit early, commit often."* — Git mantra

---

*Modul ini dibuat sebagai panduan belajar Git dari nol hingga mahir. Versi terakhir diperbarui: Maret 2026.*
