from mod1.utilsm1 import num_verify, num_verify_range, verify_str
from mod1.Event_Methods import event_visualizer


def client_create(client_db, event_db):
    print("Por favor llene sus datos de manera acorde")

    name = verify_str("Ingrese su nombre")
    dni = num_verify("Ingrese su cedula")
    age = num_verify_range(1,120,"Ingrese su edad")

    event_visualizer(event_db)
    eventop = num_verify_range(1,len(event_db))

    event = event_db[eventop]

    tickets = ticket_buy(event_db, eventop)

def ticket_buy(event_db, eventop):

    print(f'''El Evento: {event_db[eventop].title}
    tiene disponibles{event_db[eventop].layout}
    Con un precio de:
    Butaca General: {event_db[eventop].gen_price}
    Butaca VIP: {event_db[eventop].vip_price}''')

    op = num_verify_range(1,2,'''Pulse 1. para comprar en butacas VIP
    Pulse 2. para butacas GENERAL''')
    tickets = num_verify_range(1,event_db[eventop)