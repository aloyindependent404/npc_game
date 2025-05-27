import tkinter as tk

window = tk.Tk()
window.title("Cek Tkinter")

label = tk.Label(window, text="Halo, ini GUI pakai Tkinter!")
label.pack()

window.mainloop()