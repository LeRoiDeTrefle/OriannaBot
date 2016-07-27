import asyncio
import discord
from MusicFct import *
from discord.ext import commands

Beta = True

if not discord.opus.is_loaded():
    # the 'opus' library here is opus.dll on windows
    # or libopus.so on linux in the current directory
    # you should replace this with the location the
    # opus library is located in and with the proper filename.
    # note that on windows this DLL is automatically provided for you
    discord.opus.load_opus('opus')
if Beta:
	bot = commands.Bot(command_prefix=commands.when_mentioned_or('€'), description='Je suis le bot du serveur discord French Baguette, voici les commandes que vous pouvez utiliser sur moi: ')
else:
	bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'), description='Je suis le bot du serveur discord French Baguette, voici les commandes que vous pouvez utiliser sur moi: ')
bot.add_cog(Music(bot))

@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))

if Beta:
	bot.run('MjA2OTAyNzU4NjE4NDMxNDg4.CnbUtQ.3VFStiuPDBY0Pk22vpUJ9-Ovkv8')
else:
	bot.run('MjA2OTAzMzE1NTY3NjA3ODA4.CnbVOg.BVpugzhNyGDJfhBodJN96HvkvTU')
