

import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

 #ccccc      ooooo    fffffff  fffffff  eeeeeee
 #c          o    o   f        f        e
 #c          o    o   fffff    fffff    eeeee
 #c          o    o   f        f        e
 #ccccc      ooooo    f        f        eeeeeee




@app.on_message(
    command(["ميمز","مميزات","مميزات"])
 )
async def mmmezat(client, message):
        await message.reply_text(f"""**مرحبآ بك عزيزي » {message.from_user.mention}**في قسم مميزات سورس حياه ميوزك\n
𓏺𝙎𝙊𝙐𝙍𝘾𝞝 cσffєє

**𖢿قايمه مميزات سورس حياه الليبي

𖢿ميزه ⦂ المطور بيجيب المطور البوت 
𖢿ميزه ⦂ تبيه بفتح+قفل المكالمه
𖢿ميزه ⦂ ترحيب دخول و خروج الاعضاء 
𖢿ميزه ⦂ جروب بيجيب الجروب+الرابط+ايدي
𖢿ميزه ⦂ قول البوت بيقول بالكلمه اللي بتقولها 
𖢿ميزه ⦂ الالعاب +كت+تويت+العاب متطوره
𖢿ميزه ⦂ تلغراف ميديا بردعالصوره
𖢿ميزه ⦂ ايدي بالرد بالصوره
𖢿ميزه ⦂ صورتي يرد بالصوره ونسبه
𖢿ميزه ⦂ اذاعه خاص+بالتثبيت+بالمساعد+عام
𖢿ميزه ⦂ الصوتيه..ف المكالمه
𖢿ميزه ⦂ نزول تلقائي للمساعد لعدم وجود حد فالمكالمه
𖢿ميزه ⦂ بث مباشر للقنوات 
𖢿ميزه ⦂ اسمي بيجب الاسم
𖢿ميزه ⦂ سورس بيجب السورس
𖢿ميزه ⦂ حظر+كتم ميوزك
𖢿ميزه ⦂ كشف
𖢿ميزه ⦂ منشن لكل الاعضاء
𖢿ميزه ⦂ انا من
𖢿ميزه ⦂ رتبتي
𖢿ميزه ⦂ مبرمج
𖢿ميزه ⦂ المنشئ+المالك
𖢿ميزه ⦂ الاحصائيات
𖢿ميزه ⦂ كيب المطور من خلاله تتحكم في الحساب المساعد
𖢿ميزه ⦂ الاذكار
𖢿ميزه ⦂ تبيه بوقت صلاه
𖢿ميزه ⦂ دعوه في مكالمه
𖢿ميزه ⦂  دعوه فالخاص متاع البوت
𖢿ميزه ⦂ تنبيه..بانضمام بوت في الجروبات
𖢿ميزه ⦂ غنيلي 
𖢿ميزه ⦂ بايو
𖢿ميزه ⦂ خروج المساعد من جروبات لعدم تقطيع صوت..البوت
𖢿ميزه ⦂ اسال/اصراحه
𖢿ميزه ⦂ نكت
𖢿ميزه ⦂ ذكاء اصتناعي 
𖢿ميزه ⦂ مميزات. بيجبلك مميزات موجوده فسورس 
𖢿ميزه ⦂ رفع و تنزيل مطور 
𖢿ميزه ⦂ افلام
𖢿ميزه ⦂ مكالمات النشطه+مجموعات البوت شغال فيها
𖢿ميزه ⦂ اساله دينيه
𖢿ميزه ⦂ من في المكالمه+تعرف من فالمكالمه و عددهم
𖢿ميزه ⦂ الرابط+رابط مجموعه
𖢿افتح المكالمه يفتح المكالمه
مطـور الســـورس الوسـڪي الليبي
𓏺𝙎𝙊𝙐𝙍𝘾𝞝 cσffєє
لتنصيب بوت مشابه تواصل معي فالخاص @KOK0KK
**""",


        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★𓏺𝙎𝙊𝙐𝙍𝘾𝞝 cσffєє⚡", url=f"https://t.me/K_OK0KK"),                        
                 ],[
                InlineKeyboardButton(
                        "اغلاق", callback_data="close"),
               ],
          ]
        ),
    )

