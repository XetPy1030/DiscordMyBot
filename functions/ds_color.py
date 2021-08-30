import conf, discord
async def color(a, mc):
    if type(mc.author) == discord.Member:
        msg = str(mc.content)[len(list(conf.cell_char)):].split(" ")
        if len(msg) == 2 and msg[1].startswith("#"):
            if len(mc.author.roles) > 1:
                role = mc.author.top_role
                await role.edit(colour=discord.Colour(int(mc.content.split("#")[1], 16)))
            else:
                rol = await mc.guild.create_role(name=mc.author.name+"_role", colour=discord.Colour(int(mc.content.split("#")[1], 16)))
                await mc.author.add_roles(rol)
            await mc.channel.send("Готово")
        else:
            await mc.channel.send("Неправильно, надо - !color #[hex цвет]")
    else:
        await mc.channel.send("Смс не из гильдии")