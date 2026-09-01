import numpy as np
import json
import matplotlib.pyplot as plt
import requests
import time
base_url = 'https://api.mcsrranked.com'

def getThetaFromID(match_id):
    url = f"{base_url}/matches/{match_id}"
    response = requests.get(url)

    #print(f"Getting theta code: {response.status_code}")

    data = response.json()["data"]

    players = data["players"]
    if "uuid" not in data["result"]: #if draw
        return

    
    winner_uuid = data["result"]["uuid"]

     

    timelines = data["timelines"]

    with open("advanced_match_data.json", "w") as f:
        json.dump(data,f)
    winner_rod_time = 0
    loser_rod_time = 0
    for timeline in timelines: 
        if timeline["type"] == "nether.obtain_blaze_rod":
            if timeline["uuid"] == winner_uuid:
                winner_rod_time = timeline["time"]
            else:
                loser_rod_time = timeline["time"]

    if winner_rod_time and loser_rod_time:
        return loser_rod_time-winner_rod_time
    else:
        return None  


def getVersusMatchIDs(player1,player2,n =100, spamToFile = ""):
    url = f"{base_url}/users/{player1}/versus/{player2}/matches"

    parameters = {
        "season": 10, #hopefully before most people started sending 1 eyes
        "count": n
    }

    response = requests.get(url, params=parameters)
    print(f"Getting match IDS code: {response.status_code}")
    matches = response.json()["data"]

    match_ID_list = []
    for match in matches:
        match_ID_list.append(match["id"])

    return match_ID_list

def getPlayerMatchIDs(player, n=100):
    url = f"{base_url}/users/{player}/matches"

    parameters = {
        "season": 10,
        "count": n
    }

    response = requests.get(url,params=parameters)

    print(f"Getting match IDS code: {response.status_code}")

    matches = response.json()["data"]

    match_ID_list = []
    for match in matches:
        match_ID_list.append(match["id"])

    return match_ID_list








''' 
ids = getMatchIDs("doogile", "infume")

thetas = []
for match_id in ids:
    thetas.append(getThetaFromID(match_id)/1000)

print(thetas)

'''


def getPlayers(n = 50):
    url = f"{base_url}/phase-leaderboard"
    parameters = {
        "season": 10
    }

    response = requests.get(url,params = parameters)

    #print(f"Getting players code: {response.status_code}")

    data = response.json()["data"]
    
    player_nicknames = []
    for i in range(n):
        user = data["users"][i]
        user_name = user["nickname"]
        player_nicknames.append(user_name)
    
    return player_nicknames

def getUniqueMatches(players, n=100):
    match_ids = []
    for player in players:
        match_ids += getPlayerMatchIDs(player,n)

    match_ids = list(set(match_ids)) #stupid way to make unique

    return match_ids


def loadThetas(ids):
    thetas = []
    for i in range(len(ids)):
        if i%50 == 0:
            print(f"Done with {i}")
        if i%470 == 469:
            with open("thetas.json", "w") as f:
                json.dump(thetas, f)
            print("sleeping for a while")
            time.sleep(600)
        thetas.append(getThetaFromID(ids[i]))
            
            

    thetas_clean = [theta for theta in thetas if theta != None]

    return thetas_clean


    

time.sleep(600)
players = getPlayers(50)

matchids = getUniqueMatches(players, 100)
time.sleep(600)

print(loadThetas(matchids))




        



#thetas = [-12879, -37557, -31192, 25686, -14918, 3336, -43401, -27976, 37594, 51030, 4428, 7602, 17809, 18333, 203511, 57638, 101802, 42245, -7856, -73227, -131582, 34135, 99802, 31399, 52730, 53072, 16566, -45072, 64006, 6328, 86086, 63344, 2784, 43853, 87649, -348902, 11730, 3492, -24954, 126382, 4740, 32213, 31173, 53924, 12457, -12316, 17545, -304124, 93272, -260426, -277182, 44725, -132037, 148281, 13138, 34455, 16904, 13542, 4493, 4760, 76194, 6877, -45019, -2508, -11125, -23963, -42986, -10601, -4561, -17470, 3388, 4213, 7252, -3115, 15919, -18541, 3273, -21318, -27174, -3640, -58942, -7740, -17677, -12726, -29725, -21572, 10257, -29399, 11719, -39437, -10175, 27464, -35812, -161091, -30124, -8952]
#plt.plot(thetas)
#plt.show()
#print(thetas)
#print(getThetaFromID(12896972))
    
                 
            

#getWantedDataFromID(12896972)
#response = makeRequest()

#for key in response["data"]:
    #print(key)

#print(response["data"]["timelines"])

#match_id = 12896972
