import conf, random
import check
class KN_game:
    def __init__(self, p1, p2):
        self.pl1 = {"name": p1, "symb": 2}
        self.pl2 = {"name": p2, "symb": 2}
        self.field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.end = None
        self.name = "KN"
        if random.randint(0, 1) == 0:
            self.pl1["symb"] = 1
            self.hod = True
        else:
            self.pl2["symb"] = 1
            self.hod = False

    def pl(self):
        if self.hod:
            return self.pl1["name"]
        else:
            return self.pl2["name"]

    def attack(self, player, x, y):
        if self.check(x, y, player):
            if self.hod:
                self.field[x][y] = self.pl1["symb"]
            else:
                self.field[x][y] = self.pl2["symb"]
            self.check_end()
            self.hod = not self.hod
            return True
        else:
            return False
			
    def check_end(self):
        aga = False
        for i in range(3):
            if self.field[i][0] == self.field[i][1] == self.field[i][2] != 0:
                aga = True
            elif self.field[0][i] == self.field[1][i] == self.field[2][i] != 0:
                aga = True
        if self.field[0][0] == self.field[1][1] == self.field[2][2] != 0:
            aga = True
        elif self.field[2][0] == self.field[1][1] == self.field[0][2] != 0:
            aga = True
        if aga:
            if self.hod:
                self.end = self.pl1["name"]
            else:
                self.end = self.pl2["name"]
			
    def check(self, x, y, pl):
        if x not in [0, 1, 2] or y not in [0, 1, 2]:
            return False
        if self.field[x][y] == 0:
            if pl == self.pl1["name"] and self.hod:
                return True
            elif pl == self.pl2["name"] and not self.hod:
                return True
            else:
                return False
        else:
            return False
			
    def read(self):
        aa = "|"
        for ii in range(3):
            for oo in range(3):
                aa+=str(self.field[oo][ii])+"|"
            aa += "\n|"
        return aa[:len(aa)-1]

async def game(self, message):
    msg = str(message.content)[len(list(conf.cell_char)):].split(" ")
    if msg[1] == "KN":
        if msg[2] == "new" and len(msg) == 4:
            check.check_log(self.all_db, str(message.mentions[0].id))
            gam = KN_game(str(message.author.id), str(message.mentions[0].id))
            if self.all_db["accounts"][str(message.author.id)]["game"] == False and self.all_db["accounts"][str(message.mentions[0].id)]["game"] == False:
                self.all_db["games"]["KN"].update({str(message.author.id) + str(message.mentions[0].id): {"game_class": gam}})
                self.all_db["accounts"][str(message.author.id)]["game"] = True
                self.all_db["accounts"][str(message.mentions[0].id)]["game"] = True
                self.all_db["accounts"][str(message.author.id)]["gameData"].update({"id": str(message.author.id) + str(message.mentions[0].id)})
                self.all_db["accounts"][str(message.mentions[0].id)]["gameData"].update({"id": str(message.author.id) + str(message.mentions[0].id)})
                await message.channel.send("Игра начата, нолик у {}".format(await self.fetch_user(gam.pl())))
            else:
                await message.channel.send("Кто-то из вас уже играет")
        elif msg[2] == "attack" and (len(msg) == 4 or len(msg) == 5):
            gam = self.all_db["games"]["KN"][self.all_db["accounts"][str(message.author.id)]["gameData"]["id"]]["game_class"]
            if gam.name == "KN":
                if len(msg) == 4:
                    pass
                elif len(msg) == 5:
                    if gam.attack(str(message.author.id), int(msg[3]), int(msg[4])):
                        await message.channel.send("Успешно")
                    else:
                        await message.channel.send("Какая-то ошибка")
                    await message.channel.send(gam.read())

