import discord, conf

async def get_info(self, message, memberr):
    member = memberr
    emb = discord.Embed(title="Информация о пользователе", color=member.color)
    emb.add_field(name="Имя:", value=member.name,inline=False)
    emb.add_field(name="Айди пользователя:", value=member.id,inline=False)
    
    if type(member) == discord.Member:
        counter = 0
        lim = conf.len_check_msgs
        async for mssg in message.channel.history(limit=lim):
            if mssg.author == member:
                counter += 1
        t = member.status
        if t == discord.Status.online:
            d = " В сети"
        elif t == discord.Status.offline:
            d = " Не в сети"
        elif t == discord.Status.idle:
            d = " Не активен"
        elif t == discord.Status.dnd:
            d = " Не беспокоить"
        elif t == discord.Status().invisible:
            d = " Невидимка"
        emb.add_field(name="Местный ник:", value=member.nick,inline=False)
        emb.add_field(name="Статус:", value=d,inline=False)
        emb.add_field(name="% смс за {}:".format(lim), value=(counter/lim*100),inline=False)
        emb.add_field(name="Зашел на сервер: ", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p"), inline=False)
        emb.add_field(name="Роль на сервере:", value=f"{member.top_role.mention}",inline=False)
    emb.add_field(name="Акаунт был создан:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p"),inline=False)
    emb.set_thumbnail(url=member.avatar_url)
    await message.channel.send(embed = emb)

async def info(self, message):
    msg = str(message.content)[len(list(conf.cell_char)):].split(" ")
    if len(msg) == 1:
        member = message.author
        await get_info(self, message, member)
    elif len(msg) == 2:
        try:
            member = message.mentions[0]
            await get_info(self, message, member)
        except:
            await message.channel.send("ПОЛЬЗОВАТЕЛЯ, А НЕ ТЕКСТ БЛИН ИЛИ РОЛЬ")
    else:
        await message.channel.send("Неправильно написано смс, надо !info [упоминание пользователя(необязательно)]")