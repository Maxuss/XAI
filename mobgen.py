import sys
import json
import os
from decouple import config
import dev
from itemdat import Item
devmsg = dev.Dev.SendMessage()
devmsg("Loading mobdata")
pathto = str(config("XAI_PATH"))

attack = Item.Use.battle()
next_turn = Item.Use.turn()

devmsg("Loading mob generation...")
def parse_seed(seed):
    tsli = seed.split("-")
    savename = tsli[0]
    modi1 = tsli[1]
    modi2 = tsli[2]
    coder = tsli[3]

    if modi2 > modi1:
        modcoder = modi2 - modi1
    elif modi2 < modi1:
        modcoder = modi1 - modi2
    else:
        modcoder = 111
    print(modcoder)

def generate_random_mob(LOCATION:str, seed):
    pass