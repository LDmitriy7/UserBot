from api import Client

bot = Client('1')


@bot.on_message()
async def _(_, msg):
    print(msg)


bot.run()
