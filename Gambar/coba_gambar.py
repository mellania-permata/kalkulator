import tkinter as tk

window = tk.Tk()
window.title("menampilkan gambar")
window.geometry("500x500")

#Cara tampilkan gambar
gambar = tk.PhotoImage(file="kucing.png")

label_gambar = tk.Label(window, image=gambar)
label_gambar.pack()

judul = tk.Label(window, text ="Ini kucing")
judul.pack()


window.mainloop()