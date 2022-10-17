import asyncio
from aiogram import Bot, Dispatcher, executor, types
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import bot_token
import logging
from parser import collect_data, pars_link

import random
import aioschedule

logging.basicConfig(level=logging.INFO)
# storage = MemoryStorage()
bot = Bot(token=bot_token)
dp = Dispatcher(bot)

"""
urls = [
    r"http://www.encar.com/dc/dc_carsearchlist.do?carType=kor#!%7B%22action%22%3A%22(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.기아._.ModelGroup.쏘렌토.))_.Year.range(201800..201911)._.Mileage.range(..120000).)%22%2C%22toggle%22%3A%7B%7D%2C%22layer%22%3A%22%22%2C%22sort%22%3A%22ModifiedDate%22%2C%22page%22%3A1%2C%22limit%22%3A20%7D",
    r"http://www.encar.com/dc/dc_carsearchlist.do?carType=kor#!%7B%22action%22%3A%22(And.Hidden.N._.Year.range(201800..201911)._.Mileage.range(..120000)._.(C.CarType.Y._.(C.Manufacturer.현대._.ModelGroup.싼타페.)))%22%2C%22toggle%22%3A%7B%7D%2C%22layer%22%3A%22%22%2C%22sort%22%3A%22ModifiedDate%22%2C%22page%22%3A1%2C%22limit%22%3A20%7D",
    r"http://www.encar.com/dc/dc_carsearchlist.do?carType=kor#!%7B%22action%22%3A%22(And.Hidden.N._.Year.range(201800..201911)._.Mileage.range(..120000)._.(C.CarType.Y._.(C.Manufacturer.기아._.ModelGroup.스포티지.)))%22%2C%22toggle%22%3A%7B%7D%2C%22layer%22%3A%22%22%2C%22sort%22%3A%22ModifiedDate%22%2C%22page%22%3A1%2C%22limit%22%3A20%7D",
    r"http://www.encar.com/fc/fc_carsearchlist.do?carType=for&searchType=model&TG.R=B#!%7B%22action%22%3A%22(And.Hidden.N._.(C.CarType.N._.(C.Manufacturer.인피니티._.ModelGroup.QX50.))_.Year.range(201810..201909).)%22%2C%22toggle%22%3A%7B%7D%2C%22layer%22%3A%22%22%2C%22sort%22%3A%22ModifiedDate%22%2C%22page%22%3A1%2C%22limit%22%3A20%7D"
]
"""
# loop = asyncio.get_event_loop()
# delay = 30.0
# s = sched.scheduler(time.time, time.sleep)
# @dp.message_handler(commands="test")
"""
@dp.message_handler(commands="vova")
async def start_m(message: types.Message) -> None: # message: types.Message
    # print(message.chat.id)
    await message.answer("cool")
"""
async def parser():
    # while True:
    await asyncio.sleep(30)
    with open("links.txt", "r") as file:
        urls = [line.rstrip() for line in file.readlines()]
    try:
        for i, c in enumerate(urls):
            # print(i)
            sw = collect_data(c, i)
            # print(sw)
            if sw == []:
                await bot.send_message(5694868044, "Nothing change") # 5259920989
            elif sw == ["E"]:
                print("Problems link")
                await bot.send_message(5694868044, "Ошибка...Ссылка указана неверно или нет подключения к интернету")
            else:
                for ans in sw:
                    await asyncio.sleep(random.randint(1, 5))
                    await bot.send_message(5694868044, f"Vooot\n{ans}")
    except Exception as ex:
        print("#" * 20)
        print(ex)
        await bot.send_message(5694868044, "Упс...Что-то пошло не так")
        
async def scheduler():
    # aioschedule.every(90).seconds.do(parser)
    aioschedule.every(5).minutes.do(parser)
    while True:
        await aioschedule.run_pending()
async def on_startup(x):
    asyncio.create_task(scheduler())
if __name__ == "__main__":  
    # loop = asyncio.get_event_loop()
    # dp.loop.create_task(parser())
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    
    # t = threading.Timer(10.0, parser)
    # t.start()
    # dp.loop.create_task(parser(5))

