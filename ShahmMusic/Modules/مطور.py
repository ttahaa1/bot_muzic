import asyncio


import random
from coffee import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from strings.filters import command
from pyrogram import filters, Client
import config



txt = [

            "تعاال يامطووري يبووك @KOK0KK 🥺❤",


             "هذا مطوري @KOK0KK🥺❤",
            

             "يببووكككككككك @KOK0KK 🙂😒",
            
           
 
            
            

        ]


        


@app.on_message(command(["احح","اححح","احححح"]))


async def cutt(client: Client, message: Message):


      a = random.choice(txt)


      await message.reply(


        f"{a}")
