class Player:
    def __init__(self, nama):
        self.nama = nama
        self.quest = None
        self.inventory = []
        self.gold = 0
        self.xp = 0
        self.level = 1

    def ambil_item(self, item):
        if item not in self.inventory:
            self.inventory.append(item)

    def punya_item(self, item):
        return item in self.inventory
    
    def tambah_xp(self, jumlah):
        self.xp += jumlah
        while self.xp >= 100:
            self.level += 1
            self.xp -= 100
            print(f"🎉 {self.nama} naik ke level {self.level}!")

    
    def status(self):
        return (
            f"👤 Nama: {self.nama}\n"
            f"🏅 Level: {self.level} | XP: {self.xp}/100 | 💰 Gold: {self.gold}\n"
            f"🎒 Inventory: {', '.join(self.inventory) if self.inventory else 'Kosong'}\n"
            f"📜 Quest aktif: {self.quest if self.quest else 'Tidak ada'}"
        )
