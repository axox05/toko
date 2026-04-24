#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, certifi

if not os.path.isdir('dbs'):
    os.mkdir('dbs')

# الملف منشور بواسطة المبرمج ابو حمزه
# حقوقي شرف امك اذا شوفت الملف بغير حقوقي بنهك عرضك
# مبرمج الملف @FFJFF5
# قناة النشر @EgyCodes

from pyrogram import Client,errors
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton as btn
from telebot.types import InlineKeyboardMarkup as mk
from telebot.types import KeyboardButton as kb
from telebot.types import ReplyKeyboardMarkup as rep
import threading
from telebot import types
import asyncio
from Plugins.apis import *
from Plugins.SessionConverter import *
from kvsqlite.sync import Client as uu
import zipfile
import time
import re
from telethon import TelegramClient
from telethon.sessions import StringSession
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
    
if not os.path.isdir('dbs'):
    os.mkdir('dbs')

def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

new_loop = asyncio.new_event_loop()
t = threading.Thread(target=start_loop, args=(new_loop,))
t.start()

db_path = 'dbs/AbuHamza.v2'
db_folder = 'dbs/'
db = uu('dbs/AbuHamza.v2', 'bot')

# الملف منشور بواسطة المبرمج ابو حمزه
# حقوقي شرف امك اذا شوفت الملف بغير حقوقي بنهك عرضك
# مبرمج الملف @FFJFF5
# قناة النشر @EgyCodes

if not db.exists("accounts"):
    db.set("accounts", [])
App = app()

Dzz = 00000

api_id = '22256614'
api_hash = '4f9f53e287de541cf0ed81e12a68fa3b'

TOKEN = "000000" 

back = rep(row_width=2, resize_keyboard=True)

bot = telebot.TeleBot(TOKEN, threaded=False, num_threads=55, skip_pending=True, parse_mode="html", disable_web_page_preview=True)
print(bot)

@bot.message_handler(commands=['start'])
def Admin(message):
    if message.chat.id != Dzz:
        return
    
    try:
        accs = db.get("accounts") or []
        
        btn0 = InlineKeyboardButton("قسم الحسابات", callback_data="lacc")
        btn3 = InlineKeyboardButton("قسم النقل", callback_data="naql")
        btn2 = InlineKeyboardButton(f"عدد الحسابات : {len(accs)}", callback_data="account_count")
        stop = InlineKeyboardButton("ايقاف النقل", callback_data="stop_transfer")
        shrot = InlineKeyboardButton("الشروط", callback_data="shrot")
        abu = InlineKeyboardButton("المبرمج", url="t.me/FFJFF5")
        
        markup = InlineKeyboardMarkup([
            [btn2],
            [btn3, btn0],
            [stop],
            [abu, shrot]
        ])
        
        bot.send_message(
            message.chat.id,
            "مرحبا بك عزيزي المستخدم* \n\n• انا بوت نقل اعضاء متطور \n\n*المميزات* : \n🔓 نقل ظاهر \n🔐 نقل مخفي \n🧩 نقل للمجموعات انشاء جديد\n🚀 سرعة نقل عاليه",
            reply_markup=markup,
        )
    
    except Exception as e:
        bot.send_message(message.chat.id, f"حدث خطأ: {str(e)}")

@bot.callback_query_handler(func=lambda call: call.data.startswith("home"))
def home(call):
    try:
        accs = db.get("accounts") or []
        
        btn0 = InlineKeyboardButton("قسم الحسابات", callback_data="lacc")
        btn3 = InlineKeyboardButton("قسم النقل", callback_data="naql")
        btn2 = InlineKeyboardButton(f"عدد الحسابات: {len(accs)}", callback_data="account_count")
        stop = InlineKeyboardButton("إيقاف النقل", callback_data="stop_transfer")
        shrot = InlineKeyboardButton("الشروط", callback_data="shrot")
        abu = InlineKeyboardButton("المبرمج", url="t.me/FFJFF5")
        
        markup = InlineKeyboardMarkup([
            [btn2],
            [btn3, btn0],
            [stop],
            [abu, shrot]
        ])
        
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="*مرحبا بك عزيزي المستخدم*\n\n• أنا بوت نقل أعضاء متطور\n\n*المميزات*:\n🔓 نقل ظاهر\n🔐 نقل مخفي\n🧩 نقل للمجموعات إنشاء جديد\n🚀 سرعة نقل عالية",
            parse_mode="Markdown",
            reply_markup=markup
        )
        
    except Exception as e:
        bot.send_message(call.message.chat.id, f"حدث خطأ: {str(e)}")

# الملف منشور بواسطة المبرمج ابو حمزه
# حقوقي شرف امك اذا شوفت الملف بغير حقوقي بنهك عرضك
# مبرمج الملف @FFJFF5
# قناة النشر @EgyCodes

@bot.callback_query_handler(func=lambda call: call.data.startswith("lacc"))
def lacc(call):
    try:
        accs = db.get("accounts") or [] 
        
        btn0 = InlineKeyboardButton("مسح حساب", callback_data="show")
        btn1 = InlineKeyboardButton("اضافة حساب", callback_data="ssessions")
        btn2 = InlineKeyboardButton(f"عدد الحسابات: {len(accs)}", callback_data="account_count")
        btn6 = InlineKeyboardButton("تنظيف الحسابات", callback_data="clean_accounts")
        back = InlineKeyboardButton("رجوع 🔙", callback_data="home")
        
        markup = InlineKeyboardMarkup([
            [btn2],
            [btn0, btn1],
            [btn6],
            [back]
        ])
        
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="مرحبا بك عزيزي المستخدم في قسم الحسابات \n\n• يمكنك اضافة وحذف حسابات من هذا القسم",
            reply_markup=markup
        )
    
    except Exception as e:
        bot.send_message(call.message.chat.id, f"حدث خطأ: {str(e)}")

@bot.callback_query_handler(func=lambda call: call.data.startswith("naql"))
def naql(call):
    try:
        btn3 = InlineKeyboardButton("مغادرة المجموعات", callback_data="confirm_logout")
        btn7 = InlineKeyboardButton("نقل مخفي", callback_data="move_hidden")
        btn8 = InlineKeyboardButton("نقل ظاهر", callback_data="move_visible")
        stop = InlineKeyboardButton("إيقاف النقل", callback_data="stop_transfer")
        btn5 = InlineKeyboardButton("رجوع 🔙", callback_data="home")
        
        markup = InlineKeyboardMarkup([
            [btn8, btn7],  
            [btn3],        
            [stop],        
            [btn5]         
        ])
        
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="مرحبا بك عزيزي المستخدم في قسم النقل \n\n• نقل ظاهر \n• نقل مخفي \n• تحكم بالعملية",
            reply_markup=markup
        )
    
    except Exception as e:
        bot.send_message(call.message.chat.id, f"حدث خطأ: {str(e)}")

# الملف منشور بواسطة المبرمج ابو حمزه
# حقوقي شرف امك اذا شوفت الملف بغير حقوقي بنهك عرضك
# مبرمج الملف @FFJFF5
# قناة النشر @EgyCodes

@bot.callback_query_handler(func=lambda call: call.data.startswith("ssessions"))
def ssessions(call):
    try:
        btn3 = InlineKeyboardButton("استخراج كود جلسة", url="https://telegram.tools/session-string-generator#pyrogram,user")
        btn5 = InlineKeyboardButton("رجوع 🔙", callback_data="gghhh")
        
        markup = InlineKeyboardMarkup([
            [btn3],            
            [btn5]         
        ])
        
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="🧩 ارسل كود جلسة بايروجرام الخاص بالحساب\n\n📛 يجب استخراجه من الزر الموجود بالأسفل",
            reply_markup=markup
        )
        bot.register_next_step_handler(call.message, AddAccount)
    
    except Exception as e:
        bot.send_message(call.message.chat.id, f"حدث خطأ: {str(e)}")

@bot.callback_query_handler(func=lambda call: call.data.startswith("shrot"))
def shrot(call):
    
    keyboard = [
        [InlineKeyboardButton(text="رجــوع 🔙", callback_data="home")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=(
            f"❗ شروط الاستخدام :\n\n"
            "① اذا كنت سوف تستخدم اقل من 20 حساب لا تجعل التخزين اكثر من 500 عضو \n"
            "② اترك فاصل بين عمليات النقل على الاقل ساعة \n"
            "③ النقل المخفي اجعل الفاصل الزمني به كبير نسيبيا لانه يسبب ضغط كبير على الحسابات\n"
            "④ الحد الاقصى في اليوم للجروب 1k بسبب قيود تليجرام"
        ),
        reply_markup=reply_markup,
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith("accountdr_"))
def handle_account_selection(call):
    account_index = int(call.data.split('_')[1])
    load_ = db.get('accounts')
    account = load_[account_index]
    
    keyboard = [
        [InlineKeyboardButton(text="حذف الحساب", callback_data=f"delete_{account_index}")],
        [InlineKeyboardButton(text="رجــوع 🔙", callback_data="show")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=(
            f"📞 *حساب :* {account['phone_number']}\n\n"
            "اختر من الخيارات أدناه لإجراء العملية المطلوبة."
        ),
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# الملف منشور بواسطة المبرمج ابو حمزه
# حقوقي شرف امك اذا شوفت الملف بغير حقوقي بنهك عرضك
# مبرمج الملف @FFJFF5
# قناة النشر @EgyCodes

@bot.callback_query_handler(func=lambda call: call.data.startswith("show"))
def show_accounts(call):   
    load_ = db.get('accounts')
    if len(load_) == 0:
        bot.send_message(call.message.chat.id, "⚠️ لا توجد حسابات مسجلة.")
        return
    
    keyboard = []
    for i in range(0, len(load_), 2):
        row = []
        row.append(
            InlineKeyboardButton(
                text=f"{load_[i]['phone_number']}",
                callback_data=f"accountdr_{i}"
            ))
        if i + 1 < len(load_):
            row.append(
                InlineKeyboardButton(
                    text=f"{load_[i + 1]['phone_number']}",
                    callback_data=f"accountdr_{i + 1}"
                ))
        keyboard.append(row)
    
    keyboard.append([InlineKeyboardButton(text="🔙 رجوع", callback_data="home")])
   
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="📑 هذه قائمة بالحسابات المسجلة في البوت \n\n- اضغط على زر الحساب لإدارة جلسته.",
        reply_markup=reply_markup
    )    

@bot.callback_query_handler(func=lambda call: call.data.startswith("delete_"))
def delete_account(call):
    account_index = int(call.data.split('_')[1])
    load_ = db.get('accounts')
    account = load_[account_index]
    
    load_.remove(account)
    db.set("accounts", load_)
    
    bot.send_message(call.message.chat.id, "🗑 تم حذف الحساب بنجاح.")
    
import config

@bot.callback_query_handler(func=lambda call: call.data == "stop_transfer")
def stop_transfer(call):
    if not config.transfer_active:
        bot.answer_callback_query(call.id, text="⚠️ عملية النقل متوقفة بالفعل")
    else:
        config.transfer_active = False 
        bot.answer_callback_query(call.id, text="✅ تم إيقاف عملية النقل")
        
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="❌ **تم إلغاء عملية النقل بنجاح**",
            parse_mode="Markdown"
        )
    
# الملف منشور بواسطة المبرمج ابو حمزه
# حقوقي شرف امك اذا شوفت الملف بغير حقوقي بنهك عرضك
# مبرمج الملف @FFJFF5
# قناة النشر @EgyCodes
    
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    message = call.message
    
    if message.chat.id != Dzz:
        return 
    bot.clear_step_handler(message)
    cid, data, = message.from_user.id, message.text
    if call.data == 'fetch_backup':
        temp_zip_path = "backup.zip"
        db_folder = "dbs" 
    
        with zipfile.ZipFile(temp_zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for filename in os.listdir(db_folder):
                file_path = os.path.join(db_folder, filename)
                if os.path.isfile(file_path):
                    zipf.write(file_path, arcname=filename)  
    
        with open(temp_zip_path, "rb") as zip_file:
            bot.send_document(call.message.chat.id, zip_file)
    
        os.remove(temp_zip_path)
    
    if call.data == 'clean_accounts':
        true, false = 0, 0
        cx = bot.send_message(call.message.chat.id, f"<strong>جاري التنظيف</strong>\n\n💹 حسابات نشطه : {true}\n📴 حسابات منتهيه : {false}")
        load_ = db.get('accounts')
        count = 0
        for i in load_:
            x = asyncio.run_coroutine_threadsafe(check(i['session']), new_loop).result()
            if x is True:
                true += 1
            else:
                false += 1
                load_.remove(i)
                db.set("accounts", load_)
            count += 1
            if count % 30 == 0:
                bot.edit_message_text(chat_id=call.message.chat.id, text=f"<strong>جاري التنظيف</strong>\n\n💹 حسابات نشطه : {true}\n📴 حسابات منتهيه : {false}", message_id=cx.message_id)
        bot.edit_message_text(chat_id=call.message.chat.id, text=f"<strong>تم تنظيف الحسابات ✅</strong>\n\n💹 حسابات نشطه : {true}\n📴 حسابات منتهيه : {false}", message_id=cx.message_id) 
   
    if call.data == 'confirm_logout':
        msg = bot.send_message(call.message.chat.id, '• تم بدء مغادرة كل المجموعات 🚀')
        acc = db.get('accounts')
        true = 0
        for amount in acc:
            try:
                o = asyncio.run_coroutine_threadsafe(leave_chats(amount["session"]), new_loop).result()
                true += 1
            except Exception as e:
                continue
            bot.edit_message_text(chat_id=call.message.chat.id, text=f'• تم بنجاح الخروج من كل المجموعات \n• تم الخروج من <code>{true}</code> حساب بنجاح ', message_id=msg.message_id)
            
    if call.data == "move_visible":
        x = bot.reply_to(message, "➖] ارسل رابط الجروب المراد النقل منه", reply_markup=back)
        bot.register_next_step_handler(x, FromGroupDef)
     
    if call.data == "move_hidden":
        x = bot.reply_to(message, "➖] ارسل رابط الجروب المراد النقل منه", reply_markup=back)
        bot.register_next_step_handler(x, FromHiddenGroupDef)
        
def FromHiddenGroupDef(message):
    if message.text == "/start" or message.text == "رجوع":
        return messages(message)
    x = bot.send_message(chat_id=message.chat.id,text="➕] ارسل رابط الجروب المراد النقل اليه .", reply_markup=back)
    bot.register_next_step_handler(x, MaxHiddenDef, message.text)

# الملف منشور بواسطة المبرمج ابو حمزه
# حقوقي شرف امك اذا شوفت الملف بغير حقوقي بنهك عرضك
# مبرمج الملف @FFJFF5
# قناة النشر @EgyCodes

def MaxHiddenDef(message, FromGroup):
    if message.text == "/start" or message.text == "رجوع":
        return messages(message)
    x = bot.send_message(chat_id=message.chat.id,text="👥 ارسل عدد الاعضاء التي تريد نقلهم", reply_markup=back)
    bot.register_next_step_handler(x, TimeToAdd, FromGroup, message.text)

def TimeToAdd(message, FromGroup, ToGroup):
    if message.text == "/start" or message.text == "رجوع":
        return messages(message)
    MaxCount = message.text
    x = bot.send_message(chat_id=message.chat.id,text=f"⏱️ ارسل الفاصل الزمني بين كل عملية نقل\n\n- اذا تريده فوري ارسل 0", reply_markup=back)
    bot.register_next_step_handler(x, ToHiddenGroupDef, FromGroup, ToGroup, MaxCount)

from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

def ToHiddenGroupDef(message, FromGroup, ToGroup, MaxCount):
    if message.text == "/start" or message.text == "رجوع":
        return messages(message)
    
    try:
        if int(message.text) == 0:
            timeToAdd = 0
        else:
            fir = int(message.text) * 60
            timeToAdd = int(MaxCount) / int(fir)
            print(timeToAdd)
    except:
        return bot.reply_to(message, "⚠️ ارسل الوقت بأرقام فقط")
    
    accs = len(db.get('accounts'))
    msg = bot.reply_to(message, "🔍 جاري فحص الحسابات المحظورة قبل بدء عملية النقل")
    
    result = asyncio.run_coroutine_threadsafe(check_spam(), new_loop).result()
    if result is False:
        bot.edit_message_text(text="❌ حدث خطأ أثناء عملية فحص الحسابات. تم إيقاف عملية النقل", 
                              chat_id=message.from_user.id, message_id=msg.message_id)
        return
    else:
        accounts = len(result)
        if accounts == 0:
            bot.edit_message_text(text="⚠️ للأسف، تم إلغاء عملية النقل لأن كل الحسابات محظورة عام او الجلسات غير نشطه", 
                                  chat_id=message.from_user.id, message_id=msg.message_id)
            return
        else:
            bot.edit_message_text(text=f"<strong>- تم انتهاء عملية الفحص بنجاح ✅</strong>\n\n"
                                       f"- عدد الحسابات السليمة : {accounts}\n"
                                       f"- عدد الحسابات المحظورة : {accs - accounts}", 
                                  chat_id=message.from_user.id, message_id=msg.message_id)
    
    config.transfer_active = True
    msg = bot.send_message(chat_id=message.chat.id, text="جارٍ التجهيز لعملية النقل 🚀")
    
    list = asyncio.run_coroutine_threadsafe(app.GETuserHide(FromGroup, ToGroup, MaxCount), new_loop).result()
    numUser = len(list)
    true, false = 0, 0

    x = bot.edit_message_text(
        chat_id=message.from_user.id, 
        text=f"<strong>- تم تخزين الأعضاء بنجاح ✅</strong>\n\n"
             f"👥- تم تخزين : {MaxCount}\n"
             f"✅- متعرف عليهم : {numUser}\n\n"
             f"➖ - من : {FromGroup}\n"
             f"➕؛  الى : {ToGroup}\n\n"
             f"<strong>⏳- جارٍ متابعة نقل الأعضاء</strong>\n\n"
             f"✅- تم إضافة : {true}\n"
             f"❌- فشل إضافة : {false}", 
        message_id=msg.message_id
    )
    
    if config.transfer_active:
        threading.Thread(target=lambda: asyncio.run_coroutine_threadsafe(app.AddUsers(result, list, ToGroup, message.chat.id, bot, x.message_id, MaxCount, timeToAdd), new_loop).result()).start()
    else:
        bot.send_message(chat_id=message.chat.id, text="❌ تم إلغاء عملية النقل.")
    
def FromGroupDef(message):
    if message.text == "/start" or message.text == "رجوع":
        return messages(message)
    x = bot.send_message(chat_id=message.chat.id,text="➕ ارسل رابط الجروب المراد النقل اليه .", reply_markup=back)
    bot.register_next_step_handler(x, MaxDef, message.text)

# الملف منشور بواسطة المبرمج ابو حمزه
# حقوقي شرف امك اذا شوفت الملف بغير حقوقي بنهك عرضك
# مبرمج الملف @FFJFF5
# قناة النشر @EgyCodes

def MaxDef(message, FromGroup):
    if message.text == "/start" or message.text == "رجوع":
        return messages(message)
    x = bot.send_message(chat_id=message.chat.id,text="👥 ارسل عدد الاعضاء التي تريد نقلها", reply_markup=back)
    bot.register_next_step_handler(x, TimeToAdd2, FromGroup, message.text)

def TimeToAdd2(message, FromGroup, ToGroup):
    if message.text == "/start" or message.text == "رجوع":
        return messages(message)
    MaxCount = message.text
    x = bot.send_message(chat_id=message.chat.id,text=f"⏱️ ارسل الفاصل الزمني بين كل عملية نقل\n- ارسل عدد الوقت بالدقائق ، اذا تريده فوري ارسل 0", reply_markup=back)
    bot.register_next_step_handler(x, ToGroupDef, FromGroup, ToGroup, MaxCount)
     
import threading

def ToGroupDef(message, FromGroup, ToGroup, MaxCount):
    if message.text == "/start" or message.text == "رجوع":
        return messages(message)
    
    try:
        if int(message.text) == 0:
            timeToAdd = 0
        else:
            fir = int(message.text) * 60
            timeToAdd = int(MaxCount) / int(fir)
            print(timeToAdd)
    except:
        return bot.reply_to(message, "⚠️ ارسل الوقت بارقام فقط")
    
    msg = bot.reply_to(message, "🔍 جاري فحص الحسابات المحظورة قبل اتمام عملية النقل")
    accs = len(db.get('accounts'))
    result = asyncio.run_coroutine_threadsafe(check_spam(), new_loop).result()
    
    if result is False:
        bot.edit_message_text(text="❌ حدث خطأ أثناء عملية فحص الحسابات. تم إيقاف عملية النقل", 
                              chat_id=message.from_user.id, message_id=msg.message_id)
        return
    else:
        accounts = len(result)
        if accounts == 0:
            bot.edit_message_text(text="⚠️ للأسف، تم إلغاء عملية النقل لأن كل الحسابات محظورة عام او الجلسات غير نشطه", 
                                  chat_id=message.from_user.id, message_id=msg.message_id)
            return
        else:
            bot.edit_message_text(text=f"<strong>تم انتهاء عملية الفحص بنجاح ✅</strong>\n\n"
                                       f"✅- حسابات سليمة : {accounts}\n"
                                       f"❌- حسابات محظورة : {accs - accounts}", 
                                  chat_id=message.from_user.id, message_id=msg.message_id)
    
    config.transfer_active = True
    msg = bot.reply_to(message, "🚀- جارٍ التجهيز لعملية النقل")
    
    list = asyncio.run_coroutine_threadsafe(app.GETuserUnHide(FromGroup, ToGroup, MaxCount), new_loop).result()
    numUser = len(list)
    true, false = 0, 0
    
    x = bot.edit_message_text(
        chat_id=message.from_user.id, 
        text=f"<strong>تم بدء عملية النقل</strong>\n\n"
             f"👥- العدد المطلوب : {MaxCount}\n"
             f"🗃- تم تخزين : {numUser}\n\n"
             f"➖- من : {FromGroup}\n"
             f"➕- إلي : {ToGroup}\n\n"
             f"<strong>⏳- جارٍ إضافة الأعضاء</strong>\n\n"
             f"✅- تم إضافة : {true}\n"
             f"❌- فشل إضافة : {false}", 
        message_id=msg.message_id
    )

    if config.transfer_active:
        threading.Thread(target=lambda: asyncio.run_coroutine_threadsafe(app.AddUsers(result, list, ToGroup, message.chat.id, bot, x.message_id, MaxCount, timeToAdd), new_loop).result()).start()
    else:
        bot.send_message(chat_id=message.chat.id, text="❌ تم إلغاء عملية النقل.")
    
# الملف منشور بواسطة المبرمج ابو حمزه
# حقوقي شرف امك اذا شوفت الملف بغير حقوقي بنهك عرضك
# مبرمج الملف @FFJFF5
# قناة النشر @EgyCodes
    
import asyncio
from pyrogram import Client, errors
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def AddAccount(message):
    if message.text == "/start" or message.text == "رجوع":
        return messages(message)
    try:
        if "1" in message.text or ":" in message.text: 
            session_string = message.text.strip() 
            _client = Client(
                "::memory::", 
                api_id=api_id,
                api_hash=api_hash,
                session_string=session_string,
                device_model="@FFJFF5",
                system_version="@EgyCodes",
                app_version="11.4.2",
                lang_code="en"
            )
            try:
                _client.connect() 
                
                if _client.is_connected:
                    session_info = _client.export_session_string()
                    me = _client.get_me()
                    
                    data = {
                        "phone_number": getattr(me, "phone_number", "Unknown"),
                        "user_id": me.id,
                        "first_name": getattr(me, "first_name", "Unknown"),
                        "username": getattr(me, "username", "Unknown"),
                        "two-step": "None",
                        "session": session_info,
                        "session_type": "string" 
                    }
                    
                    accounts = db.get("accounts") or []
                    accounts.append(data)
                    db.set("accounts", accounts)
                    
                    cccc = InlineKeyboardButton("اضف حساب اخر", callback_data="session")
                    markup = InlineKeyboardMarkup(
                        inline_keyboard=[
                            [cccc],
                        ]
                    )
                    
                    bot.send_message(
                        message.chat.id,
                        f"✅ تم تسجيل الدخول بنجاح\n\n"
                        f"👤- الاسم : {me.first_name}\n"
                        f"📞- الرقم : {getattr(me, 'phone_number', 'غير معروف')}\n"
                        f"🆔- الايدي : {me.id}\n"
                        f"🔗- اليوزر : @{getattr(me, 'username', 'غير معروف')}",
                        reply_markup=markup
                    )
                    _client.disconnect() 
                else:
                    bot.send_message(
                        message.chat.id,
                        "❌ فشل تسجيل الدخول! يرجى التحقق من كود الجلسة.",
                        reply_markup=back
                    )
            except errors.SessionPasswordNeeded:
                Mas = bot.send_message(
                    message.chat.id,
                    "🔐 هذا الحساب محمي بالتحقق بخطوتين .. ارسل كلمة سر التحقق بخطوتين"
                )
                bot.register_next_step_handler(Mas, AddSessionPassword, _client, session_string)
            except Exception as e:
                bot.send_message(
                    message.chat.id,
                    f"⚠️ حدث خطأ أثناء تسجيل الدخول: {str(e)}",
                    reply_markup=back
                )
        else:
            bot.send_message(
                message.chat.id,
                "⚠️ صيغة كود الجلسة غير صحيحة. يرجى إرسال كود الجلسة الصحيح.",
                reply_markup=back
            )
    except Exception as e:
        bot.send_message(message.chat.id, "ERORR : " + str(e))

# الملف منشور بواسطة المبرمج ابو حمزه
# حقوقي شرف امك اذا شوفت الملف بغير حقوقي بنهك عرضك
# مبرمج الملف @FFJFF5
# قناة النشر @EgyCodes

def AddSessionPassword(message, _client, session_string):
    if message.text == "/start" or message.text == "رجوع":
        return messages(message)
    try:
        _client.check_password(message.text)
        
        session_info = _client.export_session_string()
        me = _client.get_me()
        
        data = {
            "phone_number": getattr(me, "phone_number", "Unknown"),
            "user_id": me.id,
            "first_name": getattr(me, "first_name", "Unknown"),
            "username": getattr(me, "username", "Unknown"),
            "two-step": message.text,  
            "session": session_info,
            "session_type": "string"  
        }
        
        accounts = db.get("accounts") or []
        accounts.append(data)
        db.set("accounts", accounts)
        
        cccc = InlineKeyboardButton("اضف حساب اخر", callback_data="session")
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [cccc],
            ]
        )
        
        bot.send_message(
            message.chat.id,
            f"✅ تم تسجيل الدخول بنجاح\n\n"
            f"👤- الاسم : {me.first_name}\n"
            f"📞- الرقم : {getattr(me, 'phone_number', 'غير معروف')}\n"
            f"🆔- الايدي : {me.id}\n"
            f"🔗- اليوزر : @{getattr(me, 'username', 'غير معروف')}",
            reply_markup=markup
        )
        _client.disconnect()
    except Exception as e:
        bot.send_message(
            message.chat.id,
            f"❌ التحقق بخطوتين غير صحيح",
            reply_markup=back
        )
        _client.disconnect()
          
bot.infinity_polling(none_stop=True,timeout=15, long_polling_timeout =15)