from api import Client

bot = Client('1')

fp = open('horeca_group_msgs', 'w', encoding='utf-8')


@bot.task
async def _():
    async for i in bot.iter_history('@HoReCaFamily'):
        text = i.text or i.caption

        if not text:
            print(i.message_id)
            continue

        text = text.replace('\n', r'\n').strip()

        print(text, file=fp)
        fp.flush()


bot.run_tasks()
