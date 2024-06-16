from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from MatrixMusic import app
from config import getenv


MUST_JOIN = "lggbg"


required_commands = ["تشغيل", "بوت", "ايدي", "الاوامر", "/start", "ايقاف"]




@app.on_message(filters.command(required_commands) & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(photo="https://graph.org/file/de8dc2aef9a2636c6d2a4.jpg", caption=f"↯︙ عـݪـيك اެݪاެشـتراެك فـي قـنـاެة اެݪـبـوت 📻 .\n↯︙يوزر القناة ( {link} ) .",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("اضغط هنا للاشتراك💤", url=f"{link}")]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the MUST_JOIN chat : {MUST_JOIN} !")


MUST_JOIN = "lggbg"
matrix_commands = ["تشغيل", "بوت", "ايدي", "الاوامر", "/start", "ايقاف"]


@app.on_message(filters.command(matrix_commands) & filters.group, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(photo="https://graph.org/file/de8dc2aef9a2636c6d2a4.jpg", caption=f"↯︙ عـݪـيك اެݪاެشـتراެك فـي قـنـاެة اެݪـبـوت 📻 .\n↯︙يوزر القناة ( {link} ) .",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("اضغط هنا للاشتراك💤", url=f"{link}")]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the MUST_JOIN chat : {MUST_JOIN} !")
