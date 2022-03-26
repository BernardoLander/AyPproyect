import requests
import json
from Event_Classes import *
from Event_Methods import *
from utilsm1 import *

def main():

    bd = url_database_get_and_load()
    print_list_cute
    print("Eventos Musicales:\n")

    for i in range(len(bd["Musical"])):

        print (f''' Evento numero: {i + 1}
                    Titulo: {bd["Musical"][i].title}
                    Cantidad de Artistas: {print_list_cute(bd["Musical"][i].bands)}
                    Artistas: {bd["Musical"][i].cartel}
                    Precio para butaca General: {bd["Musical"][i].gen_price}$
                    Precio para butaca VIP: {bd["Musical"][i].vip_price}$
                    Fecha del evento: {bd["Musical"][i].date}''')

    print("Eventos de Teatro:\n")

    for i in range(len(bd["Theater"])):

                print (f''' Evento numero: {i}
                            Titulo: {bd["Theater"][i].title}
                            Sinopsys: {bd["Theater"][i].synopsys}
                            Artistas: {print_list_cute(bd["Theater"][i].cartel)}
                            Precio para butaca General: {bd["Theater"][i].gen_price}$
                            Precio para butaca VIP: {bd["Theater"][i].vip_price}$
                            Fecha del evento: {bd["Theater"][i].date}''')

main()