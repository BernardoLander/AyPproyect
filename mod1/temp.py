from multiprocessing import Value
import requests
import json
from Event_Classes import *


def main():

    url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api_saman_show/main/api.json'
    response = requests.request('GET', url)
    json_db = response.json()

    bd = json_db["events"]

    newdb = {
        "Musical":[],
        "Theater":[]
    }

    for i in range(len(bd)):

        for key, Value in bd[i].items():

            if bd[i]["type"] == 1:

                newMusical = Musical(bd[i]["title"], bd[i]["type"], bd[i]["cartel"],bd[i]["layout"], bd[i]["prices"][0], bd[i]["prices"][1], bd[i]["date"], bd[i]["bands"])
                newdb["Musical"].append(newMusical)

            elif bd[i]["type"] == 2:

                newTheater = Theater(bd[i]["title"], bd[i]["type"], bd[i]["cartel"],bd[i]["layout"], bd[i]["prices"][0], bd[i]["prices"][1], bd[i]["date"], bd[i]["synopsis"])
                newdb["Theater"].append(newTheater)
    print (bd)
    print ('\n\n------------------------------------------------------------------')
    print (newdb) 

    print (newdb["Musical"][0].vip_price)


main()