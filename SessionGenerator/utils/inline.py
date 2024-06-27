

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import SUPPORT_CHAT, OWNER_ID

keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="- استخرج الان .", callback_data="gensession")],
        [
            InlineKeyboardButton(text="- مالك البوت .", url=f"tg://user?id={OWNER_ID}"),
            InlineKeyboardButton(text="- قناة التحديثات .", url=SUPPORT_CHAT),
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
            InlineKeyboardButton(text="- مالك البوت .", url=f"tg://user?id={OWNER_ID}")
        ]
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="- حاول مرى اخرى .", callback_data="gensession")]]
)
