from discord.ext import commands
import asyncio
import discord
import matplotlib.pyplot as plt
import csv
import datetime
import io

class BlankCog(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Blank Cog is online from start")

    @commands.command(aliases=["example", "Example", "eg"])
    async def exampleMMR(self, ctx):

        # C:\Users\jbabr\Downloads\13.csv

        x = []
        y = []

        with open(r"C:\Users\jbabr\Downloads\13.csv", newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                # print(int(row[0].replace(",", "")))
                y.append(int(row[0].replace(",", "")))

                # print(row[1].replace(",", ""))
                date = datetime.datetime.fromisoformat(row[1].replace(",", ""))
                x.append(date)

        # Initialize IO
        data_stream = io.BytesIO()

        plt.plot(x, y, 'r')
        plt.ylim(0, 2000)
        plt.savefig(data_stream, format='png', bbox_inches="tight", dpi=80)
        plt.close()

        data_stream.seek(0)
        chart = discord.File(data_stream, filename="rocket_chart.png")
        emb = discord.Embed(
            title='Player: Leph#9858',
            description="Gamemode: Ranked Standard",
            colour=discord.Colour.blue()
        )
        emb.set_image(
            url="attachment://rocket_chart.png"
        )

        await ctx.send(embed=emb, file=chart)


    # Commands

    # Example
    # @commands.command(aliases=["Ping", "PING"])
    # async def ping(self, ctx):
    #     await ctx.send(f"Pong! {round(self.client.latency, 4)}ms")



def setup(client):
    client.add_cog(BlankCog(client))