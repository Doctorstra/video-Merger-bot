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
𝐇𝐞𝐥𝐥𝐨! 𝐃𝐮𝐟𝐟𝐞𝐫, 𝐓𝐡𝐢𝐬 𝐢𝐬 𝐚 𝐕𝐢𝐝𝐞𝐨 𝐌𝐞𝐫𝐠𝐞𝐫 𝐁𝐨𝐭 𝐛𝐲 [@𝐓𝐡𝐞𝐓𝐞𝐥𝐞𝐑𝐨𝐢𝐝](https://t.me/TheTeleRoid)!
𝐓𝐡𝐢𝐬 𝐁𝐨𝐭 𝐜𝐚𝐧 𝐌𝐞𝐫𝐠𝐞 𝐌𝐮𝐥𝐭𝐢𝐩𝐥𝐞 𝐕𝐢𝐝𝐞𝐨𝐬 𝐢𝐧 𝐎𝐧𝐞 𝐕𝐢𝐝𝐞𝐨 𝐀𝐧𝐃 𝐕𝐢𝐝𝐞𝐨 𝐅𝐨𝐫𝐦𝐚𝐭𝐬 𝐬𝐡𝐨𝐮𝐥𝐝 𝐛𝐞 𝐬𝐚𝐦𝐞. 

𝐌𝐚𝐝𝐞 𝐛𝐲 @TheTeleRoid
"""
    CAPTION = "𝐕𝐢𝐝𝐞𝐨 𝐌𝐞𝐫𝐠𝐞𝐝 𝐛𝐲 @{}\n\n𝐌𝐚𝐝𝐞 𝐛𝐲\n\n@TheTeleRoid"
    PROGRESS = """
🛠 𝐏𝐞𝐫𝐜𝐞𝐧𝐭𝐚𝐠𝐞 : {0}%
✅ 𝐃𝐨𝐧𝐞: {1}
📡 𝐓𝐨𝐭𝐚𝐥: {2}
🚀 𝐒𝐩𝐞𝐞𝐝: {3}/s
⏳ 𝐄𝐓𝐀: {4}
"""
