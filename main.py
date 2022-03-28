from mod1.Event_Methods import *
from mod1.Event_Classes import *
from mod1.utilsm1 import *
from mod1.cargaydescarga import *

def main():

    eventdb = recibir_datos_del_txt("Eventdb.txt",eventdb)
    if eventdb is None:
        eventdb = url_database_get_and_load_Events()

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
        eventdb = event_search(eventdb)
    elif op == 2:
        pass
main()
