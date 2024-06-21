# Generate Session In Your Telegram premium @Opleech
# Copyright (c) 2023 WOODcraft
from pyrogram import filters
from pyrogram.types import Message

from SessionGenerator import Opleech
from SessionGenerator.utils import add_served_user, keyboard


@Opleech.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"🦋 Hey {message.from_user.first_name},\n\n⌘ Ini Bot {Opleech.mention},\nUntuk Membuat String Session Pyrogram Atau Telethon.\n\nJika Belum Punya API_ID & API_HASH, Silahkan Klik ❈ ʙᴜᴀᴛ ᴀᴘɪ ɪᴅ & ᴀᴘɪ ʜᴀꜱʜ ❈ ",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
