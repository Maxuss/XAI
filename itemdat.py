import sys
import json
import os
from decouple import config
import dev
import time
import captcha
import random
import pathlib
pathto = str(pathlib.Path().absolute())
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

        def GetPlayerLocation(profile:int):
            with open((pathto + f"\\playerdata\\player{profile}.json"), "r") as file:
                player = json.load(file)
            location = player["CURRENT_LOCATION"]
            return location

        def turn(self, pehp:int, filler:bool, enemy:dict, pdmg:int, loc:str, profile):
            print("\nСледующий ход!\n")
            devmsg("Initializing next turn...")
            counter = 0
            boss = loc + "_"
            # turn
            maxpehp = pehp
            enemyhp = enemy["DATA"]["CURRENT_HP"]
            enemyxp = enemy["DATA"]["EXPERIENCE"]
            enemymhp = enemy["DATA"]["MAX_HP"]
            enemydmg = enemy["DATA"]["DMG"]
            enemybname = enemy["BATTLE_NAME"]
            enemyname = enemy["NAME"]
            with open((pathto + f"\\playerdata\\player{profile}.json"), 'r') as file:
                pl = json.load(file)
            playerexp = pl["EXPERIENCE"]
            print(f"Вам встречается {enemyname}")
            while pehp > 0:
                with open((pathto + f"\\playerdata\\player{profile}.json"), 'r', encoding='utf-8') as file:
                    _pdat = json.load(file)
                playerexp = _pdat["EXPERIENCE"]
                enemyhp -= pdmg
                pehp -= enemydmg
                print(f"{enemybname.capitalize()} атаковал вас на {enemydmg} урона, а вы нанесли ему {pdmg} единиц урона.")
                if enemyhp > 0:
                    print(f"Здоровье {enemybname}а: {enemyhp}/{enemymhp}.")
                    print(f"Ваше здоровье: {pehp}/{maxpehp} ЭЗ")
                elif enemyhp <= 0:
                    print(f"Вы добиваете  {enemybname}а!")
                    print(f"Ваше здоровье: {pehp}/{maxpehp} ЭЗ")
                    print(f"Вы получаете {enemyxp} очков опыта!")
                    print(f"У вас {playerexp} всего очков опыта")
                    playerexp += enemyxp
                    counter += enemyxp
                    filler = True
                    break
                print("Нажмите ENTER для продолжения!")
                enter = input()
                with open((pathto + f"\\playerdata\\player{profile}.json"), 'w', encoding='utf-8') as file:
                    json.dump(pl, file, indent=4, sort_keys=True, ensure_ascii=False)
            if pehp <= 0:
                print("Вы погибли!")
                with open((pathto + f"\\playerdata\\player{profile}.json"), 'w', encoding='utf-8') as file:
                    json.dump(pl, file, indent=4, sort_keys=True, ensure_ascii=False)
                enter = input()
                exit()
            else:
                enter = input("Подтвердите продолжение битвы!")
                if counter >= 250:
                    counter = 0
                    print("Земля разгневана вашим побоищем! Появляется босс локации!")
                    self.battle(self, profile, boss)
                    print("Босс побежден!")
                elif counter >= 100 and counter <= 150:
                    counter += 50
                    print("Своим геноцидом вы призвали каптчамастера!")
                    captcha.summon_captcha()
                else:
                    captcha.generate_captcha()    
                self.battle(self, profile, enemy)

            
        def battle(self, profile:int, enemy):
            itemdata = ParseItemJSON()
            player_items = self.GetPlayerItems(itemdata, profile)
            location = self.GetPlayerLocation(profile)
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
            pehp = 100 + round(pdef / 2) # Players effective HP (True HP)
            enemyhp = enemy["DATA"]["CURRENT_HP"]
            enemymhp = enemy["DATA"]["MAX_HP"]
            enemyhp -= pdmg
            enemydmg = enemy["DATA"]["DMG"]
            pehp -= enemydmg
            filler = True
            enemy = generate_random_mob(location, profile)
            self.turn(self, pehp, filler, enemy, pdmg, location, profile)
        

attack = Item.Use.battle
next_turn = Item.Use.turn

def generate_random_mob(LOCATION:str, playernum):
    with open((pathto + f'\\playerdata\\player{playernum}.json'), 'r', encoding='utf-8') as file:
        playerdata = json.load(file)
    with open((pathto + '\\data\\enemies.json'), 'r', encoding='utf-8') as file:
        mobdata = json.load(file)
    devmsg("Getting mob data...")
    mobs_to_choose = list(mobdata["MOBDATA"]["NORMAL"][LOCATION].keys())
    chosen = random.choice(mobs_to_choose)
    while LOCATION in str(chosen):
        devmsg("Chosen mob is a boss! Rerolling...")
        chosen = random.choice(mobs_to_choose)
    tc = mobdata["MOBDATA"]["NORMAL"][LOCATION][chosen]
    devmsg(f"Chosen the mob with key '{chosen}'")
    return tc
