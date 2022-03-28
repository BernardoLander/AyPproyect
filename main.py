from mod1.Event_Methods import *
from mod1.Event_Classes import *
from mod1.utilsm1 import *
from mod1.cargaydescarga import *
from mod2.Ticket_Methods import *




def main():

    event_db = recibir_datos_del_txt("Eventdb.txt",event_db)
    if event_db is None:
        event_db = url_database_get_and_load_Events()
    
    client_db = recibir_datos_del_txt("Clientdb.txt", client_db)
    if client_db is None:
        client_db = []

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
    elif op == 2:
        #Event Client Creation and buy
        eventop = client_create(client_db, event_db)
        ticket_buy(client_db, event_db, eventop)
        make_bill(client_db)
    
    elif op == 3:
        #Food Fair Manager
        pass

main()
