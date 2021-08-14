import conf, pytz
from datetime import datetime
async def date(a, mc):
    msg = str(mc.content)[len(list(conf.cell_char)):].split(" ")
    if len(msg) == 2 and msg[1] == "now":
        b = pytz.timezone("Europe/Moscow")
        a = datetime.now(b).strftime("%H:%M:%S %d.%m.%Y")
        await mc.channel.send("Время по мск: " + a)