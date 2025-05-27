# main.py

from npc import Npc , Pedagang,Penyihir
from utilist import tampilkan_header, format_input
from player import Player
from save_system import muat_player, simpan_player
import tkinter as tk



def ngobrol_dengan(npc ,player):
    print(f"\nSedang berbicara dengan {npc.nama}. Ketik 'keluar' untuk kembali ke menu.\n")
    while True:
        pesan = input("Kamu: ").strip().lower()
        if pesan == "keluar":
            break
        print(npc.bicara(pesan, player))  # 🧠 player dipassing ke NPC
    simpan_player(player)  # ✅ Simpan sebelum keluar

def main_gui():
    player = muat_player()
    gorak = Npc("Gorak", "Penjaga Gerbang")
    pakjoko = Pedagang("Pak Joko")
    dewi = Penyihir("dewi")
    npcs = {
        "Gorak": gorak,
        "Pak Joko": pakjoko,
        "Dewi": dewi
    }

    def kirim_pesan():
        npc = npcs.get(npc_var.get())
        pesan = entry.get()
        if pesan.strip().lower() == "keluar":
            root.quit()
            return
        hasil = npc.bicara(pesan, player)
        teks.insert(tk.END, f"Kamu: {pesan}\n")
        teks.insert(tk.END, f"{npc.nama}: {hasil}\n\n")
        entry.delete(0, tk.END)
        simpan_player(player)

    root = tk.Tk()
    root.title("NPC Chat")

    npc_var = tk.StringVar(root)
    npc_var.set("Gorak")  # default NPC

    dropdown = tk.OptionMenu(root, npc_var, *npcs.keys())
    dropdown.pack(pady=5)

    teks = tk.Text(root, height=20, width=60)
    teks.pack()

    entry = tk.Entry(root, width=50)
    entry.pack(side=tk.LEFT, padx=5)

    tombol = tk.Button(root, text="Kirim", command=kirim_pesan)
    tombol.pack(side=tk.LEFT)

    root.mainloop()

if __name__ == "__main__":
    tampilkan_header()
    main_gui()

