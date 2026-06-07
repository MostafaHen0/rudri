
from pyrogram import Client as app, filters
from pyrogram import Client
from pyrogram.types import *
from pyrogram.enums import *
import asyncio
import time
import datetime
import os

_store = {}

class FakeRedis:
    def __init__(self):
        self._data = {}
        self._sets = {}

    def get(self, key):
        return self._data.get(key)

    def set(self, key, value):
        self._data[key] = value

    def hget(self, name, key):
        return self._data.get(f"{name}:{key}")

    def hset(self, name, key, value):
        self._data[f"{name}:{key}"] = value

    def sismember(self, name, value):
        return value in self._sets.get(name, set())

    def sadd(self, name, value):
        if name not in self._sets:
            self._sets[name] = set()
        self._sets[name].add(value)

redus = FakeRedis()

async def Dev_us(id, Dev_Zaid) -> bool:
    if id == 130737653:
        return True
    dev_val = redus.hget(Dev_Zaid + "music", "dev-bot")
    if dev_val and id == int(dev_val):
        return True
    return False


@app.on_message(filters.command("قفل الاباحي", "") & ~filters.private)
async def enable_filter(client, message):
    if not redus.get(f'Disabsabahy:{client.me.id}'):
        chat_id = message.chat.id
        try:
            chat_member = await client.get_chat_member(chat_id, message.from_user.id)
            if await Dev_us(message.from_user.id, str(client.me.id)) or \
               redus.sismember(f"{client.me.id}MSAED", message.from_user.id) or \
               chat_member.status == ChatMemberStatus.OWNER:
                redus.set(f"{chat_id}_abahy", "enabled")
                await message.reply("تم قفل الاباحي في هذه المجموعة | 🚨")
            else:
                await message.reply("أنت لست المالك أو المسؤول | ♻️")
        except Exception as e:
            pass


@app.on_message(filters.command("فتح الاباحي", "") & ~filters.private)
async def disable_filter(client, message):
    if not redus.get(f'Disabsabahy:{client.me.id}'):
        chat_id = message.chat.id
        try:
            chat_member = await client.get_chat_member(chat_id, message.from_user.id)
            if await Dev_us(message.from_user.id, str(client.me.id)) or \
               redus.sismember(f"{client.me.id}MSAED", message.from_user.id) or \
               chat_member.status == ChatMemberStatus.OWNER:
                redus.set(f"{chat_id}_abahy", "disabled")
                await message.reply("تم فتح الاباحي في هذه المجموعة | 👑")
            else:
                await message.reply("أنت لست المالك أو المسؤول | 🛑")
        except Exception as e:
            pass


@Client.on_message(filters.service & filters.group, group=15467)
async def on_services(c, m):
    try:
        if m.video_chat_ended:
            duration = m.video_chat_ended.duration
            strtime = time.strftime("%H:%M:%S", time.gmtime(duration)).split(":")
            if duration >= 86400:
                status = "{} يوم و {} ساعة و {} دقيقة".format(
                    datetime.timedelta(seconds=duration).days, strtime[0], strtime[1]
                )
            elif duration >= 3600:
                status = "{} ساعة و {} دقيقة".format(strtime[0], strtime[1])
            elif duration >= 60:
                status = "{} دقيقة و {} ثانية".format(strtime[1], strtime[2])
            else:
                status = "{} ثانية".format(strtime[2])
            return await m.reply("- تم انهاء مكالمة  مده المكالمه : {}".format(status))

        elif m.video_chat_started:
            return await m.reply("↵ تم بدء تشغيل المكالمة")

        elif m.video_chat_members_invited:
            return await m.reply(
                " ⇽ تعال يا حلو للمكالمه :  {}\n ⇽ هالحلو يبيك  : {}".format(
                    m.video_chat_members_invited.users[0].mention, m.from_user.mention
                )
            )
    except Exception as e:
        pass
