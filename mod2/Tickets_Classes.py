class Client():
    def __init__(self, name, dni, age, event) -> None:
        self.name = name
        self.dni = dni
        self.age = age
        self.event = event
        self.tickets = 0
        self.spots = []
        self.vip = False
        self.discount = False
        self.payed = 0
        