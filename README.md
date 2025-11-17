# 📄 PDF Merger Tool (Python)

Aplikasi sederhana namun *powerful* untuk menggabungkan (merge) beberapa file PDF menjadi satu. Tersedia dalam dua mode: **Command Line Interface (CLI)** untuk penggunaan cepat via terminal, dan **Graphical User Interface (GUI)** untuk pengalaman visual yang lebih mudah.



## ✨ Fitur Utama

* **Penggabungan PDF:** Menyatukan banyak file PDF menjadi satu dokumen.
* **Keamanan (Enkripsi):** Opsi untuk mengunci file hasil dengan password.
* **Validasi File:** Sistem otomatis mengecek apakah file input rusak (corrupt) sebelum diproses untuk mencegah error.
* **Pengaturan Urutan:** (Mode GUI) Bisa menggeser urutan file naik/turun sebelum digabung.
* **Portable:** Bisa dikompilasi menjadi file `.exe` (Windows Executable).

---

## 📂 Struktur Proyek

```text
📁 Project_PDF/
│
├── gabung.py           # Script untuk mode CLI (Terminal)
├── gui_gabung.py       # Script untuk mode GUI (Jendela Aplikasi)
├── requirements.txt    # Daftar library yang dibutuhkan
└── README.md           # Dokumentasi ini
