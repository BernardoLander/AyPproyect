from cargaydescarga import *
from mod1.Event_Methods import event_search, url_database_get_and_load_Events
from mod1.utilsm1 import get_list_cute, num_verify_range, yes_no
from mod2.Ticket_Methods import client_create, client_search_in_db, make_bill_event, ticket_buy, event_select
from mod3.FoodFair_Methods import url_database_get_and_load_FoodFair, food_fair_vizualizer, product_search_manager
from mod4.FoodSell_Methods import product_search_client, make_bill_food
from mod5.Statitistics_Methods import client_average_spending, client_percentage_nobuyfood, loyal_clients, top_events, best_food




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

    op = num_verify_range( 1, 5,'''Para ingresar a un modulo marque el numero:
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

        make_bill_event(client_db)

        cargar_datos_en_txt("Clientdb.txt", client_db)
    
    elif op == 3:
        #Food Fair Manager
        food_fair_vizualizer(food_db)

        product_search_manager(food_db)

        cargar_datos_en_txt("FoodFair.txt", food_db)
        
    
    elif op == 4:
        #Food fair buy/ client create
        if yes_no("Ya tiene un Usuario creado en la Base de Datos?"):
            client_index = client_search_in_db(client_db)
        else:
            client_create(client_db)
            client_index = -1

        product_search_client(food_db, client_db, client_index)
        make_bill_food(client_db, client_index)
        cargar_datos_en_txt("Clientdb.txt", client_db)

    else:
        #Statistics
        print(f''' ESTADISTICAS:
        PROMEDIO DE GASTO: {client_average_spending(client_db)}
        PORCENTAJE DE CLIENTES QUE NO COMPRAN COMIDA: {client_percentage_nobuyfood(client_db)}
        CLIENTES MAS LEALES: {get_list_cute(loyal_clients(client_db, []))}
        TOP 3 EVENTOS CON MAS INGRESOS {get_list_cute(top_events(event_db, []))}
        TOP 5 PRODUCTOS MAS VENDIDOS EN LA FERIA DE COMIDA: {get_list_cute(best_food(food_db, []))}
        ''')

main()
