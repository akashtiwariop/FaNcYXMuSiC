# OxyXmusic (Telegram bot project )
# Copyright (C) 2021 RiZoeL

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
     await message.reply_sticker("CAACAgEAAxkBAAEKSWJgwGQMxYa9he0KQnk0DQiRXs8lFAACTgIAAlEpDTkIb4MnCr3Ohx8E")
     await message.reply_text(
        f"""â ðŧðððð {message.from_user.first_name}  ð ðððĢ ðĨðĄððŪ ðĒðŠðĻðð ððĢ ðŦðĪððð ððððĐðĻ ðĪð ðððĄðððððĒ ðð§ðĪðŠðĨðĻ. ð ðððŦð ð ðĄðĪðĐ ðĪð ððĪðĪðĄ ððððĐðŠð§ð ðĐðððĐ ðŽððĄðĄ ððĒððŊð ðŪðĪðŠ â.\n\nâ ðŋðĪ ðŪðĪðŠ ðŽððĢðĐ ðĒð ðĐðĪ ðĨðĄððŪ ðĒðŠðĻðð ððĢ ðŪðĪðŠð§ ðððĄððð§ððĒ ðð§ðĪðŠðĨðĻ'ðŦðĪððð ððððĐðĻ? ððĄðððĻð ððĄððð  ðĐðð "ÆÖĘĘÉÕēÕŠs" ððŠðĐðĐðĪðĢ ðððĄðĪðŽ ðĐðĪ ð ðĢðĪðŽ ððĪðŽ ðŪðĪðŠ ðððĢ ðŠðĻð ðĒð.\n\nâ ððĻð ðĐðð ððŠðĐðĐðĪðĢðĻ ðððĄðĪðŽ ðĐðĪ ð ðĢðĪðŽ ðĒðĪð§ð ðððĪðŠðĐ ðĒð ð.\n\nâ ðð ðððð ðððððð ððððððð ððððððð ðð ððððð āĪĶāĨāĪļāĨ ÎÏīáīáÍēáŠ""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "ð cÏÐžÐžÎąÎ·âs ð", url="https://telegra.ph/N%C3%B8b%CE%90-%EA%AA%8E-M%E0%B8%99%E0%BA%AEic-06-06-2")
                  ],[
                    InlineKeyboardButton(
                        "ðĨMŨĨ OwÅeâðĨ", url="https://t.me/DesiNobita"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "âĪïļ ÏŌŌÎđcÎđÎąâ gŅÏÏÏ âĪïļ", url="https://t.me/cartoons_007"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**âĪ Music player is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ðĨMŨĨ OwÅeâ ðĨ", url="https://t.me/DesiNobita")
                ]
            ]
        )
   )
@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Here Is Cmd Of NÃļÍĒÍĒÍĒbÎ ęŠ MÍĒÍĒÍĒāļāšŪic !
ââââââââââ°âĶâąâââââââââ
/aud  - play audio or link you requested
/play  - play song you requested
/dplay  - play song you requested via deezer
/splay  - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song  - download songs you want quickly
/search  - search videos on youtube with details
/deezer  - download songs you want quickly via deezer
/saavn  - download songs you want quickly via saavn

âĒAdmins onlyâĒ
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
ââââââââââ°âĶâąâââââââââ
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "âē AssÉŠsáīáīÉīáī âģ", url="https://t.me/NoBiTa_vC_pLaYeR?startgroup=true"
                    )
                ],[
                    InlineKeyboardButton(
                        "ðą ïžŊï―ï―ï―ï― ðą", url="https://t.me/DesiNobita"
                    ),
                    InlineKeyboardButton(
                        "âáīáīáī áīáī ÉŠÉī ĘáīáīĘ ÉĒĘáīáīáīâ", url="https://t.me/NoBi_vC_PlAyEr_RoBoT?startgroup=true"
                    )
                ]
            ]
        )
    )

    
