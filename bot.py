import conf, discord, pickle
import functions
import check
import random #для теста
import datetime

class DisBot(discord.Client):
    all_db = {"accounts":{}, "guilds":{}}

    async def on_ready(self):
        print("Бот начал работу")
        self.testt = "Ага"
        self.repl_hour.start()

    async def on_message(self, message):
        test = True
        #self.all_db["accounts"][str(message.author.id)]["game"] = ""ehgegfshw
        #self.all_db.update({"other": {"base_map_game_green": message.content}})
        #try:
        if str(message.author)!=str(self.user):

            if test:
                if random.randint(0, 2) == 0:#будет ли тест функция
                    if random.randint(0, 1) == 0:#будет запоминать или отправлять, в дан случае запомин
                        self.testt = message.content
                    else:
                        try:
                            await message.reply(self.testt)
                        except:
                            pass

            check.check_log(self.all_db, str(message.author.id))
            if type(message.author) == discord.Member:
                if str(message.guild.id) not in self.all_db["guilds"].keys():
                    self.all_db["guilds"].update({str(message.guild.id): {"mailing_channel": None}})
            else:
                print(message)
                print(message.content)
            if str(message.content).startswith(conf.cell_char):
                msg = str(message.content)[len(list(conf.cell_char)):].split(" ")
                if hasattr(globals()["functions"], msg[0].lower()):
                    await getattr(globals()["functions"], msg[0].lower())(self, message)
                else:
                    await message.channel.send("Такой команды не существует")
        #except Exception as e:
            #await message.channel.send("Ошибка. " + e)
        
        #self.save()

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

    @discord.tasks.loop(hours=1)
    async def repl_hour(self):
        if 8 < datetime.time.hour < 10:
            for i in self.all_db["guilds"]

    def save(self):
        with open('db.pickle', 'wb') as f:
            pickle.dump(self.all_db, f)

def load():
    with open('db.pickle', 'rb') as f:
        return pickle.load(f)

client = DisBot(intents=discord.Intents.all())
aldb = load()
#aldb["accounts"] = {}
#aldb.update({"games": {"KN": {}}})
client.all_db = aldb
client.run(conf.token)