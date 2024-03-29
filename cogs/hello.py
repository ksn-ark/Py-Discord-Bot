import discord
from discord.ext import commands, tasks

class hello(commands.Cog): #creates a class that inherits from commands.cog
    def __init__(self, client): #client created in main passed in
        self.client = client #lets us initialize the client object here
        
    
    #commands
    @commands.command() 
    async def Hello(self, ctx): #command called ping
        await ctx.send(f'Hello! <@{ctx.author.id}>') #responds with pong when triggered


def setup(client): #sets up the client object
    client.add_cog(hello(client)) #runs a client method and passes this class i.e command into the bot object