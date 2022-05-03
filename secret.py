import asyncio
import logging

from aiogram_utils.errors import suppress

import config
from api import Client

bot = Client('1')

log = logging.getLogger()


async def safe_edit(text: str):
    with suppress(Exception, log=log):
        await bot.edit_message_text(
            chat_id=config.Secret.channel_id,
            message_id=config.Secret.post_id,
            text=text,
            disable_web_page_preview=True,
        )


@bot.task
async def _():
    while True:
        for text in config.Secret.texts:
            await safe_edit(text)
            await asyncio.sleep(0.2)


bot.run_tasks()
