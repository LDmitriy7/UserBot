import asyncio

from pyrogram import Client

import config

app: Client = Client('1', config.Api.ID, config.Api.HASH)
CHANNEL_ID = '@diunder0'

ASCII_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
# CYRILLIC_LETTERS = 'абвгдеёжзийклмнопрстуфхцчшщьъыэюя'
CYRILLIC_LETTERS = 'абвгдеёжзийклмнопрстуфхцчшщыэюя'

USERS_IDS = set()
QUERIES_COUNT = 0


async def get_members(query: str, alphabet: str):
    global QUERIES_COUNT

    members = await app.get_chat_members(CHANNEL_ID, filter='all', query=query)
    USERS_IDS.update([m.user.id for m in members])
    QUERIES_COUNT += 1

    if len(members) >= 200:
        print(f'{query} ({len(members)})')

        if len(query) <= 2:
            for letter in alphabet:
                await get_members(query + letter, alphabet)


async def main():
    async with app:
        # for i in CYRILLIC_LETTERS:
        #     await get_members(i)

        for i in ASCII_LETTERS:
            await get_members(i, ASCII_LETTERS)

    print(f'Total users: {len(USERS_IDS)}')
    print(f'Total queries: {QUERIES_COUNT}')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
