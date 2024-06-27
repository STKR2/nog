# YT : @ultroidofficial
# Copyright (c) 2023 WOODcraft
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT, OWNER_ID

keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="❈ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇᴀꜱꜱɪᴏɴ ❈", callback_data="gensession")],
        [
            InlineKeyboardButton(text="❈ ᴏᴡɴᴇʀ ❈", url=f"tg://user?id={OWNER_ID}"),
            InlineKeyboardButton(text="❈ ᴄʜᴀɴɴᴇʟ ❈", url=SUPPORT_CHAT),
        ],
    ]
)


gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="🦋 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐯2 🦋", callback_data="pyrogram1"),
            InlineKeyboardButton(text="🌼 𝐓𝐞𝐥𝐞𝐭𝐡𝐨𝐧 🌼", callback_data="telethon"),
        ],
        [
            InlineKeyboardButton(text="🔹 𝐎𝐰𝐧𝐞𝐫 🔹", url=f"tg://user?id={OWNER_ID}")
        ]
    ]
    
retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="⚡️ Coba Lagi ⚡️", callback_data="gensession")]]
)
