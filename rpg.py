import json
import sys
import os
import exceptions as e
import dev
from decouple import config

devmsg = dev.Dev.SendMessage()
pathto = str(config("XAI_PATH"))
devmsg("Setting up RPG module...")

class RPG():
    def __call__(self):
        self.start_up()
        pass
    
    def get_user_inv(self):
        devmsg("Getting user inv data...")
        with open((pathto + "\\playerdata\\player1.json"), "r") as file:
            userdata = json.load(file)
        inv = userdata["INV"]
        if inv is None:
            raise e.Fatals.CantFindPlayerDataFiles("PLAYER1.JSON IS EMPTY")
        else:
            with open((pathto + "\\data\\items.json"), "r", encoding='utf-8') as file:
                itemdata = json.load(file)
            for i in inv:
                try:
                    item_name = itemdata[i]["NAME"]
                    item_lore = itemdata[i]["INFO"]
                    a = "\nПредмет:\n" + item_name + "\n" + item_lore
                    print(a)
                except KeyError:
                    raise e.JSONErrors.CantParseInventoryData("PLAYER1.JSON HAS ILLEGAL ITEMDATA")
        

    def start_up(self):
        print("##########################")
        print("#####================#####")
        print("#####===-   XAI  -===#####")
        print("#####================#####")
        print("##########################")
        print("Welcome to XAI!\n")
        print("Введите 1 чтобы получить данные вашего инвентаря")
        print("Введите 2 чтобы выйти")

        answ = input("\Ваш ввод:\n")

        if answ == "2":
            devmsg("Exiting...")
            exit()
        elif answ == "1":
            devmsg('User input = {"answ": "1"}')
            self.get_user_inv()
        answ2 = input("\n")
    