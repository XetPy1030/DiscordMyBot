import conf, discord
async def delete(self, message):
    for i in await message.channel.history(limit=200).flatten():
        if i.author == self.user:
            await i.delete()