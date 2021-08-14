async def mailing(self, message):
    if self.all_db["guilds"][str(message.guild.id)]["mailing_channel"] == None:
        self.all_db["guilds"][str(message.guild.id)]["mailing_channel"] = str(message.channel.id)
        await message.channel.send("Подписка оформлена")
    else:
        self.all_db["guilds"][str(message.guild.id)]["mailing_channel"] = None
        await message.channel.send("Подписка убрана")