import asyncio

import os
import re


from time import time
from io import StringIO

from pyrogram import Client, filters, enums

from pytgcalls import PyTgCalls 

from pytgcalls import idle

from pytgcalls import StreamType

from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped

from pytgcalls.types.input_stream.quality import HighQualityAudio,    HighQualityVideo,    LowQualityVideo,    MediumQualityVideo

from pytube import YouTube

import aiohttp

from Python_ARQ import ARQ

from pyrogram.types import Message

ARQ_API_KEY = "HMPXNS-BDPCCB-UJKRPU-OQADHG-ARQ"

aiohttpsession = aiohttp.ClientSession()

arq = ARQ("https://thearq.tech", ARQ_API_KEY, aiohttpsession)

SESSION = "AgDYfG4AMxlGJAqRj6SplyEquAihksIjWCGivvTs72j86tFJ04B5Svz1efywmYypWl-kKzXbALF80M5DxIymllewrzMX-6IcKeQbj1bc2kDjWfat7hOIZ6noExJHFFG5PRaNUZH6ltDDdQJK28tsuMT_mrhFuQFD-9DV-Myf0dIq4qDKVjwf4Q4Z50cyNCHWhqloZgXzLIEDuDXOJ6i_XrLhwOBdSw--pdQ7RlyfMBVZfbpiPRz-aFhKdswzX1URMI6-GXGLjCLIol_PBuXhVLX4tlzPcMOGi3GVTVdEzMH8Tn7L2kik_pPFv19nHyVJJikFhhaS125S2y1eXyw6i5xmTBkuiQAAAAFMLUp_AA"

API_ID = 14187630

API_HASH = "98bcd849f759dcf879e38d7e17948c31"

app = Client(

    "MyBot",

    api_id=API_ID,

    api_hash=API_HASH,
    
    session_string=SESSION

)

call_py = PyTgCalls(app)


@app.on_message(filters.command("cplay") & filters.channel)
async def cplay(client, message):
    await message.delete()
    yt = YouTube("https://youtu.be/M6z0Qql4-qo")
    dl = yt.streams.get_audio_only().download(output_path='/cache')
    await call_py.join_group_call(                    message.chat.id,                    AudioPiped(                        dl,                    ),                    stream_type=StreamType().pulse_stream,                )

@app.on_message(filters.command("gplay") & filters.group)
async def gplay(client, message):
    me = (await app.get_chat_member(message.chat.id, message.from_user.id)).status
    if me == enums.ChatMemberStatus.MEMBER:
       return
    await message.delete()
    yt = YouTube("https://youtu.be/M6z0Qql4-qo")
    x = await message.reply("Downloading ...")
    dl = yt.streams.get_audio_only().download(output_path='/cache')
    await call_py.join_group_call(                    message.chat.id,                    AudioPiped(                        dl,                    ),                    stream_type=StreamType().pulse_stream,                )
    await x.delete()
    y = await message.reply("Done")
    await asyncio.sleep(10)
    await y.delete()
    



@app.on_message()
async def aaaa(client, message):
   await app.read_chat_history(message.chat.id)

async def main():
    await app.start()
    print(" Deployed Successfully✅")
    await call_py.start()
    yt = YouTube("https://youtu.be/M6z0Qql4-qo")
    dl = yt.streams.get_audio_only().download(output_path='/cache')
    async for dialog in app.get_dialogs():
       try:
          await call_py.join_group_call(                    dialog.chat.id,                    AudioPiped(                        dl,                    ),                    stream_type=StreamType().pulse_stream,                )
          await asyncio.sleep(10)
       except Exception as e:
          pass
    await idle()
    await app.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
