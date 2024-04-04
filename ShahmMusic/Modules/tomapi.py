import asyncio
import os
from pyrogram.types import CallbackQuery
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified



@app.on_message(
    filters.command("help")
    
)
async def cr_source(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/3e5039ee25df9814417c8.jpg",
        caption=f"""** 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 coffee**\nمرحبا بك عزيزي {message.from_user.mention}\nانا بوت الذكاء الاصطناعي الخاص بسورس حياه \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n** 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "طريقة الإستخدام", callback_data="usage"), 
                 ],[
                    InlineKeyboardButton(
                        "cσffєє", url=f"https://t.me/KOK0KK"),
                    InlineKeyboardButton(
                        "حسابي الثاني", url=f"https://t.me/l_s_I_I"),
                ],[
                
                    InlineKeyboardButton(
                        "★ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 cσffєє⚡", url=f"https://t.me/K_OK0KK"),
                ],

            ]

        ),

    )

    
@app.on_callback_query(filters.regex("usage"))
async def cr_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""** 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 cσffєє**
★¦ اهلا بك عزيزي في قسم الأوامر
★¦ لتتمكن من تشغيل الذكاء الاصطناعي فقط اكتب
★¦ /gpt - لـلـسـؤال آي سـؤال بالـذكـاء الاسـطـناعي

** 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 cσffєє**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "العودة", callback_data="back"), 
                ]
            ]
        )
    )

    
@app.on_callback_query(filters.regex("back"))
async def cr_back(_, callback_query: CallbackQuery):
    message = callback_query.message
  
    await message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("طريقة الإستخدام", callback_data="دليل")],
            [InlineKeyboardButton("cσffєє", url=f"https://t.me/KOK0KK"),
             InlineKeyboardButton("حسابي الثاني", url=f"https://t.me/l_s_I_I")],
            [InlineKeyboardButton("★ 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 cσffєє⚡", url=f"https://t.me/K_OK0KK")],
        ]
    ))

