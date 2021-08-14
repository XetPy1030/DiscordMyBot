import conf, discord, functions.other.splashes
from random import randint
async def splash(a, mc):
    msg = str(mc.content)[len(list(conf.cell_char)):].split(" ")
    if len(msg) == 2:
        try:
            b = int(msg[1])
            a = functions.other.splashes.aaa["splashes"]
            await mc.channel.send(str(b)+". "+a[b])
        except:
            await mc.channel.send("Не число или не то число")
    elif len(msg) == 1:
        a = functions.other.splashes.aaa["splashes"]
        b = randint(0, len(a)-1)
        await mc.channel.send(str(b)+". "+a[b])