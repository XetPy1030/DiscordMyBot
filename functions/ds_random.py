import conf
from random import randint
from random import choice
async def random(a, mc):
    msg = str(mc.content)[len(list(conf.cell_char)):].split(" ")
    if len(msg) == 3:
        try:
            if msg[1] < msg[2]:
                await mc.channel.send(randint(int(msg[1]), int(msg[2])))
            else:
                await mc.channel.send("Первое число должно быть меньше второго")
        except Exception as exc:
            await mc.channel.send(choice(msg[1:]))
    elif len(msg) > 1:
        await mc.channel.send(choice(msg[1:]))
    else:
        await mc.channel.send("Введите еще чтонить через пробел")