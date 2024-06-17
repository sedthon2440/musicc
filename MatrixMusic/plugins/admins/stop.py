from MatrixMusic.plugins.play.filters import command
from pyrogram import filters
from pyrogram.types import Message

from MatrixMusic import app
from MatrixMusic.core.call import Zelzaly
from MatrixMusic.utils.database import set_loop
from MatrixMusic.utils.decorators import AdminRightsCheck
from MatrixMusic.utils.inline import close_markup
from config import BANNED_USERS

force_btn = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(   
              text=f"𝗕𝗟𝗔𝗖𝗞 |⌯𖤒˼ ˹🖤˼", url=f"https://t.me/lggbg",)                        
        ],        
    ]
)
async def check_is_joined(message):    
    try:
        userid = message.from_user.id
        user_name = message.from_user.first_name
        status = await app.get_chat_member("lggbg", userid)
        return True
    except Exception:
        await message.reply_text(f'┇عزيزي: {message.from_user.mention}\n┇أشتࢪك في قناة البوت أولاً.\n┇قناة البوت: @lggbg 🍓. ',reply_markup=force_btn,disable_web_page_preview=False)
        return False


#comand
@app.on_message(
    command(["/stop", "اسكت", "انهاء", "ايقاف"]) & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    await Zelzaly.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    user_mention = message.from_user.mention if message.from_user else "المشـرف"
    await message.reply_text(
        _["admin_5"].format(user_mention), reply_markup=close_markup(_)
    )
