from mod1.utilsm1 import *
from mod1.m1main import event_managerm1
from mod1.Event_Methods import url_database_get_and_load_Events



def main():
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
        eventdb = event_managerm1(eventdb)
main()
