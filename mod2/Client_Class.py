class Client():
    def __init__(self, name, dni, age,) -> None:
        self.name = name
        self.dni = dni
        self.age = age
        self.event = None
        self.tickets = 0
        self.spots = []
        self.vip = False
        self.discount = False
        self.payed = 0
        self.food = []