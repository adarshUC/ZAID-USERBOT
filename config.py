import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "3244057")) #optional
API_HASH = getenv("API_HASH", "b8a814ed15eada43bc8c86d89d7f7618") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = int(getenv("OWNER_ID", "1153171536")
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "5226602654:AAFrzzpACGxkamXIdVfNi8MXUc-pFFqyMPY")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/adarshuc/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkANLCAypbZ38k8QKOnft4gkyyHLCAR4YtqOSl1XKgnj3PcT-SuoEjmzqEdg-c0yPKn-vDpnsU_Zw2vU47sB-9WaQzXBzbnBm_OlEyNTfU34toLBv4fLb7BnVrtjDaZyjT7krJxNbUHTxMLdNncyFAOvINJeGyIE3jzmM_uRHNd19XJSaXysMMXlGo8oh4U2hs7Es2aBWOY9MHdE2Ydji9wAR_otMepbHoE8i183AQEL-9U_IFmclUsiAtZa6tXVIE0CzLyk-dUDcZRQXNQGD-bCk0XNGwzRUKcvZ2noIKi4c_-3_vCMGL3Ly9kKc8NL1PomC2LIVWKCtqrKHyQtlA3IwAAAABEvABQAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
