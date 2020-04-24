class Valuables:
    def __init__(self, name, value, amount, units):
        self.name = name
        self.value = value
        self.amount = amount
        self.units = units
    def convert_amount_to_grams(self):
        if self.units == 'kg':
            return self.amount * 1000
        elif self.units == 'lb':
            return self.amount * 453.592
        elif self.units == 'g':
            return self.amount

    def get_name(self):
        return self.name 

    def get_value(self):
        return self.value

    def get_amount(self):
        return self.convert_amount_to_grams()
    
    def get_units(self):
        return 'all weights are processed in grams original units were ' + str(self.units)
    
    def set_amount_left(self, taken):
        self.amount = self.amount - taken

def build_raid(items, item_value, amount_found, units):
    steal = []
    for i in range(len(items)):
        steal.append(Valuables(name=items[i], 
                            value=item_value[i], 
                            amount=amount_found[i], 
                            units=units[i]))
    return steal

def greedy(steal, MaxCapacity):
    sorted_items = sorted(steal, key = Valuables.get_value(), reversed=True)

    hull = []
    total_value = 0.0
    for i in range(len(sorted_items)):


items = ['gold', 'silver', 'raisins']
values = [53.27,0.49,0.01]
amount = [2, 5000, 15] 
units = ['kg', 'g', 'lb']

steal_items = build_raid(items, values, amount, units)



print(steal_items[0].get_units())