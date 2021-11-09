# RenameBot
# This file is a part of code-x-mania rename repo 
# Dont kang !!!
# © code-x-mania

import os, logging
from Adarsh.config import Config
from logging.handlers import RotatingFileHandler
from pyrogram import Client

banner='''                 
 ██████╗ ██████╗ ██████╗ ███████╗    ██╗  ██╗         ███╗   ███╗ █████╗ ███╗   ██╗██╗ █████╗ 
██╔════╝██╔═══██╗██╔══██╗██╔════╝    ╚██╗██╔╝         ████╗ ████║██╔══██╗████╗  ██║██║██╔══██╗
██║     ██║   ██║██║  ██║█████╗       ╚███╔╝          ██╔████╔██║███████║██╔██╗ ██║██║███████║
██║     ██║   ██║██║  ██║██╔══╝       ██╔██╗          ██║╚██╔╝██║██╔══██║██║╚██╗██║██║██╔══██║
╚██████╗╚██████╔╝██████╔╝███████╗    ██╔╝ ██╗         ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║██║  ██║
 ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝    ╚═╝  ╚═╝         ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝  '''

if os.path.exists("Log.txt"):
    with open("Log.txt", "r+") as f_d:
        f_d.truncate(0)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt="%d-%b-%y %H:%M:%S",
                    handlers=[
        RotatingFileHandler(
            "Log.txt",
            maxBytes=1000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)

log = logging.getLogger(__name__)

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Bot(Client):

    def __init__(self):
        super().__init__(
            session_name="RENAMEBOT_CodeXMania",
            api_id=Config.APP_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins={"root": "root/plugins"},
            sleep_threshold=5
        )

    async def start(self):
        await super().start()
        os.makedirs(Config.DOWNLOAD_LOCATION,exist_ok=True)
        log.info(f"<<[Bot Started]>>  {banner}")
    async def stop(self, *args):
        await super().stop()
        log.info("<<[Bot Stopped]>>")

app = Bot()
app.run()

