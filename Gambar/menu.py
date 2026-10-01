import tkinter as tk
import subprocess
import sys

def buka_luas():
    # Tutup window menu
    window.destroy()

    # Buka 
    subprocess.Popen([
        sys.executable,
        "bangun_datar.py"  #Disesuaikan dengan nama file mu
    ])

window = tk.Tk()
window.title("Program Bangun Datar")
window.geometry("600x500")

judul = tk.Label(
    window,
    text="PROGRAM BANGUN DATAR",
    font=("Arial", 22, "bold")
)
judul.pack(pady=50)

deskripsi = tk.Label(
    window,
    text="Aplikasi Perhitungan Luas dan Keliling Bangun Datar",
    font=("Arial", 11)
)
deskripsi.pack(pady=10)

button_luas = tk.Button(
    window,
    text="HITUNG LUAS",
    font=("Arial", 12, "bold"),
    width=25,
    height=2,
    command=buka_luas
)
button_luas.pack(pady=20)

button_keliling = tk.Button(
    window,
    text="HITUNG KELILING",
    font=("Arial", 12, "bold"),
    width=25,
    height=2
)
button_keliling.pack(pady=10)


window.mainloop()