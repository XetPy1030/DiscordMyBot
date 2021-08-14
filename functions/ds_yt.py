import youtube_dl, discord
youtube_dl.utils.bug_reports_message = lambda: ''
from youtubesearchpython import VideosSearch
ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename


import conf
async def yt(a, mc):
    msg = str(mc.content)[len(list(conf.cell_char)):].split(" ")
    voice_client = mc.guild.voice_client
    server = mc.guild
    voice_channel = server.voice_client
    if msg[1] == "play":
        if not mc.author.voice:
            await mc.channel.send("{} is not connected to a voice channel".format(mc.author.name))
            return
        else:
            try:
                channel = mc.author.voice.channel
            except:
                pass
        try:
            await channel.connect()
        except:
            pass
        try:
            await channel.connect()
        except:
            pass
        if True :
            url = " ".join(msg[2:])
            server = mc.guild
            voice_channel = server.voice_client

            async with mc.channel.typing():
                filename = await YTDLSource.from_url(url, loop=a.loop)
                voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
            await mc.channel.send('**Now playing:** {}'.format(filename))
        #except:
            #await mc.channel.send("The bot is not connected to a voice channel.")
    elif msg[1] == "stop":
        if voice_client.is_playing():
            voice_client.stop()
            if voice_client.is_connected():
                await voice_client.disconnect()
            else:
                await mc.channel.send("А бот не подключен к гч")
        else:
            await mc.channel.send("А я и не играю, зачем мне тормозить?")
    elif msg[1] == "pause":
        if voice_client.is_playing():
            await voice_client.pause()
        else:
            await mc.channel.send("Бот не играет в данный момент")
    elif msg[1] == "resume":
        if voice_client.is_paused():
            await voice_client.resume()
        else:
            await mc.channel.send("Бот не играет в данный момент")

