import asyncio
import discord
import sys
from discord.ext import commands


class Admin:
    """Bot adminstration commands.

    Works in multiple servers at once.
    """
    
    def __init__(self, bot):
        self.bot = bot
        self.voice_states = {}
			
    @commands.command(hidden=True)
    async def QuitBot(self, Password : str):
        """Simply kill the python process of the bot"""
        Configured = False
        try:
            File = open("PasswordAdmin.pwd","r")
            Configured = True
        except:
            await self.bot.say("Mot de passe non configuré. Je vais devoir utiliser le mot de passe par defaut, bravo l'adiministrateur...")
        if Configured:
            PasswordAdmin = File.read()
        else:
            PasswordAdmin = "1234"
        if Password == PasswordAdmin:
            await self.bot.say("I'll be back...")
            sys.exit()
        else:
            await self.bot.say("H4H4H4H4H4H4H Mauvais mot de passe o  https://www.youtube.com/watch?v=lVIFzVy3tEo")