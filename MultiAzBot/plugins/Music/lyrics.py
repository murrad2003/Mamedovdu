import os, lyricsgenius
from MultiAzBot import *
from pyrogram import filters
from pyrogram.types import Message, User
from pyrogram.types import (
    Message
)

@app.on_message(filters.command(["lyrics"]))
async def lyrics(_, message: Message):
    m = await message.delete()  
    if len(message.command) < 2:
        return await message.reply_text("**İstifadə:** `/lyrics Uzak Gelecekten`")
    m = await message.reply_text("✍️ Mahnı sözləri axtarılır...")
    query = message.text.split(None, 1)[1]
    x = "OXaVabSRKQLqwpiYOn-E4Y7k3wj-TNdL5RfDPXlnXhCErbcqVvdCF-WnMR5TBctI"
    y = lyricsgenius.Genius(x)
    y.verbose = False
    S = y.search_song(query, get_full_info=False)
    if S is None:
        return await m.edit("Mahnı sözləri tapılmadı: 🥹")
    xxx = f"""
**🤖 Yüklədi {BOT_USERNAME}**
**🎶 Axtarılan Mahnı:** __{query}__
**📖 Tapılmış Mahnı Sözləri:** __{S.title}__
**✍️ Rəssam:** {S.artist}
**📄 __Mahnı Sözləri:__**

{S.lyrics}"""
    if len(xxx) > 4096:
        await m.delete()
        filename = "lyrics.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(xxx.strip()))
        await message.reply_document(
            document=filename,
            caption=f"**Sözlər çox olduğundan fayl edib atdım...**\n\n`Lyrics`",
            quote=False,
        )
        os.remove(filename)
    else:
        await m.edit(xxx)
