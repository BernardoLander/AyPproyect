from email import utils
import json
import requests
from Event_Classes import *
from utilsm1 import *

def url_database_get_and_load():
    '''Getting from json from url and loading into preset objects'''
    url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api_saman_show/main/api.json'
    response = requests.request('GET', url)
    json_db = response.json()

    bd = json_db["events"]

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



def Event_visualizer(bd):

    '''Visualizer of database in formatted strings'''

    print("Eventos Musicales:\n")

    for i in range(len(bd["Musical"])):

        print (f''' Evento numero: {i}
                    Titulo: {bd["Musical"][i].title}
                    Cantidad de Artistas: {bd["Musical"][i].bands}
                    Artistas: {bd["Musical"][i].cartel}
                    Precio para butaca General: {bd["Musical"][i].gen_price}
                    Precio para butaca VIP: {bd["Musical"][i].vip_price}
                    Fecha del evento: {bd["Musical"][i].date}''')

    print("Eventos de Teatro:\n")

    for i in range(len(bd["Theater"])):

                print (f''' Evento numero: {i}
                            Titulo: {bd["Theater"][i].title}
                            Synopsys: {bd["Theater"][i].bands}
                            Artistas: {bd["Theater"][i].cartel}
                            Precio para butaca General: {bd["Theater"][i].gen_price}
                            Precio para butaca VIP: {bd["Theater"][i].vip_price}
                            Fecha del evento: {bd["Theater"][i].date}''')

    return
    