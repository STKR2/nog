import asyncio

from pyrogram import Client, filters
from oldpyro import Client as Client1
from oldpyro.errors import ApiIdInvalid as ApiIdInvalid1
from oldpyro.errors import PasswordHashInvalid as PasswordHashInvalid1
from oldpyro.errors import PhoneCodeExpired as PhoneCodeExpired1
from oldpyro.errors import PhoneCodeInvalid as PhoneCodeInvalid1
from oldpyro.errors import PhoneNumberInvalid as PhoneNumberInvalid1
from oldpyro.errors import SessionPasswordNeeded as SessionPasswordNeeded1
from pyrogram.errors import (
    ApiIdInvalid,
    FloodWait,
    PasswordHashInvalid,
    PhoneCodeExpired,
    PhoneCodeInvalid,
    PhoneNumberInvalid,
    SessionPasswordNeeded,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telethon import TelegramClient
from telethon.errors import (
    ApiIdInvalidError,
    PasswordHashInvalidError,
    PhoneCodeExpiredError,
    PhoneCodeInvalidError,
    PhoneNumberInvalidError,
    SessionPasswordNeededError,
)
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest
from pyromod.listen.listen import ListenerTimeout

from config import SUPPORT_CHAT, API_ID, API_HASH
from SessionGenerator import Opleech
from SessionGenerator.utils import retry_key

async def gen_session(
    message, user_id: int, telethon: bool = False, old_pyro: bool = False
):
    if telethon:
        ty = f"ثليثون"
    elif old_pyro:
        ty = f""
    else:
        ty = f"بايروجرام"

    await message.reply_text(f"- لقد قمت بالضغط على {ty} .")

    api_id = API_ID
    api_hash = API_HASH

    try:
        phone_number = await Opleech.ask(
            identifier=(message.chat.id, user_id, None),
            text="- الان ارسل لي رقمك \n- على سبيل المثال : +9640000000000",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Opleech.send_message(
            user_id,
            "- وين رحت ترى تأخرت .",
            reply_markup=retry_key,
        )

    if await cancelled(phone_number):
        return
    phone_number = phone_number.text

    await Opleech.send_message(user_id, "- يتم التحقق من الرقم .")
    if telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="Opleech", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()

    try:
        if telethon:
            code = await client.send_code_request(phone_number)
        else:
            code = await client.send_code(phone_number)
        await asyncio.sleep(1)

    except FloodWait as f:
        return await Opleech.send_message(
            user_id,
            f" - الحساب بلع فلود انتضر {f.value or f.x} ثانية وحاول مرة أخرى .",
            reply_markup=retry_key,
        )
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        return await Opleech.send_message(
            user_id,
            "- الايدي ايبي والايبي هاش غلط او انت داز وهميات .",
            reply_markup=retry_key,
        )
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        return await Opleech.send_message(
            user_id,
            "- الرقم غلط او ماكو حساب بهذا الرقم .
            .",
            reply_markup=retry_key,
        )

    try:
        otp = await Opleech.ask(
            identifier=(message.chat.id, user_id, None),
            text=f"- تمام حب هذا رقمك {phone_number} \n- هسه دزلي الكود بس شرط \n\n- يكون بأرقام مفصوله كمثال : 2 7 3 2 4 ",
            filters=filters.text,
            timeout=600,
        )
        if await cancelled(otp):
            return
    except ListenerTimeout:
        return await Opleech.send_message(
            user_id,
            "- وين رحت ترى تأخرت .",
            reply_markup=retry_key,
        )

    otp = otp.text.replace(" ", "")
    try:
        if telethon:
            await client.sign_in(phone_number, otp, password=None)
        else:
            await client.sign_in(phone_number, code.phone_code_hash, otp)
    except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
        return await Opleech.send_message(
            user_id,
            "- الكود غلط .",
            reply_markup=retry_key,
        )
    except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
        return await Opleech.send_message(
            user_id,
            "- انتهت صلاحية الكود .",
            reply_markup=retry_key,
        )
    except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
        try:
            pwd = await Opleech.ask(
                identifier=(message.chat.id, user_id, None),
                text="- ارسل لي التحقق بخطوتين .",
                filters=filters.text,
                timeout=300,
            )
        except ListenerTimeout:
            return Opleech.send_message(
                user_id,
                "- وين رحت ترى تأخرت .",
                reply_markup=retry_key,
            )

        if await cancelled(pwd):
            return
        pwd = pwd.text

        try:
            if telethon:
                await client.sign_in(password=pwd)
            else:
                await client.check_password(password=pwd)
        except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
            return await Opleech.send_message(
                user_id,
                "- باسورد تحقق بخطوتين غلط حب .",
                reply_markup=retry_key,
            )

    except Exception as ex:
        return await Opleech.send_message(user_id, f"Error: <code>{str(ex)}</code>")

    try:
        txt = "- تم استخراج {0} بنجاح {1} \n\n- المطور : @RR8R9 \n-قناة المطور : @xl444"
        if telethon:
            string_session = client.session.save()
            await client.send_message(
                "me",
                txt.format(ty, string_session, SUPPORT_CHAT),
                link_preview=False,
                parse_mode="html",
            )
            # await client(JoinChannelRequest("@ultroidofficial_chat"))
        else:
            string_session = await client.export_session_string()
            await client.send_message(
                "me",
                txt.format(ty, string_session, SUPPORT_CHAT),
                disable_web_page_preview=True,
            )
            # await client.join_chat("ultroidofficial_chat")
    except KeyError:
        pass
    try:
        await client.disconnect()
        await Opleech.send_message(
            chat_id=user_id,
            text=f"- تم استخراج {ty} بنجاح .\n- تم الكود الى رسائلك المحفوضة .",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="- الرسائل المحفوضة .",
                            url=f"tg://openmessage?user_id={user_id}",
                        )
                    ]
                ]
            ),
            disable_web_page_preview=True,
        )
    except:
        pass

async def cancelled(message):
    if "الغاء" in message.text:
        await message.reply_text(
            "- تم الإلغاء بنجاح .", reply_markup=retry_key
        )
        return True
    elif "ريستارت" in message.text:
        await message.reply_text(
            "- تم اعادة تشغيل البوت .", reply_markup=retry_key
        )
        return True
    elif message.text.startswith("/"):
        await message.reply_text(
            "- تم الإلغاء بنجاح .", reply_markup=retry_key
        )
        return True
    else:
        return False
