import tkinter as tk
from tkinter import filedialog, messagebox, Listbox, Scrollbar
import os
from pypdf import PdfWriter, PdfReader

# --- BAGIAN LOGIKA (Sama seperti sebelumnya) ---
def cek_validitas_file(filepath):
    try:
        reader = PdfReader(filepath)
        if len(reader.pages) > 0:
            return True
        return False
    except:
        return False

def proses_gabung():
    # 1. Ambil daftar file dari Listbox
    files = listbox_files.get(0, tk.END)
    password = entry_password.get()
    
    if not files:
        messagebox.showwarning("Peringatan", "Pilih minimal 2 file PDF dulu!")
        return

    # 2. Minta user memilih lokasi simpan & nama file
    output_file = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")],
        title="Simpan Hasil Gabungan Sebagai..."
    )
    
    if not output_file:
        return # User batal menyimpan

    # 3. Mulai Proses
    merger = PdfWriter()
    btn_merge.config(text="Sedang Memproses...", state="disabled")
    root.update()

    try:
        # Validasi & Append
        for pdf in files:
            if not cek_validitas_file(pdf):
                messagebox.showerror("Error", f"File rusak terdeteksi:\n{pdf}\n\nProses dibatalkan.")
                btn_merge.config(text="GABUNGKAN PDF", state="normal")
                return
            merger.append(pdf)

        # Enkripsi jika password diisi
        if password:
            merger.encrypt(password)

        # Tulis File
        merger.write(output_file)
        merger.close()
        
        messagebox.showinfo("Sukses", f"Berhasil digabungkan!\nDisimpan di: {output_file}")

    except Exception as e:
        messagebox.showerror("Error System", f"Terjadi kesalahan: {e}")
    
    finally:
        btn_merge.config(text="GABUNGKAN PDF", state="normal")

# --- BAGIAN TAMPILAN (GUI) ---
def tambah_file():
    filenames = filedialog.askopenfilenames(
        title="Pilih File PDF",
        filetypes=[("PDF Files", "*.pdf")]
    )
    for f in filenames:
        listbox_files.insert(tk.END, f)

def hapus_file():
    selected = listbox_files.curselection()
    for index in selected[::-1]: # Hapus dari belakang agar indeks tidak bergeser
        listbox_files.delete(index)

def clear_all():
    listbox_files.delete(0, tk.END)

def naikkan_urutan():
    selected = listbox_files.curselection()
    if not selected: return
    for pos in selected:
        if pos > 0:
            text = listbox_files.get(pos)
            listbox_files.delete(pos)
            listbox_files.insert(pos-1, text)
            listbox_files.selection_set(pos-1)

def turunkan_urutan():
    selected = listbox_files.curselection()
    if not selected: return
    # Loop reverse
    for pos in selected[::-1]:
        if pos < listbox_files.size() - 1:
            text = listbox_files.get(pos)
            listbox_files.delete(pos)
            listbox_files.insert(pos+1, text)
            listbox_files.selection_set(pos+1)

# Setup Jendela Utama
root = tk.Tk()
root.title("Tool Penggabung PDF")
root.geometry("500x600")
root.configure(bg="#f0f0f0")

# Frame Atas (Tombol File)
frame_top = tk.Frame(root, bg="#f0f0f0")
frame_top.pack(pady=10)

btn_add = tk.Button(frame_top, text="+ Tambah PDF", command=tambah_file, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_add.pack(side=tk.LEFT, padx=5)

btn_remove = tk.Button(frame_top, text="- Hapus Terpilih", command=hapus_file, bg="#FF5722", fg="white", font=("Arial", 10))
btn_remove.pack(side=tk.LEFT, padx=5)

btn_clear = tk.Button(frame_top, text="Hapus Semua", command=clear_all, font=("Arial", 10))
btn_clear.pack(side=tk.LEFT, padx=5)

# Listbox (Daftar File)
frame_list = tk.Frame(root)
frame_list.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)

scrollbar = Scrollbar(frame_list)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox_files = Listbox(frame_list, selectmode=tk.EXTENDED, yscrollcommand=scrollbar.set, font=("Consolas", 9))
listbox_files.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox_files.yview)

# Tombol Urutan (Naik/Turun)
frame_order = tk.Frame(root, bg="#f0f0f0")
frame_order.pack(pady=5)
tk.Button(frame_order, text="▲ Geser Naik", command=naikkan_urutan).pack(side=tk.LEFT, padx=5)
tk.Button(frame_order, text="▼ Geser Turun", command=turunkan_urutan).pack(side=tk.LEFT, padx=5)

# Frame Bawah (Password & Action)
frame_bottom = tk.LabelFrame(root, text="Opsi & Eksekusi", bg="#f0f0f0", padx=10, pady=10)
frame_bottom.pack(padx=20, pady=20, fill=tk.X)

tk.Label(frame_bottom, text="Password (Opsional):", bg="#f0f0f0").pack(anchor="w")
entry_password = tk.Entry(frame_bottom, show="*", font=("Arial", 10))
entry_password.pack(fill=tk.X, pady=5)

btn_merge = tk.Button(frame_bottom, text="GABUNGKAN PDF", command=proses_gabung, bg="#2196F3", fg="white", font=("Arial", 12, "bold"), height=2)
btn_merge.pack(fill=tk.X, pady=10)

# Menjalankan Aplikasi
root.mainloop()