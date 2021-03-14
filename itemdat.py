import sys
import json
import os
from decouple import config
import dev
import time

pathto = str(config("XAI_PATH"))
devmsg = dev.Dev.SendMessage()
devmsg("Loading itemdata")

def ParseItemJSON():
    with open((pathto + "\\data\\items.json"), "r", encoding='utf-8') as file:
        items = json.load(file)
        devmsg("Opening datafile")
    return items["ITEMDATA"]
class Item():
    
    class Create():
        def __init__(
            self, name:str, info:str, itemtype:str,
            ident:str, dmgtype:str, dmg:int, defence:int
        ):
            self.name = name
            self.info = info
            self.itemtype = itemtype
            self.dmgtype = dmgtype
            self.dmg = dmg
            self.defence = defence
            self.ident = ident

    class Use(): 
        def GetPlayerItems(itemdata, profile:int):
            with open((pathto + f"\\playerdata\\player{profile}.json"), "r") as file:
                player = json.load(file)
            inv = player["INV"]
            devmsg("Parsing player's inventory")
            player_items = {
            }
            for item in inv:
                if item is not None:
                    nd = {f"{item}": itemdata[item]}
                    player_items.update(nd)
            return player_items
            
        def turn(self, enemyhp:int, enemymhp:int, enemydmg:int, pehp:int, enemyname:str, enemybname:str, filler:bool, enemy:dict, pdmg:int):
            print("Следующий ход!\n")
            devmsg("Initializing next turn...")
            # turn
            maxpehp = pehp
            enemyhp = enemy["DATA"]["CURRENT_HP"]
            enemymhp = enemy["DATA"]["MAX_HP"]
            enemydmg = enemy["DATA"]["DMG"]
            while pehp > 0:
                enemyhp -= pdmg
                pehp -= enemydmg
                time.sleep(1)
                print(f"{enemybname.capitalize()} атаковал вас на {enemydmg} урона, а вы нанесли ему {pdmg} единиц урона.")
                if enemyhp > 0:
                    print(f"Здоровье {enemybname}а: {enemyhp}/{enemymhp}.")
                    print(f"Ваше здоровье: {pehp}/{maxpehp} ЭЗ")
                elif enemyhp <= 0:
                    print(f"Вы добиваете  {enemybname}а!")
                    print(f"Ваше здоровье: {pehp}/{maxpehp} ЭЗ")
                    filler = True
                    break
                print("Нажмите ENTER для продолжения!")
                enter = input()
            if pehp < 1:
                print("Вы погибли!")
                enter = input()
                filler = True
                pass
            else:
                filler = True
                pass

            
        def battle(self, profile:int, enemy):
            itemdata = ParseItemJSON()
            player_items = self.GetPlayerItems(itemdata, profile)
            self._pdata = player_items
            self._idata = itemdata
            devmsg("Successfully gotten player's itemdata!")
            devmsg("Getting total player's dmg and defence...")
            pdmg = 0
            pdef = 0
            for item in self._pdata:
                idat = self._pdata[item]["DATA"]
                if idat["STATS"]["DMG"] is not None:
                    idat_dmg = idat["STATS"]["DMG"]
                else:
                    idat_dmg = 0
                if idat["STATS"]["DEFENCE"] is not None:
                    idat_def = idat["STATS"]["DEFENCE"]
                else:
                    idat_def = 0
                pdmg += idat_dmg
                pdef += idat_def
                devmsg(f"Processed item {item}!")
            devmsg("Processed all the items in player's inventory!")
            enemyname = enemy["NAME"]
            enemybname = enemy["BATTLE_NAME"]
            devmsg("Starting battle...")
            print("Вам встречается " + enemyname)
            print(round(pdef/3))
            pehp = 100 + round(pdef / 2) # Players effective HP (True HP)
            enemyhp = enemy["DATA"]["CURRENT_HP"]
            enemymhp = enemy["DATA"]["MAX_HP"]
            enemyhp -= pdmg
            enemydmg = enemy["DATA"]["DMG"]
            pehp -= enemydmg

            time.sleep(1)

            print(f"{enemybname.capitalize()} атаковал вас на {enemydmg} урона, а вы нанесли ему {pdmg} единиц урона.")
            print(f"Здоровье {enemybname}а: {enemyhp}/{enemymhp}.")
            print("Начинается битва!\n")
            filler = True
            self.turn(self, enemyhp, enemymhp, enemydmg, pehp, enemyname, enemybname, filler, enemy, pdmg)
            enter = input("Вы победили!")
enemytest = {
                "BOAR_RIDER": {
                    "NAME": "Упырь на кабане!",
                    "BATTLE_NAME": "упырь-наездник",
                    "?TYPE": "RARE",
                    "DATA": {
                        "DMG": 10,
                        "MAX_HP": 50,
                        "CURRENT_HP": 50
                    }
                }
}
