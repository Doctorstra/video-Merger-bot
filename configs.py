# (c) @AbirHasan2005 | @PredatorHackerzZ

import os


class Config(object):
    API_ID = os.environ.get("API_ID")
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Video-Merger_Bot")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL")
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    TIME_GAP = int(os.environ.get("TIME_GAP", 5))
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", 5))
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME")
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS")
    MONGODB_URI = os.environ.get("MONGODB_URI")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1445283714))

    START_TEXT = """
ššš„š„šØ! šš®šššš«, šš”š¢š¬ š¢š¬ š šš¢šššØ ššš«š šš« ššØš­ šš² [@Dads_links](https://t.me/Dads_links)!
šš”š¢š¬ ššØš­ ššš§ ššš«š š šš®š„š­š¢š©š„š šš¢šššØš¬ š¢š§ šš§š šš¢šššØ šš§š šš¢šššØ ššØš«š¦šš­š¬ š¬š”šØš®š„š šš š¬šš¦š. 

šššš šš² @Dads_links
"""
    CAPTION = "šš¢šššØ ššš«š šš šš² @{}\n\nšššš šš²\n\n@Dads_links"
    PROGRESS = """
š  ššš«ššš§š­šš š : {0}%
ā ššØš§š: {1}
š” ššØš­šš„: {2}
š šš©ššš: {3}/s
ā³ ššš: {4}
"""
