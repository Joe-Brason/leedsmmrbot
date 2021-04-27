import json
import urllib.request

from bs4 import BeautifulSoup

# Bean URL https://api.tracker.gg/api/v1/rocket-league/player-history/mmr/483476
# Leph URL https://api.tracker.gg/api/v1/rocket-league/player-history/mmr/76093

# Get playerId: https://api.tracker.gg/api/v2/rocket-league/standard/profile/steam/lehpro22

# if public exists Leph: https://public-api.tracker.gg/api/v1/rocket-league/player-history/mmr/76093

def getJSON(URL):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
    req = urllib.request.Request(url=URL, headers=headers)
    data = urllib.request.urlopen(req).read()

    return json.loads(data)


def getPlayerId(platform, name):
    URL = f"https://api.tracker.gg/api/v2/rocket-league/standard/profile/{platform}/{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
    req = urllib.request.Request(url=URL, headers=headers)
    data = urllib.request.urlopen(req).read()

    foo = getJSON(URL)
    playerId = foo["data"]["metadata"]["playerId"]
    #print(URL)
    return playerId

def getMMR(playerId):
    """
    Scrapes TRN for player MMR given their playerId
    """


    URL = f"https://api.tracker.gg/api/v1/rocket-league/player-history/mmr/{playerId}"


    foo = getJSON(URL)

    # print(foo)
    return foo



    # Old method

    # URL = f"https://rocketleague.tracker.network/rocket-league/profile/steam/{playerID}/overview"
    # # print(URL)
    # page = requests.get(URL)
    #
    # soup = BeautifulSoup(page.content, 'html.parser')
    # # print(soup)
    #
    # results = soup.find_all("div", {"class": "mmr", "data-v-2dd6b9bc": ""})
    # results2 = soup.find_all("div", {"class": "playlist", "data-v-2dd6b9bc": ""})
    # # print(results)
    #
    # # print(results)
    #
    # mmrValues = [int(re.sub(r"\D", '', r.text)) for r in results]
    # mmrNames = [r.text.strip() for r in results2]
    #
    # if mmrNames[0] == "Un-Ranked":
    #     mmrNames.append(mmrNames.pop(0))
    #     mmrValues.append(mmrValues.pop(0))
    # # print(mmrNames)
    #
    # return dict(zip(mmrNames, mmrValues))
    #
    # #mmrNames = ["Unranked", "1v1", "2v2", "3v3", "Hoops", "Rumble", "Dropshot", "Snowday", "Tournament"]

def scrape(platform, platformId, playlist):
    """
    :param platform: must be "steam", "epic", "xbox", or "playstation"
    :param platformId: must be int
    :param playlist:
    :return: playerId, JSON like object containing MMR
    """

    playerId = getPlayerId(platform, platformId)
    data = getMMR(playerId)

    if playlist == "all":
        return playerId, data

    playlistDict = {"casual":"0", "1v1":"10", "2v2":"11", "unknown":"12", "3v3":"13", "hoops":"27", "rumble":"28", "dropshot":"29", "snowday":"30", "tournament":"34"}

    p = playlistDict[playlist]

    # print(p)

    # print(data)

    return playerId, data["data"][p]

    # for item in data["data"][p]:
    #     print(item)







if __name__ == "__main__":
    import time

    startTime = time.time()

    print(scrape("steam", "76561198054107914", "3v3"))

    raise Exception

    print(getPlayerId("steam", "76561198054107914"))

    print(getMMR(483476), "Greenbean")  # Bean

    print(getMMR(76561198115240786), "Leph")  # Leph
    print(getMMR(76561198157711330), "Wandil")  # Wandil
    print(getMMR(76561198257787951), "Aspct")  # Aspct
    print(getMMR(76561198260381791), "GnB")  # GnB
    print(getMMR(76561198982539588), "Dx")  # dx
    print(getMMR(76561198049647170), "Mr. Soupz")  # soupz
    print(getMMR(76561198046237561), "Luke")  # luke


    print(f"Finished in [{time.time() - startTime}]")