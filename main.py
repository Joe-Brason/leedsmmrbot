# Brason making a bot!

# imports
from rltrackerScraper import getMMR
import discord
import os, sys

token = os.getenv("discordBotToken")
usingHeroku = os.getenv("usingHeroku")
if usingHeroku == "True":
    usingHeroku = True
elif usingHeroku == None:
    usingHeroku = False
print("usingHeroku var:", usingHeroku, type(usingHeroku))

# try:
#     token = os.getenv("token")
#     print("The token is", token)
#     # import boto
#     #
#     # from boto.s3.connection import S3Connection
#     # s3 = S3Connection(os.environ['token'])
#
#     # print("HEOIUAHOEIRHRO{Er")
#     # print(s3)
# except ModuleNotFoundError:
#     print("Boto doesn't exist!")
#     usingHeroku = False
#
#     # Get environment variables
#     token = os.getenv('BotToken')
#     # print(token)


from discord.ext import commands, tasks

prefix = "!"

if not usingHeroku:
    os.chdir(r'C:\Users\jbabr\PycharmProjects\pnsBot3')

client = commands.Bot(command_prefix= prefix)
counter = 0


def isBotPerson():
    def predicate(ctx):
        return ctx.message.author.id in [195587810131050496]
    return commands.check(predicate)

@client.command()
@isBotPerson()
async def load(ctx, extension):
    if ctx.author.id != 195587810131050496:  # Check if Lehpro called this or not
        await ctx.send("Only the Bot creator can load bot cogs")
        return
    client.load_extension(f"cogs.{extension}")

@client.command()
@isBotPerson()
async def unload(ctx, extension):
    if ctx.author.id != 195587810131050496:  # Check if Lehpro called this or not
        await ctx.send("Only the Bot creator can unload bot cogs")
        return
    client.unload_extension(f"cogs.{extension}")

@client.command()
@isBotPerson()
async def reload(ctx, extension):
    if ctx.author.id != 195587810131050496:  # Check if Lehpro called this or not
        await ctx.send("Only the Bot creator can reload bot cogs")
        return
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"{extension} cog unloaded")
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"{extension} cog loaded. Reload successful!")

@client.command()
@isBotPerson()
async def kill(ctx):

    if ctx.author.id != 195587810131050496:  # Check if Lehpro called this or not
        await ctx.send("Only the Bot creator can shut the bot down")
        return

    await ctx.send("Bot shutting down...")
    await ctx.bot.logout()


if usingHeroku:
    cogsDir = r'cogs'
else:
    cogsDir = r'C:\Users\jbabr\PycharmProjects\LeedsMMRbot\cogs'
for filename in os.listdir(cogsDir):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


#EXAMPLE LOOPED TASK
@client.event
async def on_ready():
    gamePlaying = "Greenbean Smells"
    await client.change_presence(status=discord.Status.online, activity=discord.Game(gamePlaying))
    change_status.start()  # Remove if wanting to change game status

@tasks.loop(minutes=1)
async def change_status():
    global counter
    await client.change_presence(activity=discord.Game(f"Uptime: {counter} minutes"))
    counter += 1

client.run(token)

print("end")
