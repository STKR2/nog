# YT : @ultroidofficial
# Copyright (c) 2023 WOODcraft
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="❈ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇᴀꜱꜱɪᴏɴ ❈", callback_data="gensession")],
        [
            InlineKeyboardButton(text="❈ ʙᴜᴀᴛ ᴀᴘɪ ɪᴅ & ᴀᴘɪ ʜᴀꜱʜ ❈", url="https://my.telegram.org/auth"),
        ],
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="❣️ 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐯1 ❣️", callback_data="pyrogram1"),
            InlineKeyboardButton(text="🦋 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐯2 🦋", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="🌼 𝐓𝐞𝐥𝐞𝐭𝐡𝐨𝐧 🌼", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="⚡️ Coba Lagi ⚡️", callback_data="gensession")]]
)
