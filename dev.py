import os
import sys
import json
from decouple import config

pathto = str(config("XAI_PATH"))

with open('data.json', 'r') as file:
    data = json.load(file)

devmode = data["DEV"]

class Dev():

    class SendMessage():
        def __call__(self, message:str):
            self.send(message)
            pass
        def send(self, message:str):
            self.msgstart = "[XAI-DEV] > "
            self.fullmsg = self.msgstart + message
            if devmode:
                print(self.fullmsg)