from api import Client

bot = Client('1')


@bot.task
async def check_session():
    me = await bot.get_me()
    print(me)


bot.run_tasks()
