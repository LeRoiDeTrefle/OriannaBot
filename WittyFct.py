import asyncio
import discord
from discord.ext import commands

Triggers = []
Remarks = []


class Witty:

    def __init__(self, bot):
        self.bot = bot

    """Heeeeuuuu, ca répond des trucs quand on dit des choses"""

    @commands.command(hidden=True)
    async def TestBot(self, Password : str):
        """Simply kill the python process of the bot"""
        await self.bot.say("H4H4H4H4H4H4H Mauvais mot de passe o  https://www.youtube.com/watch?v=lVIFzVy3tEo")

    @commands.command(no_pm=True)
    async def addwit(self, Argu : str):
        """Ajoute un nouveau déclencheur et la remarque associée à Wittyremarks.

        Le déclencheur et la remarque doivent être séparées par un "/".
        Exemple : Louder/yay !

        Du coup, il faut pas utiliser de "/" dans la remarque ni dans le déclancheur, silly !
        Et n'utiliser qu'un seul "/".
        """
        Argus = Argu.split("/")
        print(Argus)
        if len(Argus) != 2:
            await self.bot.say('Il faut entrer un déclancheur et une remarque à associer séparées par un "/"')
            return False
        Triggers.append(Argus[0])
        Remarks.append(Argus[1])
        last = len(Triggers) - 1
        text = 'Remarque ' + Remarks[last] + ' ajoutée lorsque le déclancheur ' + Triggers[last] + ' est écrit dans le chat'
        await self.bot.say(text)
        WittyFile = open("./Collections/WittyCol.csv","a+")
        string = Remarks[last]+';'+Triggers[last]+'\n'
        WittyFile.write(string)
        WittyFile.close()

        return True
        

