import json
import requests
from Event_Classes import *
from utilsm1 import *

def url_database_get_and_load_Events():

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
        if bd[i]["type"] == 1:

            newMusical = Musical(bd[i]["title"], bd[i]["type"], bd[i]["cartel"],bd[i]["layout"], bd[i]["prices"][0], bd[i]["prices"][1], bd[i]["date"], bd[i]["bands"])
            newdb["Musical"].append(newMusical)

        elif bd[i]["type"] == 2:

            newTheater = Theater(bd[i]["title"], bd[i]["type"], bd[i]["cartel"],bd[i]["layout"], bd[i]["prices"][0], bd[i]["prices"][1], bd[i]["date"], bd[i]["synopsis"])
            newdb["Theater"].append(newTheater)
    
    return newdb



def event_visualizer(bd):

    '''Visualizer of database in formatted strings'''

    print("EVENTOS DE MUSICA:\n")

    for i in range(len(bd["Musical"])):

        print (f''' Evento numero: {i + 1}
                    Titulo: {bd["Musical"][i].title}
                    Cantidad de Artistas: {bd["Musical"][i].bands}
                    Artistas: {get_list_cute(bd["Musical"][i].cartel)}
                    Precio para butaca General: {bd["Musical"][i].gen_price}
                    Precio para butaca VIP: {bd["Musical"][i].vip_price}
                    Fecha del evento: {bd["Musical"][i].date}''')
        if bd["Musical"][i].is_selling:
            print("La venta de tickets de este evento esta abierta\n")
        else:
            print("La venta de tickets de este evento esta cerrada\n")
    
    print("EVENTOS DE TEATRO:\n")

    for i in range(len(bd["Theater"])):

        print (f''' Evento numero: {i + 1}
                    Titulo: {bd["Theater"][i].title}
                    Synopsys: {bd["Theater"][i].synopsys}
                    Artistas: {get_list_cute(bd["Theater"][i].cartel)}
                    Precio para butaca General: {bd["Theater"][i].gen_price}
                    Precio para butaca VIP: {bd["Theater"][i].vip_price}
                    Fecha del evento: {bd["Theater"][i].date}''')

        if bd["Theater"][i].is_selling:
            print("La venta de tickets de este evento esta abierta\n")
        else:
            print("La venta de tickets de este evento esta cerrada\n")

    return
    

def event_openclose(db):

    op = num_verify(1,2,'''Presione:
    1. Para trabajar en eventos Musicales
    2. Para trabajar en eventos teatrales
    ''')

    if op == 1:
        event_op = num_verify(1,len(db["Musical"]),'''Indique por favor el numero del evento musical el cual quiere seleccionar''')

        if db["Musical"][event_op-1].is_selling:
            db["Musical"][event_op-1].is_selling = False
            print(f'''Cerrada la venta de tickets para el evento numero {event_op} 
                    titulo:{db["Musical"][event_op].title}''')
         
        else:
            db["Musical"][event_op-1].is_selling = True
            print(f'''Abierta la venta de tickets para el evento numero {event_op} 
                    titulo:{db["Musical"][event_op].title}''')

    else:
        
        event_op = num_verify(1,len(db["Theater"]),'''Indique por favor el numero del evento musical el cual quiere seleccionar''')

        if db["Theater"][event_op-1].is_selling:
            db["Theater"][event_op-1].is_selling = False
            print(f'''Cerrada la venta de tickets para el evento numero {event_op} 
                    titulo:{db["Theater"][event_op].title}''')
         
        else:
            db["Theater"][event_op-1].is_selling = True
            print(f'''Abierta la venta de tickets para el evento numero {event_op} 
                    titulo:{db["Theater"][event_op].title}''')