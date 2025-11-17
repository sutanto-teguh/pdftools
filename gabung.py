import argparse
import os
from pypdf import PdfWriter, PdfReader

def cek_validitas_file(filepath):
    """
    Mencoba membuka dan membaca file untuk memastikan tidak corrupt.
    Mengembalikan True jika valid, False jika rusak.
    """
    try:
        reader = PdfReader(filepath)
        # Mencoba mengakses jumlah halaman untuk memicu error jika struktur file rusak
        jumlah_halaman = len(reader.pages)
        if jumlah_halaman > 0:
            return True
        return False
    except Exception:
        return False

def gabung_pdf(input_files, output_name, password=None):
    # --- TAHAP 1: VALIDASI KETAT ---
    print("-" * 40)
    print("-> TAHAP 1: Memeriksa kesehatan semua file...")
    
    for pdf in input_files:
        # 1. Cek keberadaan file
        if not os.path.exists(pdf):
            print(f"[FATAL] File tidak ditemukan: {pdf}")
            print("ABORT: Proses dibatalkan. Harap cek path file Anda.")
            return

        # 2. Cek ekstensi
        if not pdf.lower().endswith('.pdf'):
            print(f"[FATAL] Bukan file PDF: {pdf}")
            print("ABORT: Hanya menerima input file .pdf")
            return

        # 3. Cek apakah file corrupt (rusak)
        print(f"   Checking: {pdf} ... ", end="")
        if cek_validitas_file(pdf):
            print("OK")
        else:
            print("CORRUPT!")
            print(f"\n[ERROR KRITIS] File '{pdf}' tampaknya rusak atau tidak bisa dibaca.")
            print("ABORT: Penggabungan dibatalkan untuk mencegah hasil error.")
            return

    print("[OK] Semua file valid. Lanjut ke penggabungan.")
    
    # --- TAHAP 2: PENGGABUNGAN ---
    print("-" * 40)
    print("-> TAHAP 2: Menggabungkan file...")
    
    merger = PdfWriter()
    
    try:
        for pdf in input_files:
            merger.append(pdf)
            print(f"[V] Menambahkan: {pdf}")

        # --- TAHAP 3: ENKRIPSI & SIMPAN ---
        if not output_name.lower().endswith('.pdf'):
            output_name += ".pdf"

        if password:
            merger.encrypt(password)
            print(f"[LOCK] Mengunci file dengan password...")

        merger.write(output_name)
        merger.close()
        
        print("-" * 40)
        print(f"SUKSES! File tersimpan di: {output_name}")
        if password:
            print("Status: PASSWORD PROTECTED")
            
    except Exception as e:
        print(f"[SYSTEM ERROR] Terjadi kesalahan tak terduga: {e}")

def main():
    parser = argparse.ArgumentParser(description="Tool Penggabung PDF (Validasi Anti-Corrupt + Enkripsi)")
    
    parser.add_argument('files', nargs='+', help='Daftar file PDF input')
    parser.add_argument('-o', '--output', default='gabungan.pdf', help='Nama file output')
    parser.add_argument('-p', '--password', help='Password enkripsi', default=None)

    args = parser.parse_args()
    
    gabung_pdf(args.files, args.output, args.password)

if __name__ == "__main__":
    main()
