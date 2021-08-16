from bs4 import BeautifulSoup
import requests as req
import conf
async def search(self, messages):
    msg = str(messages.content)[len(list(conf.cell_char)):].split(" ")
    if msg[1] == "wiki":
        wiki = "https://ru.wikipedia.org/wiki/"
        resp = req.get(wiki+" ".join(msg[2:]))
        soup = BeautifulSoup(resp.text, 'lxml')
        for child in soup.recursiveChildGenerator():
            if str(child.name) == "div":
                if child.id  == "mw-content-text":
                    print(child.p)