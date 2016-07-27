import asyncio
import discord
import system
from discord.ext import commands


class Admin:
    """Bot adminstration commands.

    Works in multiple servers at once.
    """
			
    @commands.command(hidden=True)
    async def QuitBot(self, ctx, *, Password : str):
        """Joins a voice channel."""
        Configured = False
        try:
            File = Open("PasswordAdmin.pwd","r")
            Configured = True
        else:
            Print("Password File not found, default password will be used")
        if Configured:
            PasswordAdmin = File.read()
        else:
            PasswordAdmin = "1234"
        if Password == PasswordAdmin:
            await self.bot.say("I'll be back...")
            sys.exit()
        else:
            await self.bot.say("H4H4H4H4H4H4H  https://www.youtube.com/watch?v=lVIFzVy3tEo")