


class inventory():
    def __init__(self, name, price, amount, type):
        self.name = name
        self.price = price
        self.amount = amount
        self.type = type
        

class drink(inventory):
    def __init__(self, name, price, amount, type, size):
        super().__init__(name, price, amount, type)
        self.size = size


class food(inventory):
    def __init__(self, name, price, amount, type, presentation):
        super().__init__(name, price, amount, type)

        if presentation == 1:
            presentation_text = "Preparado"
        elif presentation == 2:
            presentation_text = "Empacado"

        self.presentation = presentation_text
