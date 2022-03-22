from Event_Classes import *
from utilsm1 import *
from Event_Methods import *



def Event_Manager():

    '''Event manager main'''
    option = num_verify(1,4,'''Bienvenido a la interfaz de Manejo de Eventos:
                        1. Para vizualizar los diferentes eventos disponibles presione.
                        2. Para abrir o cerrar la venta de tickets
                        3. Para buscar eventos por filtro''')

    if option == 1:
      pass  
    #1.ver eventos

    elif option == 2:
    #abrir o cerrar venta de tickets
        pass
    elif option == 3:
    #3.buscar eventos por filtro: Tipo, fecha, actor o Cantante, Nombre del evento
        pass

    else:

        pass
    #Salir del manejador de eventos