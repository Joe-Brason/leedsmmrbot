import matplotlib.pyplot as plt
import csv
import datetime
import io
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
plt.savefig(data_stream, format='png', bbox_inches="tight", dpi = 80)
plt.close()

data_stream.seek(0)
chart = discord.File(data_stream,filename="rocket_chart.png")
emb = discord.Embed(
            title='Player Information Database Search Result',
            description="This embed shows all players matching the university search",
            colour=discord.Colour.blue()
        )
emb.set_image(
   url="attachment://unemployment_chart.png"
)

await context.send(embed=embed, file=chart)