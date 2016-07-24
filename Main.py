import asyncio
import discord
from MusicFct import *
from discord.ext import commands

if not discord.opus.is_loaded():
    # the 'opus' library here is opus.dll on windows
    # or libopus.so on linux in the current directory
    # you should replace this with the location the
    # opus library is located in and with the proper filename.
    # note that on windows this DLL is automatically provided for you
    discord.opus.load_opus('opus')

bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'), description='Je suis le bot du serveur discord French Baguette, voici les commandes que vous pouvez utiliser sur moi: ')
bot.add_cog(Music(bot))

@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))

bot.run('MjA2ODU2Nzg4MzQyMDc5NDg4.Cnap5Q.vWAJ1niwI47yzqOxQLAQ_GV63c0')
