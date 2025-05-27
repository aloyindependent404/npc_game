class Npc:
    def __init__(self, nama ,role):
        self.nama = nama
        self.role = role
        self.izin_masuk = False
        self.quest_diberikan = False
      

    
    def bicara(self,pesan,player):
        pesan = pesan.lower()
        if "nama saya" in pesan:
            player.nama = pesan.replace("nama saya", "").strip().title()
            return f"{self.nama} : baik, aku akan mengingatkmu, {player.nama}"
        elif "siapa saya ?" in pesan:
            if player.nama:
                return f"{self.nama} kamu adalah {player.nama}"
            else:
                return f"{self.nama} aku belom tau nama kamu"
        elif "halo" in pesan or "hai" in pesan:
            return f"{self.nama}: Salam, petualang. Ada yang bisa saya bantu?"
        elif "siapa kamu" in pesan:
            return f"{self.nama}: Saya adalah {self.role} di kota ini."
        elif "bolehkah saya masuk" in pesan:
            if self.izin_masuk:
                return f"{self.nama}: Silakan masuk. Gerbang sudah terbuka."
            else:
                return f"{self.nama}: Maaf, kamu belum punya izin dari wali kota."
        elif "saya dapat izin" in pesan:
            self.izin_masuk = True
            return f"{self.nama}: Baik, sekarang kamu bisa masuk."
        elif "ada misi?" in pesan:

            if not self.quest_diberikan:
               self.quest_diberikan = True
               player.quest = "ambil_ramuan"
               return f"{self.nama}: Ambil ramuan dari Pak Joko dan kembali ke saya."
            else:
                return f"{self.nama}: Sudah kuberikan. Sudah kamu ambil ramuannya?"
            
        elif "selesai" in pesan:
            if player.punya_item("ramuan"):
                player.inventory.remove("ramuan")
                player.quest = None
                player.gold += 50
                player.tambah_xp(100)
                return f"{self.nama}: Terima kasih, kamu telah menyelesaikan misi"
            else:
                return f"{self.nama}: Kamu belum membawa ramuannya."
        elif "status saya" in pesan:
             return player.status()


        return f"{self.nama}: Saya tidak mengerti maksudmu."
      

class Pedagang(Npc):
    def __init__(self,nama):
        super().__init__(nama, "Pedagang")
        self.barang = ["ramuan", "roti","pedang"]

    def bicara(self,pesan,player):
        pesan =  pesan.lower()

        if "apa yang kamu jual" in pesan:
            daftar = ", ".join(self.barang)
            return f"{self.nama} : saya menjual {daftar}"
        
        elif "ambil ramuan" in pesan:
            if player.quest == "ambil_ramuan":
                if not player.punya_item("ramuan"):
                    player.ambil_item("ramuan")
                    return f"{self.nama}: Ini ramuannya. Hati-hati di jalan."
                else:
                    return f"{self.nama}: Kamu sudah mengambil ramuan."
            else:
                return f"{self.nama}: Saya tidak bisa memberimu ramuan."
            
        return super().bicara(pesan,player)


class Penyihir(Npc):
    def __init__(self, nama):
        super().__init__(nama, "penyihir")
        self.mantra = ["api" , "es" , "petir"]

    def bicara(self,pesan,player):
        pesan = pesan.lower()
        if "ajarkan mantra" in pesan:
            return f"{self.nama}: Aku bisa mengajarkanmu mantra: {','.join(self.mantra)}"
        elif "api" in pesan:
            return f"blakutut blakotet jadilah api yanmg membara... syahhh..."
        elif "es" in pesan:
            return f"kuck kucuk kucuk slup slup jadilah es, ngekk.. "
        elif "petir" in pesan:
            return f"blakutut blakotet jadilah petir yanmg meledak... duar"
    
 
        return super().bicara(pesan,player)