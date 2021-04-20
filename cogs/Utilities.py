from discord.ext import commands
import asyncio
import discord

class Utilities(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Utilities is online from start")


    # Commands

    @commands.command(aliases=["Ping", "PING"])
    async def ping(ctx):
        await ctx.send(f"Pong! {round(self.client.latency, 4)}ms")

    # clear command in a guild
    @commands.command(aliases=["c"])
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def clear(self, ctx, amount : int):
        await ctx.channel.purge(limit=amount+1)  # Includes the "!clear [number]" message


    @clear.error
    async def clearError(self, ctx, error):
        # If user messages "!clear"
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Usage: {ctx.prefix}clear [number of messages to clear]")
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send(f"The bot role does not have permission to remove messages in this guild")
            print(error)
        elif isinstance(error, commands.CheckFailure):
            await ctx.send(f"You do not have permission to use that command {ctx.message.author.mention}")
        print(error)

    # clear command in a DM
    @commands.command(aliases=["cdm"])
    @commands.dm_only()
    async def cleardm(self, ctx, amount: int):
        removeCount = 0
        async for message in ctx.author.history(limit=amount*4):
            if removeCount == amount:
                break
            elif message.author.id == self.client.user.id:
                await message.delete()
                await asyncio.sleep(0.5)
                removeCount += 1

    @cleardm.error
    async def cleardmError(self, ctx, error):
        # If user messages "!clear"
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Usage: {ctx.prefix}clear [number of messages to clear]")
        elif isinstance(error, commands.CheckFailure):
            await ctx.send(f"You do not have permission to use that command {ctx.message.author.mention}")
        else:
            print("Uncaught error", error)





    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)

    @kick.error
    async def kickError(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"{ctx.author.mention} You do not have permission to use this command ({ctx.prefix}kick)")
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send(f"This bot does not have permission to kick people in this guild")
        else:
            await ctx.send(f"Error: {error}")


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.ban(reason=reason)
            await ctx.send(f"Unbanned {user.mention}")
        except discord.Forbidden:
            await ctx.send("Nice try. This function is disabled here.")
        else:
            await member.ban(reason=reason)  # Dumb code again lmao. Works tho


    @ban.error
    async def banError(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"{ctx.author.mention} You do not have permission to use this command ({ctx.prefix}ban)")
        elif isinstance(error, discord.Forbidden):
            await ctx.send(f"{ctx.author.mention} I can't do that!")
        else:
            await ctx.send(f"Error: {error}")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member:discord.user):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}")
                return

    @unban.error
    async def unbanError(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"{ctx.author.mention} You do not have permission to use this command ({ctx.prefix}ban)")
        else:
            await ctx.send(f"Error: {error}")


def setup(client):
    client.add_cog(Utilities(client))