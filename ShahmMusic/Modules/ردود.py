import asyncio


import random
from coffee import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from strings.filters import command
from pyrogram import filters, Client
from config import OWNER_ID

dev = (OWNER_ID)


txt = [
            "دوٌمُ ٱڷضٍـحڪهْهْ ♥️😻",


             "ضٍـحڪڹٱ مُعُٱٱڪ🙄🙄",
            

            "ضٍـحڪڹٱ مُعُٱٱڪ🙄🙄",
            
            
            "۾ـآ ڣي ڜي يڞحـڪ يبـآڕد 😒😒",
            
            
            "ࢪبـي يـدوٍ۾ آلڞـحـڪـهہ يآﭰلبـي🥺🔥",
            
            
             "ضحكه بدون نيهه🙂😒",
            
            
 
            
            

        ]
txt1 = [

            "**دوومم ياامطوورييي♥️😻**",


             "**مطوري الغالي محلاها ضحكتك**",
            

            "**ضحكني معاك يا حبي المطور الاساسي🥺🔥**",
            
            
          
            
 
            
            

        ]

        
        


@app.on_message(command(["ههه","😂😂","😂😂😂😂😂","😂🤣","ههههههههههههههههههه","😂😂😂😂😂😂"]))


async def cutt(client: Client, message: Message):

     dev = (OWNER_ID)
     if message.from_user.id in dev:


         b = random.choice(txt1)


         await message.reply(

         f"{b}")
     else:
         a = random.choice(txt)


         await message.reply(


         f"{a}")
       
         # قائمة الردود الجديدة
txt3 = [
    "هذه رد جديدة.",
    "هذه رد جديدة أيضًا.",
    "رد جديد على الاطلاق!"
]


txt3.append("اؤمر دارك شتريد؟❤️🥺.")


txt3.append("❤️اى يقلب دارك.")


txt3.append("🙄ثانيه واحده بتشقط وجى.")


txt3.append("❤️😂شبيك لبيك.")


@app.on_message(filters.command(["كوفي"]))
async def hello(client, message):
    await message.reply(random.choice(txt3))
