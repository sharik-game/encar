import asyncio
from aiogram import Bot, Dispatcher, executor, types
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
import aiofiles
import random
import logging
import re
logging.basicConfig(level=logging.INFO)
# 5765131386:AAGVAN3kJQMpBKcyHIpyno30ekIrtpNNVMU
bot = Bot(token="5736161057:AAE-5ZLi-a6HZEUfF0g-wbi6hKesHqrxb18") # 5742677500:AAGkig-NmFqJ5CY0prF7NN-X_9Cysp4PlM0 right
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start_message(message: types.Message):
    await message.answer("Введите help что-бы увидеть что я могу")
@dp.message_handler()
async def cmd_test1(message: types.Message):
    # print(message)
    if message.text == "show":
        async with aiofiles.open("links.txt", mode="r") as file:
            lines = await file.readlines()
            # lines = [line.rstrip() async for line in lines]
            await message.answer("All links here (:")
            # print(lines)
        for c in lines:
            await message.answer(c)
            sleep_time = random.randint(1, 3)
            await asyncio.sleep(sleep_time)
    if message.text == "help":
        await message.answer("help - показывает справку по всем командам,\nshow - показывает все ссылки,\nadd http://something - добавляет ссылку,\ndelete http://something - удаляет ссылку.")
    if list(message.text)[:4] == ["a", "d", "d", " "]:
        add_link = list(message.text)[4:]
        ans = ''
        for c in add_link:
            ans += c
        async with aiofiles.open("links.txt", mode="r") as some_file:
            lines = await some_file.readlines()
        if ans in lines:
            await message.answer("Эта ссылка уже есть в списке")
        else:
            async with aiofiles.open("links.txt", mode="a") as my_file:
                await my_file.write("\n" + ans)
            await message.answer("Ссылка успешно добавлена :)")
    if list(message.text)[:7] == ["d", "e", "l", "e", "t", "e", " "]:
        del_link = list(message.text)[7:]
        ans = ""
        for e in del_link:
            ans += e
        
        # print(f"ans: {ans}")
        async with aiofiles.open("links.txt", mode="r") as f1:
            lines = await f1.readlines()
        answer_list: list = []
        for c in lines:
            answer_list.append(c.replace("\n", ""))
        check = answer_list.count(ans)
            # print(first_con_list)
        if check == 0:
            await message.answer("Я не знаю такой ссылки")
        else:
            
            async with aiofiles.open("links.txt", mode="w") as wr_file:
                try:
                    answer_list.remove(ans)
                    len_answer_list: int = len(answer_list)
                    ans1: list = []
                    for number, value in enumerate(answer_list):
                        if (number + 1) >= len_answer_list:
                            ans1.append(value)
                        else:
                            ans1.append(f"{value}\n")
                    await message.answer("Ссылка успешно удалена")
                    await wr_file.writelines(ans1)
                except ValueError:
                    print("#" * 20)
                    print("Ошибка в удалении")
                    await message.answer("В удалении ссылки произошёл какой-то сбой")
                """
                lines = await wr_file.readlines()
                print(lines)
                # matches = re.search("\n", )
                lines2 = list(filter(lambda a: a != "\n", lines))
                print(lines2)
                first_con = lines.index(ans)
                first_con_list = lines[:first_con]
                second_con = first_con + 1
                second_con_list = lines[second_con:]
                for z in second_con_list:
                    first_con_list.append(z)
                # idx = lines.index(ans)
                await wr_file.seek(0)
                await wr_file.truncate()
                await wr_file.writelines(first_con_list)
                """
            # await message.answer("Ссылка успешно удалена")




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)