import conf
async def snake(a, mc):
    print(a.all_db)
    msg = str(mc.content)[len(list(conf.cell_char)):].split(" ")
    if len(msg) == 2 and msg[1] == "new":
        if a.all_db["accounts"][str(mc.author.id)]["game"] == "":
            a.all_db["accounts"][str(mc.author.id)]["game"] = "snake"
            base_map = []
            for x in range(10):
                base_map +=[[]]
                for y in range(10):
                    base_map[x] += [[]]
            for x in range(10):
                for y in range(10):
                    base_map[x][y] = a.all_db["other"]["base_map_game"]
            text = str(mc.author.name)+"\n"
            for x in range(10):
                for y in range(10):
                    text+=base_map[x][y]
                text+="\n"
            msgg = await mc.channel.send(text)
            a.all_db["accounts"][str(mc.author.id)]["gameData"] = ["r", ["24", "14", "04"]]
            a.loop.create_task(loop_func(a, mc, msgg))

async def loop_func(aa, mcc, msg):
    text = str(mcc.author.name) + "\n"
    cols = [a.all_db["other"]["base_map_game"], a.all_db["other"]["base_map_game_red"], a.all_db["other"]["base_map_game_green"]]

    base_map = []
    for x in range(10):
        base_map +=[[]]
        for y in range(10):
            base_map[x] += [[]]
    for x in range(10):
        for y in range(10):
            base_map[x][y] = cols[0]
    if aa.all_db["accounts"][str(mc.author.id)]["gameData"][0] == "r":
        for x in aa.all_db["accounts"][str(mc.author.id)]["gameData"][1]:
            if x[0] 
    for x in range(len(aa.all_db["accounts"][str(mc.author.id)]["gameData"][1])):
        base_map[int(aa.all_db["accounts"][str(mc.author.id)]["gameData"][x][0])][int(aa.all_db["accounts"][str(mc.author.id)]["gameData"][x][1])] = cols[2]

    await msg.edit()
    await asyncio.sleep(1) 