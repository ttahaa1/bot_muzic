import asyncio


import random
from coffee import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from strings.filters import command
from pyrogram import Client
from config import OWNER_ID, MUSIC_BOT_NAME
from pyrogram import filters

txt = [

            f"بطل كذب🙁🙁🙁",


            f"نعشقكك😻🫶",
            

            f"ونا نكرهك🙃🙃",
            
            
            f"اكذب على غيري😒😒",
            
            
            f"انا بحب رودي",
            
           
            f"انا بحب كوفي",
            
            
            f"انا بحب انكل",       
            
            
            f"انا بحب سبيد",
            
            
            f"انا بحب جنازة",
            
            
            "ﺷِﻧڻ تـبـي🙂😒",
           

            
 
            
            

        ]
txt1 = [

            f"**انمووت فيكك يا مطوري الغالي**",


            f"**احلى كلمه سمعتهاا نرجا فيها ليا سننين 😻🫶**",
            

            f"**ننععليي منكككك**",
            
            f"*انمووتتت فييككك**",
           
            
            
 
            
            

        ]



        


@app.on_message(command(["بحبك"]))


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
       
     
        
