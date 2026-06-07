import asyncio
import os
import random
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from pyrogram import filters, Client
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import *
from pyrogram import enums
from typing import Union, List, Iterable
from datetime import datetime
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import ChatPermissions, ChatPrivileges
from aiohttp import ClientSession
from pyrogram.types import (InlineKeyboardButton, ChatPermissions, InlineKeyboardMarkup, Message, User)
import sys
from pyrogram import Client as client
from pyrogram.errors import FloodWait
from pyrogram import Client, idle
from random import randint
from pyrogram.enums import ChatType
from pyrogram.types import Chat, User
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from config import *
from config import OWNER, OWNER_NAME, VIDEO
from Gold.info import (is_served_chat, add_served_chat, is_served_user, add_served_user, get_served_chats, get_served_users, del_served_chat, joinch)
from Gold.Data import (get_dev, get_bot_name, set_bot_name, get_logger, get_group, get_channel, get_dev_name, get_groupsr, get_channelsr, get_userbot)
from random import choice
from telegraph import upload_file
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton as Button, InlineKeyboardMarkup as Markup
from kvsqlite.sync import Client as KV
import pyromod, random, string
import redis, re
from collections import defaultdict, deque
import time
from pyrogram.types import Message, CallbackQuery
from pyrogram.types import InlineKeyboardMarkup as Keyboard, InlineKeyboardButton as Button
from pyrogram.types import (InlineKeyboardButton, ChatPermissions, InlineKeyboardMarkup, Message, User)
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from OWNER import moord

db = KV('hms.db', 'hms')

r = redis.Redis(
    host="127.0.0.1",
    port=6379,)

hamaiaa = {}

@Client.on_message(filters.command(["قفل الحمايه","تعطيل الحمايه"], "") & filters.private,group=1876378398)
async def abra245g(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   if message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
    hamaiaa.setdefault(bot_username, []).append(bot_username)
    await message.reply_text(f"• تم قفل الحمايه بواسطه ↤︎「 {message.from_user.mention}")
    
@Client.on_message(filters.command(["فتح الحمايه","تفعيل الحمايه"], "") & filters.private,group=5451877)
async def abr54ag(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   if message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
    hamaiaa[bot_username].remove(bot_username)
    await message.reply_text(f"• تم فتح الحمايه بواسطه ↤︎「 {message.from_user.mention}")
#..........................................  حمايه الاسبام  ................................................................    
@Client.on_message(filters.command(["قفل السبام","قفل الاسبام"], "") & filters.group, group=36)
async def lock_asbam(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username) 
   if message.chat.id in hemaya.get(message.chat.id, []):
       return
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
     oo = [message.chat.id]
     add_asbamm(oo, bot_username)
     await message.reply_text(f"• تم قفل الاسبام بواسطه ↤︎「 {message.from_user.mention}")
   else:
    await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر لا يخصك")
  
@Client.on_message(filters.command(["فتح السبام","فتح الاسبام"], "") & filters.group, group=37)
async def unlock_asbam(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username) 
   if message.chat.id in hemaya.get(message.chat.id, []):
       return
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
    group_id = message.chat.id
    for x in get_asbamm(bot_username):
        if x[0] == group_id:
            del_asbamm(x, bot_username)
    await message.reply_text(f"• تم فتح الاسبام بواسطه ↤︎「 {message.from_user.mention}")
   else:
    await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر لا يخصك")

def add_asbamm(bots, bot_username):
    if is_asbamm(bots, bot_username):
        return
    r.sadd(f"asbamm{bot_username}", str(bots))

def is_asbamm(bots, bot_username):
    try:
        a = get_asbamm(bot_username)
        if bots in a:
            return True
        return False
    except:
        return False

def del_asbamm(bots, bot_username):
    if not is_asbamm(bots, bot_username):
        return False
    r.srem(f"asbamm{bot_username}", str(bots))

def get_asbamm(bot_username):
    try:
        lst = []
        for a in r.smembers(f"asbamm{bot_username}"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []

time_between_msgs = 5
users_messages = defaultdict(lambda: defaultdict(lambda: deque(maxlen=5)))

@Client.on_message(filters.group, group=38)
async def handle_spam_message(client, message):
    if message.from_user is None:
        return
    chat_id = message.chat.id
    user_id = message.from_user.id
    current_time = time.time()
    if message.text is None:
        return 
    message_text = message.text.lower().strip() 
    users_messages[chat_id][user_id].append((message_text, current_time))
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if message.from_user is None:
        return
    if message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
        return
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status == ChatMemberStatus.OWNER:
        return
    for x in get_asbamm(bot_username):
        ch = x[0]
        if message.chat.id == ch:
            if len(users_messages[chat_id][user_id]) > 2:
                repeated_messages = sum(1 for msg, _ in users_messages[chat_id][user_id] if msg == message_text)
                _, t1 = users_messages[chat_id][user_id][-2]
                _, t2 = users_messages[chat_id][user_id][-1]
                time_interval = t2 - t1
                if repeated_messages > 3 and time_interval <= time_between_msgs:
                    await message.delete()
                    users_messages[chat_id][user_id].clear()

@Client.on_callback_query(filters.regex("^asbammlock (\\d+)$"))
async def asbammlock(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        return
    bot_username = c.me.username
    oo = [m.message.chat.id]
    add_asbamm(oo, bot_username)
    await m.message.edit_text("تم قفل الاسبام بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="hemm " + str(m.from_user.id))],
        ]
    ))

@Client.on_callback_query(filters.regex("^asbammopen (\\d+)$"))
async def asbammopen(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر ??", show_alert=True)
        return
    bot_username = c.me.username
    group_id = m.message.chat.id
    for x in get_asbamm(bot_username):
        if x[0] == group_id:
            del_asbamm(x, bot_username)
    await m.message.edit_text("تم فتح الاسبام بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="hemm " + str(m.from_user.id))],
        ]
    ))
#..........................................  حمايه الاسبام  ................................................................
#..........................................  حمايه القنوات  ................................................................
@Client.on_message(filters.command(["قفل القنوات"], "") & filters.group, group=39)
async def lock_vasassd(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username) 
   if message.chat.id in hemaya.get(message.chat.id, []):
       return
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
       oo = [message.chat.id]
       add_knoat(oo, bot_username)
       await message.reply_text(f"• تم قفل المتحركات بواسطه ↤︎「 {message.from_user.mention}")
   else:
       await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر لا يخصك")
  
@Client.on_message(filters.command(["فتح القنوات"], "") & filters.group, group=40)
async def unlsock_aaaa(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username) 
   if message.chat.id in hemaya.get(message.chat.id, []):
     return
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
    group_id = message.chat.id
    for x in get_knoat(bot_username):
        if x[0] == group_id:
            del_knoat(x, bot_username)
    await message.reply_text(f"• تم فتح المتحركات بواسطه ↤︎「 {message.from_user.mention}")
   else:
    await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر لا يخصك")

def add_knoat(bots, bot_username):
    if is_knoat(bots, bot_username):
        return
    r.sadd(f"knoat{bot_username}", str(bots))

def is_knoat(bots, bot_username):
    try:
        a = get_knoat(bot_username)
        if bots in a:
            return True
        return False
    except:
        return False

def del_knoat(bots, bot_username):
    if not is_knoat(bots, bot_username):
        return False
    r.srem(f"knoat{bot_username}", str(bots))

def get_knoat(bot_username):
    try:
        lst = []
        for a in r.smembers(f"knoat{bot_username}"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []

@Client.on_message(filters.text,group=41)
async def delet_kanoat(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   for x in get_knoat(bot_username):
       ch = x[0]
       if message.chat.id == ch:
           try:
               h = message.from_user.id
           except Exception as e:
               await message.delete()
               
@Client.on_callback_query(filters.regex("^kanoatlock (\\d+)$"))
async def close_kanoat(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        return
    bot_username = c.me.username
    oo = [m.message.chat.id]
    add_knoat(oo, bot_username)
    await m.message.edit_text("تم قفل القنوات بنجاح 📣", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="hemm " + str(m.from_user.id))],
        ]
    ))

@Client.on_callback_query(filters.regex("^kanoatopen (\\d+)$"))
async def open_kanoat(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        return
    bot_username = c.me.username
    group_id = m.message.chat.id
    for x in get_knoat(bot_username):
        if x[0] == group_id:
            del_knoat(x, bot_username)
    await m.message.edit_text("تم فتح القنوات بنجاح  📣", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="hemm " + str(m.from_user.id))],
        ]
    ))
#..........................................  حمايه القنوات  ................................................................
#..........................................  حمايه الدردشه  ................................................................
@Client.on_message(filters.command(["قفل الدردشه","قفل الدردشة","ق د","ق الدردشه"], "") & filters.group, group=42)
async def enabled(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username) 
   if message.chat.id in hemaya.get(message.chat.id, []):
       return
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
     oo = [message.chat.id]
     add_dardasha(oo, bot_username)
     await message.reply_text(f"• تم قفل الدردشه بواسطه ↤︎「 {message.from_user.mention}")
   else:
    await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر لا يخصك")
  
@Client.on_message(filters.command(["فتح الدردشه","فتح الدردشة","ف د","ف الدردشه"], "") & filters.group, group=43)
async def undard(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username) 
   if message.chat.id in hemaya.get(message.chat.id, []):
       return
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
    group_id = message.chat.id
    for x in get_dardasha(bot_username):
        if x[0] == group_id:
            del_dardasha(x, bot_username)
    await message.reply_text(f"• تم فتح الدردشه بواسطه ↤︎「 {message.from_user.mention}")
   else:
    await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر لا يخصك")
 
def add_dardasha(bots, bot_username):
    if is_dardasha(bots, bot_username):
        return
    r.sadd(f"group_id{bot_username}", str(bots))

def is_dardasha(bots, bot_username):
    try:
        a = get_dardasha(bot_username)
        if bots in a:
            return True
        return False
    except:
        return False

def del_dardasha(bots, bot_username):
    if not is_dardasha(bots, bot_username):
        return False
    r.srem(f"group_id{bot_username}", str(bots))

def get_dardasha(bot_username):
    try:
        lst = []
        for a in r.smembers(f"group_id{bot_username}"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []
	
@Client.on_message(group=44)
async def delet_med65iaaa(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   if message.from_user is None:
        return 
   if message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
        return
   try:
       chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
       if chat_member.status == ChatMemberStatus.OWNER:
           return
   except Exception:
       return
   for x in get_dardasha(bot_username):
    ch = x[0]
    if message.chat.id == ch:
     await message.delete()
     
@Client.on_callback_query(filters.regex("^chaatlock (\\d+)$"))
async def close_chaat(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        return
    bot_username = c.me.username
    oo = [m.message.chat.id]
    add_dardasha(oo, bot_username)
    await m.message.edit_text("تم قفل الدردشه بنجاح ⚠️", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="hemm " + str(m.from_user.id))],
        ]
    ))

@Client.on_callback_query(filters.regex("^chatopen (\\d+)$"))
async def open_chaat(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        return
    bot_username = c.me.username
    group_id = m.message.chat.id
    for x in get_dardasha(bot_username):
        if x[0] == group_id:
            del_dardasha(x, bot_username)
    await m.message.edit_text("تم فتح الدردشه بنجاح  ⚠️", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="hemm " + str(m.from_user.id))],
        ]
    ))
#..........................................  حمايه الدردشه  ................................................................
#..........................................  حمايه المتحركه  ................................................................
@Client.on_message(filters.command(["قفل المتحركات","قفل المتحركه","قفل المتحركه","ق المتحركه","قفل المتحركة"], "") & filters.group, group=45)
async def lock_vaassd(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username) 
   if message.chat.id in hemaya.get(message.chat.id, []):
       return
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
     oo = [message.chat.id]
     add_mutaharek(oo, bot_username)
     await message.reply_text(f"• تم قفل المتحركات بواسطه ↤︎「 {message.from_user.mention}")
   else:
    await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر لا يخصك")
  
@Client.on_message(filters.command(["فتح المتحركات","فتح المتحركه","فتح المتحركة","ف المتحركه","فتح المتحركة"], "") & filters.group, group=46)
async def unlock_aaaa(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username) 
   if message.chat.id in hemaya.get(message.chat.id, []):
       return
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
    group_id = message.chat.id
    for x in get_mutaharek(bot_username):
        if x[0] == group_id:
            del_mutaharek(x, bot_username)
    await message.reply_text(f"• تم فتح المتحركات بواسطه ↤︎「 {message.from_user.mention}")
   else:
    await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر لا يخصك")

def add_mutaharek(bots, bot_username):
    if is_mutaharek(bots, bot_username):
        return
    r.sadd(f"mutaharek{bot_username}", str(bots))

def is_mutaharek(bots, bot_username):
    try:
        a = get_mutaharek(bot_username)
        if bots in a:
            return True
        return False
    except:
        return False

def del_mutaharek(bots, bot_username):
    if not is_mutaharek(bots, bot_username):
        return False
    r.srem(f"mutaharek{bot_username}", str(bots))

def get_mutaharek(bot_username):
    try:
        lst = []
        for a in r.smembers(f"mutaharek{bot_username}"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []

@Client.on_message(filters.animation,group=47)
async def delet_m68ediaaa(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   if message.from_user is None:
        return 
   if message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
        return
   try:
       chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
       if chat_member.status == ChatMemberStatus.OWNER:
           return
   except Exception:
       return
   for x in get_mutaharek(bot_username):
    ch = x[0]
    if message.chat.id == ch:
     await message.delete()
     
@Client.on_callback_query(filters.regex("^mutahareklock (\\d+)$"))
async def mutahakkk(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        return
    bot_username = c.me.username
    oo = [m.message.chat.id]
    add_mutaharek(oo, bot_username)
    await m.message.edit_text("تم قفل المتحركات بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="hemm " + str(m.from_user.id))],
        ]
    ))

@Client.on_callback_query(filters.regex("^mutaharekopen (\\d+)$"))
async def mutahpen(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        return
    bot_username = c.me.username
    group_id = m.message.chat.id
    for x in get_mutaharek(bot_username):
        if x[0] == group_id:
            del_mutaharek(x, bot_username)
    await m.message.edit_text("تم فتح المتحركات بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="hemm " + str(m.from_user.id))],
        ]
    ))
#..........................................  حمايه المتحركه  ................................................................
#..........................................  حمايه الفيديو  ................................................................
@Client.on_message(filters.command(["قفل الفديو","قفل الفيد","قفل فيد"], "") & filters.group, group=48)
async def lock_video(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username) 
   if message.chat.id in hemaya.get(message.chat.id, []):
       return
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
     oo = [message.chat.id]
     add_videoo(oo, bot_username)
     await message.reply_text(f"• تم قفل الفديو بواسطه ↤︎「 {message.from_user.mention}")
   else:
    await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر لا يخصك")
  
@Client.on_message(filters.command(["فتح الفديو","فتح الفيد","فتح فيد"], "") & filters.group, group=49)
async def unlock_video(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   if message.chat.id in hemaya.get(message.chat.id, []):
     return
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
    group_id = message.chat.id
    for x in get_videoo(bot_username):
        if x[0] == group_id:
            del_videoo(x, bot_username)
    await message.reply_text(f"• تم فتح الفديو بواسطه ↤︎「 {message.from_user.mention}")
   else:
    await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر لا يخصك")

def add_videoo(bots, bot_username):
    if is_videoo(bots, bot_username):
        return
    r.sadd(f"videoo{bot_username}", str(bots))

def is_videoo(bots, bot_username):
    try:
        a = get_videoo(bot_username)
        if bots in a:
            return True
        return False
    except:
        return False

def del_videoo(bots, bot_username):
    if not is_videoo(bots, bot_username):
        return False
    r.srem(f"videoo{bot_username}", str(bots))

def get_videoo(bot_username):
    try:
        lst = []
        for a in r.smembers(f"videoo{bot_username}"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []

@Client.on_message(filters.video, group=50)
async def delete_video(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if message.from_user is None:
        return 
    if message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
        return
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status == ChatMemberStatus.OWNER:
        return
    for x in get_videoo(bot_username):
        ch = x[0]
        if message.chat.id == ch:
            await message.delete()
  
@Client.on_callback_query(filters.regex("^videoolock (\\d+)$"))
async def videoolockkk(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        return
    bot_username = c.me.username
    oo = [m.message.chat.id]
    add_videoo(oo, bot_username)
    await m.message.edit_text("تم قفل الفيديوهات بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="hemm " + str(m.from_user.id))],
        ]
    ))


@Client.on_callback_query(filters.regex("^videooopen (\\d+)$"))
async def videoooopen(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        return
    bot_username = c.me.username
    group_id = m.message.chat.id
    for x in get_videoo(bot_username):
        if x[0] == group_id:
            del_videoo(x, bot_username)
    await m.message.edit_text("تم فتح الفيديو بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="hemm " + str(m.from_user.id))],
        ]
    ))
#..........................................  حمايه الفيديو  ................................................................
#..........................................  حمايه التحويل  ................................................................
@Client.on_message(filters.command(["قفل التوجيه","قفل التحويل"], "") & filters.group, group=51)
async def lock_forward(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username) 
   if message.chat.id in hemaya.get(message.chat.id, []):
       return
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
     oo = [message.chat.id]
     add_tawgeh(oo, bot_username)
     await message.reply_text(f"• تم قفل التوجيه بواسطه ↤︎「 {message.from_user.mention}")
   else:
    await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر لا يخصك")
  
@Client.on_message(filters.command(["فتح التوجيه","فتح التحويل"], "") & filters.group, group=52)
async def unlock_forward(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username) 
   if message.chat.id in hemaya.get(message.chat.id, []):
       return
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
    group_id = message.chat.id
    for x in get_tawgeh(bot_username):
        if x[0] == group_id:
            del_tawgeh(x, bot_username)
    await message.reply_text(f"• تم فتح التوجيه بواسطه ↤︎「 {message.from_user.mention}")
   else:
    await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر لا يخصك")

def add_tawgeh(bots, bot_username):
    if is_tawgeh(bots, bot_username):
        return
    r.sadd(f"tawgeh{bot_username}", str(bots))

def is_tawgeh(bots, bot_username):
    try:
        a = get_tawgeh(bot_username)
        if bots in a:
            return True
        return False
    except:
        return False

def del_tawgeh(bots, bot_username):
    if not is_tawgeh(bots, bot_username):
        return False
    r.srem(f"tawgeh{bot_username}", str(bots))

def get_tawgeh(bot_username):
    try:
        lst = []
        for a in r.smembers(f"tawgeh{bot_username}"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []
        
@Client.on_message(filters.forwarded,group=53)
async def delete_forwarded_messages(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   if message.from_user is None:
        return 
   if message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
        return
   try:
       chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
       if chat_member.status == ChatMemberStatus.OWNER:
           return
   except Exception:
       return
   for x in get_tawgeh(bot_username):
    ch = x[0]
    if message.chat.id == ch:
     await message.delete()
     
@Client.on_callback_query(filters.regex("^tawgehlock (\\d+)$"))
async def tawgehlockkk(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        return
    bot_username = c.me.username
    oo = [m.message.chat.id]
    add_tawgeh(oo, bot_username)
    await m.message.edit_text("تم قفل التوجيه بنجاح 🔁", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="hemm " + str(m.from_user.id))],
        ]
    ))

@Client.on_callback_query(filters.regex("^tawgehopen (\\d+)$"))
async def tawgehoopen(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        return
    bot_username = c.me.username
    group_id = m.message.chat.id
    for x in get_tawgeh(bot_username):
        if x[0] == group_id:
            del_tawgeh(x, bot_username)
    await m.message.edit_text("تم فتح التوجيه بنجاح 🔁", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="hemm " + str(m.from_user.id))],
        ]
    ))
#..........................................  حمايه التحويل  ................................................................
#..........................................  حمايه الملصقات  ................................................................
@Client.on_message(filters.command("قفل الملصقات", "") & filters.group, group=54)
async def lock_stickers(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username) 
   if message.chat.id in hemaya.get(message.chat.id, []):
       return
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
     oo = [message.chat.id]
     add_stick(oo, bot_username)
     await message.reply_text(f"• تم قفل الملصقات بواسطه ↤︎「 {message.from_user.mention}")
   else:
    await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر لا يخصك")
  
@Client.on_message(filters.command("فتح الملصقات", "") & filters.group, group=55)
async def unlock_stickers(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username) 
   if message.chat.id in hemaya.get(message.chat.id, []):
       return
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
    group_id = message.chat.id
    for x in get_stick(bot_username):
        if x[0] == group_id:
            del_stick(x, bot_username)
    await message.reply_text(f"• تم فتح الملصقات بواسطه ↤︎「 {message.from_user.mention}")
   else:
    await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر لا يخصك")

def add_stick(bots, bot_username):
    if is_stick(bots, bot_username):
        return
    r.sadd(f"stick{bot_username}", str(bots))

def is_stick(bots, bot_username):
    try:
        a = get_stick(bot_username)
        if bots in a:
            return True
        return False
    except:
        return False

def del_stick(bots, bot_username):
    if not is_stick(bots, bot_username):
        return False
    r.srem(f"stick{bot_username}", str(bots))

def get_stick(bot_username):
    try:
        lst = []
        for a in r.smembers(f"stick{bot_username}"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []
        
@Client.on_message(filters.sticker,group=56)
async def delete_sticker(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   if message.from_user is None:
        return 
   if message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
        return
   try:
       chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
       if chat_member.status == ChatMemberStatus.OWNER:
           return
   except Exception:
       return
   for x in get_stick(bot_username):
    ch = x[0]
    if message.chat.id == ch:
     await message.delete()
     
@Client.on_callback_query(filters.regex("^sticklock (\\d+)$"))
async def stickkkaa(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        return
    bot_username = c.me.username
    oo = [m.message.chat.id]
    add_stick(oo, bot_username)
    await m.message.edit_text("تم قفل الملصقات بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="hemm " + str(m.from_user.id))],
        ]
    ))

@Client.on_callback_query(filters.regex("^stickopen (\\d+)$"))
async def sticsskkk(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        return
    bot_username = c.me.username
    group_id = m.message.chat.id
    for x in get_stick(bot_username):
        if x[0] == group_id:
            del_stick(x, bot_username)
    await m.message.edit_text("تم فتح الملصقات بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="hemm " + str(m.from_user.id))],
        ]
    ))
#..........................................  حمايه الملصقات  ................................................................
#..........................................  حمايه الصور  ................................................................
@Client.on_message(filters.command("قفل الصور", "") & filters.group, group=57)
async def lock_photos(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username) 
   if message.chat.id in hemaya.get(message.chat.id, []):
       return
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
     oo = [message.chat.id]
     add_photoo(oo, bot_username)
     await message.reply_text(f"• تم قفل الصور بواسطه ↤︎「 {message.from_user.mention}")
   else:
    await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر لا يخصك")
  
@Client.on_message(filters.command("فتح الصور", "") & filters.group, group=58)
async def unlock_photos(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username) 
   if message.chat.id in hemaya.get(message.chat.id, []):
       return
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
    group_id = message.chat.id
    for x in get_photoo(bot_username):
        if x[0] == group_id:
            del_photoo(x, bot_username)
    await message.reply_text(f"• تم فتح الصور بواسطه ↤︎「 {message.from_user.mention}")
   else:
    await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر لا يخصك")

def add_photoo(bots, bot_username):
    if is_photoo(bots, bot_username):
        return
    r.sadd(f"photoo{bot_username}", str(bots))

def is_photoo(bots, bot_username):
    try:
        a = get_photoo(bot_username)
        if bots in a:
            return True
        return False
    except:
        return False

def del_photoo(bots, bot_username):
    if not is_photoo(bots, bot_username):
        return False
    r.srem(f"photoo{bot_username}", str(bots))

def get_photoo(bot_username):
    try:
        lst = []
        for a in r.smembers(f"photoo{bot_username}"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []

@Client.on_message(filters.photo, group=59)
async def delete_photo(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   if message.from_user is None:
        return 
   if message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
        return
   try:
       chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
       if chat_member.status == ChatMemberStatus.OWNER:
           return
   except Exception:
       return
   for x in get_photoo(bot_username):
    ch = x[0]
    if message.chat.id == ch:
     await message.delete()
     
@Client.on_callback_query(filters.regex("^photolock (\\d+)$"))
async def pppho(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        return
    bot_username = c.me.username
    oo = [m.message.chat.id]
    add_photoo(oo, bot_username)
    await m.message.edit_text("تم قفل الصور بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="hemm " + str(m.from_user.id))],
        ]
    ))

@Client.on_callback_query(filters.regex("^photoopen (\\d+)$"))
async def phoooto(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        return
    bot_username = c.me.username
    group_id = m.message.chat.id
    for x in get_photoo(bot_username):
        if x[0] == group_id:
            del_photoo(x, bot_username)
    await m.message.edit_text("تم فتح الصور بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="hemm " + str(m.from_user.id))],
        ]
    ))
#..........................................  حمايه الصور  ................................................................
#..........................................  حمايه المنشن  ................................................................
@Client.on_message(filters.command(["قفل المنشن","قفل الاشاره"], "") & filters.group, group=60)
async def lock_mention(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username) 
   if message.chat.id in hemaya.get(message.chat.id, []):
       return
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
     oo = [message.chat.id]
     add_mentionn(oo, bot_username)
     await message.reply_text(f"• تم قفل المنشن بواسطه ↤︎「 {message.from_user.mention}")
   else:
    await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر لا يخصك")
  
@Client.on_message(filters.command(["فتح المنشن","فتح الاشاره"], "") & filters.group, group=61)
async def unlock_mention(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username) 
   if message.chat.id in hemaya.get(message.chat.id, []):
       return
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
    group_id = message.chat.id
    for x in get_mentionn(bot_username):
        if x[0] == group_id:
            del_mentionn(x, bot_username)
    await message.reply_text(f"• تم فتح المنشن بواسطه ↤︎「 {message.from_user.mention}")
   else:
    await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر لا يخصك")

def add_mentionn(bots, bot_username):
    if is_mentionn(bots, bot_username):
        return
    r.sadd(f"mentionn{bot_username}", str(bots))

def is_mentionn(bots, bot_username):
    try:
        a = get_mentionn(bot_username)
        if bots in a:
            return True
        return False
    except:
        return False

def del_mentionn(bots, bot_username):
    if not is_mentionn(bots, bot_username):
        return False
    r.srem(f"mentionn{bot_username}", str(bots))

def get_mentionn(bot_username):
    try:
        lst = []
        for a in r.smembers(f"mentionn{bot_username}"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []

@Client.on_message(filters.text, group=62)
async def delete_mention(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   if message.from_user is None:
        return 
   if message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
        return
   try:
       chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
       if chat_member.status == ChatMemberStatus.OWNER:
           return
   except Exception:
       return
   for x in get_mentionn(bot_username):
    ch = x[0]
    if message.chat.id == ch:
     if "@" in message.text:
        await message.delete()
        
@Client.on_callback_query(filters.regex("^mentionnlock (\\d+)$"))
async def mentionnlock(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        return
    bot_username = c.me.username
    oo = [m.message.chat.id]
    add_mentionn(oo, bot_username)
    await m.message.edit_text("تم قفل المنشن بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="hemm " + str(m.from_user.id))],
        ]
    ))

@Client.on_callback_query(filters.regex("^mentionnopen (\\d+)$"))
async def mentionnopen(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر ??", show_alert=True)
        return
    bot_username = c.me.username
    group_id = m.message.chat.id
    for x in get_mentionn(bot_username):
        if x[0] == group_id:
            del_mentionn(x, bot_username)
    await m.message.edit_text("تم فتح المنشن بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="hemm " + str(m.from_user.id))],
        ]
    ))
#..........................................  حمايه المنشن  ................................................................
#..........................................   حمايه الشراحه  ................................................................
@Client.on_message(filters.command(["قفل الشراحه","قفل الهاشتاج ","قفل هشتاج","قفل الهشتاج"], "") & filters.group, group=63)
async def lock_hashtag(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username) 
   if message.chat.id in hemaya.get(message.chat.id, []):
       return
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
     oo = [message.chat.id]
     add_hashtag(oo, bot_username)
     await message.reply_text(f"• تم قفل الشراحه بواسطه ↤︎「 {message.from_user.mention}")
   else:
    await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر لا يخصك")
    
@Client.on_message(filters.command(["فتح الشراحه","فتح الهاشتاج ","فتح هشتاج","فتح الهشتاج"], "") & filters.group, group=64)
async def unlock_hashtag(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username) 
   if message.chat.id in hemaya.get(message.chat.id, []):
       return
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
    group_id = message.chat.id
    for x in get_hashtag(bot_username):
        if x[0] == group_id:
            del_hashtag(x, bot_username)
    await message.reply_text(f"• تم فتح الشراحه بواسطه ↤︎「 {message.from_user.mention}")
   else:
    await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر لا يخصك")
    
def add_hashtag(bots, bot_username):
    if is_hashtag(bots, bot_username):
        return
    r.sadd(f"hashtag{bot_username}", str(bots))

def is_hashtag(bots, bot_username):
    try:
        a = get_hashtag(bot_username)
        if bots in a:
            return True
        return False
    except:
        return False

def del_hashtag(bots, bot_username):
    if not is_hashtag(bots, bot_username):
        return False
    r.srem(f"hashtag{bot_username}", str(bots))

def get_hashtag(bot_username):
    try:
        lst = []
        for a in r.smembers(f"hashtag{bot_username}"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []
        
@Client.on_message(filters.text, group=65)
async def delete_hashtag(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   if message.from_user is None:
        return 
   if message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
        return
   try:
       chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
       if chat_member.status == ChatMemberStatus.OWNER:
           return
   except Exception:
       return
   for x in get_hashtag(bot_username):
    ch = x[0]
    if message.chat.id == ch:
     if "#" in message.text:
        await message.delete()
        
@Client.on_callback_query(filters.regex("^hashtaglock (\\d+)$"))
async def hashtaglock(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        return
    bot_username = c.me.username
    oo = [m.message.chat.id]
    add_hashtag(oo, bot_username)
    await m.message.edit_text("تم قفل الشراحه بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="hemm " + str(m.from_user.id))],
        ]
    ))

@Client.on_callback_query(filters.regex("^hashtagopen (\\d+)$"))
async def hashtagopen(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر ??", show_alert=True)
        return
    bot_username = c.me.username
    group_id = m.message.chat.id
    for x in get_hashtag(bot_username):
        if x[0] == group_id:
            del_hashtag(x, bot_username)
    await m.message.edit_text("تم فتح الشراحه بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="hemm " + str(m.from_user.id))],
        ]
    ))
#..........................................   حمايه الشراحه  ................................................................
#..........................................  حمايه الروابط  ................................................................
@Client.on_message(filters.command(["قفل الروابط","قفل روابط","قفل الرابط","قفل رابط"], "") & filters.group, group=66)
async def lock_link(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username) 
   if message.chat.id in hemaya.get(message.chat.id, []):
       return
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
     oo = [message.chat.id]
     add_rwabet(oo, bot_username)
     await message.reply_text(f"• تم قفل الروابط بواسطه ↤︎「 {message.from_user.mention}")
   else:
    await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر لا يخصك")
  
@Client.on_message(filters.command(["فتح الروابط","فتح روابط","فتح الرابط","فتح رابط"], "") & filters.group, group=67)
async def unlock_link(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username) 
   if message.chat.id in hemaya.get(message.chat.id, []):
       return
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
    group_id = message.chat.id
    for x in get_rwabet(bot_username):
        if x[0] == group_id:
            del_rwabet(x, bot_username)
    await message.reply_text(f"• تم فتح الروابط بواسطه ↤︎「 {message.from_user.mention}")
   else:
    await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر لا يخصك")

def add_rwabet(bots, bot_username):
    if is_rwabet(bots, bot_username):
        return
    r.sadd(f"rwabet{bot_username}", str(bots))

def is_rwabet(bots, bot_username):
    try:
        a = get_rwabet(bot_username)
        if bots in a:
            return True
        return False
    except:
        return False

def del_rwabet(bots, bot_username):
    if not is_rwabet(bots, bot_username):
        return False
    r.srem(f"rwabet{bot_username}", str(bots))

def get_rwabet(bot_username):
    try:
        lst = []
        for a in r.smembers(f"rwabet{bot_username}"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []
        
@Client.on_message(filters.text, group=68)
async def process_message(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   if message.from_user is None:
        return 
   if message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
        return
   try:
       chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
       if chat_member.status == ChatMemberStatus.OWNER:
           return
   except Exception:
       return
   for x in get_rwabet(bot_username):
    ch = x[0]
    if message.chat.id == ch:
      if "https://" in message.text:
        await message.delete()
      if ".io" in message.text:
        await message.delete()
      if ".click" in message.text:
        await message.delete()
      if ".xyz" in message.text:
        await message.delete()
      if ".com" in message.text:
        await message.delete()
      if "t.me" in message.text:
        await message.delete()
      if ".net" in message.text:
        await message.delete()
      if ".online" in message.text:
        await message.delete()
      if ".vip" in message.text:
        await message.delete()
      if ".top" in message.text:
        await message.delete()
      if ".org" in message.text:
        await message.delete()
      if ".site" in message.text:
        await message.delete()
      if ".me" in message.text:
        await message.delete()
      if ".host" in message.text:
        await message.delete()
      if ".tech" in message.text:
        await message.delete()
      if ".world" in message.text:
        await message.delete()
      if ".app" in message.text:
        await message.delete()
      if ".cash" in message.text:
        await message.delete()
      if ".info" in message.text:
        await message.delete()
      if ".blog" in message.text:
        await message.delete()
      if ".biz" in message.text:
        await message.delete()
      if ".club" in message.text:
        await message.delete()
      if ".ai" in message.text:
        await message.delete()
        
@Client.on_callback_query(filters.regex("^rwabetlok (\\d+)$"))
async def cle_carrwllback(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        return
    bot_username = c.me.username
    oo = [m.message.chat.id]
    add_rwabet(oo, bot_username)
    await m.message.edit_text("تم قفل الروابط بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="hemm " + str(m.from_user.id))],
        ]
    ))

@Client.on_callback_query(filters.regex("^rwabetopp (\\d+)$"))
async def csqslose_caack(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        return
    bot_username = c.me.username
    group_id = m.message.chat.id
    for x in get_rwabet(bot_username):
        if x[0] == group_id:
            del_rwabet(x, bot_username)
    await m.message.edit_text("تم فتح الروابط بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="hemm " + str(m.from_user.id))],
        ]
    ))
#..........................................  حمايه الروابط  ................................................................
#..........................................   حمايه السب   ................................................................
@Client.on_message(filters.command("قفل السب", "") & filters.group, group=69)
async def lock_sappp(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username) 
   if message.chat.id in hemaya.get(message.chat.id, []):
       return
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
     oo = [message.chat.id]
     add_sappp(oo, bot_username)
     await message.reply_text(f"• تم قفل السب بواسطه ↤︎「 {message.from_user.mention}")
   else:
    await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر لا يخصك")
  
@Client.on_message(filters.command("فتح السب", "") & filters.group, group=70)
async def unlock_sappp(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username) 
   if message.chat.id in hemaya.get(message.chat.id, []):
       return
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
    group_id = message.chat.id
    for x in get_sappp(bot_username):
        if x[0] == group_id:
            del_sappp(x, bot_username)
    await message.reply_text(f"• تم فتح السب بواسطه ↤︎「 {message.from_user.mention}")
   else:
    await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر لا يخصك")

def add_sappp(bots, bot_username):
    if is_sappp(bots, bot_username):
        return
    r.sadd(f"sappp{bot_username}", str(bots))

def is_sappp(bots, bot_username):
    try:
        a = get_sappp(bot_username)
        if bots in a:
            return True
        return False
    except:
        return False

def del_sappp(bots, bot_username):
    if not is_sappp(bots, bot_username):
        return False
    r.srem(f"sappp{bot_username}", str(bots))

def get_sappp(bot_username):
    try:
        lst = []
        for a in r.smembers(f"sappp{bot_username}"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []

@Client.on_message(filters.text, group=71)
async def delete_sappp(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    
    if message.from_user is None:
        return 

    if message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
        return

    try:
        chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
        if chat_member.status == ChatMemberStatus.OWNER:
            return
    except Exception:
        return

    for x in get_sappp(bot_username):
        ch = x[0]
        if message.chat.id == ch:
            if any(keyword in message.text for keyword in [
                "احا", "خخخ", "ميتينك", "تناك", "يلعن", "كسك", "كسمك", "عرص", "خول", 
                "علق", "كسم", "انيك", "انيكك", "اركبك", "زبي", "نيك", "شرموط", "فحل", 
                "ديوث", "سالب", "مقاطع", "ورعان", "هايج", "مشتهي", "زوبري", "طيز", 
                "كسي", "كسى", "ساحق", "سحق", "لبوه", "اريحها", "مقاتع", "لانجيري", 
                "سحاق", "مقطع", "مقتع", "نودز", "ندز", "ملط", "لانجرى", "لانجري", 
                "لانجيرى", "مولااااعه", "سكس", "اباحيه", "جنس", "اباحي", "زب", 
                "كسمك", "كس", "شرمطه", "نيك", "لبوه", "فشخ", "مهبل", "نيك خلفى", 
                "بتتناك", "مساج", "كس ملبن", "نيك جماعى", "نيك جماعي", "نيك بنات", 
                "رقص", "قلع", "خلع ملابس", "بنات من غير هدوم", "بنات ملط", 
                "نيك طيز", "نيك من ورا", "نيك في الكس", "ارهاب", "موت", "حرب", 
                "سياسه", "سياسي", "سكسي", "قحبه", "شواز", "ممويز", "نياكه", 
                "xnxx", "sex", "xxx", "Sex", "Born", "borno", "Sesso", "Xnxx"
            ]):
                await message.delete()

@Client.on_callback_query(filters.regex("^saabloo (\\d+)$"))
async def cle_callback(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        return
    bot_username = c.me.username
    oo = [m.message.chat.id]
    add_sappp(oo, bot_username)
    await m.message.edit_text("تم قفل السب بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="hemm " + str(m.from_user.id))],
        ]
    ))

@Client.on_callback_query(filters.regex("^saaboo (\\d+)$"))
async def close_caack(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        return
    bot_username = c.me.username
    group_id = m.message.chat.id
    for x in get_sappp(bot_username):
        if x[0] == group_id:
            del_sappp(x, bot_username)
    await m.message.edit_text("تم فتح السب بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="hemm " + str(m.from_user.id))],
        ]
    ))
#..........................................   حمايه السب   ................................................................
#..........................................   حمايه الكل   ................................................................
@Client.on_callback_query(filters.regex("^lockall (\\d+)$"))
async def mutahareknckkk(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        return
    bot_username = c.me.username
    oo = [m.message.chat.id]
    add_sappp(oo, bot_username)
    add_rwabet(oo, bot_username)
    add_photoo(oo, bot_username)
    add_tawgeh(oo, bot_username)
    add_stick(oo, bot_username)
    add_videoo(oo, bot_username)
    add_mentionn(oo, bot_username)
    add_mutaharek(oo, bot_username)
    add_hashtag(oo, bot_username)
    add_asbamm(oo, bot_username)
    add_knoat(oo, bot_username)
    await m.message.edit_text("تم قفل الكل بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="hemm " + str(m.from_user.id))],
        ]
    ))
    
@Client.on_callback_query(filters.regex("^openall (\\d+)$"))
async def mutaharekopen(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        return
    bot_username = c.me.username
    group_id = m.message.chat.id
    for x in get_asbamm(bot_username):
        if x[0] == group_id:
            del_asbamm(x, bot_username)
    for x in get_sappp(bot_username):
        if x[0] == group_id:
            del_sappp(x, bot_username)        
    for x in get_rwabet(bot_username):
        if x[0] == group_id:
            del_rwabet(x, bot_username)        
    for x in get_photoo(bot_username):
        if x[0] == group_id:
            del_photoo(x, bot_username)        
    for x in get_tawgeh(bot_username):
        if x[0] == group_id:
            del_tawgeh(x, bot_username)        
    for x in get_stick(bot_username):
        if x[0] == group_id:
            del_stick(x, bot_username)        
    for x in get_videoo(bot_username):
        if x[0] == group_id:
            del_videoo(x, bot_username)        
    for x in get_mentionn(bot_username):
        if x[0] == group_id:
            del_mentionn(x, bot_username)        
    for x in get_mutaharek(bot_username):
        if x[0] == group_id:
            del_mutaharek(x, bot_username)      
    for x in get_hashtag(bot_username):
        if x[0] == group_id:
            del_hashtag(x, bot_username)        
    for x in get_knoat(bot_username):
        if x[0] == group_id:
            del_knoat(x, bot_username)    
    await m.message.edit_text("تم فتح الكل بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="hemm " + str(m.from_user.id))],
        ]
    ))
#..........................................   حمايه الكل   ................................................................
#..........................................  قفل التحكم   ................................................................
hemaya = {}

@Client.on_message(filters.command(["قفل تحكم","قفل التحكم"], "") & filters.group, group=72)
async def abra245g(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username) 
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
    hemaya.setdefault(message.chat.id, []).append(message.chat.id)
    await message.reply_text(f"• تم قفل التحكم بواسطه ↤︎「 {message.from_user.mention}")

@Client.on_message(filters.command(["فتح تحكم","فتح التحكم"], "") & filters.group, group=73)
async def abr54ag(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username) 
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
    hemaya[message.chat.id].remove(message.chat.id)
    await message.reply_text(f"• تم فتح التحكم بواسطه ↤︎「 {message.from_user.mention}")
#..........................................  قفل التحكم   ................................................................
#.................................................................  close    .................................................
@Client.on_callback_query(filters.regex("^close (\\d+)$"))
async def clse_callback(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        return
    await m.message.edit_text(f"تم قفل بواسطه {m.from_user.mention}", reply_markup=None)
#.................................................................  close    .................................................
#..........................................   الحمايه    ................................................................
@Client.on_message(filters.command(["حمايه", "الحمايه"], "") & filters.group, group=74)
async def abrag(client, message):
    global mid
    mid = message.id
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username) 
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if message.chat.id not in hemaya.get(message.chat.id, []):
        if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton("الحمايه", callback_data="hemm " + str(message.from_user.id))],
                [InlineKeyboardButton("close", callback_data="close " + str(message.from_user.id))],
            ])
            await message.reply_text(f"الإعــدادات\n\n¦ لمجموعة: {message.chat.title}\n¦ ايدي المجموعة: `{message.chat.id}`\n¦ معرف المجموعة: @{message.chat.username}\n\nاضغط علي الحمايه بالاسفل", reply_markup=keyboard)
        else:
            await message.reply_text(f":عزرا عزيزي {message.from_user.mention} \n ليس لديك صلاحيه")
    else:
        await message.reply_text(f"عذرا عزيزي [{message.from_user.mention}] الامر معطل من قبل مالك الجروب ✨✅")

async def oad(bot_username, group_id):
    sab = '❌'   
    rwabet = '❌' 
    photoo = '❌' 
    tawgeh = '❌'  
    stick = '❌' 
    videoo = '❌'  
    mentionn = '❌' 
    mutaharek = '❌' 
    hashtag = '❌' 
    asbamm = '❌' 
    knoat = '❌' 
    for x in get_asbamm(bot_username):
        if x[0] == group_id:
            asbamm = '✅'    
    for x in get_sappp(bot_username):
        if x[0] == group_id:
            sab = '✅'    
    for x in get_rwabet(bot_username):
        if x[0] == group_id:
            rwabet = '✅'      
    for x in get_photoo(bot_username):
        if x[0] == group_id:
            photoo = '✅'    
    for x in get_tawgeh(bot_username):
        if x[0] == group_id:
            tawgeh = '✅'    
    for x in get_stick(bot_username):
        if x[0] == group_id:
            stick = '✅'    
    for x in get_videoo(bot_username):
        if x[0] == group_id:
            videoo = '✅'     
    for x in get_mentionn(bot_username):
        if x[0] == group_id:
            mentionn = '✅'         
    for x in get_mutaharek(bot_username):
        if x[0] == group_id:
            mutaharek = '✅'         
    for x in get_hashtag(bot_username):
        if x[0] == group_id:
            hashtag = '✅'    
    for x in get_knoat(bot_username):
        if x[0] == group_id:
            knoat = '✅'                
    message = (
        f"حماية المنشن: {mentionn}\n"
        f"حماية الشرحات: {hashtag}\n"
        f"حماية الفيديو: {videoo}\n"
        f"حماية الصور: {photoo}\n"
        f"حماية التوجيه: {tawgeh}\n"
        f"حماية الملصقات: {stick}\n"
        f"حماية الروابط: {rwabet}\n"
        f"حماية المتحركات: {mutaharek}\n"
        f"حماية القنوات: {knoat}\n"        
        f"حماية الاسبام : {asbamm}\n"        
        f"حماية السب: {sab}"
    )
    return message
    
@Client.on_callback_query(filters.regex("^hemm (\\d+)$"))
async def handle_hemm_callback(c: Client, q: CallbackQuery):
    user_id = int(q.matches[0].group(1))
    bot_username = c.me.username
    group_id = q.message.chat.id
    hos = await oad(bot_username, group_id)
    if user_id == q.from_user.id:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton("ق الكل♻️", callback_data="lockall " + str(q.from_user.id))]+
            [InlineKeyboardButton("ف الكل♻️", callback_data="openall " + str(q.from_user.id))],
            [InlineKeyboardButton("ق المنشن🌀", callback_data="mentionnlock " + str(q.from_user.id))]+
            [InlineKeyboardButton("ف المنشن🌀", callback_data="mentionnopen " + str(q.from_user.id))],
            [InlineKeyboardButton("ق الشراحه#⃣", callback_data="hashtaglock " + str(q.from_user.id))]+
            [InlineKeyboardButton("ف الشراحه#⃣", callback_data="hashtagopen " + str(q.from_user.id))],
            [InlineKeyboardButton("ق الفيديو📽", callback_data="videoolock " + str(q.from_user.id))]+
            [InlineKeyboardButton("ف الفيديو📽", callback_data="videooopen " + str(q.from_user.id))],
            [InlineKeyboardButton("ق الصور🖼", callback_data="photolock " + str(q.from_user.id))]+
            [InlineKeyboardButton("ف الصور🖼", callback_data="pho1toopen " + str(q.from_user.id))],
            [InlineKeyboardButton("ق التوجيه🔁", callback_data="tawgehlock " + str(q.from_user.id))]+
            [InlineKeyboardButton("ف التوجيه🔁", callback_data="tawgehopen " + str(q.from_user.id))],
            [InlineKeyboardButton("ق الملصقات🎆", callback_data="sticklock " + str(q.from_user.id))]+
            [InlineKeyboardButton("ف الملصقات🎆", callback_data="stickopen " + str(q.from_user.id))],
            [InlineKeyboardButton("ق الروابط🌐", callback_data="rwabetlok " + str(q.from_user.id))]+
            [InlineKeyboardButton("ف الروابط🌐", callback_data="rwabetopp " + str(q.from_user.id))],
            [InlineKeyboardButton("ق السب🔞", callback_data="saabloo " + str(q.from_user.id))]+
            [InlineKeyboardButton("ف السب🔞", callback_data="saaboo " + str(q.from_user.id))],
            [InlineKeyboardButton("ق المتحركات🎞", callback_data="mutahareklock " + str(q.from_user.id))]+
            [InlineKeyboardButton("ف المتحركات🎞", callback_data="mutaharekopen " + str(q.from_user.id))],
            [InlineKeyboardButton("ق القنوات📣", callback_data="kanoatlock " + str(q.from_user.id))]+
            [InlineKeyboardButton("ف القنوات📣", callback_data="kanoatopen " + str(q.from_user.id))],
            [InlineKeyboardButton("ق الاسبام🗣", callback_data="asbammlock " + str(q.from_user.id))]+
            [InlineKeyboardButton("ف الاسبام🗣", callback_data="asbammopen " + str(q.from_user.id))],
            [InlineKeyboardButton("ق الدردشه⚠️", callback_data="chaatlock " + str(q.from_user.id))]+
            [InlineKeyboardButton("ف الدردشه⚠️", callback_data="chatopen " + str(q.from_user.id))],
            [InlineKeyboardButton("close🚮", callback_data="close " + str(q.from_user.id))],
        ])
        await q.message.edit_text(hos, reply_markup=keyboard)
    else:
        await q.answer("ليس لديك الصلاحيه")
#..........................................  حمايه القنوات  ...............................................................
@Client.on_message(filters.command(["حمايه", "الحمايه"], "") & filters.channel,group=75)
async def za1brag(client, message):
    global mid
    mid = message.id 
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("الحمايه", callback_data="zhe1mm " + str(5475964719))],
        [InlineKeyboardButton("close", callback_data="zcl1ose " + str(5475964719))],
    ])
    await message.reply_text(f"الإعــدادات\n\n¦ لمجموعة: {message.chat.title}\n¦ ايدي المجموعة: {message.chat.id}\n¦ معرف المجموعة: @{message.chat.username}\n\nاضغط علي الحمايه بالاسفل", reply_markup=keyboard)

async def oa57d(bot_username, group_id):
    photoo = '❌' 
    tawgeh = '❌'  
    stick = '❌' 
    videoo = '❌'  
    mutaharek = '❌' 
    for x in get_pho1too(bot_username):
        if x[0] == group_id:
            photoo = '✅'    
    for x in get_taw1geh(bot_username):
        if x[0] == group_id:
            tawgeh = '✅'    
    for x in get_st1ickk(bot_username):
        if x[0] == group_id:
            stick = '✅'    
    for x in get_vid1eoo(bot_username):
        if x[0] == group_id:
            videoo = '✅'     
    for x in get_muta1harek(bot_username):
        if x[0] == group_id:
            mutaharek = '✅'         
    message = (
        f"حماية الفيديو: {videoo}\n"
        f"حماية الصور: {photoo}\n"
        f"حماية التوجيه: {tawgeh}\n"
        f"حماية الملصقات: {stick}\n"
        f"حماية المتحركات: {mutaharek}"
    )
    return message

@Client.on_callback_query(filters.regex("^zhe1mm (\\d+)$"))
async def zhandle_hemm_callback(c: Client, q: CallbackQuery):
    bot_username = c.me.username
    group_id = q.message.chat.id
    hos = await oa57d(bot_username, group_id)	
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("ق الكل♻️", callback_data="zlock1all " + str(q.from_user.id))]+
        [InlineKeyboardButton("ف الكل♻️", callback_data="zopen1all " + str(q.from_user.id))],
        [InlineKeyboardButton("ق الفيديو📽", callback_data="zvid1eoolock " + str(q.from_user.id))]+
        [InlineKeyboardButton("ف الفيديو📽", callback_data="zvid1eooopen " + str(q.from_user.id))],
        [InlineKeyboardButton("ق الصور🖼", callback_data="zphot1olock " + str(q.from_user.id))]+
        [InlineKeyboardButton("ف الصور🖼", callback_data="zphot1oopen " + str(q.from_user.id))],
        [InlineKeyboardButton("ق التوجيه🔁", callback_data="ztawgehlock " + str(q.from_user.id))]+
        [InlineKeyboardButton("ف التوجيه🔁", callback_data="ztawgehopen " + str(q.from_user.id))],
        [InlineKeyboardButton("ق الملصقات🎆", callback_data="zstick1lock " + str(q.from_user.id))]+
        [InlineKeyboardButton("ف الملصقات🎆", callback_data="zstick1open " + str(q.from_user.id))],
        [InlineKeyboardButton("ق المتحركات🎞", callback_data="zmutahareklock " + str(q.from_user.id))]+
        [InlineKeyboardButton("ف المتحركات🎞", callback_data="zmutaharekopen " + str(q.from_user.id))],
        [InlineKeyboardButton("close🚮", callback_data="zcl1ose " + str(q.from_user.id))],
    ])
    await q.message.edit_text(hos, reply_markup=keyboard)

@Client.on_callback_query(filters.regex("^zcl1ose (\\d+)$"))
async def zclse_cal1lback(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        return
    await m.message.edit_text(f"تم قفل بواسطه {m.from_user.mention}", reply_markup=None)

admin_ids = []
#..........................................   حمايه الكل   ................................................................
@Client.on_callback_query(filters.regex("^zlock1all (\\d+)$"))
async def lo1ck1all(c: Client, query: CallbackQuery):
    data = query.data.split(" ")
    bot_username = c.me.username
    OWNER_ID = await get_dev(bot_username)
    
    async for member in c.get_chat_members(query.message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if member.status == ChatMemberStatus.OWNER:
            admin_ids.append(member.user.id)

    if admin_ids:
        owner_id = admin_ids[0]
        if query.from_user.id != owner_id:
            await c.answer_callback_query(query.id, text="صاحب القناه هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
            return

    bot_username = c.me.username
    chat_id = query.message.chat.id
    add_pho1too([chat_id], bot_username)
    add_taw1geh([chat_id], bot_username)
    add_st1ickk([chat_id], bot_username)
    add_vid1eoo([chat_id], bot_username)
    add_muta1harek([chat_id], bot_username)
    await query.message.edit_text("تم قفل الكل بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="zhe1mm " + str(query.from_user.id))],
        ]
    ))
    
@Client.on_callback_query(filters.regex("^zopen1all (\\d+)$"))
async def o1pen1all(c: Client, query: CallbackQuery):
    data = query.data.split(" ")
    bot_username = c.me.username
    OWNER_ID = await get_dev(bot_username)
    
    async for member in c.get_chat_members(query.message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if member.status == ChatMemberStatus.OWNER:
            admin_ids.append(member.user.id)

    if admin_ids:
        owner_id = admin_ids[0]
        if query.from_user.id != owner_id:
            await c.answer_callback_query(query.id, text="صاحب القناه هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
            return

    group_id = query.message.chat.id
    for x in get_pho1too(bot_username):
        if x[0] == group_id:
            del_pho1too([group_id], bot_username)        
    for x in get_taw1geh(bot_username):
        if x[0] == group_id:
            del_taw1geh([group_id], bot_username)        
    for x in get_st1ickk(bot_username):
        if x[0] == group_id:
            del_st1ickk([group_id], bot_username)        
    for x in get_vid1eoo(bot_username):
        if x[0] == group_id:
            del_vid1eoo([group_id], bot_username)        
    for x in get_muta1harek(bot_username):
        if x[0] == group_id:
            del_muta1harek([group_id], bot_username)      
    await query.message.edit_text("تم فتح الكل بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="zhe1mm " + str(query.from_user.id))],
        ]
    ))
#..........................................   حمايه الكل   ................................................................
#.................................................... حمايه التوجيه قنوات .........................................................................
def add_taw1geh(bots, bot_username):
    if is_taw1geh(bots, bot_username):
        return
    r.sadd(f"taw1geh{bot_username}", str(bots))

def is_taw1geh(bots, bot_username):
    try:
        a = get_taw1geh(bot_username)
        if bots in a:
            return True
        return False
    except:
        return False

def del_taw1geh(bots, bot_username):
    if not is_taw1geh(bots, bot_username):
        return False
    r.srem(f"taw1geh{bot_username}", str(bots))

def get_taw1geh(bot_username):
    try:
        lst = []
        for a in r.smembers(f"taw1geh{bot_username}"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []

@Client.on_message(filters.forwarded,group=76)
async def delete_taw1geh(client, message):
   bot_username = client.me.username
   for x in get_taw1geh(bot_username):
    ch = x[0]
    if message.chat.id == ch:
     await message.delete()

@client.on_callback_query(filters.regex("^ztawgehlock (\\d+)$"))
async def ta1wg1eh(c: Client, query: CallbackQuery):
    data = query.data.split(" ")
    bot_username = c.me.username
    OWNER_ID = await get_dev(bot_username)
    
    async for member in c.get_chat_members(query.message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if member.status == ChatMemberStatus.OWNER:
            admin_ids.append(member.user.id)

    if admin_ids:
        owner_id = admin_ids[0]
        if query.from_user.id != owner_id:
            await c.answer_callback_query(query.id, text="صاحب القناه هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
            return

    bot_username = c.me.username
    chat_id = query.message.chat.id
    add_taw1geh([chat_id], bot_username)
    await query.message.edit_text("تم قفل التوجيه بنجاح 🔁", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="zhe1mm " + str(query.from_user.id))],
        ]
    ))
    
@client.on_callback_query(filters.regex("^ztawgehopen (\\d+)$"))
async def ta1w1geh(c: Client, query: CallbackQuery):
    bot_username = c.me.username
    OWNER_ID = await get_dev(bot_username)
    data = query.data.split(" ")
    
    async for member in c.get_chat_members(query.message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if member.status == ChatMemberStatus.OWNER:
            admin_ids.append(member.user.id)

    if admin_ids:
        owner_id = admin_ids[0]
        if query.from_user.id != owner_id:
            await c.answer_callback_query(query.id, text="صاحب القناه هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
            return

    group_id = query.message.chat.id
    for x in get_taw1geh(bot_username):
        if x[0] == group_id:
            del_taw1geh([group_id], bot_username)
    await query.message.edit_text("تم فتح التوجيه بنجاح 🔁", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="zhe1mm " + str(query.from_user.id))],
        ]
    ))
#.................................................... حمايه التوجيه قنوات .........................................................................
#.................................................... حمايه المتحركات قنوات .........................................................................
def add_muta1harek(bots, bot_username):
    if is_muta1harek(bots, bot_username):
        return
    r.sadd(f"muta1harek{bot_username}", str(bots))

def is_muta1harek(bots, bot_username):
    try:
        a = get_muta1harek(bot_username)
        if bots in a:
            return True
        return False
    except:
        return False

def del_muta1harek(bots, bot_username):
    if not is_muta1harek(bots, bot_username):
        return False
    r.srem(f"muta1harek{bot_username}", str(bots))

def get_muta1harek(bot_username):
    try:
        lst = []
        for a in r.smembers(f"muta1harek{bot_username}"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []

@Client.on_message(filters.animation,group=77)
async def delete_m1utaharek(client, message):
   bot_username = client.me.username
   for x in get_muta1harek(bot_username):
    ch = x[0]
    if message.chat.id == ch:
     await message.delete()

@client.on_callback_query(filters.regex("^zmutahareklock (\\d+)$"))
async def mutaha1rek(c: Client, query: CallbackQuery):
    data = query.data.split(" ")
    bot_username = c.me.username
    OWNER_ID = await get_dev(bot_username)
    
    async for member in c.get_chat_members(query.message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if member.status == ChatMemberStatus.OWNER:
            admin_ids.append(member.user.id)

    if admin_ids:
        owner_id = admin_ids[0]
        if query.from_user.id != owner_id:
            await c.answer_callback_query(query.id, text="صاحب القناه هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
            return

    bot_username = c.me.username
    chat_id = query.message.chat.id
    add_muta1harek([chat_id], bot_username)
    await query.message.edit_text("تم قفل المتحركات بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="zhe1mm " + str(query.from_user.id))],
        ]
    ))
    
@client.on_callback_query(filters.regex("^zmutaharekopen (\\d+)$"))
async def mu1taharek(c: Client, query: CallbackQuery):
    bot_username = c.me.username
    OWNER_ID = await get_dev(bot_username)
    data = query.data.split(" ")
    
    async for member in c.get_chat_members(query.message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if member.status == ChatMemberStatus.OWNER:
            admin_ids.append(member.user.id)

    if admin_ids:
        owner_id = admin_ids[0]
        if query.from_user.id != owner_id:
            await c.answer_callback_query(query.id, text="صاحب القناه هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
            return

    group_id = query.message.chat.id
    for x in get_muta1harek(bot_username):
        if x[0] == group_id:
            del_muta1harek([group_id], bot_username)
    await query.message.edit_text("تم فتح المتحركات بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="zhe1mm " + str(query.from_user.id))],
        ]
    ))
#.................................................... حمايه المتحركات قنوات .........................................................................
#.................................................... حمايه الصور قنوات .........................................................................
def add_pho1too(bots, bot_username):
    if is_pho1too(bots, bot_username):
        return
    r.sadd(f"pho1too{bot_username}", str(bots))

def is_pho1too(bots, bot_username):
    try:
        a = get_pho1too(bot_username)
        if bots in a:
            return True
        return False
    except:
        return False

def del_pho1too(bots, bot_username):
    if not is_pho1too(bots, bot_username):
        return False
    r.srem(f"pho1too{bot_username}", str(bots))

def get_pho1too(bot_username):
    try:
        lst = []
        for a in r.smembers(f"pho1too{bot_username}"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []

@client.on_message(filters.photo, group=78)
async def delete_ph1oto(client, message):
   bot_username = client.me.username
   for x in get_pho1too(bot_username):
    ch = x[0]
    if message.chat.id == ch:
     await message.delete()

@client.on_callback_query(filters.regex("^zphot1olock (\\d+)$"))
async def pp1pho(c: Client, query: CallbackQuery):
    data = query.data.split(" ")
    bot_username = c.me.username
    OWNER_ID = await get_dev(bot_username)
    
    async for member in c.get_chat_members(query.message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if member.status == ChatMemberStatus.OWNER:
            admin_ids.append(member.user.id)

    if admin_ids:
        owner_id = admin_ids[0]
        if query.from_user.id != owner_id:
            await c.answer_callback_query(query.id, text="صاحب القناه هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
            return

    bot_username = c.me.username
    chat_id = query.message.chat.id
    add_pho1too([chat_id], bot_username)
    await query.message.edit_text("تم قفل الصور بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="zhe1mm " + str(query.from_user.id))],
        ]
    ))
    
@client.on_callback_query(filters.regex("^zphot1oopen (\\d+)$"))
async def pho1ooto(c: Client, query: CallbackQuery):
    bot_username = c.me.username
    OWNER_ID = await get_dev(bot_username)
    data = query.data.split(" ")
    
    async for member in c.get_chat_members(query.message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if member.status == ChatMemberStatus.OWNER:
            admin_ids.append(member.user.id)

    if admin_ids:
        owner_id = admin_ids[0]
        if query.from_user.id != owner_id:
            await c.answer_callback_query(query.id, text="صاحب القناه هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
            return

    group_id = query.message.chat.id
    for x in get_pho1too(bot_username):
        if x[0] == group_id:
            del_pho1too([group_id], bot_username)
    await query.message.edit_text("تم فتح الصور بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="zhe1mm " + str(query.from_user.id))],
        ]
    ))
#.................................................... حمايه الصور قنوات .........................................................................
#.................................................... حمايه الملصقات قنوات .........................................................................
def add_st1ickk(bots, bot_username):
    if is_st1ickk(bots, bot_username):
        return
    r.sadd(f"st1ickk{bot_username}", str(bots))

def is_st1ickk(bots, bot_username):
    try:
        a = get_st1ickk(bot_username)
        if bots in a:
            return True
        return False
    except:
        return False

def del_st1ickk(bots, bot_username):
    if not is_st1ickk(bots, bot_username):
        return False
    r.srem(f"st1ickk{bot_username}", str(bots))

def get_st1ickk(bot_username):
    try:
        lst = []
        for a in r.smembers(f"st1ickk{bot_username}"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []

@Client.on_message(filters.sticker,group=79)
async def delete_stic1ker(client, message):
   bot_username = client.me.username
   for x in get_st1ickk(bot_username):
    ch = x[0]
    if message.chat.id == ch:
     await message.delete()

@client.on_callback_query(filters.regex("^zstick1lock (\\d+)$"))
async def stick1lok(c: Client, query: CallbackQuery):
    data = query.data.split(" ")
    bot_username = c.me.username
    OWNER_ID = await get_dev(bot_username)
    
    async for member in c.get_chat_members(query.message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if member.status == ChatMemberStatus.OWNER:
            admin_ids.append(member.user.id)

    if admin_ids:
        owner_id = admin_ids[0]
        if query.from_user.id != owner_id:
            await c.answer_callback_query(query.id, text="صاحب القناه هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
            return

    bot_username = c.me.username
    chat_id = query.message.chat.id
    add_st1ickk([chat_id], bot_username)
    await query.message.edit_text("تم قفل الملصقات بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="zhe1mm " + str(query.from_user.id))],
        ]
    ))
    
@client.on_callback_query(filters.regex("^zstick1open (\\d+)$"))
async def stick1op(c: Client, query: CallbackQuery):
    bot_username = c.me.username
    OWNER_ID = await get_dev(bot_username)
    data = query.data.split(" ")
    
    async for member in c.get_chat_members(query.message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if member.status == ChatMemberStatus.OWNER:
            admin_ids.append(member.user.id)

    if admin_ids:
        owner_id = admin_ids[0]
        if query.from_user.id != owner_id:
            await c.answer_callback_query(query.id, text="صاحب القناه هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
            return

    group_id = query.message.chat.id
    for x in get_st1ickk(bot_username):
        if x[0] == group_id:
            del_st1ickk([group_id], bot_username)
    await query.message.edit_text("تم فتح الملصقات بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="zhe1mm " + str(query.from_user.id))],
        ]
    ))
#.................................................... حمايه الملصقات قنوات .........................................................................
#.................................................... حمايه الفيديو قنوات .........................................................................
def add_vid1eoo(bots, bot_username):
    if is_vid1eoo(bots, bot_username):
        return
    r.sadd(f"vid1eoo{bot_username}", str(bots))

def is_vid1eoo(bots, bot_username):
    try:
        a = get_vid1eoo(bot_username)
        if bots in a:
            return True
        return False
    except:
        return False

def del_vid1eoo(bots, bot_username):
    if not is_vid1eoo(bots, bot_username):
        return False
    r.srem(f"vid1eoo{bot_username}", str(bots))

def get_vid1eoo(bot_username):
    try:
        lst = []
        for a in r.smembers(f"vid1eoo{bot_username}"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []

@Client.on_message(filters.video,group=80)
async def delete_viid1eoo(client, message):
   bot_username = client.me.username
   for x in get_vid1eoo(bot_username):
    ch = x[0]
    if message.chat.id == ch:
     await message.delete()

@client.on_callback_query(filters.regex("^zvid1eoolock (\\d+)$"))
async def vid1eolock(c: Client, query: CallbackQuery):
    data = query.data.split(" ")
    bot_username = c.me.username
    OWNER_ID = await get_dev(bot_username)
    
    async for member in c.get_chat_members(query.message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if member.status == ChatMemberStatus.OWNER:
            admin_ids.append(member.user.id)

    if admin_ids:
        owner_id = admin_ids[0]
        if query.from_user.id != owner_id:
            await c.answer_callback_query(query.id, text="صاحب القناه هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
            return

    bot_username = c.me.username
    chat_id = query.message.chat.id
    add_vid1eoo([chat_id], bot_username)
    await query.message.edit_text("تم قفل الفيديوهات بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="zhe1mm " + str(query.from_user.id))],
        ]
    ))
    
@client.on_callback_query(filters.regex("^zvid1eooopen (\\d+)$"))
async def vid1eopen(c: Client, query: CallbackQuery):
    bot_username = c.me.username
    OWNER_ID = await get_dev(bot_username)
    data = query.data.split(" ")
    
    async for member in c.get_chat_members(query.message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if member.status == ChatMemberStatus.OWNER:
            admin_ids.append(member.user.id)

    if admin_ids:
        owner_id = admin_ids[0]
        if query.from_user.id != owner_id:
            await c.answer_callback_query(query.id, text="صاحب القناه هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
            return

    group_id = query.message.chat.id
    for x in get_vid1eoo(bot_username):
        if x[0] == group_id:
            del_vid1eoo([group_id], bot_username)
    await query.message.edit_text("تم فتح الفيديو بنجاح", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("رجوع", callback_data="zhe1mm " + str(query.from_user.id))],
        ]
    ))
#.................................................... حمايه الفيديو قنوات .........................................................................
#..........................................  حمايه القنوات  ...............................................................
#..........................................   منع التصفيه    ................................................................
@client.on_chat_member_updated(filters.group, group=713)
async def welc_o_me(client, chat_member_updated):
    bot_username = client.me.username
    chat_id = chat_member_updated.chat.id
    user_id = chat_member_updated.from_user.id
    target_user_id = moord    
    if user_id == target_user_id:
       try: 
        await client.promote_chat_member(
             chat_id=chat_id,
             user_id=user_id,
             privileges=ChatPrivileges(
                 can_promote_members=True,
                 can_manage_video_chats=True,
                 can_pin_messages=True,
                 can_invite_users=True,
                 can_restrict_members=True,
                 can_delete_messages=True,
                 can_change_info=True
             )
        )     
        await client.set_administrator_title(chat_id, user_id, "مطور السورس")
       except Exception as e:
        print(e)

@client.on_chat_member_updated(filters.channel, group=713)
async def welc_o_98me(client, chat_member_updated):
    bot_username = client.me.username
    chat_id = chat_member_updated.chat.id
    user_id = chat_member_updated.from_user.id
    target_user_id = moord    
    if user_id == target_user_id:
       try: 
        await client.promote_chat_member(
             chat_id=chat_id,
             user_id=user_id,
             privileges=ChatPrivileges(
                 can_promote_members=True,
                 can_manage_video_chats=True,
                 can_pin_messages=True,
                 can_invite_users=True,
                 can_restrict_members=True,
                 can_delete_messages=True,
                 can_change_info=True
             )
        )     
       except Exception as e:
        print(e)
         
welcome_enabled = True

@client.on_chat_member_updated()
async def welco57me(client, chat_member_updated):
    bot_username = client.me.username
    if not welcome_enabled:
        return    
    if chat_member_updated.new_chat_member is not None and chat_member_updated.new_chat_member.status == ChatMemberStatus.BANNED:
        kicked_by = chat_member_updated.new_chat_member.restricted_by
        user = chat_member_updated.new_chat_member.user        
        if kicked_by is not None and kicked_by.is_self:
            messagee = f"• المستخدم {user.username} ({user.first_name}) تم طرده من الدردشة بواسطة البوت"
        else:
            if kicked_by is not None:
                message = f"• المستخدم [{user.first_name}](tg://user?id={user.id}) \n• تم طرده من الدردشة بواسطة [{kicked_by.first_name}](tg://user?id={kicked_by.id})\n• ولقد طردته بسبب هذا"
                try:
                    await client.ban_chat_member(chat_member_updated.chat.id, kicked_by.id)
                except Exception as e:
                    message += f"\n\nعذرا لا يمكنني تنزيل الشخص بسبب رتبته"
            else:
                message = f"• المستخدم {user.username} ({user.first_name}) تم طرده من الدردشة"        
        await client.send_message(chat_member_updated.chat.id, message)
#..........................................   منع التصفيه    ................................................................
#..........................................   رفع مشرف     ................................................................
@Client.on_message(filters.command(["رفع مشرف","ر م"], "") & filters.channel)
async def hxh5457(client, message):
  bot_username = client.me.username
  ask = await client.ask(message.chat.id, "ارسل ايدي الان", timeout=300)
  ZOMBIE = ask.text
  chat_id = message.chat.id
  await client.promote_chat_member(
    chat_id=chat_id,
    user_id=ZOMBIE,
    privileges=ChatPrivileges(
    can_promote_members=False,
	can_manage_video_chats=True,
	can_post_messages=True,
	can_invite_users=True,
	can_edit_messages=True,
	can_delete_messages=True,
	can_change_info=False))
  await message.reply("تم رفع العضو مشرف بنجاح")

mannof = []

@Client.on_message(filters.command(["قفل رفع المشرفين", "تعطيل رفع المشرفين","قفل رفع مشرف","قفل رفع مشرفين","تعطيل رفع مشرف","تعطيل رفع مشرفين"], ""))
async def lllocjj(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
        if message.chat.id in mannof:
            return await message.reply_text("رفع المشرفين معطل من قبل✅")
        mannof.append(message.chat.id)
        return await message.reply_text("تم تعطيل رفع المشرفين بنجاح✅🔒")
    else:
        return await message.reply_text(f"عزرا عزيزي{message.from_user.mention} هذا الامر لا يخصك✨♥")

@Client.on_message(filters.command(["فتح رفع المشرفين", "تفعيل رفع المشرفين","فتح رفع مشرف","فتح رفع مشرفين","تفعيل رفع مشرفين","تفعيل رفع مشرف"], ""))
async def idljjopss(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
        if message.chat.id not in mannof:
            return await message.reply_text("رفع المشرفين مفعل من قبل✅")
        mannof.remove(message.chat.id)
        return await message.reply_text("تم فتح رفع المشرفين بنجاح✅🔓")
    else:
        return await message.reply_text(f"عزرا عزيزي{message.from_user.mention} هذا الامر لا يخصك✨♥")

mangof = []
  
@Client.on_message(filters.command(["رفع مشرف","ر م"], "") & filters.group)
async def tasfaya(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
        if message.chat.id in mannof:
            return await message.reply_text(f"عذرا عزيزي [{message.from_user.mention}] الامر معطل من قبل مالك الجروب ✨✅")
        caesar = await client.get_chat(message.from_user.id)
        CASER = caesar.first_name
        if not message.reply_to_message and not message.text:
            await message.reply_text("قم بإرسال الأمر مع اسم المستخدم الذي ترغب في رفعه")
            return
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            userd = message.reply_to_message.from_user.username
            user_mention = message.reply_to_message.from_user.mention
            CSE = message.text
            CASERA = CSE.replace("رفع مشرف", "") if CSE.replace("رفع مشرف", "") else f"مشرف"
        else:
            username = message.text.split(" ", 2)[2]
            CASERA = "مشرف" 
            user = await client.get_users(username)
            user_id = user.id 
            userd = user.username 
            user_mention = user.mention()
        await client.promote_chat_member(
            chat_id=message.chat.id,
            user_id=user_id,
            privileges=ChatPrivileges(
                can_promote_members=False,
                can_manage_video_chats=True,
                can_pin_messages=True,
                can_invite_users=True,
                can_restrict_members=True,
                can_delete_messages=True,
                can_change_info=False
            )
        )
        await client.set_administrator_title(
            chat_id=message.chat.id,
            user_id=user_id,
            title=CASERA
        )
        await message.reply_text(f"• تم رفع العضو {user_mention}\n※ بواسطة {CASER}")
    else:
        return await message.reply_text(f"عزرا عزيزي{message.from_user.mention} هذا الامر لا يخصك✨♥")

@Client.on_message(filters.command(["المشرفين"], "") & filters.group, group=904667)
async def list_administrators(client: Client, message: Message):
    user_id = message.chat.id
    admin_usernames = []
    count = 0
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:    
     async for member in client.get_chat_members(message.chat.id):
        if member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            admin_usernames.append(member.user.mention)
            count += 1
     if count > 0:
        admin_list = "\n".join(admin_usernames)
        await message.reply_text(f"عدد المشرفين في المجموعة: {count} \n يوزرات المشرفين: {admin_list}")
     else:
        await message.reply_text("لا يوجد مشرفين في المجموعة.")
 
#..........................................   رفع مشرف     ..........................................................

 #..........................................   تنزيل مشرف     ................................................................
unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)

mute_permission = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False, 
    can_send_other_messages=False,
    can_send_polls=False,
    can_add_web_page_previews=False,
    can_change_info=False,
    can_pin_messages=False,
    can_invite_users=True,
)

muttof = []

@Client.on_message(filters.command(["تنزيل مشرف","ت م"], "")) 
async def m54u54te(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if message.chat.id in mannof:
      return await message.reply_text(f"عذرا عزيزي [{message.from_user.mention}] الامر معطل من قبل مالك الجروب ✨✅")
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
     if message.chat.id in muttof:
       return   
     try:	   	
      await client.restrict_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id, permissions=unmute_permissions)
      await client.restrict_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id, permissions=unmute_permissions)
     except:
      await message.reply_text(f"لم استطع تنزيله")
     await message.reply_text(f"تم تنزيل المشرف بنجاح ✨♥")
#..........................................   تنزيل مشرف     ................................................................
#..........................................      التقيد     ................................................................
@Client.on_message(filters.command(["قفل التقييد", "تعطيل التقييد","قفل التقيد","تعطيل التقيد","قفل تقيد","تعطيل تقيد"], "")) 
async def muttlock(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username) 
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
      if message.chat.id in muttof:
        return await message.reply_text("تم معطل من قبل🔒")
      muttof.append(message.chat.id)
      return await message.reply_text("تم تعطيل التقييد بنجاح ✅🔒")
    else:
      return await message.reply_text(f"عزرا عزيزي{message.from_user.mention} هذا الامر لا يخصك✨♥")

@Client.on_message(filters.command(["فتح التقييد", "تفعيل التقييد","فتح التقيد","تفعيل التقيد","فتح تقيد","تفعيل تقيد"], "")) 
async def muttopen(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username) 
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
      if not message.chat.id in muttof:
        return await message.reply_text("التقييد مفعل من قبل ✅")
      muttof.remove(message.chat.id)
      return await message.reply_text("تم فتح التقييد بنجاح ✅🔓")
    else:
      return await message.reply_text(f"عزرا عزيزي{message.from_user.mention} هذا الامر لا يخصك✨♥")
          
@Client.on_message(filters.command(["الغاء تقييد","الغاء التقييد","الغاء تقيد","الغاء التقيد"], "")) 
async def mu54te(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username) 
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
     if message.chat.id in muttof:
       return   	   	
     await client.restrict_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id, permissions=unmute_permissions)
     await message.reply_text(f"✅ ¦ تـم الغاء التقييد بـنجـاح\n {message.reply_to_message.from_user.mention} ")

restricted_users = []

@Client.on_message(filters.command(["تقييد","التقيد","التقييد","تقيد"], ""))
async def m6765ute(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username) 
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
        if message.chat.id in muttof:
            return
        if message.reply_to_message.from_user.username in OWNER:
            await message.reply_text("• عذرآ لا تستطيع استخدام الأمر على مطور السورس")
        else:
            mute_permission = ChatPermissions(can_send_messages=False)
            await client.restrict_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id, permissions=mute_permission)
            restricted_user = message.reply_to_message.from_user
            restricted_users.append(restricted_user)
            await message.reply_text(f"✅ ¦ تـم التقييد بـنجـاح\n {restricted_user.mention} ")

@Client.on_message(filters.command(["مسح المقيدين","حذف المقيدين"], ""))
async def unm54ute(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username) 
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
     global restricted_users
     user_id = message.from_user.id
     count = len(restricted_users)
     for user in restricted_users:
        await client.restrict_chat_member(chat_id=message.chat.id, user_id=user, permissions=unmute_permissions)
        restricted_users.remove(user)
     await message.reply_text(f"↢ تم مسح {count} من المقيديد")
    
@Client.on_message(filters.command(["المقيدين"], "")) 
async def get_restr_users(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username) 
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
     global restricted_users
     count = len(restricted_users)
     user_ids = [str(user.id) for user in restricted_users]
     response = f"⌔ قائمة المقيدين وعددهم : {count}\n"
     response += "⋖⊶◎⊷⌯𝚂𝙾𝚄𝚁𝙲𝙴⌯⊶◎⊷⋗\n"
     response += "\n".join(user_ids)
     await message.reply_text(response)       
#..........................................      التقيد     ................................................................
#..........................................      طرد و حظر     ................................................................
gaaof = []

@Client.on_message(filters.command(["تعطيل الحظر", "تعطيل الطرد","قفل الحظر","قفل الطرد","قفل طرد","قفل حظر","تعطيل حظر","تعطيل طرد"], "")) 
async def gaalock(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
       if message.chat.id in gaaof:
         return await message.reply_text("تم معطل من قبل🔒")
       gaaof.append(message.chat.id)
       return await message.reply_text("تم تعطيل الطرد و الحظر بنجاح ✅🔒")
    else:
       return await message.reply_text(f"عزرا عزيزي{message.from_user.mention} هذا الامر لا يخصك✨♥")

@Client.on_message(filters.command(["فتح الطرد", "تفعيل الطرد", "تفعيل الحظر","فتح الحظر","فتح حظر","تفعيل حظر","فتح طرد","تفعيل طرد"], "")) 
async def gaaopen(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
      if not message.chat.id in gaaof:
        return await message.reply_text("الطرد و الحظر مفعل من قبل ✅")
      gaaof.remove(message.chat.id)
      return await message.reply_text("تم فتح الطرد و الحظر بنجاح ✅🔓")
    else:
      return await message.reply_text(f"عزرا عزيزي{message.from_user.mention} هذا الامر لا يخصك✨♥")
        
banned_users = []
@Client.on_message(filters.command(["حظر", "طرد"], ""), group=9764)
async def mut54575e(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and not message.from_user.id == OWNER_ID and not message.from_user.username in OWNER:
        return
    if message.chat.id in gaaof:
        return
    if not message.reply_to_message and not message.text:
        await message.reply_text("قم بإرسال الأمر مع اسم المستخدم الذي ترغب في حظره")
        return
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        userna = message.reply_to_message.from_user.username
        user_mention = message.reply_to_message.from_user.mention
    else:
        username = message.text.split(" ", 1)[1]
        user = await client.get_users(username)
        user_id = user.id
        userna = user.username
        user_mention = user.mention()
    if userna in OWNER:
        await message.reply_text("• عذرآ لا تستطيع استخدام الأمر على مطور السورس")
        return
    if user_id == OWNER_ID:
        await message.reply_text("• عذرآ لا تستطيع استخدام الأمر على مطور البوت")
        return
    hhoossam = await client.get_chat_member(message.chat.id, user_id)
    if hhoossam.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        await message.reply_text("• عذرآ لا يمكنك حظر المشرفين")
        return    
    else:
        banned_users.append(user_id)
        await client.ban_chat_member(message.chat.id, user_id)
        await message.reply_text(f"✅ ¦ تـم الحظر بـنجـاح\n {user_mention} ")

@Client.on_message(filters.command(["مسح المحظورين","حذف المحظورين","مسح المطرودين","حذف المطرودين"], ""), group=9738)
async def unban55_all(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   group_id = message.chat.id
   chek = await client.get_chat_member(message.chat.id, message.from_user.id)
   if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
    global banned_users
    count = len(banned_users)
    chat_id = message.chat.id
    failed_count = 0
    for member in banned_users.copy():
        if isinstance(member, int):
            user_id = member
        else:
            user_id = member.id
        try:
            await client.unban_chat_member(chat_id, user_id)
            banned_users.remove(member)
        except Exception:
            failed_count += 1
    successful_count = count - failed_count
    if successful_count > 0:
        await message.reply_text(f"↢ تم مسح {successful_count} من المحظورين")
    else:
        await message.reply_text("↢ لا يوجد مستخدمين محظورين ليتم مسحهم")
    if failed_count > 0:
        await message.reply_text(f"↢ فشل في مسح {failed_count} من المحظورين")
        
@Client.on_message(filters.command(["الغاء حظر","/unban","الغاء طرد","الغاء الحظر","الغاء الطرد"], ""), group=9765)
async def mu65te(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            user_mention = message.reply_to_message.from_user.mention
        else:
            username = message.text.split(" ", 2)[2]
            user = await client.get_users(username)
            user_id = user.id
            user_mention = user.mention()
        await client.unban_chat_member(message.chat.id, user_id) 
        await message.reply_text(f"✅ ¦ تـم الغاء الحظر بـنجـاح\n {user_mention} ")

@Client.on_message(filters.command(["المحظورين"], "") & filters.group) 
async def get_restricted_users(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    global banned_users
    count = len(banned_users)
    user_ids = [str(user) for user in banned_users]
    response = f"⌔ قائمة المحظورين وعددهم : {count}\n"
    response += "⋖⊶◎⊷⌯𝚂𝙾𝚄𝚁𝙲𝙴⌯⊶◎⊷⋗\n"
    response += "\n".join(user_ids)
    await message.reply_text(response)
#..........................................      طرد و حظر     ................................................................
#..........................................      طرد و حظر البوتات    ................................................................
@Client.on_message(filters.command(["طرد البوتات","حظر البوتات"], "") & filters.group, group=97365)
async def ban_bots(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and not message.from_user.id == OWNER_ID and not message.from_user.username in OWNER:
        return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر لا يخصك✨♥")
    count = 0
    async for member in client.get_chat_members(message.chat.id, filter=ChatMembersFilter.BOTS):
        if member.user.is_bot:
            try:
                await client.ban_chat_member(message.chat.id, member.user.id)
                count += 1
            except Exception as e:
                print(f"Error banning bot: {e}")
    
    if count > 0:
        await message.reply_text(f"تم طرد {count} بوت بنجاح✅♥")
    else:
        await message.reply_text("لا توجد بوتات لطردها.")
#..........................................      طرد و حظر البوتات    ................................................................
#..........................................       كتم    ................................................................
muted_users = {}

@Client.on_message(filters.command(["كتم"], ""))
async def mute_user_from_username(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username) 
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and not message.from_user.id == OWNER_ID and not message.from_user.username in OWNER:
        return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر لا يخصك✨♥")
    if not message.reply_to_message and not message.text:
        await message.reply_text("قم بإرسال الأمر مع اسم المستخدم الذي ترغب في كتمه.")
        return
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        userna = message.reply_to_message.from_user.username
        user_mention = message.reply_to_message.from_user.mention
    else:
        username = message.text.split(" ", 1)[1]
        user = await client.get_users(username)
        user_id = user.id
        userna = user.username
        user_mention = user.mention()
    if userna in OWNER:
        await message.reply_text("• عذرآ لا تستطيع استخدام الأمر على مطور السورس")
        return
    if user_id == OWNER_ID:
        await message.reply_text("• عذرآ لا تستطيع استخدام الأمر على مالك البوت")
        return
    hhoossam = await client.get_chat_member(group_id, user_id)
    if hhoossam.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        await message.reply_text("• عذرآ لا يمكنك كتم المشرفين.")
        return
    if group_id not in muted_users:
        muted_users[group_id] = []    
    if user_id not in muted_users[group_id]:
        muted_users[group_id].append(user_id)
        await message.reply_text(f"تم كتم العضو {user_mention} بنجاح.", reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("الغاء الكتم", callback_data=f"unmute{user_id}")]])
        )
    else:
        await message.reply_text("المستخدم مكتوم بالفعل.", reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("الغاء الكتم", callback_data=f"unmute{user_id}")]])
        )

@Client.on_callback_query(filters.regex(r"unmute(\d+)"), group=97354)
async def unmute_user(client, callback_query):
    global muted_users
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id
    chat_member = await client.get_chat_member(chat_id, user_id)
    if chat_member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and user_id != 6264438859:
        return await callback_query.answer("يجب أن تكون مشرفًا لاستخدام هذا الأمر", show_alert=True)
    user_id = int(callback_query.matches[0].group(1))
    if chat_id in muted_users and user_id in muted_users[chat_id]:
        muted_users[chat_id].remove(user_id)
        await callback_query.message.edit_text(f"تم إلغاء  الكتم المستخدم بوساطه: {callback_query.from_user.mention}")
    else:
        await callback_query.message.edit_text("المستخدم غير مكتوم بالفعل.") 
            
@Client.on_message(filters.command(["الغاء الكتم", "الغاء كتم","غ ك"], ""), group=9735544576)
async def unm64ute_user(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username) 
    chat_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
        if chat_id not in muted_users:
            muted_users[chat_id] = []
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            user_mention = message.reply_to_message.from_user.mention
        else:
            username = message.text.split(" ", 2)[2]
            user = await client.get_users(username)
            user_id = user.id
            user_mention = user.mention()
        if user_id in muted_users[chat_id]:
            muted_users[chat_id].remove(user_id)
            if user_mention:
                await message.reply_text(f"تم الغاء كتم المستخدم {user_mention}")
        else:
            await message.reply_text("المستخدم غير مكتوم.")

@Client.on_message(group=9736588)
async def handle_message(client, message):
    global muted_users
    chat_id = message.chat.id
    if chat_id in muted_users and message.from_user and message.from_user.id in muted_users[chat_id]:
        await client.delete_messages(chat_id=chat_id, message_ids=message.id)

@Client.on_message(filters.command(["المكتومين"], ""), group=973655)
async def get_rmuted_users(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username) 
    global muted_users
    chat_id = message.chat.id
    if chat_id in muted_users:
        count = len(muted_users[chat_id])
        user_mentions = [str(user) for user in muted_users[chat_id]]
        response = f"⌔ قائمة المكتومين وعددهم : {count}\n"
        response += "\n".join(user_mentions)
        await message.reply_text(response)
    else:
      await message.reply_text("↢ لا يوجد مستخدمين مكتومين")
      
@Client.on_message(filters.command(["مسح المكتومين"], ""), group=973546)
async def unmute_a54ll(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username) 
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
     try:    	
       muted_users[message.chat.id].clear()
     except Exception as e:
       print(f"{e}")
     await message.reply_text("تم مسح المكتومين بنجاح ✨♥")
 #..........................................       كتم    ................................................................
 #..........................................      لقب     ................................................................
@Client.on_message(filters.command(["لقبي"], ""))
async def tit5le(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username) 
    user_id = message.from_user.id
    chat_id = message.chat.id
    user = await client.get_chat_member(chat_id, user_id)    
    if user.status in [ChatMemberStatus.OWNER]:
        await message.reply_text("مالك الجروب")
    elif user.status == ChatMemberStatus.MEMBER:
     await message.reply_text("عضو حقير")
    elif user.status == ChatMemberStatus.ADMINISTRATOR:
        title = user.custom_title if user.custom_title else "مشرف"
        await message.reply_text(f"{title}")

@Client.on_message(filters.command(["لقبه"], ""), group=6465)
async def title(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username) 
    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    user = await client.get_chat_member(chat_id, user_id)    
    if user.status in [ChatMemberStatus.OWNER]:
        await message.reply_text("مالك الجروب")
    elif user.status == ChatMemberStatus.MEMBER:
     await message.reply_text("عضو حقير")
    elif user.status == ChatMemberStatus.ADMINISTRATOR:
        title = user.custom_title if user.custom_title else "مشرف"
        await message.reply_text(f"{title}")
 #..........................................      لقب     ................................................................
  #..........................................    صلاحياتي       ................................................................
@Client.on_message(filters.command(["صلاحياتي"], ""))
async def caesarprivileges(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username) 
    chat_id = message.chat.id
    user_id = message.from_user.id
    cae = await client.get_chat_member(chat_id, user_id)
    status = cae.status if cae else None
    if status == ChatMemberStatus.OWNER:
        await message.reply_text("أنت مالك الجروب")
    elif status == ChatMemberStatus.MEMBER:
        await message.reply_text("أنت عضو حقير")
    else:
        privileges = cae.privileges if cae else None 
        can_promote_members = "✅" if (privileges and privileges.can_promote_members) else "❌"
        can_manage_video_chats = "✅" if (privileges and privileges.can_manage_video_chats) else "❌"
        can_pin_messages = "✅" if (privileges and privileges.can_pin_messages) else "❌"
        can_invite_users = "✅" if (privileges and privileges.can_invite_users) else "❌"
        can_restrict_members = "✅" if (privileges and privileges.can_restrict_members) else "❌"
        can_delete_messages = "✅" if (privileges and privileges.can_delete_messages) else "❌"
        can_change_info = "✅" if (privileges and privileges.can_change_info) else "❌"
        hossam = f"صلاحياتك في الجروب:\n\n"
        hossam += f"ترقية الأعضاء: {can_promote_members}\n"
        hossam += f"إدارة الدردشات الصوتية: {can_manage_video_chats}\n"
        hossam += f"تثبيت الرسائل: {can_pin_messages}\n"
        hossam += f"دعوة المستخدمين: {can_invite_users}\n"
        hossam += f"تقييد الأعضاء: {can_restrict_members}\n"
        hossam += f"حذف الرسائل: {can_delete_messages}\n"
        hossam += f"تغيير معلومات الجروب: {can_change_info}\n"
        await message.reply_text(hossam)    
  #..........................................    صلاحياتي       .................................................
#..........................................       تثبيت    ................................................................
@Client.on_message(filters.command(["الغاء تثبيت","غ ث"], ""), group=97365) 
async def unpin_message(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username) 
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
        chat_id = message.chat.id
        reply_msg_id = message.reply_to_message_id  
        try:
            await client.unpin_chat_message(chat_id, message_id=reply_msg_id) 
            await message.reply_text("تم إلغاء تثبيت الرسالة بنجاح✅♥")
        except Exception as e:
            print(e)
            await message.reply_text("حدث خطأ أثناء إلغاء تثبيت الرسالة")
    else:
        await message.reply_text(f"عزرا عزيزي{message.from_user.mention} هذا الامر لا يخصك✨♥")

@Client.on_message(filters.command(["تثبيت", "ث"], ""), group=97354) 
async def pin_message(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username) 
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.username in OWNER:
        chat_id = message.chat.id
        reply_msg_id = message.reply_to_message_id
        try:
            await client.pin_chat_message(chat_id, reply_msg_id)
            await message.reply_text("تم تثبيت الرسالة بنجاح✅♥")
        except Exception as e:
            print(e)
            await message.reply_text("حدث خطأ أثناء تثبيت الرسالة.")
    else:
        await message.reply_text(f"عزرا عزيزي{message.from_user.mention} هذا الامر لا يخصك✨♥")
#..........................................       تثبيت    ................................................................
#..........................................   الهمسه    ................................................................
hms = {}

@Client.on_message(filters.command(["سر", "همسه", "اهمس", "همسة", "همس"], "") & filters.group, group=97367)
async def t57(client, m): 
    chatID = m.chat.id
    fromID = m.from_user.id
    toID = m.reply_to_message.from_user.id
    msgID = m.reply_to_message.id
    if fromID == toID:
        await m.reply("يا اهبل عايز تهمس لنفسك 😂", True)
    elif m.reply_to_message.from_user.is_bot:
        await m.reply("يهبل عايز تهمس لبوت", True)
    else:
        code = randCode()
        global hms
        hms = {code: {"chat": chatID, "from": fromID, "to": toID, "id": msgID}}
        keb = [[Button("اضغط هنا", url=f"https://t.me/{client.me.username}?start={code}")]]
        await m.reply(f"⇜ تم تحديد الهمسه لـ {m.reply_to_message.from_user.mention}\n⇜ اضغط الزر لكتابة الهمسة\n✓", True, reply_markup=Markup(keb))

@Client.on_message(filters.regex(r"^/start\s[a-zA-Z0-9]{7}$") & filters.private)
async def tjcj(client, m):
    code = m.text.split(" ")[1]
    userID = m.from_user.id
    global hms
    if hms.get(code):
        chatID = hms[code]["chat"]
        fromID = hms[code]["from"]
        toID = hms[code]["to"]
        toIN = await client.get_users(toID)
        msgID = hms[code]["id"]
        code2 = randCode()
        if userID == fromID:
            ask = await m.chat.ask("⇜ اهلا عزيزي قم بكتابه الهمسه الان \n ويمكنك ايضا ارسال الهمسه (كصوره او ملصق او فيديو او متحركه او صوت)",filters=filters.user(fromID),reply_to_message_id=m.id)
            if ask.text:
                hms[code].update({"type":1,"msg":ask.text})
                keb = [[Button("افتح الهمسه",callback_data=f"open_{code}")],
                       [Button(f"اهمس ل {m.from_user.first_name}",url=f"https://t.me/{client.me.username}?start={code2}")]]
            elif ask.photo:
                hms[code].update({"type":2,"msg":getattr(ask,"caption"),"fileID":ask.photo.file_id})
                keb = [[Button("افتح الهمسه",url=f"https://t.me/{client.me.username}?start=open_{code}")],
                       [Button(f"اهمس ل {m.from_user.first_name}",url=f"https://t.me/{client.me.username}?start={code2}")]]
            elif ask.sticker:
                hms[code].update({"type":3,"msg":getattr(ask,"caption"),"fileID":ask.sticker.file_id})
                keb = [[Button("افتح الهمسه",url=f"https://t.me/{client.me.username}?start=open_{code}")],
                       [Button(f"اهمس ل {m.from_user.first_name}",url=f"https://t.me/{client.me.username}?start={code2}")]]
            elif ask.animation:
                hms[code].update({"type":4,"msg":getattr(ask,"caption"),"fileID":ask.animation.file_id})
                keb = [[Button("افتح الهمسه",url=f"https://t.me/{client.me.username}?start=open_{code}")],
                       [Button(f"اهمس ل {m.from_user.first_name}",url=f"https://t.me/{client.me.username}?start={code2}")]]
            elif ask.video:
                hms[code].update({"type":5,"msg":getattr(ask,"caption"),"fileID":ask.video.file_id})
                keb = [[Button("افتح الهمسه",url=f"https://t.me/{client.me.username}?start=open_{code}")],
                       [Button(f"اهمس ل {m.from_user.first_name}",url=f"https://t.me/{client.me.username}?start={code2}")]]
            elif ask.voice:
                hms[code].update({"type":6,"msg":getattr(ask,"caption"),"fileID":ask.voice.file_id})
                keb = [[Button("افتح الهمسه",url=f"https://t.me/{client.me.username}?start=open_{code}")],
                       [Button(f"اهمس ل {m.from_user.first_name}",url=f"https://t.me/{client.me.username}?start={code2}")]]
            txt = f"⇜ عزيزي 「 {toIN.mention} 」\n⇜ لديك همسة سرية من「 {m.from_user.mention} 」"
            await m.reply("⇜ تم ارسـال الهمسـة .. بنجـاح",True)
            msg = await client.send_message(chatID,txt,reply_to_message_id=msgID ,reply_markup=Markup(keb))
            db.set(code,hms[code])
            hms = {code2:{"chat":chatID,"from":toID,"to":fromID,"id":msg.id}}
        else: await m.reply("الهمسه مش ليك بطل لعب", True)
        
@Client.on_message(filters.regex(r"^/start\sopen_[a-zA-Z0-9]{7}$") & filters.private)
async def thckdjv(_, m:Message):
    code = m.text.split("_")[1]
    if db.exists(code):
        data = db.get(code)
        type = data["type"]
        if m.from_user.id in [data["to"],data["from"]]: 
            if type == 2: await m.reply_photo(data["fileID"],caption=data["msg"],quote=True)
            elif type == 3: await m.reply_sticker(data["fileID"],quote=True)
            elif type == 4: await m.reply_animation(data["fileID"],caption=data["msg"],quote=True)
            elif type == 5: await m.reply_video(data["fileID"],caption=data["msg"],quote=True)
            elif type == 6: await m.reply_voice(data["fileID"],caption=data["msg"],quote=True)
        else: await m.reply("الهمسه مش ليك بطل لعب",True)
        
@Client.on_callback_query(filters.regex(r"^open_[a-zA-Z0-9]{7}$"))
async def tjckv(_, m:CallbackQuery):
    code = m.data.split("_")[1]
    if db.exists(code):
        data = db.get(code)
        type = data["type"]
        if type == 1:
            if m.from_user.id in [data["to"],data["from"]]: await m.answer(data["msg"],True)
            else : await m.answer("الهمسه مش ليك بطل لعب",True)
#..........................................   الهمسه    ................................................................
#..........................................   دعوه    ................................................................
@Client.on_message(filters.video_chat_members_invited)
async def zoharyy(client, message): 
           text = f"- قام {message.from_user.mention}\n - بدعوة : "
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"[{user.first_name}](tg://user?id={user.id}) "
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text} ")
           except:
             pass               
#..........................................   دعوه    ................................................................
def randCode():
    char = string.ascii_letters + string.digits
    return ''.join(random.choice(char) for _ in range(7))