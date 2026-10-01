import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess
import sys

def kembali():
    # Tutup window menu
    window.destroy()

    # Buka 
    subprocess.Popen([
        sys.executable,
        "menu.py"  #Disesuaikan dengan nama file mu
    ])
    
    
def hitung_persegi():
    sisi = float(entry_sisi.get())
    luas = sisi * sisi
    hasil_persegi.config(text=f"luas persegi = {luas}")
    
def hitung_persegi_panjang():
    panjang = float(entry_panjang.get())
    lebar = float(entry_lebar.get())
    luas = panjang * lebar
    hasil_persegi_panjang.config(text=f"luas persegi panjang = {luas}")
    
#Window
window = tk.Tk()
window.title("Program Bangun Datar")
window.geometry("600x500")

#judul
judul = tk.Label(window,
                 text="Program Luas Bangun Datar",
                 font=("Arial", 16, "bold"))
judul.pack(pady=15)

btn_kembali = tk.Button(window, text="Kembali ke Menu", command=kembali)
btn_kembali.pack()

notebook = ttk.Notebook(window)
notebook.pack(fill ="both",
              expand=True,
              padx = 20,
              pady = 10)

tab_persegi = tk.Frame(notebook)
notebook.add(tab_persegi, text="Persegi")

tab_persegi_panjang = tk.Frame(notebook)
notebook.add(tab_persegi_panjang,
             text="Persegi Panjang")

tab_segitiga = tk.Frame(notebook)
notebook.add(tab_segitiga,
             text="segitiga")
#Isi persegi
judul_persegi = tk.Label(tab_persegi,
                         text="Menghitung Luas Persegi",
                         font=("Arial", 14, "bold"))

judul_persegi.grid(row = 0,
                   column = 0,
                   columnspan = 2,
                   pady = 30)

#Gambar
gambar_persegi = Image.open("persegi.png")
gambar_persegi = gambar_persegi.resize((150,150))
gambar_tk = ImageTk.PhotoImage(gambar_persegi)
label_gambar = tk.Label(tab_persegi, image=gambar_tk)
label_gambar.grid(row=1, column=0, pady=0)

label_sisi = tk.Label(tab_persegi,
                      text="Panjang sisi :")
label_sisi.grid(row = 1,
                column = 1,
                padx = 10,
                pady = 10)
entry_sisi = tk.Entry(tab_persegi)
entry_sisi.grid(row=1,
                column=2,
                padx=10,
                pady=10)

button_persegi = tk.Button(tab_persegi,
                           text="hitung luas",
                           command=hitung_persegi)

button_persegi.grid(row=2,
                    column=1,
                    pady=10,
                    padx=10)

hasil_persegi = tk.Label(tab_persegi,
                         text="Luas Persegi = ...")
hasil_persegi.grid(row=3,
                   column=1,
                   columnspan=2,
                   pady=10)

#Isi persegi panjang
judul_persegi_panjang = tk.Label(tab_persegi_panjang,
                         text="Menghitung Luas Persegi Panjang",
                         font=("Arial", 14, "bold"))

judul_persegi_panjang.grid(row = 0,
                   column = 0,
                   columnspan = 2,
                   pady = 30)

label_panjang = tk.Label(tab_persegi_panjang,
                      text="Panjang :")
label_panjang.grid(row = 1,
                column = 0,
                padx = 10,
                pady = 10)
entry_panjang = tk.Entry(tab_persegi_panjang)
entry_panjang.grid(row=1,
                column=1,
                padx=10,
                pady=10)

label_lebar = tk.Label(tab_persegi_panjang,
                      text="Lebar :")
label_lebar.grid(row = 2,
                column = 0,
                padx = 10,
                pady = 10)
entry_lebar = tk.Entry(tab_persegi_panjang)
entry_lebar.grid(row=2,
                column=1,
                padx=10,
                pady=10)

button_persegi_panjang = tk.Button(tab_persegi_panjang,
                           text="hitung luas",
                           command=hitung_persegi_panjang)

button_persegi_panjang.grid(row=3,
                    column=1,
                    pady=10,
                    padx=10)

hasil_persegi_panjang = tk.Label(tab_persegi_panjang,
                         text="Luas Persegi Panjang = ...")
hasil_persegi_panjang.grid(row=4,
                   column=0,
                   columnspan=2,
                   pady=10)

window.mainloop()
