import sys
import json
import os
from decouple import config
import dev

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
        def __call__(self, itemid):
            self.use(item)
            pass
        
        def GetPlayerItems(itemdata, profile:int):
            with open((pathto + f"\\playerdata\\player{profile}.json"), "r") as file:
                player = json.load(file)
            inv = player["INV"]
            player_items = {
            }
            for item in inv:
                if item is not None:
                    nd = {f"{item}": itemdata[item]}
                    player_items.update(nd)
            return player_items

        def use(self, profile:int):
            itemdata = ParseItemJSON()
            player_items = self.GetPlayerItems(itemdata, profile)
            self._pdata = player_items
            self._idata = itemdata
            print(player_items)


Item.Use.use(Item.Use, 1)