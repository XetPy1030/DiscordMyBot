import conf, discord, pickle
import functions

class DisBot(discord.Client):
    all_db = {"accounts":{}, "guilds":{}}

    async def on_ready(self):
        print("Бот начал работу")

    async def on_message(self, message):
        #self.all_db["accounts"][str(message.author.id)]["game"] = ""
        #self.all_db.update({"other": {"base_map_game_green": message.content}})
        #try:
        if str(message.author)!=str(self.user):
            if str(message.author.id) not in self.all_db["accounts"].keys():
                self.all_db["accounts"].update({str(message.author.id): {"xp": 0, "popularity": 0}})
            if str(message.guild.id) not in self.all_db["guilds"].keys():
                self.all_db["guilds"].update({str(message.guild.id): {"mailing_channel": None}})
            if str(message.content).startswith(conf.cell_char):
                msg = str(message.content)[len(list(conf.cell_char)):].split(" ")
                if hasattr(globals()["functions"], msg[0].lower()):
                    await getattr(globals()["functions"], msg[0].lower())(self, message)
                else:
                    await message.channel.send("Такой команды не существует")
        #except Exception as e:
            #await message.channel.send("Ошибка. " + e)
        
        self.save()

    async def on_member_update(self, bef, aft):
        if self.all_db["guilds"][str(bef.guild.id)]["mailing_channel"] == None:
            pass
        else:
            if bef.nick != aft.nick:
                emb = discord.Embed(title="Событие от участника", color=bef.color)
                emb.add_field(name="Событие: ", value=" смена ника",inline=False)
                emb.add_field(name="Имя:", value=bef.name,inline=False)
                emb.add_field(name="Старое имя:", value=bef.nick,inline=False)
                emb.add_field(name="Новое имя:", value=aft.nick,inline=False)
                await self.get_channel(int(self.all_db["guilds"][str(aft.guild.id)]["mailing_channel"])).send(embed = emb)

    def save(self):
        with open('db.pickle', 'wb') as f:
            pickle.dump(self.all_db, f)

def load():
    with open('db.pickle', 'rb') as f:
        return pickle.load(f)



intents = discord.Intents(messages=True, guilds=True)
intents.members = True
intents.presences = True
client = DisBot(intents=intents)
client.all_db = load()
client.run(conf.token)