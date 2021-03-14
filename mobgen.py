# COMMENTED SO IT WONT EXECUTE

# import sys
# import json
# import os
# from decouple import config
# import dev
# from itemdat import Item
# from random import randint
# from random import seed
# devmsg = dev.Dev.SendMessage()
# devmsg("Loading mobdata")
# pathto = str(config("XAI_PATH"))

# attack = Item.Use.battle
# next_turn = Item.Use.turn

# chars = {
#     "a": "2",
#     "b": "3",
#     "c": "4",
#     "d": "5",
#     "e": "8",
#     "f": "9",
#     "g": "16",
#     "h": "17",
#     "i": "32",
#     "j": "33",
#     "k": "64",
#     "l": "65",
#     "m": "128",
#     "n": "129",
#     "o": "256",
#     "p": "257",
#     "q": "512",
#     "r": "513",
#     "s": "1024",
#     "t": "1025",
#     "u": "2048",
#     "v": "2049",
#     "w": "4096",
#     "x": "4097",
#     "y": "8192",
#     "z": "8193",
# }

# devmsg("Loading mob generation...")
# def parse_seed(seed):
#     tsli = seed.split("-")
#     savename = tsli[0]
#     modi1 = int(tsli[1])
#     modi2 = int(tsli[2])
#     coder = tsli[3]

#     if modi2 > modi1:
#         modcoder = modi2 - modi1
#     elif modi2 < modi1:
#         modcoder = modi1 - modi2
#     else:
#         modcoder = 1111
#     devmsg(f"Seed modifier-coder for seed '{seed}' is {modcoder}")

#     _decodeds = coder.split("$")
#     _decodednum1 = chars[_decodeds[0]]
#     _decodednum2 = chars[_decodeds[0]]
#     _decodednum3 = chars[_decodeds[0]]
#     __decoded = int(_decodednum1) + int(_decodednum2) + int(_decodednum3)

#     true_seed = abs(__decoded - modcoder)
#     return true_seed


    

# def generate_random_mob(LOCATION:str, seed):
#     ns = parse_seed(seed)
#     seed(ns)

    

# parse_seed("DEV_TEST-1278-2381-dzg")
