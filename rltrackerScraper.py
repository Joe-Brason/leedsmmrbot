import requests
import re

from bs4 import BeautifulSoup

# Bean URL https://api.tracker.gg/api/v1/rocket-league/player-history/mmr/483476
# Leph URL https://api.tracker.gg/api/v1/rocket-league/player-history/mmr/76093

def getMMR(playerID, raw=False):
    """
    Scrapes TRN for player MMR
    """

    URL = f"https://rocketleague.tracker.network/rocket-league/profile/steam/{playerID}/overview"
    # print(URL)
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all("div", {"class": "mmr", "data-v-2dd6b9bc": ""})
    results2 = soup.find_all("div", {"class": "playlist", "data-v-2dd6b9bc": ""})

    # print(results)

    mmrValues = [int(re.sub(r"\D", '', r.text)) for r in results]
    mmrNames = [r.text.strip() for r in results2]
    if mmrNames[0] == "Un-Ranked":
        mmrNames.append(mmrNames.pop(0))
        mmrValues.append(mmrValues.pop(0))
    # print(mmrNames)

    return dict(zip(mmrNames, mmrValues))

    #mmrNames = ["Unranked", "1v1", "2v2", "3v3", "Hoops", "Rumble", "Dropshot", "Snowday", "Tournament"]





if __name__ == "__main__":
    import time

    startTime = time.time()

    print(getMMR(76561198054107914), "Greenbean")  # Bean
    print(getMMR(76561198115240786), "Leph")  # Leph
    # print([1775, 1207, 1554, 1729, 1131, 1213, 1123, 1196, 1618])
    print(getMMR(76561198157711330), "Wandil")  # Wandil
    print(getMMR(76561198257787951), "Aspct")  # Aspct
    print(getMMR(76561198260381791), "GnB")  # GnB
    print(getMMR(76561198982539588), "Dx")  # dx
    print(getMMR(76561198049647170), "Mr. Soupz")  # soupz
    print(getMMR(76561198046237561), "Luke")  # luke


    print(f"Finished in [{time.time() - startTime}]")