import tkinter as tk
from tkinter import ttk


# ==========================
# FUNGSI HITUNG PERSEGI
# ==========================
def hitung_persegi():
    try:
        sisi = float(entry_sisi.get())
        luas = sisi * sisi

        hasil_persegi.config(
            text=f"Luas Persegi = {luas}"
        )
    except ValueError:
        hasil_persegi.config(
            text="Masukkan angka yang valid!"
        )


# ==========================
# FUNGSI HITUNG PERSEGI PANJANG
# ==========================
def hitung_persegi_panjang():
    try:
        panjang = float(entry_panjang.get())
        lebar = float(entry_lebar.get())

        luas = panjang * lebar

        hasil_persegi_panjang.config(
            text=f"Luas Persegi Panjang = {luas}"
        )
    except ValueError:
        hasil_persegi_panjang.config(
            text="Masukkan angka yang valid!"
        )


# ==========================
# WINDOW UTAMA
# ==========================
window = tk.Tk()

window.title("Kalkulator Luas Bangun Datar")
window.geometry("500x400")


# ==========================
# JUDUL
# ==========================
judul = tk.Label(
    window,
    text="KALKULATOR LUAS BANGUN DATAR",
    font=("Arial", 16, "bold")
)

judul.pack(pady=15)


# ==========================
# MEMBUAT NOTEBOOK / TAB
# ==========================
notebook = ttk.Notebook(window)

notebook.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)


# ==========================
# MEMBUAT TAB
# ==========================
tab_persegi = tk.Frame(notebook)

tab_persegi_panjang = tk.Frame(notebook)


# ==========================
# MENAMBAHKAN TAB
# ==========================
notebook.add(
    tab_persegi,
    text="Persegi"
)

notebook.add(
    tab_persegi_panjang,
    text="Persegi Panjang"
)


# ==================================================
# ISI TAB PERSEGI
# ==================================================

judul_persegi = tk.Label(
    tab_persegi,
    text="MENGHITUNG LUAS PERSEGI",
    font=("Arial", 14, "bold")
)

judul_persegi.grid(
    row=0,
    column=0,
    columnspan=2,
    pady=30
)


# Label Sisi
label_sisi = tk.Label(
    tab_persegi,
    text="Sisi"
)

label_sisi.grid(
    row=1,
    column=0,
    padx=10,
    pady=10
)


# Entry Sisi
entry_sisi = tk.Entry(
    tab_persegi
)

entry_sisi.grid(
    row=1,
    column=1,
    padx=10,
    pady=10
)


# Button
button_persegi = tk.Button(
    tab_persegi,
    text="Hitung Luas",
    command=hitung_persegi
)

button_persegi.grid(
    row=2,
    column=0,
    columnspan=2,
    pady=15
)


# Hasil
hasil_persegi = tk.Label(
    tab_persegi,
    text="Luas Persegi = ..."
)

hasil_persegi.grid(
    row=3,
    column=0,
    columnspan=2,
    pady=10
)


# ==================================================
# ISI TAB PERSEGI PANJANG
# ==================================================

judul_pp = tk.Label(
    tab_persegi_panjang,
    text="MENGHITUNG LUAS PERSEGI PANJANG",
    font=("Arial", 14, "bold")
)

judul_pp.grid(
    row=0,
    column=0,
    columnspan=2,
    pady=30
)


# Label Panjang
label_panjang = tk.Label(
    tab_persegi_panjang,
    text="Panjang"
)

label_panjang.grid(
    row=1,
    column=0,
    padx=10,
    pady=10
)


# Entry Panjang
entry_panjang = tk.Entry(
    tab_persegi_panjang
)

entry_panjang.grid(
    row=1,
    column=1,
    padx=10,
    pady=10
)


# Label Lebar
label_lebar = tk.Label(
    tab_persegi_panjang,
    text="Lebar"
)

label_lebar.grid(
    row=2,
    column=0,
    padx=10,
    pady=10
)


# Entry Lebar
entry_lebar = tk.Entry(
    tab_persegi_panjang
)

entry_lebar.grid(
    row=2,
    column=1,
    padx=10,
    pady=10
)


# Button
button_pp = tk.Button(
    tab_persegi_panjang,
    text="Hitung Luas",
    command=hitung_persegi_panjang
)

button_pp.grid(
    row=3,
    column=0,
    columnspan=2,
    pady=15
)


# Hasil
hasil_persegi_panjang = tk.Label(
    tab_persegi_panjang,
    text="Luas Persegi Panjang = ..."
)

hasil_persegi_panjang.grid(
    row=4,
    column=0,
    columnspan=2,
    pady=10
)


# ==========================
# MENJALANKAN PROGRAM
# ==========================
window.mainloop()

