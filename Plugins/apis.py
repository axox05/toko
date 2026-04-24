#!/usr/bin/env python
# -*- coding: utf-8 -*-

# الملف منشور بواسطة المبرمج ابو حمزه
# حقوقي شرف امك اذا شوفت الملف بغير حقوقي بنهك عرضك
# مبرمج الملف @FFJFF5
# قناة النشر @EgyCodes

import random, threading, asyncio, os, string,re
from pyrogram import Client
from kvsqlite.sync import Client as uu
from telethon import TelegramClient, functions as functele, types
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telethon.errors.rpcerrorlist import UserDeactivatedBanError
from telethon.sessions import StringSession
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon.tl.functions.account import GetAuthorizationsRequest
from telethon.tl.functions.messages import GetHistoryRequest
from Plugins.SessionConverter import *

def detect(text):
    pattern = r'https:\/\/t\.me\/\+[a-zA-Z0-9]+'
    match = re.search(pattern, text)
    return match is not None
    
api_id = "22256614"
api_hash = "4f9f53e287de541cf0ed81e12a68fa3b"

db = uu('dbs/AbuHamza.v2', 'bot')

# الملف منشور بواسطة المبرمج ابو حمزه
# حقوقي شرف امك اذا شوفت الملف بغير حقوقي بنهك عرضك
# مبرمج الملف @FFJFF5
# قناة النشر @EgyCodes

import config
import asyncio
from time import time

class app:
    async def AddUsers(accounts, FromGroup, ToGroup, id, bot, mid, MaxCount, delay):
        true = 0
        false = 0
        list = accounts
        usersAdd = 1
        ToGroup = ToGroup.split("/")[3]
        added_users = set() 
        last_action_time = 0
        request_count = 0   
        
        while FromGroup and config.transfer_active:
            for name in list:
                if not config.transfer_active:
                    return
                
                try:
                    async with Client("::memory::", api_id, api_hash, no_updates=True, in_memory=True, lang_code="ar", session_string=name["session"]) as app:
                        try:
                            await app.join_chat(ToGroup)
                        except Exception as e:
                            print(f"❌ فشل الانضمام للمجموعة {ToGroup}: {e}")
                            false += 1
                            continue

                        for user in FromGroup.copy(): 
                            if not config.transfer_active:
                                return
                            
                            username = user.replace("@", "").strip()
                            username = "@" + username
                            
                            if username in added_users:
                                FromGroup.remove(user)
                                continue
                            
                            current_time = time()
                            if current_time - last_action_time < delay:
                                remaining_delay = delay - (current_time - last_action_time)
                                await asyncio.sleep(remaining_delay)
                            
                            request_count += 1
                            if request_count >= 5: 
                                await asyncio.sleep(delay * 2)
                                request_count = 0
                            
                            try:
                                await app.add_chat_members(ToGroup, user)
                                true += 1
                                added_users.add(username)
                                FromGroup.remove(user)
                                last_action_time = time()
                                
                            except Exception as e:
                                if "FLOOD_WAIT" in str(e):
                                    wait_time = 10
                                    if "FLOOD_WAIT_" in str(e):
                                        try:
                                            wait_time = int(str(e).split("FLOOD_WAIT_")[1].split(")")[0])
                                        except:
                                            pass
                                    print(f"⚠️ انتظار {wait_time} ثانية بسبب Flood...")
                                    await asyncio.sleep(wait_time)
                                    continue
                                
                                print(f"❌ خطأ مع المستخدم {user}: {e}")
                                false += 1
                                await asyncio.sleep(delay)
                            
                            keyboard = InlineKeyboardMarkup()
                            stop_button = InlineKeyboardButton("إيقاف النقل", callback_data="stop_transfer")
                            keyboard.add(stop_button)
                            
                            try:
                                await bot.edit_message_text(
                                    chat_id=id,
                                    text=f"<strong>- تم بدء عملية النقل 🚀</strong>\n\n"
                                         f"➕] إلي : @{ToGroup}\n\n"
                                         f"<strong>• جارٍ إضافة الأعضاء ⏳</strong>\n\n"
                                         f"👥] العدد المخزن : {MaxCount}\n\n"
                                         f"✅] تم إضافة : {true}\n"
                                         f"❌] فشل إضافة : {false}\n"
                                         f"❕] متبقي للإضافة : {len(FromGroup)}",
                                    message_id=mid,
                                    reply_markup=keyboard
                                )
                            except Exception as e:
                                print(f"⚠️ خطأ في تحديث الرسالة: {e}")

                except Exception as a:
                    print(f"⚠️ فشل إنشاء جلسة للعميل: {a}")
                    false += 1
                    await asyncio.sleep(delay)
                    continue
        
        try:
            await bot.send_message(
                chat_id=id,
                text=f"<strong>تم اكتمال عملية النقل ✅</strong>\n\n"
                     f"➕] إلي : https://t.me/{ToGroup}\n\n"
                     f"👥] العدد المخزن : {MaxCount}\n\n"
                     f"✅] تم إضافة : {true}\n\n"
                     f"❌] فشل إضافة : {false}",
                parse_mode="HTML"
            )
        except Exception as e:
            print(f"⚠️ خطأ في إرسال رسالة الإكتمال: {e}")
        
    async def GETuserUnHide(FromGroup, ToGroup, MaxCount):
        ToGroup = ToGroup.split("/")[3]
    
        list = db.get("accounts")
        name = random.choice(list)
    
        members = []
    
        async with Client(
            "::memory::", 
            api_id, 
            api_hash, 
            no_updates=True, 
            in_memory=True, 
            lang_code="ar", 
            session_string=name["session"]
        ) as app:
        
            await app.join_chat(ToGroup)
        
            if detect(FromGroup):
                print(True)
                FromGroup = FromGroup
                await app.join_chat(FromGroup)
                chat = await app.get_chat(FromGroup)
                FromGroup = chat.id
            else:
                FromGroup = FromGroup.split("/")[3]
                print(False)
        
            async for member in app.get_chat_members(FromGroup):
                try:
                    if member.user.username and member.user.username not in members:
                        members.append(member.user.username)
                    
                        if len(members) >= int(MaxCount):
                            print(members)
                            return members
                except Exception as a:
                    pass
    
        return members
    
    async def GETuserHide(FromGroup, ToGroup, MaxCount):
        ToGroup = ToGroup.split("/")[3]
        list = db.get("accounts")
        members = []
        
        session = random.choice(list)
        async with Client("::memory::", api_id, api_hash,no_updates=True,in_memory=True,lang_code="ar",session_string=session["session"]) as app:
            try:
                await app.join_chat(ToGroup)
            except:
                pass
            if detect(FromGroup):
                print(True)
                FromGroup = FromGroup
                await app.join_chat(FromGroup)
                chat = await app.get_chat(FromGroup)
                FromGroup = chat.id
            else:
                FromGroup = FromGroup.split("/")[3]
                print(False)
            async for message in app.get_chat_history(FromGroup):
                try:
                    if message.from_user.username != None and message.from_user.username not in members:
                        members.append(message.from_user.username)
                        if len(members) >= int(MaxCount):
                            print(members)
                            return members
                    
                except Exception as a:
                    pass
        return members

# الملف منشور بواسطة المبرمج ابو حمزه
# حقوقي شرف امك اذا شوفت الملف بغير حقوقي بنهك عرضك
# مبرمج الملف @FFJFF5
# قناة النشر @EgyCodes

async def check_spam():
    try:
        lists = []
        list = db.get("accounts")
        for i in list:
            c = Client('::memory::', in_memory=True, api_hash='4f9f53e287de541cf0ed81e12a68fa3b', api_id=22256614,lang_code="ar", no_updates=True, session_string=i["session"])
            try:
            	await c.start()
            except:
            	continue
            try:
                await c.send_message('SpamBot', "/start")
                await asyncio.sleep(1)
                async for message in c.get_chat_history("SpamBot", limit=1):
                    try:
                        if "لاتوجد قيود" in str(message.text) or "Good news" in str(message.text):
                            lists.append(i)
                        elif "للأسف" in str(message.text) or "sorry" in str(message.text):
                            break
                    except Exception as a:
                        print(a)
                        pass
            except:
                continue
        return lists
    except Exception as a:
        print(a)
        return False
    return False
 
# الملف منشور بواسطة المبرمج ابو حمزه
# حقوقي شرف امك اذا شوفت الملف بغير حقوقي بنهك عرضك
# مبرمج الملف @FFJFF5
# قناة النشر @EgyCodes
 
async def check(session):
    c = Client('::memory::', in_memory=True, api_hash='4f9f53e287de541cf0ed81e12a68fa3b', api_id=22256614,lang_code="ar", no_updates=True, session_string=session)
    try:
        await c.start()
    except:
        return False
        
    try:
        await c.get_me()
    except:
        return False
    return True

# الملف منشور بواسطة المبرمج ابو حمزه
# حقوقي شرف امك اذا شوفت الملف بغير حقوقي بنهك عرضك
# مبرمج الملف @FFJFF5
# قناة النشر @EgyCodes

async def leave_chats(session: str):
    c = Client('::memory::', in_memory=True, api_hash='4f9f53e287de541cf0ed81e12a68fa3b', api_id=22256614,lang_code="ar", no_updates=True, session_string=session)
    try:
        await c.start()
        
    except:
        return False
    types = ['ChatType.CHANNEL', 'ChatType.SUPERGROUP', 'ChatType.GROUP']
    
    async for dialog in c.get_dialogs():
        if str(dialog.chat.type) in types:
            id = dialog.chat.id
            try:
                await c.leave_chat(id)
            except:
                continue
        else:
            continue
    await c.stop()
    return True