class Event():

    '''Object blueprint for data base'''

    def __init__(self, title, type, cartel, layout, gen_price, vip_price, date):
        self.title = title
        self.type = type
        self.cartel = cartel
        self.layout = layout
        self.gen_price = gen_price
        self.vip_price = vip_price
        self.date = date



class Musical(Event):

    '''Musical event same as normal event but with bands added'''

    def __init__(self, title, type, cartel, layout, gen_price, vip_price, date, bands):
        super().__init__(title, type, cartel, layout, gen_price, vip_price, date)
        
        self.bands = bands



class Theater(Event):

    '''Theater event same as normal event but with synopsis of play added'''

    def __init__(self, title, type, cartel, layout, gen_price, vip_price, date, synopsys):
        super().__init__(title, type, cartel, layout, gen_price, vip_price, date)

        self.synopsys = synopsys