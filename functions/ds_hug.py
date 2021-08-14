import conf, discord
from random import randint
async def hug(a, mc):
    msg = str(mc.content)[len(list(conf.cell_char)):].split(" ")
    a = open("functions/other/hug.txt", "r")
    b = a.read()
    a.close()
    b = b.split("\n")
    c = randint(0, len(b)-1)
    if len(msg) > 1:
        try:
            await mc.channel.send(f"{mc.author.mention} hugs "+" ".join(msg[1:])+f" {message.mentions[0].mention} "+b[c])
        except:
            await mc.channel.send(f"{mc.author.mention} hugs "+" ".join(msg[1:])+" "+b[c])
    elif len(msg) == 1:
        await mc.channel.send(f"{mc.author.mention} is hugged "+b[c])
