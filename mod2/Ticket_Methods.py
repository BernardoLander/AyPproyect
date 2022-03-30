from Tickets_Classes import Client
from mod1.utilsm1 import get_list_cute, num_verify, num_verify_range, verify_str, verify_str_num, yes_no
from mod1.Event_Methods import event_visualizer
from string import ascii_uppercase


def client_create(client_db):
    '''Create client'''
    print("Por favor llene sus datos de manera acorde")

    name = verify_str("Ingrese su nombre")
    dni = num_verify("Ingrese su cedula")
    age = num_verify_range(1,120,"Ingrese su edad")
    client_db.append(Client(name, dni, age))
    return


def event_select(event_db, client_db, client_index = -1):
    '''With index in clientdb client selects event'''

    event_visualizer(event_db)
    eventop = num_verify_range(1,len(event_db), "Ingrese el Numero del evento donde desea realizar una compra")
    eventop = eventop - 1
    if event_db[eventop].is_selling:

        client_db[client_index].event = event_db[eventop]
            
        return eventop

    else:
        print("El evento no esta aceptando compras Intente comprar en otro evento")
        return event_select(client_db, event_db, client_index)
        



def ticket_buy(client_db, event_db, eventop, client_index):
    '''Select spot type and show spots to buy tickets'''


    print(f'''El Evento: {event_db[eventop].title}
    Precio General en bruto:  {event_db[eventop].gen_price}
    Precio VIP en bruto: {event_db[eventop].vip_price}''')

    op = num_verify_range(1,2,'''Pulse 1. para comprar en butacas VIP
    Pulse 2. para butacas GENERAL''')

    if op == 1:

        tickets = num_verify_range( 1, event_db[eventop].vipqty,"Ingrese la cantidad de Tickets que desea comprar")

        layout_show(event_db, eventop, 1)

        for i in range(tickets):

            spot = verify_str_num(2,"Por favor ingrese el Codigo Alfanumerico de la butaca que desea comprar")

            reserve_spot(spot, event_db[eventop], 1)
            event_db[eventop].vipqty = event_db[eventop].vipqty - 1
            client_db[client_index].spots.append(spot + "VIP")

            print("Proximo ticket")

        client_db[client_index].vip = True

            
    else:

        tickets = num_verify_range( 1, event_db[eventop].genqty,"Ingrese la cantidad de Tickets que desea comprar")

        layout_show(event_db, eventop, 2)

        for i in range(tickets):

            spot = verify_str_num(2,"Por favor ingrese el Codigo Alfanumerico de la butaca que desea comprar")

            reserve_spot(spot, event_db[eventop], 2)
            client_db[client_index].spots.append(spot)
            event_db[eventop].genqty = event_db[eventop].genqty - 1
            print("Proximo ticket")
    
    return
            



def layout_show(event_db, eventop,op):
    '''To show layout of selected group'''

    if op == 2:
        if len(event_db[eventop].layoutgen) > 0:
            layout = event_db[eventop].layout["general"]
            layoutgen = []
            for i in range(layout[0]):
                for j in range(layout[1]):
                    spot = ascii_uppercase[i] + str(j + 1) + " | "
                    layoutgen.append(spot)

                layoutgen.append("\n")

            event_db[eventop].layoutgen = layoutgen

        for i in range(len(layoutgen)):
            print (layoutgen[i])
        return
    
    else:
        if len(event_db[eventop].layoutvip) > 0:
            layout = event_db[eventop].layout["vip"]
            layoutvip = []
            for i in range(layout[0]):
                for j in range(layout[1]):
                    spot = ascii_uppercase[i] + str(j + 1) + " | "
                    layoutvip.append(spot)

                layoutvip.append("\n")

            event_db[eventop].layoutvip = layoutvip

        for i in range(len(event_db[eventop].layoutvip)):
            print (event_db[eventop].layoutvip)
        return



def reserve_spot (spot, event, op):
    '''Reserves spot on event layout'''

    if op == 1:
        aux = 0
        for i in range(len(event.layoutvip)):

            if event.layoutvip[i] == spot:

                event.layoutvip[i] = "X"

                aux += 1
        
        if aux == 1:
            print("Reservado con exito")
            return
        else:
            print("Error puesto invalido")
            spot = verify_str_num(2,"Por favor ingrese el Codigo Alfanumerico de la butaca que desea comprar")
            reserve_spot(spot, event, op)

    else:

        aux = 0
        for i in range(len(event.layoutgen)):
            if event.layoutgen[i] == spot:
                event.layoutgen[i] = "OCC"
                aux += 1
        
        if aux == 1:
            print("Reservado con exito")
            return
        else:
            print("Error puesto invalido")
            spot = verify_str_num(2,"Por favor ingrese el Codigo Alfanumerico de la butaca que desea comprar")
            reserve_spot(spot, event, op)


            
            
def make_bill(client_db, client_index = -1):
    '''Makes bill from client obj'''
    customer = client_db[client_index]
    print(f''' FACTURA
    
    NOMBRE: {customer.name}
    CEDULA: {customer.dni}
    EDAD: {customer.age}
    EVENTO: {customer.event.title}
    PUESTOS:{get_list_cute(customer.spots)}''')

    if customer.vip:

        total = customer.event.vip_price * len(customer.spots) + customer.event.vip_price * len(customer.spots)*0.16
        print(f'''PRECIO POR PUESTO VIP: {customer.event.vip_price}
        PRECIO CON IVA DE ENTRADA: {customer.event.vip_price + customer.event.vip_price*0.16}
        PRECIO TOTAL A PAGAR: {total}
        ''')

        if customer.discount:
            total = customer.event.vip_price * len(customer.spots) - customer.event.vip_price * len(customer.spots)*0.50 + customer.event.vip_price * len(customer.spots)*0.16
            print (f'''SE APLICA DESCUENTO PARA TOTAL DE: {total}''')
        customer.payed = total
    
    else:

        total = customer.event.gen_price * len(customer.spots) + customer.event.gen_price * len(customer.spots)*0.16 
        print(f'''PRECIO POR PUESTO GENERAL: {customer.event.gen_price}
        PRECIO CON IVA DE ENTRADA: {customer.event.gen_price + customer.event.gen_price*0.16}
        PRECIO TOTAL A PAGAR: {customer.event.gen_price * len(customer.spots) + customer.event.gen_price * len(customer.spots)*0.16}
        ''')

        if customer.discount:
            total = customer.event.gen_price * len(customer.spots) - customer.event.gen_price * len(customer.spots)*0.50 + customer.event.gen_price * len(customer.spots)*0.16
            print (f'''SE APLICA DESCUENTO PARA TOTAL DE: {total}''')

        customer.payed = total


def client_search_in_db(client_db):

    client_dni = num_verify("Ingrese su Cedula:")
    for i in range(len(client_db)):
        if client_dni == client_db[i].dni:
            return i
    print("Su cedula no esta en la base de datos por favor cree un perfil")
    return

