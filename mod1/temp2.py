from Event_Classes import *
import json
import requests

def url_database_get_and_load():
    '''Getting from json from url and loading into preset objects'''
    url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api_saman_show/main/api.json'
    response = requests.request('GET', url)
    json_db = response.json()

    bd = json_db["events"]
    
    print(json_db)

    newdb = {
        "Musical":[],
        "Theater":[]
    }

    for i in range(len(bd)):

        for key, value in bd[i].items():

            if bd[i]["type"] == 1:

                newMusical = Musical(bd[i]["title"], bd[i]["type"], bd[i]["cartel"],bd[i]["layout"], bd[i]["prices"][0], bd[i]["prices"][1], bd[i]["date"], bd[i]["bands"])
                newdb["Musical"].append(newMusical)

            elif bd[i]["type"] == 2:

                newTheater = Theater(bd[i]["title"], bd[i]["type"], bd[i]["cartel"],bd[i]["layout"], bd[i]["prices"][0], bd[i]["prices"][1], bd[i]["date"], bd[i]["synopsis"])
                newdb["Theater"].append(newTheater)
    
    return newdb

def main():
    db = url_database_get_and_load()
    
    for i in range(len(db["Musical"])):

        print(db["Musical"][i].title)

        print("\n")

main()