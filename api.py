import asyncio

from pyrogram import Client as _Client

import config


class Client(_Client):
    def __init__(self, session_name: str):
        super().__init__(f'sessions/{session_name}', config.Api.ID, config.Api.HASH)
        self._tasks = []

    def task(self, func):
        self._tasks.append(func)
        return func

    async def _run_tasks(self):
        async with self:
            for task in self._tasks:
                await task()

    def run_tasks(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._run_tasks())
