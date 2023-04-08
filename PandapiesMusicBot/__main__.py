import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from PandapiesMusicBot import LOGGER, app, userbot
from PandapiesMusicBot.core.call import Pandapies
from PandapiesMusicBot.plugins import ALL_MODULES
from PandapiesMusicBot.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("PandapiesMusicBot").error("Add Pyrogram string session and then try...")
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("PandapiesMusicBot.plugins" + all_module)
    LOGGER("PandapiesMusicBot.plugins").info("Necessary Modules Imported Successfully.")
    await userbot.start()
    await Pandapies.start()
    try:
        await Pandapies.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("PandapiesMusicBot").error(
            "[ERROR] - \n\nTurn on group voice chat and don't put it off otherwise I'll stop working thanks."
        )
        sys.exit()
    except:
        pass
    await Pandapies.decorators()
    LOGGER("PandapiesMusicBot").info("Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("PandapiesMusicBot").info("Stopping Music Bot")
