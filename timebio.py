from telethon.errors import FloodWaitError
from telethon import TelegramClient,functions, events
from datetime import datetime
import pytz ,aiocron, asyncio, random, os
from telethon.tl.functions.account import UpdateProfileRequest
# ============= #
api_id, api_hash = 2909555, "34ca9900dd5223fbc7b3e9a305764c3f"
# ============= #
try:
	if not "emoji.txt" in os.listdir():
		x = open("emoji.txt","w")
		em = "❤️ 🧡 💛 💚 💙 💜 🖤 🤍 🤎"
		x.write(str(em))
		x.close()
except:
	None
# ============= #
unknown = TelegramClient("unknoenTime", api_id, api_hash)
# ============= #
@unknown.on(events.NewMessage(outgoing=True))
async def get(event):
	if event.raw_text == "راهنما":
		await event.edit("""♦️ به بخش راهنما خوش امدید :

🔸 برای تغییر ایموجی بعد از تایم فقط کافیه دستور emoji رو بزنید و ایموجی هارو با فاصله وارد کنید
مثال:
emoji ❤️ 💦 🥲 🥺👍

اینجا ایموجی ها با فاصله از هم جدا شدن ولی اخری به هم چسبیده
𝚌𝚘𝚍𝚍 𝚋𝚢 : -/ℙ𝕄 \n𝚌𝚑𝚗𝚕𝚕: @BL4CK_T34M
ایموجی ها هربار بصورت اتفاقی انتخاب میشن و با فاصله از هم جدا میشن یعنی الا اون 👍🥺 یک ایموجی به حساب میاد و اگر انتخاب شود به همان شکل بغل تایم قرار میگیره و بقیه هم به همون صورت که با فاصله از هم جدا شدند مثلا
❤️ همونطور جایگذاری میشه""")
	if "emoji" in event.raw_text:
		emo = event.raw_text.replace("emoji",'')
		await event.edit(f"""✅ ایموجی های زیر با موفقیت جایگزین لیست قبلی شدند 👇🏻
{emo}""")
		c = open("emoji.txt","w")
		c.write(str(emo))
		c.close()

@aiocron.crontab('*/1 * * * *')
async def s():
	x = open("emoji.txt")
	emoji = x.readline()
	x.close()
	iran = pytz.timezone("Asia/Tehran")
	time=str(datetime.now(iran).strftime("%H:%M"))+" "+str(random.choice(emoji.split()))
	await unknown(UpdateProfileRequest( about=str(time)))
# ============= #
unknown.start()
s.start()
unknown.run_until_disconnected()
asyncio.get_event_loop().run_forever()