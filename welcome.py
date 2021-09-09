import time
import asyncio
import sys
import random
import threading
from dotenv import load_dotenv
from telethon.sessions import StringSession

from telethon import TelegramClient, events, utils

# gunakan api id dan hash punya anda sendiri, atau cari aja punya orang lain
# Telegram App KEY and HASH
API_ID = int(os.environ.get("API_ID") or 0)
API_HASH = str(os.environ.get("API_HASH") or None)

# Userbot Session String
STRING_SESSION = os.environ.get("STRING_SESSION", None)

session_file = '/data/data/com.termux/files/home/sesisReply'  # bisa ditulis walau belum login asal punya akses write
password = 'YOUR_PASSWORD'  # jika anda menerapkan two step verification

# Isi pesan
message = "lagi off"

if __name__ == '__main__':
    # Create the client and connect
    # use sequential_updates=True to respond to messages one at a time
    client = TelegramClient(session_file, api_id=Config.APP_ID, api_hash=Config.API_HASH, sequential_updates=True)

if STRING_SESSION:
    # pylint: disable=invalid-name
    bot = TelegramClient(
        session=StringSession(STRING_SESSION),
        api_id=API_ID,
        api_hash=API_HASH,
        auto_reconnect=True,
        connection_retries=-1,
    )
else:
    # pylint: disable=invalid-name
    bot = TelegramClient("userbot", API_ID, API_HASH)
        
        @client.on(events.NewMessage(incoming=True))
    async def handle_new_message(event):
        if event.is_private:  # only auto-reply to private chats
            from_ = await event.client.get_entity(event.from_id)  # this lookup will be cached by telethon
            if not from_.bot:  # don't auto-reply to bots
                print(time.asctime(), '-', event.message)  # optionally log time and message
                time.sleep(1)  # pause for 1 second to rate-limit automatic replies
                await event.respond(message)


    print(time.asctime(), '-', 'Auto-replying...')
    client.start()
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')
