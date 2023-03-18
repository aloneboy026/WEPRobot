import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from WEPRobot.events import register
from WEPRobot import telethn as tbot


PHOTO = "https://te.legra.ph/file/cfbfa51a91768caba4ce1.jpg"


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm WEP Robot.** \n\n"
    TEXT += "⚪ **I'm Working Properly** \n\n"
    TEXT += f"⚪ **Managed By : [<🇲ᴀʜᴀᴅᴇᴠ ˹🍁˼/>](https://t.me/ll_Mahadev_ll)** \n\n"
    TEXT += f"⚪ **Library Version :** `{telever}` \n\n"
    TEXT += f"⚪ **Telethon Version :** `{tlhver}` \n\n"
    TEXT += f"⚪ **Pyrogram Version :** `{pyrover}` \n\n"
    TEXT += "**Thanks For Adding Me Here ❤️**"
    BUTTON = [
        [
            Button.url("ʜᴇʟᴘ​", "https://t.me/WEP_Robot?start=help"),
            Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/Girls_Talking_Group"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
