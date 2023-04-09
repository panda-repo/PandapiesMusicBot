from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from PandapiesMusicBot.utils.database import is_on_off
from PandapiesMusicBot import app


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        logger_text = f"""
❏ **🐼 {MUSIC_BOT_NAME} ᴍᴜsɪᴄ ʟᴏɢs **
├ **🐼 Nama Grup/Channel : >** {message.chat.title} [`{message.chat.id}`]
├ **🐼 Nama : ›** {message.from_user.mention}
├ **🐼 Username : ›** @{message.from_user.username}
├ **🐼 Id  : ›** `{message.from_user.id}`
├ **🐼 Chat Link: >** {chatusername}
├ **🐼 Jenis Perintah:** {message.text}
└ **🐼 Stream Type:** {streamtype}


Powered OwlCode @PandaProject_Id"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
