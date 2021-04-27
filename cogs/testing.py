from discord.ext import commands
import asyncio
import discord


class Testing(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Testing is online from start")

    @commands.command(aliases=["send"])
    async def sendDM(self, ctx, member: discord.Member):



        #await member.send(f"I'm from the past. WARN LEPH OF THE FOLLOWING: Bots cannot DM people without being in a shared guild. So tell him not to spend 2 hours creatin an elaborate plan to create a command which this bot would have which when you call it  would call a function on the LadderBot which in turn calls the original function starting a loop, and then message CLJS saying whatever you do DONT write that function and call it ")
        await member.send("oh and btw, i cant see what you DM this bot")
        pass

    @commands.command(aliases=["die"])
    async def dieBotDie(self, ctx, member: discord.Member):
        await member.send(f"Hello ")
        pass


# Commands

    # Example
    # @commands.command(aliases=["Ping", "PING"])
    # async def ping(self, ctx):
    #     await ctx.send(f"Pong! {round(self.client.latency, 4)}ms")



def setup(client):
    client.add_cog(Testing(client))