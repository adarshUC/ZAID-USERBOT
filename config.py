import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "3244057")) #optional
API_HASH = getenv("API_HASH", "") #optional

SUDO_USERS = list(map(int, getenv('SUDO_USERS", "").split()))
OWNER_ID = int(getenv("OWNER_ID", "1153171536"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Yo:AnW6kleYzPip5CHo@cluster0.xm7il2c.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5226602654:AAFrzzpACGxkamXIdVfNi8MXUc-pFFqyMPY")
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/bd3b0d03de25d5a565e44.jpg")
ALIVE_TEXT = getenv("ALIVE_TEXT", "RAAT KA MEHNAT IS LIVE!")
PM_LOGGER = getenv("PM_LOGGER", "1001486674002")
LOG_GROUP = getenv("LOG_GROUP", "1001486674002")
GIT_TOKEN = getenv("GIT_TOKEN", "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") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/AadarshLegend01/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAorPsgm8W86WLA5Uv8VndzEUKfPFTiFoR8muherbtqET9KV1TMjMaOiIaoQqnO6LLc86jyYNOtVF61dqrCl3516niJ0dvS2DUpojVwWe8N02FboTp0YPsWvXpEeoXwrdL9f-2GGWHbLl3tk4ntquLBH1qcx8O8zphD5g9tmM1aiVfbhPnaXEKJ6J8tabKcCzYUJc1tvTyyvst--wvAakxLZD8bTFxbgW-jq7wWbz-XVWLWzaaba_vZfcpAD1u--v-2uo4j97cuRto_3U44ugZsXvif1MYy4ySISfvxUd6vzqXmKkg05MZ5zzE4g72DDWC0gpuamSE-AXmfnZf2CaiXgAAAABEvABQAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
