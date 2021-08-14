import conf, discord
async def color(a, mc):
    msg = str(mc.content)[len(list(conf.cell_char)):].split(" ")
    if len(msg) == 2 and msg[1].startswith("#"):
        if len(mc.author.roles) > 1:
            role = mc.author.roles[len(mc.author.roles)-1:][0]
            await role.edit(colour=discord.Colour(int(mc.content.split("#")[1], 16)))
        else:
            await guild.create_role(name=mc.author.name + message.content.split("#")[1], colour=discord.Colour(int(message.content.split("#")[1], 16)))
        await mc.channel.send("Готово")