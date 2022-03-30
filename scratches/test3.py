import asyncio
import time

from aiogram import Bot

user_ids = {2101530116, 2137920134, 2146613767, 2134607113, 2118517642, 2111956236, 2126322060, 2122977683, 2112258071,
            2106443032, 2135787290, 2104600346, 2101809825, 2138360738, 2089379109, 2104733483, 2130048811, 2120079405,
            2135671727, 2100828464, 2115394479, 2132873778, 2119266354, 2008457780, 2129599159, 2131260344, 2101629242,
            2113977020, 2139828925, 811336764, 2117519171, 2141173958, 2062497867, 2131396689, 2069532882, 2143241938,
            2118942165, 2111718742, 2105070935, 2133330264, 2133472859, 2126809948, 2120455902, 2108180447, 2136080611,
            2105872868, 2135564645, 2142778852, 1748576997, 2120017898, 2077082475, 2034758765, 2115730034, 2122311542,
            2117016954, 2105144443, 2133308796}

bot = Bot('')


async def main():
    for ui in user_ids:
        print(ui)
        await bot.kick_chat_member('@diunder0', ui, until_date=int(time.time()) + 100)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())