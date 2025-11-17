# 📄 PDF Merger Tool (Python)
## Oleh. Teguh Sutanto

Aplikasi sederhana namun *powerful* untuk menggabungkan (merge) beberapa file PDF menjadi satu. Tersedia dalam dua mode: **Command Line Interface (CLI)** untuk penggunaan cepat via terminal, dan **Graphical User Interface (GUI)** untuk pengalaman visual yang lebih mudah.

## ✨ Fitur Utama

* **Penggabungan PDF:** Menyatukan banyak file PDF menjadi satu dokumen.
* **Keamanan (Enkripsi):** Opsi untuk mengunci file hasil dengan password.
* **Validasi File:** Sistem otomatis mengecek apakah file input rusak (corrupt) sebelum diproses untuk mencegah error.
* **Pengaturan Urutan:** (Mode GUI) Bisa menggeser urutan file naik/turun sebelum digabung.
* **Portable:** Bisa dikompilasi menjadi file `.exe` (Windows Executable).


## 📂 Struktur Proyek

```text
📁 Project_PDF/
│
├── gabung.py           # Script untuk mode CLI (Terminal)
├── gui_gabung.py       # Script untuk mode GUI (Jendela Aplikasi)
├── requirements.txt    # Daftar library yang dibutuhkan
└── README.md           # Dokumentasi ini
```

## ⚙️ Instalasi & Persiapan

Pastikan **Python 3.x** sudah terinstal di komputer Anda.

1.  **Clone atau Download** repository ini.

2.  Buka terminal/CMD di folder proyek.

3.  Instal library yang dibutuhkan (pypdf & cryptography):

    ```bash
    pip install -r requirements.txt
    ```


## 🚀 Cara Penggunaan

### 1\. Mode CLI (Command Line)

Gunakan `gabung.py` jika Anda terbiasa menggunakan terminal atau ingin membuat otomatisasi.

**Format Perintah:**

```bash
python gabung.py [file1] [file2] ... [-o nama_output] [-p password]
```

**Contoh:**

  * **Basic:**
    ```bash
    python gabung.py part1.pdf part2.pdf
    ```
  * **Dengan Nama Output & Password:**
    ```bash
    python gabung.py skripsi_bab1.pdf skripsi_bab2.pdf -o skripsi_final.pdf -p rahasia123
    ```
  * **Bantuan:**
    ```bash
    python gabung.py -h
    ```

### 2\. Mode GUI (Tampilan Grafis)

Gunakan `gui_gabung.py` untuk tampilan antarmuka yang user-friendly (mirip aplikasi Windows biasa).

**Cara Menjalankan:**

```bash
python gui_gabung.py
```
![Alt text](https://github.com/sutanto-teguh/pdftools/blob/main/GUI_Gabung.PNG "GUI Gabung")
**Langkah-langkah di Aplikasi:**

1.  Klik tombol **"+ Tambah PDF"** untuk memilih file.
2.  Gunakan tombol **"Geser Naik"** atau **"Geser Turun"** untuk mengatur urutan halaman.
3.  (Opsional) Isi kolom **Password** jika ingin file output terkunci.
4.  Klik **"GABUNGKAN PDF"** dan pilih lokasi penyimpanan.

-----

## 📦 Membuat Aplikasi Portable (.EXE)

Anda dapat mengubah script ini menjadi aplikasi `.exe` agar bisa dijalankan di komputer yang tidak memiliki Python.

1.  **Instal PyInstaller:**

    ```bash
    pip install pyinstaller
    ```

2.  **Build file EXE:**

      * **Untuk versi GUI (Tanpa layar hitam console):**

        ```bash
        pyinstaller --onefile --noconsole --name "AplikasiGabungPDF" gui_gabung.py
        ```

      * **Untuk versi CLI (Tetap butuh console):**

        ```bash
        pyinstaller --onefile --name "PDFGabungCLI" gabung.py
        ```

3.  File `.exe` akan muncul di dalam folder `dist/`.

-----

## 🛠️ Teknologi yang Digunakan

  * [Python](https://www.python.org/) - Bahasa Pemrograman Utama
  * [pypdf](https://pypi.org/project/pypdf/) - Manipulasi file PDF
  * [Tkinter](https://docs.python.org/3/library/tkinter.html) - Framework GUI (Bawaan Python)
  * [Argparse](https://docs.python.org/3/library/argparse.html) - Parsing argumen CLI

-----

## ⚠️ Catatan Penting

  * Aplikasi memiliki fitur **validasi ketat**. Jika salah satu file input terdeteksi rusak/corrupt, proses penggabungan akan dibatalkan sepenuhnya demi keamanan hasil akhir.
  * Pastikan file input tidak sedang dibuka oleh aplikasi lain saat proses penggabungan.

-----

*Dibuat untuk tujuan pembelajaran dan produktivitas.*

```
```
