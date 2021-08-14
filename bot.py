import conf, discord, pickle
import functions.com as funcs

class DisBot(discord.Client):
    all_db = {"accounts":{}}

    async def on_ready(self):
        self.load()
        print("Бот начал работу")

    async def on_message(self, message):
        #self.all_db["accounts"][str(message.author.id)]["game"] = ""
        #self.all_db.update({"other": {"base_map_game_green": message.content}})
        print(self.all_db)
        if str(message.author)!=self.user:
            if str(message.author.id) in self.all_db["accounts"].keys():
                pass
            else:
                self.all_db["accounts"].update({str(message.author.id): {"game": "", "gameData": "", "xp": 0, "xpUpSee": 1}})
            if str(message.content).startswith(conf.cell_char):
                msg = str(message.content)[len(list(conf.cell_char)):].split(" ")
                if msg[0] in conf.commands:
                    await funcs.com(self, message)
                else:
                    await message.channel.send("Такой команды не существует")

        self.save()

    def save(self):
        with open('db.pickle', 'wb') as f:
            pickle.dump(self.all_db, f)

    def load(self):
        with open('db.pickle', 'rb') as f:
            self.all_db = pickle.load(f)

client = DisBot()
client.run(conf.token)