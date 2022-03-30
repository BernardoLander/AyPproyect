class Client():
    def __init__(self, name, dni, age,) -> None:
        self.name = name
        self.dni = dni
        self.age = age
        self.event = []
        self.tickets = 0
        self.spots = []
        self.vip = False
        self.discount = False
        self.discountfood = False
        self.payed = 0
        self.payedfood = 0
        self.food = []