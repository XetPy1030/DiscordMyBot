import functions.ds_help as ds_help
import functions.ds_date as ds_date
import functions.ds_random as ds_random
import functions.ds_color as ds_color
import functions.ds_yt as ds_yt
import functions.ds_hug as ds_hug
import functions.ds_splash as ds_splash
import functions.ds_emoji as ds_emoji
#import functions.ds_snake as ds_snake
import conf
async def com(self, message):
    msg = str(message.content)[len(list(conf.cell_char)):].split(" ")
    await getattr(globals()["ds_"+msg[0]], msg[0])(self, message)