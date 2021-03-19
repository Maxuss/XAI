import exceptions
import anti_exploit as ae
import dev
import loot_gen
import json
import os
import sys 
import collections
import rpg as r
import pathlib
pathto = str(pathlib.Path().absolute())
devmode = dev.devmode
devmsg = dev.Dev.SendMessage()
with open((pathto + "\\program.xdat"), 'r') as file:
    xdat = json.load(file)

devmsg(xdat["version"])
devmsg(f'.git link: {xdat["gitlink"]}')

devmsg("Starting...") 
devmsg(f"Loading at path {pathto}")
Exploiter = ae.ExploitCheck()

Exploiter()

devmsg("Finished starting up!")

rpg = r.RPG()

rpg()