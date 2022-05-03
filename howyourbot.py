import asyncio
import json

from pyrogram.raw.core import TLObject

from api import Client
from pyrogram.raw import types

bot = Client('1')


@bot.task
async def _():
    offset = ""

    items = []

    while True:
        res: types.messages.BotResults = await bot.get_inline_bot_results(
            bot='@HowYourBot',
            query=':   qwerty  ',
            offset=offset,
        )
        print(f'{len(res.results)=}, {res.next_offset=}')
        offset = res.next_offset
        await asyncio.sleep(1)

        items.extend(res.results)

        if not res.results:
            break

    print(f'{len(items)=}')
    json.dump(
        obj=items,
        fp=open('items5.json', 'w', encoding='utf-8'),
        default=TLObject.default,
        ensure_ascii=False,
        indent=2,
    )


bot.run_tasks()
