from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from SessionGenerator import Opleech
from SessionGenerator.utils import add_served_user, keyboard

@Opleech.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"""-  تم تحديث بوت الاستخراج الجديد .
- البوت يشتغل على كل سورسات البايروجرام  .

- المطور الوحيد : by developer .""",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
