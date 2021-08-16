import discord
async def info(self, message):
    member = message.author

    emb = discord.Embed(title="Информация о пользователе", color=member.color)
    emb.add_field(name="Имя:", value=member.name,inline=False)
    emb.add_field(name="Местный ник:", value=member.nick,inline=False)
    emb.add_field(name="Айди пользователя:", value=member.id,inline=False)

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

    emb.add_field(name="Статус:", value=d,inline=False)
    emb.add_field(name="Зашел на сервер: ", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p"), inline=False)
    emb.add_field(name="Роль на сервере:", value=f"{member.top_role.mention}",inline=False)
    emb.add_field(name="Акаунт был создан:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p"),inline=False)
    emb.set_thumbnail(url=message.author.avatar_url)
    await message.channel.send(embed = emb)