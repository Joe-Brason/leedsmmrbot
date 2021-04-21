from discord.ext import commands
import asyncio
import discord

class BlankCog(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Blank Cog is online from start")


    # Commands

    # Example
    # @commands.command(aliases=["Ping", "PING"])
    # async def ping(self, ctx):
    #     await ctx.send(f"Pong! {round(self.client.latency, 4)}ms")



def setup(client):
    client.add_cog(BlankCog(client))