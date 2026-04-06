# Tutorial Instalasi Pada MacOS

## Metode 1 : Menggunakan Xcode Command Line Tools
macOS biasanya sudah menyediakan Git secara built-in melalui paket alat pengembang Apple.
1. Buka Terminal 
2. Ketik perintah berikut dan tekan Enter : 
    ``` bash
    git --version
    ```
3. Jika Git belum terinstal, sebuah pop-up akan muncul meminta kamu untuk menginstal Command Line Developer Tools.
4. Klik Install dan setujui persyaratannya.
5. Tunggu proses unduhan dan instalasi selesai.

## Metode 2 : Menggunakan Homebrew
Homebrew adalah package manager untuk macOS yang memudahkan pengelolaan aplikasi berbasis terminal. Ini adalah cara terbaik jika kamu ingin mendapatkan versi Git terbaru.
1. Instal Homebrew (jika belum ada) dengan menjalankan:
    ``` bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
2. Setelah Homebrew terinstal, jalankan perintah instalasi Git:
    ``` bash
    brew install git
    ```
3. Homebrew akan secara otomatis mengunduh dan memasang Git versi terbaru.

## Metode 3 : Menggunakan Installer Binary (GUI)
Metode ini akan seperti di Windows, yaitu menggunakan installer seperti `.exe`.
1. Buka situs resmi Git: [git-scm.com/download/mac](git-scm.com/download/mac).
2. Klik pada installer (biasanya akan diarahkan ke proyek SourceForge).
3. Unduh file `.dmg` yang tersedia.
4. Buka file tersebut dan ikuti instruksi instalasi di layar.

## Verifikasi Instalasi 
Setelah selesai melakukan salah satu metode di atas, pastikan Git sudah terpasang dengan benar.
Ketik perintah ini di Terminal:
``` bash
git --version
```
Jika muncul `git version ....` berarti sudah terpasang dengan baik.

## Konfigurasi Awal
Setelah instalasi berhasil, kita harus memperkenalkan diri pada Git agar setiap commit yang kamu buat memiliki identitas yang jelas.
1. Atur Nama:
   ``` bash
   git config --global user.name "Nama Lengkap Anda"
   ```
2. Atur Email:
   ``` bash
    git config --global user.email "emailanda@example.com"
   ```
3. Cek Konfigurasi
   ``` bash
    git config --list
   ```