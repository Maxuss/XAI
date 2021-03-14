import sys
import json
import os
from decouple import config
import dev

devmsg = dev.Dev.SendMessage()
devmsg("Loading mobdata")
pathto = str(config("XAI_PATH"))
