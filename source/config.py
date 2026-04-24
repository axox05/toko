import os
from os import getenv

from dotenv import load_dotenv

load_dotenv("sample.env")

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "توكين بوت النقل")

    APP_ID = int(os.environ.get("APP_ID", 21627756))
    
    API_HASH = os.environ.get("API_HASH", "fe77fbf0cae9f7f5ece37659e2466cf1")
    
    OWNER_ID = int(os.environ.get("OWNER_ID", 1411672636))
    
    Devs = [1405636280,1411672636]
    
    

