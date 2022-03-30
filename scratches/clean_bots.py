import asyncio
from datetime import datetime

from pyrogram import Client

import config

app: Client = Client('1', config.Api.ID, config.Api.HASH)
CHANNEL_ID = '@diunder0'


async def clean_bots():
    members = await app.get_chat_members(CHANNEL_ID)
    user_ids = set()

    for m in members:
        joined_date = datetime.fromtimestamp(m.joined_date)
        if datetime(2021, 11, 29, 21, 20, 15) < joined_date < datetime(2021, 11, 29, 22, 50):
            print(joined_date, m.user.first_name, m.user.last_name)
            user_ids.add(m.user.id)
            # await app.kick_chat_member(CHANNEL_ID, m.user.id, until_date=int(time.time()) + 100)

    print(user_ids)


async def main():
    async with app:
        await clean_bots()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
