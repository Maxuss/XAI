import json
import sys
import os
import exceptions as e
import dev
from decouple import config
import time
devmsg = dev.Dev.SendMessage()
pathto = str(config("XAI_PATH"))
devmsg("Setting up RPG module...")

class RPG():
    def __call__(self):
        self.start_up()
        pass
    
    def get_user_inv(self, profile):
        devmsg("Getting user inv data...")
        with open((pathto + f"\\playerdata\\player{profile}.json"), "r") as file:
            userdata = json.load(file)
        inv = userdata["INV"]
        if inv is None:
            raise e.Fatals.CantFindPlayerDataFiles(f"PLAYER{profile}.JSON IS EMPTY")
        else:
            with open((pathto + "\\data\\items.json"), "r", encoding='utf-8') as file:
                itemd = json.load(file)
                itemdata = itemd["ITEMDATA"]
            for i in inv:
                try:
                    item_name = itemdata[i]["NAME"]
                    item_lore = itemdata[i]["INFO"]
                    a = "\nПредмет:\n" + item_name + "\n" + item_lore
                    print(a)
                except KeyError:
                    raise e.JSONErrors.CantParseInventoryData(f"PLAYER{profile}.JSON HAS ILLEGAL ITEMDATA")
        

    def start_up(self):
        prof = {}
        for i in [1, 2, 3]:
            with open((pathto + f"\\playerdata\\player{i}.json"), "r") as file:
                devmsg(f"Checking file number {i}...")
                profiledata = json.load(file)
            isocc = profiledata["?EMPTY"]
            if not isocc:
                prof[f"prof{i}"] = 'полон'
            else:
                prof[f"prof{i}"] = 'пуст'
        profstr = "Профиль 1 - " + prof["prof1"] + "\nПрофиль 2 - " + prof["prof2"] + "\nПрофиль 3 - " + prof["prof3"]
        print("##########################")
        print("#####================#####")
        print("#####===-   XAI  -===#####")
        print("#####================#####")
        print("##########################")
        print("Welcome to XAI!\n")
        print("Введите 1 чтобы начать")
        print("Введите 2 чтобы выйти")
        profstr = "Профиль 1 - " + prof["prof1"] + "\nПрофиль 2 - " + prof["prof2"] + "\nПрофиль 3 - " + prof["prof3"]
        filet = True
        while filet is True:
            try:
                answ = input("Ваш ввод:\n")
                filet = False
            except ValueError:
                print("Это не число!")
        if answ == "2":
            devmsg("Exiting...")
            exit()
        elif answ == "1":
            devmsg('User input = {"answ": "1"}')
            print("Вы выбрали начать.")
            print("Введите номер профиля для открытия/создания. Если профиль полон, то он будет открыт, иначе он будет создан.")
            print(profstr)
            filet = True
            while filet is True:
                try:
                    profile_chosen = int(input("Введите номер профиля...\n"))
                    if profile_chosen == "":
                        raise ValueError
                    filet = False
                except ValueError:
                    print("Это не число!")
            
            devmsg(f"User chose to open profile{profile_chosen}.json")
            devmsg("Trying to open profile data...")
        if profile_chosen >= 1 and profile_chosen <= 3:
            newps = "Вы выбрали профиль " + str(profile_chosen)
            devmsg(f"Profile{profile_chosen} exists and will be opened")
            profiledata = self.Profile.new_profile(self, profile_chosen)
        else:
            devmsg(f"Profile{profile_chosen} doesnt exists!")
            print("Профиль не существует! Выходим...")
            time.sleep(1)
            exit()
        
        print(f"Вы выбрали и открыли профиль {profile_chosen}. Что теперь?")
        print("Доступные функции:")
        print("1 - просмотреть инвентарь")
        print("2 - добавить предметы в инвентарь (не стабильно). Предметы - это ID с 001 до 008 включительно.")
        print("3 - выйти.")
        filet = True
        while filet is True:
            try:
                answ = int(input("Введите число."))
                filet = False
            except ValueError:
                print("Это не число!")
            
        if answ == 3:
            devmsg("Closing...")
            exit()
        elif answ == 2:
            self.Profile.give(self, profile_chosen)
        elif answ == 1:
            self.get_user_inv(profile_chosen)
        answ2 = input("\n")


    class Profile():
        def __call__(self, slotnum, playername):
            self.new_profile(slotnum, playername)
            pass
        
        sample_profile_data = {
            "?EMPTY": False,
            "ENDINGS_COMPLETED": {
                "POSITIVE": False,
                "NEGATIVE": False,
                "MIDDLE": False,
                "SHREK": False,
                "OUTBREAK": False,
                "SECRET": False,
                "S_DEATH": False,
                "TRUTH": False
            },
            "LOCATIONS VISITED": {
                "FIELDS": False,
                "BROKEN_TOWN": False,
                "ABANDONED_FARMS": False,
                "TEMPLE": False,
                "MOUNT_VILLAGE": False,
                "SUMMIT": False,
                "LAB": False,
                "HARDMODE_LOCS": {
                    "HOPELESS_FIELDS": False,
                    "REMNANTS_OF_TOWN": False,
                    "BURNT_FARMS": False,
                    "FORBIDDEN_TEMPLE": False,
                    "HIGH_PEAKS": False,
                    "LAST_SUMMIT": False,
                    "CLONE_LAB": False
                }
            },
            "DEATH_AMOUNT": 0,
            "HM_ON": False,
            "INV": [],
            "CURRENT_LOCATION": "00",
            "BALANCE": 0,
            "ENEMIES_SLAIN": {
                "NORMAL": {
                "FIELDS": 0,
                "BROKEN_TOWN": 0,
                "ABANDONED_FARMS": 0,
                "TEMPLE": 0,
                "MOUNT_VILLAGE": 0,
                "SUMMIT": 0,
                "LAB": 0
            },
            "HM": {
                "HOPELESS_FIELDS": 0,
                "REMNANTS_OF_TOWN": 0,
                "BURNT_FARMS": 0,
                "FORBIDDEN_TEMPLE": 0,
                "HIGH_PEAKS": 0,
                "LAST_SUMMIT": 0,
                "CLONE_LAB": 0,
                "STRONGHOLD": 0
            }
        }
    }
        def new_profile(self, slotnum:int):
            if slotnum >= 0 and slotnum <= 3:
                with open((pathto + f"\\playerdata\\player{slotnum}.json"), "r") as file:
                    devmsg(f"Creating new profile with number {slotnum}...")
                    profiledata = json.load(file)
                isempty = profiledata["?EMPTY"]
                if not isempty:
                    devmsg(f"Cant overwrite an existing file with number '{slotnum}'")
                    devmsg("Looking for solution...")
                    time.sleep(1)
                    with open((pathto + f"\\playerdata\\player{slotnum}.json"), "r") as file:
                        devmsg(f"Opening the file instead")
                        profiledata = json.load(file)
                    return profiledata
                else:
                    playername = input("Введите имя нового персонажа\n")
                    self.Profile.sample_profile_data["NAME"] = playername.capitalize()
                    devmsg(f"Dumping sample data into existing json file...")
                    with open((pathto + f"\\playerdata\\player{slotnum}.json"), "w", encoding="utf-8") as file:
                        json.dump(self.Profile.sample_profile_data, file, indent=4, sort_keys=True, ensure_ascii=False)
                    with open((pathto + f"\\playerdata\\player{slotnum}.json"), "r", encoding='utf-8') as file:
                        profiledata = json.load(file)
                        return profiledata
            else:
                devmsg(f"Couldnt create a new profile with number {slotnum}, as it doesn't exist!")
                print("Профиль не существует...")
                time.sleep(1)
                raise e.Fatals.CantFindDataFiles("Профиль не существует")
        
        def give(self, profile):
            with open((pathto + f"\\playerdata\\player{profile}.json"), "r") as file:
                devmsg(f"Loading profile with number {profile}...")
                profiledata = json.load(file)
            print("Выберите айди предмета, чтобы дать персонажу. АЙДИ доступны с 001 до 008")
            id_item = input("Введите айди\n")
            try:
                with open((pathto + "\\data\\items.json"), "r") as file:
                    devmsg("Opening itemdata...")
                    itemd = json.load(file)
                    itemdata = itemd["ITEMDATA"]
                _current = itemdata[id_item]
                profiledata["INV"].append(id_item)
                with open((pathto + f"\\playerdata\\player{profile}.json"), "w") as file:
                    devmsg("Dumping data to profile...")
                    json.dump(profiledata, file, indent=4, sort_keys=True, ensure_ascii=False)
                print("Предмет добавлен!\nПерезайдите, чтобы посмотреть данные инвентаря!")
            except KeyError:
                devmsg("Item with this ID doesn't exist!")
                print("Такой предмет не существует.")
                time.sleep()
                raise e.FileErrors.CantGenerateLoot("Предмет не существует.")