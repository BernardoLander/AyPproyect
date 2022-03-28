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

    newdb = []

    for i in range(len(bd)):
        if bd[i]["type"] == 1:

            newMusical = Musical(bd[i]["title"], bd[i]["type"], bd[i]["cartel"],bd[i]["layout"], bd[i]["prices"][0], bd[i]["prices"][1], bd[i]["date"], bd[i]["bands"])
            newdb.append(newMusical)

        elif bd[i]["type"] == 2:

            newTheater = Theater(bd[i]["title"], bd[i]["type"], bd[i]["cartel"],bd[i]["layout"], bd[i]["prices"][0], bd[i]["prices"][1], bd[i]["date"], bd[i]["synopsis"])
            newdb.append(newTheater)
    
    return newdb



def event_visualizer(bd):

    '''Visualizer of database in formatted strings'''
    for i in range(len(bd)):
        if bd[i].type == 1:
            print (f'''Evento de Tipo Musical
Evento numero: {i + 1}
Titulo: {bd[i].title}
Cantidad de Artistas: {bd[i].bands}
Artistas: {get_list_cute(bd[i].cartel)}
Precio para butaca General: {bd[i].gen_price}
Precio para butaca VIP: {bd[i].vip_price}
Fecha del evento: {bd[i].date}''')
            if bd[i].is_selling:
                print("La venta de tickets de este evento esta abierta\n")
            else:
                print("La venta de tickets de este evento esta cerrada\n")

        elif bd[i].type == 2:
            print (f'''Evento de Tipo Teatro
Evento numero: {i + 1}
Titulo: {bd["Theater"][i].title}
Synopsys: {bd["Theater"][i].synopsys}
Artistas: {get_list_cute(bd["Theater"][i].cartel)}
Precio para butaca General: {bd["Theater"][i].gen_price}
Precio para butaca VIP: {bd["Theater"][i].vip_price}
Fecha del evento: {bd["Theater"][i].date}''')

            if bd[i].is_selling:
                print("La venta de tickets de este evento esta abierta\n")
            else:
                print("La venta de tickets de este evento esta cerrada\n")

    return
    

def event_openclose(db):

    
        event_op = num_verify(1,len(db),'''Indique por favor el numero del evento musical el cual quiere seleccionar''')

        if db[event_op-1].is_selling:
            db[event_op-1].is_selling = False
            print(f'''Cerrada la venta de tickets para el evento numero {event_op} 
                    titulo:{db[event_op].title}''')
         
        else:
            db[event_op-1].is_selling = True
            print(f'''Abierta la venta de tickets para el evento numero {event_op} 
                    titulo:{db[event_op].title}''')



def event_search(db):
    '''Shows events by attributes'''

    op = num_verify(1,4,'''Indique que atributo de los eventos quiere usar para buscarlo:
    1. Para buscar por tipo
    2. Para buscar por Fecha
    3. Para buscar por Actor o Cantante en el Cartel
    4. Para buscar por el nombre del evento
    ''')

    if op == 1:
        #Por type
        print ("Organizaodo por tipo")
        auxdb = []
        for i in range(len(db)):
            auxdb.append(db[i].type)

        auxdb = sorted(auxdb)

        for i in range(len(db)):
        
            for j in range(len(db)):

                if db[j].type == auxdb[i]:

                    db[j], db[i] = db[i], db[j]

        event_visualizer(db)

        boolop =  yes_no('''Desea modificar la venta de tickets de algun evento?
            Y/N''')
        if boolop:
            event_openclose(db)

    elif op == 2:
      #Por Fecha
        print("Organizado por fecha")
        auxdb = []
        for i in range(len(db)):
                auxdb.append(db[i].date.replace("-",""))
        
        auxdb = sorted(auxdb)
       
        for i in range(len(db)):
            for j in range(len(db)):

                if db[j].date.replace("-","") == auxdb[i]:
                    db[j], db[i] = db[i], db[j]
        
        event_visualizer(db)

        boolop =  yes_no('''Desea modificar la venta de tickets de algun evento?
        Y/N''')

        if boolop:
            event_openclose(db)
    
    elif op == 3:
        #Por actor o Cartel
        #broken
        print("Seccion en mantenimiento")
        pass
    else:
        #Por titulo
        print("Organizado por Titulo")

        auxdb = []

        for i in range(len(db)):

            auxdb.append(db[i].title.replace(" ",""))


        auxdb = sorted(auxdb)

        for i in range(len(db)):
                
            for j in range(len(db)):

                if db[j].title.replace(" ","") == auxdb[i]:
                    db[j], db[i] = db[i], db[j]

        event_visualizer(db)

        boolop =  yes_no('''Desea modificar la venta de tickets de algun evento?
        Y/N''')

        if boolop:
            event_openclose(db)
    
    return db