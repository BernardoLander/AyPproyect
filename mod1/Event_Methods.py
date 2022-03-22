from Event_Classes import *

def load_objects(bd):
    '''For loading objects (diferent types of events) from api or text file'''

    newdb = {
        "Musical":[],
        "Theater":[]
    }

    for i in range(len(bd)):

        for key, value in bd[i].items():

            if bd[i]["type"] == 1:
                
                newMusical = Musical(bd[i]["title"], bd[i]["type"], bd[i]["cartel"],bd[i]["layout"], bd[i]["prices"][0], bd[i]["prices"][1], bd[i]["date"], bd[i]["bands"])
                newdb["Musical"].append(newMusical)

            elif key["type"] == 2:

                newTheater = Theater(bd[i]["title"], bd[i]["type"], bd[i]["cartel"],bd[i]["layout"], bd[i]["prices"][0], bd[i]["prices"][1], bd[i]["date"], bd[i]["synopsys"])
                newdb["Theater"].append(newTheater)
    
    return newdb



def Event_visualizer(bd):
    
    for i in range(len(bd["Musical"])):

        print (f''' Titulo: {bd["Musical"][i].title}
                    Cantidad de Artistas: {bd["Musical"][i].bands}
                    Artistas: {bd["Musical"][i].cartel}
                    Precio para butaca General: {bd["Musical"][i].gen_price}
                    Precio para butaca VIP: {bd["Musical"][i].vip_price}
                    Fecha del evento: {bd["Musical"][i].date}''')

    for i in range(len(bd["Theater"])):

                print (f''' Titulo: {bd["Theater"][i].title}
                    Synopsys: {bd["Theater"][i].bands}
                    Artistas: {bd["Theater"][i].cartel}
                    Precio para butaca General: {bd["Theater"][i].gen_price}
                    Precio para butaca VIP: {bd["Theater"][i].vip_price}
                    Fecha del evento: {bd["Theater"][i].date}''')

    return
    