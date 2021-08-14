import conf
from random import randint
async def random(a, mc):
    msg = str(mc.content)[len(list(conf.cell_char)):].split(" ")
    if len(msg) == 3:
        try:
            if msg[1] < msg[2]:
                await mc.channel.send(randint(int(msg[1]), int(msg[2])))
            else:
                await mc.channel.send("Первое число должно быть меньше второго")
        except Exception as exc:
            await mc.channel.send("Введите числа, а не буквы")
    else:
        await mc.channel.send("Введите только 2 числа через пробел")