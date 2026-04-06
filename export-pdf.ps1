param(
    [string]$InputFile = "draft_Module_Git.md"
)

$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$inputPath = Join-Path $root $InputFile
$preparedInputPath = Join-Path $root ([System.IO.Path]::GetFileNameWithoutExtension($InputFile) + ".pdfbuild.md")
$preparedPdfPath = Join-Path $root ([System.IO.Path]::GetFileNameWithoutExtension($InputFile) + ".pdfbuild.pdf")
$legacyBackupPath = Join-Path $root ([System.IO.Path]::GetFileNameWithoutExtension($InputFile) + ".prelinkfix.pdf")
$configPath = Join-Path $root "md-to-pdf.config.js"
$prepareScriptPath = Join-Path $root "prepare_markdown_for_pdf.py"
$tocScriptPath = Join-Path $root "update_toc_pages.py"
$fixScriptPath = Join-Path $root "fix_pdf_links.py"

if (-not (Test-Path $inputPath)) {
    throw "File markdown tidak ditemukan: $inputPath"
}

if (-not (Test-Path $configPath)) {
    throw "Config md-to-pdf tidak ditemukan: $configPath"
}

if (-not (Test-Path $prepareScriptPath)) {
    throw "Script persiapan markdown PDF tidak ditemukan: $prepareScriptPath"
}

if (-not (Test-Path $tocScriptPath)) {
    throw "Script sinkronisasi daftar isi tidak ditemukan: $tocScriptPath"
}

if (-not (Test-Path $fixScriptPath)) {
    throw "Script perbaikan PDF tidak ditemukan: $fixScriptPath"
}

Push-Location $root
try {
    $outputPath = [System.IO.Path]::ChangeExtension($inputPath, ".pdf")
    Remove-Item $preparedInputPath, $preparedPdfPath, $legacyBackupPath -ErrorAction SilentlyContinue
    $maxPasses = 5
    $changed = $true

    for ($pass = 1; $pass -le $maxPasses; $pass++) {
        Write-Host ""
        Write-Host "Render pass $pass..."

        & python $prepareScriptPath $inputPath $preparedInputPath

        if ($LASTEXITCODE -ne 0) {
            throw "Persiapan markdown PDF gagal."
        }

        & npx md-to-pdf $preparedInputPath --config-file $configPath

        if ($LASTEXITCODE -ne 0) {
            throw "Proses konversi PDF gagal."
        }

        $syncOutput = & python $tocScriptPath $inputPath $preparedPdfPath

        if ($LASTEXITCODE -ne 0) {
            throw "Sinkronisasi daftar isi gagal."
        }

        $syncOutput | ForEach-Object { Write-Host $_ }
        $changed = $syncOutput -match "CHANGED=1"

        if (-not $changed) {
            break
        }
    }

    if ($changed) {
        throw "Nomor halaman daftar isi belum stabil setelah $maxPasses pass render."
    }

    Copy-Item $preparedPdfPath $outputPath -Force
    & python $fixScriptPath $outputPath $inputPath

    if ($LASTEXITCODE -ne 0) {
        throw "Perbaikan link internal PDF gagal."
    }

    Write-Host ""
    Write-Host "PDF berhasil dibuat:"
    Write-Host $outputPath
    Write-Host ""
    Write-Host "Catatan: daftar isi sudah disinkronkan ke nomor halaman terbaru, link internal diperbaiki, bookmark PDF ditambahkan, dan footer nomor halaman tetap aktif."
}
finally {
    Remove-Item $preparedInputPath, $preparedPdfPath, $legacyBackupPath -ErrorAction SilentlyContinue
    Pop-Location
}
