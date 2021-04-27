import pymongo
import rltrackerScraper

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["RocketLeagueDB"]
mycol = mydb["playerMMR"]

def scrapeToMongo(discordName, discordDiscriminatior, platform, platformId):
    # x = mycol.find({"playerId": "483476"})
    # print(x.count_documents())

    myquery = {"DiscordName": discordName, "DiscordDiscriminator": discordDiscriminatior}
    mydoc = mycol.count_documents(myquery) != 0
    if mydoc == 1:
        print(f"DB entry for {discordName}#{discordDiscriminatior} already exists")
        return
    else:
        print(f"Attempting to add data for {discordName}#{discordDiscriminatior} to the db")


    playerInfo = {
        "DiscordName": discordName,
        "DiscordDiscriminator": discordDiscriminatior,
        "platform": platform,
        "platformId": platformId
    }
    playerId, mmr = rltrackerScraper.scrape(platform, platformId, "all")
    result = mycol.insert_one({**playerInfo, **mmr, **{"playerId": playerId}})
    print("Done!")
    return True

if __name__ == "__main__":


    scrapeToMongo("Leph", "9858", "steam", 76561198115240786)
    scrapeToMongo("Greenbean", "4970", "steam", 76561198054107914)
    scrapeToMongo("Wandil", "4754", "steam", 76561198157711330)
    scrapeToMongo("Aspct", "9858", "steam", 76561198257787951)
    scrapeToMongo("GnB", "1282", "steam", 76561198260381791)
    scrapeToMongo("Dx", "0686", "steam", 76561198982539588)
    scrapeToMongo("Soupz", "8327", "steam", 76561198049647170)
    scrapeToMongo("Luke", "0174", "steam", 76561198046237561)
