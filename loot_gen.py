import os
import pathlib
import dev
import random
import json

pathto = str(pathlib.Path().absolute())
devmsg = dev.Dev.SendMessage()
devmsg("Loading lootgen module...")

class Loot():
    def __call__(self, current_location:str, enemy_name:str, player:int):
        self.Generate(current_location, enemy_name, player)

    def Generate(current_location:str, enemy_name:str, player_profile:int, gamemode="NORMAL_MODE"):
        with open((pathto + "\\ref\\lootgen\\loot_tables.json"), 'r', encoding='utf-8') as file:
            loot_table = json.load(file)
        with open((pathto + f"\\playerdata\\player{player_profile}.json"), 'r', encoding='utf-8') as file:
            player_data = json.load(file)

        playerinv = player_data["INV"]
        enemy_loot = loot_table[gamemode][current_location][enemy_name]
        loot_keys = list(enemy_loot.keys())

        for key in loot_keys:
            itemchance = enemy_loot[key]
            rolled = random.randint(1, itemchance)
            devmsg(f"Rolling chance for item {key} in loot of {enemy_name}...")
            if rolled == itemchance:
                playerinv.append(key)
                devmsg("Rolled successfully!")
            else:
                devmsg("Rolled unsuccessfully!")

GenerateLoot = Loot.Generate