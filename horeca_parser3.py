from api import Client

bot = Client('1')

fp = open('horeca_group_usernames', 'w', encoding='utf-8')


@bot.task
async def _():
    async for i in bot.iter_chat_members('@HoReCaFamily', filter='all'):
        user = i.user

        if user.is_bot or user.is_deleted:
            continue

        username = user.username

        if not username:
            continue

        print('@' + username, file=fp)
        fp.flush()


bot.run_tasks()
