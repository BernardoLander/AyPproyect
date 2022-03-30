from mod1.Event_Methods import event_search, url_database_get_and_load_Events
from mod1.utilsm1 import num_verify, num_verify_range, yes_no, verify_str_num
from cargaydescarga import *
from mod2.Ticket_Methods import client_create, client_search_in_db, make_bill, ticket_buy, event_select
from mod3.FoodFair_Methods import *




def main():

    event_db = recibir_datos_del_txt("Eventdb.txt",event_db)
    if event_db is None:
        event_db = url_database_get_and_load_Events()
    
    client_db = recibir_datos_del_txt("Clientdb.txt", client_db)
    if client_db is None:
        client_db = []
    
    food_db = recibir_datos_del_txt("Food.txt", food_db)
    if food_db is None:
        client_db = url_database_get_and_load_FoodFair()

    print("BIENVENIDO AL PROGRAMA DE GESTION DEL SAMAN SHOW")

    op = num_verify( 1, 5,'''Para ingresar a un modulo marque el numero:
    1. Gestion de eventos
    2. Venta de Tickets
    3. Gestion de Feria de Comida
    4. Venta de Feria de Comida
    5. Estadisticas'''
    )

    if op == 1:
        #Event Manager
        event_db = event_search(event_db)

        cargar_datos_en_txt("Eventdb.txt",event_db)

    elif op == 2:
        #Event Client Creation and buy
        if yes_no("Ya tiene un Usuario creado en la Base de Datos?"):
            client_index = client_search_in_db(client_db)
        else:
            client_create(client_db)
            client_index = -1

        eventop = event_select(event_db, client_db, client_index)

        ticket_buy(client_db, event_db, eventop)

        make_bill(client_db)

        cargar_datos_en_txt("Clientdb.txt", client_db)
    
    elif op == 3:
        #Food Fair Manager
        food_fair_vizualizer(food_db)

        product_search_manager(food_db)
    
    elif op == 4:
        #Food fair buy/ client create
        if yes_no("Ya tiene un Usuario creado en la Base de Datos?"):
            client_index = client_search_in_db(client_db)
        else:
            client_create(client_db)
            client_index = -1
        
        
    else:
        #Stadistics
        pass

main()
