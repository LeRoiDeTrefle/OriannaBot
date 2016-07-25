import asyncio
import discord
import math
import os
import sys
import getopt
import numpy as np
from MusicFct import *
from discord.ext import commands

Beta = False

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



def main(argv):
    verbose = False
    Beta = False
    DebugMode = False
    offset = 0
    opts, args = getopt.getopt(argv,"bhdv")
    for opt, arg in opts:
        if opt == '-h':
            print('Main.py -b <BetaMode> -h <help> -d <DebugMode [Activated by default on beta mode]> -v <Verbose>')
            return 0
        elif opt == '-b':
            Beta = True
        elif opt == '-d':
            DebugMode= True
        elif opt == '-v':
            verbose =  True
    print('Lançement du bot en mode: Beta - '+str(Beta)+' Debug - '+str(DebugMode)+' Verbose - '+str(verbose))
    if Beta:
        File = open("BetaToken.txt","r")
        Token = File.read()
        bot.run(Token)
    else:
        File = open("Token.txt","r")
        Token = File.read()
        bot.run(Token)
        
    
if __name__ == "__main__":
   main(sys.argv[1:])