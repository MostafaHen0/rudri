import asyncio
import os
from aiohttp import web
from bot import *

BOT_START_TIME = None

async def handle_status(request):
    import time
    uptime = ""
    if BOT_START_TIME:
        secs = int(time.time() - BOT_START_TIME)
        h, r = divmod(secs, 3600)
        m, s = divmod(r, 60)
        uptime = f"{h}h {m}m {s}s"
    html = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
<meta charset="UTF-8">
<title>مصنع ميوزك - rodrigo™</title>
<style>
  body {{ background:#0d0d0d; color:#fff; font-family:Arial,sans-serif; display:flex; align-items:center; justify-content:center; height:100vh; margin:0; }}
  .card {{ background:#1a1a2e; border:1px solid #16213e; border-radius:16px; padding:40px; text-align:center; max-width:400px; }}
  .status {{ color:#00ff88; font-size:18px; margin:10px 0; }}
  .title {{ font-size:26px; font-weight:bold; margin-bottom:20px; }}
  .info {{ color:#aaa; font-size:14px; margin:6px 0; }}
  a {{ color:#4fc3f7; text-decoration:none; }}
</style>
</head>
<body>
<div class="card">
  <div class="title">🤖 مصنع ميوزك</div>
  <div class="status">● البوت شغال</div>
  <div class="info">⏱ وقت التشغيل: {uptime or 'جاري...'}</div>
  <div class="info">👑 المطور: <a href="https://t.me/M_A_171">rodrigo™</a></div>
  <div class="info">📢 القناة: <a href="https://t.me/x_aa_a">@x_aa_a</a></div>
  <div class="info">💬 الجروب: <a href="https://t.me/f_g_d_d">@f_g_d_d</a></div>
</div>
</body>
</html>"""
    return web.Response(text=html, content_type="text/html")

async def run_web():
    port = int(os.environ.get("PORT", 5000))
    app_web = web.Application()
    app_web.router.add_get("/", handle_status)
    app_web.router.add_get("/health", handle_status)
    runner = web.AppRunner(app_web)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"[INFO]: صفحة الحالة شغالة على port {port}")

async def main():
    global BOT_START_TIME
    import time
    await asyncio.gather(
        run_web(),
        start_bot()
    )
    BOT_START_TIME = time.time()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
