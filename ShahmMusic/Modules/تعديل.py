
# from config import OWNER_ID
# import asyncio
# from pyrogram import Client, filters
# from coffee import app
# import random
# from strings.filters import command
# from pyrogram.types import Message
# from pyrogram.enums import ParseMode, ChatMemberStatus
# iddof = []

# @app.on_message(
#      command(["تعطيل التعديل"])
#      & filters.group

   
# )
# async def iddlock(client:Client, message:Message):
#     get = await client.get_chat_member(message.chat.id, message.from_user.id)
#     if get.status in [ChatMemberStatus.ADMINISTRATOR]:
#          rotba = "الادمن"
#     elif get.status in [ChatMemberStatus.OWNER]:
#          rotba = "المالك"
#     else:
#         return await message.reply_text(f"**يا {message.from_user.mention} انت لست مشرفا هنا**")    
#     dev = (OWNER_ID)
#     get = await client.get_chat_member(message.chat.id, message.from_user.id)
#     if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
#         if message.chat.id in iddof:
#             return await message.reply_text(f"يا {message.from_user.mention}\n التعديل معطل من قبل")
#         iddof.append(message.chat.id)
#         return await message.reply_text(f"تم تعطيل التعديل بنجاح\n\n بواسطة {rotba}←{message.from_user.mention}")
#     else:
#         return await message.reply_text(f"**يا {message.from_user.mention} انت لست مشرفا هنا**")
# ##|cσffєє
# @app.on_message(
#     command(["تفعيل التعديل"])
#     & filters.group
# )
# async def idljjopen(client:Client, message:Message):
#     get = await client.get_chat_member(message.chat.id, message.from_user.id)
#     if get.status in [ChatMemberStatus.ADMINISTRATOR]:
#          rotba = "الادمن"
#     elif get.status in [ChatMemberStatus.OWNER]:
#          rotba = "المالك"
#     else:
#         return await message.reply_text(f"**يا {message.from_user.mention} انت لست مشرفا هنا**")    
#     dev = (OWNER_ID)
#     get = await client.get_chat_member(message.chat.id, message.from_user.id)
#     if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
#       if not message.chat.id in iddof:
#         return await message.reply_text(f"يا {message.from_user.mention}\nالتعديل معفل من قبل")
#       iddof.remove(message.chat.id)
#       return await message.reply_text(f"تم تفعيل التعديل بنجاح\n\n بواسطة {rotba} ←{message.from_user.mention}")

# @app.on_message(Client.edit_message_text)
# async def delete_edited_message(client:Client, message:Message):
#     if message.chat.id in iddof:
#         await client.delete_messages(chat_id=message.chat.id, message_ids=message.id)


