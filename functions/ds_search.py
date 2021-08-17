from bs4 import BeautifulSoup
import requests as req
import conf
async def search(self, messages):
    msg = str(messages.content)[len(list(conf.cell_char)):].split(" ")
    if msg[1] == "wiki":
        wiki = "https://ru.wikipedia.org/wiki/"
        resp = req.get(wiki+" ".join(msg[2:]))
        soup = BeautifulSoup(resp.text, 'lxml')
        for i in soup.find_all("div"):
            try:
                if i["id"] == "mw-content-text":
                    await messages.channel.send(i.p.text)
                    break
            except:
                pass
    elif msg[1] == "photo":
        search = "https://yandex.ru/images/search?text="
        dop = " ".join(msg[2:]).lower()+"&nomisspell=1&noreask=1"
        """
        dop = dop.replace("xxx", "")
        dop = dop.replace("секс", "")
        dop = dop.replace("ебл", "")
        dop = dop.replace("пися", "")
        dop = dop.replace("sex", "")
        dop = dop.replace("ххх", "")
        dop = dop.replace("порно", "")
        dop = dop.replace("порн", "")
        dop = dop.replace("прон", "")
        dop = dop.replace("цыпочк", "")
        dop = dop.replace("горячие", "")
        dop = dop.replace("сучки", "")
        dop = dop.replace("анал", "")
        dop = dop.replace("орал", "")
        dop = dop.replace("сиськи", "")
        dop = dop.replace("чайлдпрон", "")
        dop = dop.replace("чайлдпорн", "")
        dop = dop.replace("porn", "")
        dop = dop.replace("hot", "")
        dop = dop.replace("sexual", "")
        dop = dop.replace("anal", "")
        dop = dop.replace("хуй", "")
        dop = dop.replace("пизда", "")
        dop = dop.replace("джигурда", "")
        dop = dop.replace("пёзды", "")
        dop = dop.replace("пезды", "")
        dop = dop.replace("сосет", "")
        dop = dop.replace("сосёт", "")
        dop = dop.replace("дроч", "")
        dop = dop.replace("вагин", "")
        dop = dop.replace("член", "")
        dop = dop.replace("гол", "")
        dop = dop.replace("обнаж", "")
        dop = dop.replace("мастурб", "")
        dop = dop.replace("x-art", "")
        dop = dop.replace("34", "")
        dop = dop.replace("nudi", "")
        dop = dop.replace("nake", "")
        dop = dop.replace("pron", "")
        dop = dop.replace("срат", "")
        dop = dop.replace("срет", "")
        dop = dop.replace("срёт", "")
        dop = dop.replace("жопа", "")
        dop = dop.replace("попа", "")
        dop = dop.replace("пися", "")
        dop = dop.replace("кис", "")
        dop = dop.replace("69", "")
        dop = dop.replace("nude", "")
        dop = dop.replace("pussy", "")
        dop = dop.replace("shit", "")
        dop = dop.replace("teen", "")
        dop = dop.replace("влагал", "")
        dop = dop.replace("гей", "")
        dop = dop.replace("геи", "")
        dop = dop.replace("генитал", "")
        dop = dop.replace("группову", "")
        dop = dop.replace("еба", "")
        dop = dop.replace("ебё", "")
        dop = dop.replace("ебу", "")
        dop = dop.replace("залуп", "")
        dop = dop.replace("зоофил", "")
        dop = dop.replace("извращ", "")
        dop = dop.replace("интим", "")
        dop = dop.replace("лесб", "")
        dop = dop.replace("лезб", "")
        dop = dop.replace("мин", "")
        dop = dop.replace("пелотк", "")
        dop = dop.replace("пилотк", "")
        dop = dop.replace("соса", "")
        dop = dop.replace("сперм", "")
        dop = dop.replace("шлюх", "")
        dop = dop.replace("эрот", "")
        dop = dop.replace("сперм", "")
        """
        resp = req.get(search+dop)
        soup = BeautifulSoup(resp.text, 'lxml')
        for i in soup.find_all("div"):
            try:
                if "serp-item_pos_0" in i["class"]:
                    await messages.channel.send("https:"+i.div.a.img["src"])
                    break
            except:
                pass