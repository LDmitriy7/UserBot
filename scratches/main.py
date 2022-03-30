import asyncio
import time

from pyrogram import Client

import config

app: Client = Client('1', config.Api.ID, config.Api.HASH)


async def _():
    c0 = 0
    c = 0
    time_now = int(time.time())

    async for member in app.iter_chat_members('@diunder0', filter='all'):
        c0 += 1
        user = member.user

        # if user.status in ['offline', 'online', 'recently', None, 'within_week']:
        #     continue

        if not user.last_online_date:
            continue

        if time_now - user.last_online_date < 60 * 60 * 24 * 7:
            continue

        c += 1
        print(c, user.status, user.username)
        await app.kick_chat_member('@diunder0', user.id, int(time.time()) + 500)

    print(c0)


async def main():
    async with app:
        await _()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
