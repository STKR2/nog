

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import SUPPORT_CHAT

keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="- استخرج الان .", callback_data="gensession")],
        [
            InlineKeyboardButton(text="- مالك البوت .", url=f"https://t.me/RR8R9"),
            InlineKeyboardButton(text="- قناة التحديثات .", url="https://t.me/Xl444"),
        ],
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="- بايروجرام .", callback_data="pyrogram"),
            InlineKeyboardButton(text="- ثليثون .", callback_data="telethon")
        ],
        [
            InlineKeyboardButton(text="- مالك البوت .", url=f"https://t.me/RR8R9")
        ]
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="- حاول مرى اخرى .", callback_data="gensession")]]
)
