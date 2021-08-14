import conf, pytz
from datetime import datetime
from random import randint
async def emoji(bb, mc):
    msg = str(mc.content)[len(list(conf.cell_char)):].split(" ")
    if len(msg) == 1:
        a = []
        for em in mc.guild.emojis:
            a += [em.id]
        await mc.channel.send(bb.get_emoji(a[randint(0, len(a)-1)]))