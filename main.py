import os
from pyrofork.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrofork import Client, filters
import redis


DEVS = [6747695334] 
API_ID = int("8186557")
API_HASH = "efd77b34c69c164ce158037ff5a0d117"
Bots = []
off =None
redus =  redis.Redis(
        host="127.0.0.1",
        port=6379,
        charset="utf-8",
        decode_responses=True
    )

bot = Client(
    "FR3ON",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token="8726080630:AAHLLglurOBNFWfGXngTMamI_NWho3bOgN8"
    )
#يوزرات المطورين المصنع
@bot.on_message(filters.private)
async def me(client, message):
   if off:
    if not message.from_user.id in DEVS:
     return await message.reply_text("☥ الوضع المجاني معطل الان  💎 .\n☥ راسل المطور لتنصيب مدفوع  💎 . \n☥ Dev : @it_Yoko 💎 .")
   message.continue_propagation()

@bot.on_message(filters.command("start") & filters.private)
@bot.on_message(filters.command("رجوع","") & filters.private)
async def start(client, message):
   if message.from_user.id in DEVS:
     kep = ReplyKeyboardMarkup([["صنع بوت", "حذف بوت"], ["البوتات المصنوعه"], ["تعطيل المجاني", "تفعيل المجاني"], ["السورس"]],resize_keyboard=True,is_persistent=True,placeholder="𝒑𝒓𝒐𝒈𝒓𝒂𝒎𝒎𝒆𝒓 𝒇𝒓𝒂𝒐𝒏")
     return await message.reply_text("اهلا بيك ف مصنع بوتات نقل اعضاء", reply_markup=kep)
   kep = ReplyKeyboardMarkup([["صنع بوت","حذف بوت"], ["السورس"]],resize_keyboard=True,is_persistent=True,placeholder="𝒑𝒓𝒐𝒈𝒓𝒂𝒎𝒎𝒆𝒓 𝒇𝒓𝒂𝒐𝒏")
   await message.reply_text("اهلا بيك ف مصنع بوتات  نقل اعضاء", reply_markup=kep)

@bot.on_message(filters.command(["السورس"], ""))
async def alivehi(client: Client, message):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("𝙶𝚁𝙾𝚄𝙿️", url=f"https://t.me/e_eeeh"),
                InlineKeyboardButton("𝚂𝙾𝚄𝚁𝙲𝙴️", url=f"https://t.me/VIPUXX"),
            ],
            [
                 InlineKeyboardButton(f"Developer💎", url=f"https://t.me/it_Yoko")
            ]
        ]
    )

    await message.reply_photo(
        photo="https://envs.sh/IZH.jpg",
        caption="",
        reply_markup=keyboard,
    )
@bot.on_message(filters.command(["تفعيل المجاني", "تعطيل المجاني"], "") & filters.private)
async def onoff(client, message):
  if not message.from_user.id in DEVS:
    return
  global off
  if message.text == "تفعيل المجاني":
    off = None
    return await message.reply_text("تم تفعيل المجاني بنجاح .")
  else:
    off = True
    await message.reply_text("تم تعطيل المجاني بنجاح .")
    
    
@bot.on_message(filters.command("صنع بوت", "") & filters.private)
async def makehelal(client, message):
  if not message.from_user.id in DEVS:
    for x in Bots:
        if x[1] == message.from_user.id:
          return await message.reply_text("لقد قمت بصنع بوت من قبل . ")
  await message.reply_text("ارسل الان توكن البوت")
  bot.register_next_step_handler(ask1)
  
async def ask1(client, message): 
  TOKEN = message.text
  if message.from_user.id in DEVS:
    await message.reply_text("ارسل الان ايدي المطور")
    user_info = {
    "TOKEN" : TOKEN
    }
    bot.register_next_step_handler(partial(ask2,user_info=user_info))
  else:
    Dev = message.from_user.id
    info={
      "TOKEN" : TOKEN,
      "Dev" : Dev,
    }
    await alldone(client, message,info)
    
async def ask2(client, message,user_info: dict): 
  try:
    Dev = int(message.text)
  except:
    return await message.reply_text("قم بارسال الايدي بشكل صحيح")
  info={
    "TOKEN" : user_info['TOKEN'],
    "Dev" : Dev,
  }
  await alldone(client, message,info)
  


async def alldone(client, message,info: dict):
  bots = Client(f"{info['TOKEN']}", api_id=API_ID, api_hash=API_HASH, bot_token=info['TOKEN'])
  try:
    await bots.start()
    username = await bots.get_me()
    username = username.username
    await bots.stop()
  except:
    return await message.reply_text("تاكد من التوكن أو الجلسة")
  id = username
  for x in Bots:
        if x[0] == id:
          return await message.reply_text("لقد قمت بصنع هذا البوت من قبل . ")
  os.system(f"cp -a source users/{id}")
  with open(f"users/{id}/sample.env", "w+", encoding="utf-8") as env:  
      x = f"BOT_TOKEN={info['TOKEN']}\nOWNER_ID={info['Dev']}"
      env.write(x)
  os.system(f"cd users/{id} && screen -d -m -S {id} python3 -m app")
  oo = [id, info['Dev']]
  Bots.append(oo)
  for i in DEVS:
    try:
      await client.send_message(i, f"تم تنصيب البوت علي سورس نقل الاعضاء 🌿♥️\nتوكن : {info['TOKEN']}\nاليوزر : @{username}")
    except:
      pass
  os.remove(f"{info['TOKEN']}")
  await message.reply_text(f"تم تنصيب البوت علي سورس نقل الاعضاء 🌿♥️\nتوكن : {info['TOKEN']}\nاليوزر : @{username}")



@bot.on_message(filters.command("حذف بوت", "") & filters.private)
async def deletbothelal(client, message):
   if not message.from_user.id in DEVS:
     for x in Bots:
         bot = x[0]
         if x[1] == message.from_user.id:       
           os.system(f"sudo rm -fr users/{bot}")
           os.system(f"screen -XS {bot} quit")
           Bots.remove(x)
           return await message.reply_text("تم حذف بوتك من الصانع .")
     return await message.reply_text("لم تقم بصنع بوتات")
   try:
      bot = await client.ask(message.chat.id, "هات يوزر البوت", timeout=200)
   except:
      return
   bot = bot.text.replace("@", "")
   for x in Bots:
       if x[0] == bot:
          Bots.remove(x)
   os.system(f"sudo rm -fr users/{bot}")
   os.system(f"screen -XS {bot} quit")
   await message.reply_text("تم حذف البوت بنجاح")


@bot.on_message(filters.command("البوتات المصنوعه", ""))
async def bothelal(client, message):
  if not message.from_user.id in DEVS:
   return
  o = 0
  text = "قايمه البوتات\n"
  for x in Bots:
      o += 1
      text += f"{o}- @{x[0]}\n"
  if o == 0:
    return await message.reply_text("لا يوجد بوتات مصنوعه")
  await message.reply_text(text)


if __name__ == "__main__":
    bot.run()