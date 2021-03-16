import exceptions
import anti_exploit as ae
import dev
import loot_gen
import mobgen
import json
import os
import sys
import collections
import rpg as r

devmode = dev.devmode
devmsg = dev.Dev.SendMessage()

devmsg("Starting...") 

Exploiter = ae.ExploitCheck()

Exploiter()

devmsg("Finished starting up!")

rpg = r.RPG()

rpg()