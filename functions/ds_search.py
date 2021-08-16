from bs4 import BeautifulSoup
import requests as req
import conf
async def search(self, messages):
    msg = str(messages.content)[len(list(conf.cell_char)):].split(" ")
    if msg[1] == "wiki":
        wiki = "https://ru.wikipedia.org/wiki/"
        dop = "_".join(msg[2:])
        resp = req.get(wiki+dop)
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
        resp = req.get(search+"".join(msg[2:]).lower()+"&nomisspell=1&noreask=1")
        print(search+"".join(msg[2:]).lower()+"&nomisspell=1&noreask=1")
        soup = BeautifulSoup(resp.text, 'lxml')
        for i in soup.find_all("div"):
            try:
                if "serp-item_pos_0" in i["class"]:
                    await messages.channel.send("https:"+i.div.a.img["src"])
                    break
            except:
                pass