from Event_Classes import *

def cargar_objetos(bd):
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