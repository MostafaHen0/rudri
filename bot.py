import asyncio
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from pyromod import listen



bot = Client(
    "Goldsex",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Maker")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    for attempt in range(5):
        try:
            await bot.start()
            break
        except Exception as e:
            print(f"[INFO]: محاولة {attempt+1} فشلت: {e}")
            if attempt < 4:
                wait = 3 * (attempt + 1)
                print(f"[INFO]: انتظار {wait} ثانية ثم إعادة المحاولة...")
                await asyncio.sleep(wait)
            else:
                raise
    try:
        Gold = "M_A_171"
        await bot.send_message(Gold, "**تم تشغيل ال صانع عزيزي المطور ،**")
        print("[INFO]: تم تشغيل الصانع وارسال رسالة للمطور🚦.")
    except Exception as e:
        print(f"[INFO]: تم تشغيل الصانع بنجاح (لم يتم إرسال رسالة: {e})")
    print("[INFO]: جاري تشغيل البوتات المصنوعة تلقائياً...")
    try:
        from Maker.Goldsex import auto_bot
        await auto_bot()
        print("[INFO]: تم تشغيل البوتات المصنوعة بنجاح 🚦")
    except Exception as e:
        print(f"[INFO]: خطأ في تشغيل البوتات: {e}")
    await idle()
