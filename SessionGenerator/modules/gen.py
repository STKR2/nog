#YT : https://www.youtube.com/@ultroidofficial
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

from config import SUPPORT_CHAT
from SessionGenerator import Opleech
from SessionGenerator.utils import retry_key


async def gen_session(
    message, user_id: int, telethon: bool = False, old_pyro: bool = False
):
    if telethon:
        ty = f"Telethon"
    elif old_pyro:
        ty = f"Pyrogramm V1"
    else:
        ty = f"Pyrogram V2"

    await message.reply_text(f"Trying to start {ty} Session generator...")

    try:
        api_id = await Opleech.ask(
            identifier=(message.chat.id, user_id, None),
            text="❖ Mohon Masukkan API_ID:",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Opleech.send_message(
            user_id,
            "Limit Setiap 5 Menit.\n\n❖ Mohon Mulai Kembali.",
            reply_markup=retry_key,
        )

    if await cancelled(api_id):
        return

    try:
        api_id = int(api_id.text)
    except ValueError:
        return await Opleech.send_message(
            user_id,
            "API_ID Yang Anda Masukkan Tidak Valid.\n\n❖ Mohon Mulai Kembali.",
            reply_markup=retry_key,
        )

    try:
        api_hash = await Opleech.ask(
            identifier=(message.chat.id, user_id, None),
            text="❖ Sekarang Masukkan API_HASH √",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Opleech.send_message(
            user_id,
            "Limit Setiap 5 Menit.\n\n❖ Mohon Mulai Kembali.",
            reply_markup=retry_key,
        )

    if await cancelled(api_hash):
        return
    api_hash = api_hash.text

    if len(api_hash) < 30:
        return await Opleech.send_message(
            user_id,
            "API_HASH Yang Anda Masukkan Tidak Valid.\n\n❖ Mohon Mulai Kembali.",
            reply_markup=retry_key,
        )

    try:
        phone_number = await Opleech.ask(
            identifier=(message.chat.id, user_id, None),
            text="❖ Masukkan Nomor Telepon, contoh : +628231234567:",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Opleech.send_message(
            user_id,
            "Limit Setiap 5 Menit.\n\n❖ Mohon Mulai Kembali.",
            reply_markup=retry_key,
        )

    if await cancelled(phone_number):
        return
    phone_number = phone_number.text

    await Opleech.send_message(user_id, "❖ Mencoba Mengirimkan OTP Ke Nomor Anda...")
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
            f"Gagal Mengirimkan Kode.\n\n❖ Mohon Menunggu {f.value or f.x} Detik Dan Coba Lagi.",
            reply_markup=retry_key,
        )
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        return await Opleech.send_message(
            user_id,
            "API_ID Atau API_HASH Tidak Valid.\n\n❖ Mohon Mulai Kembali..",
            reply_markup=retry_key,
        )
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        return await Opleech.send_message(
            user_id,
            "Nomor Telepon Tidak Valid.\n\n❖ Mohon Mulai Kembali.",
            reply_markup=retry_key,
        )

    try:
        otp = await Opleech.ask(
            identifier=(message.chat.id, user_id, None),
            text=f"❖ Mohon Masukkan Kode OTP Yang Telah Di Kirim Ke {phone_number}.\n\n❖ Jika OTP Adalah <code>12345</code>, Mohon Masukkan Menggunakan Spasi Disetiap Karakter.\n\n❖ Contoh <code>1 2 3 4 5.</code>",
            filters=filters.text,
            timeout=600,
        )
        if await cancelled(otp):
            return
    except ListenerTimeout:
        return await Opleech.send_message(
            user_id,
            "Limit Setiap 5 Menit.\n\n❖ Mohon Mulai Kembali.",
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
            "OTP Yang Anda Masukkan <b>Salah.</b>\n\n❖ Mohon Mulai Kembali.",
            reply_markup=retry_key,
        )
    except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
        return await Opleech.send_message(
            user_id,
            "OTP Yang Anda Masukkan <b>Kedaluarsa.</b>\n\n❖ Mohon Mulai Kembali.",
            reply_markup=retry_key,
        )
    except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
        try:
            pwd = await Opleech.ask(
                identifier=(message.chat.id, user_id, None),
                text="❖ Mohon Masukkan 2 step verification password untuk melanjutkan √",
                filters=filters.text,
                timeout=300,
            )
        except ListenerTimeout:
            return Opleech.send_message(
                user_id,
                "Limit Setiap 5 Menit.\n\n❖ Mohon Mulai Kembali.",
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
                "Password Yang Anda Masukkan <b>Salah<b>.\n\n❖ Mohon Mulai Kembali.",
                reply_markup=retry_key,
            )

    except Exception as ex:
        return await Opleech.send_message(user_id, f"Error: <code>{str(ex)}</code>")

    try:
        txt = "⎙ Ini Adalah {0} String Session Anda\n\n<code>{1}</code>\n\n🦋 A String Session Bot by Cihut Bot\n☠ <b>Note :</b> Jangan Bagikan String Session Kepada Siapapun"
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
            text=f"⎙ Berhasil Membuat {ty} String Session √\n\n❖ Silahkan Cek Di Pesan Tersimpan.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Pergi Ke Pesan Tersimpan",
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
    if "/cancel" in message.text:
        await message.reply_text(
            "Cancelled the ongoing string generation process..", reply_markup=retry_key
        )
        return True
    elif "/restart" in message.text:
        await message.reply_text(
            "Successfully restarted this bot.", reply_markup=retry_key
        )
        return True
    elif message.text.startswith("/"):
        await message.reply_text(
            "Cancelled the ongoing string generation process..", reply_markup=retry_key
        )
        return True
    else:
        return False
