import json

def simpan_player(player):
    data = {
        "nama": player.nama,
        "quest": player.quest,
        "inventory": player.inventory,
        "gold": player.gold,
        "xp": player.xp,
        "level": player.level
    }

    with open("save.json", "w") as f:
        json.dump(data,f)

    
def muat_player():
    with open("save.json", "r") as f:
        data = json.load(f)
    from player import Player
    player = Player(data["nama"])
    player.quest = data["quest"]
    player.inventory = data["inventory"]
    player.gold = data["gold"]
    player.xp = data["xp"]
    player.level = data["level"]
    return player