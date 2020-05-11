# Toy continuous knapsack problem

class Valuables:
    def __init__(self, name, value, amount, units):
        self.name = name
        self.value = value
        self.units = units
        self.amount = self.convert_amount_to_grams(amount)

    def convert_amount_to_grams(self, amount):
        if self.units == 'kg':
            return amount * 1000
        elif self.units == 'lb':
            return amount * 453.592
        elif self.units == 'g':
            return amount

    def get_name(self):
        return self.name 

    def get_value(self):
        return self.value

    def get_amount(self):
        return self.amount
    
    def get_units(self):
        return 'all weights are processed in grams original units were '\
             + str(self.units)
    
    def set_amount_left(self, taken):
        self.amount = self.amount - taken

def build_raid(items, item_value, amount_found, units):
    # initializes Valuables 
    # returns list of Valuables instances
    steal = []
    for i in range(len(items)):
        steal.append(Valuables(name=items[i], 
                            value=item_value[i], 
                            amount=amount_found[i], 
                            units=units[i]))
    return steal

def greedy(steal, max_capacity):
    # greedy routine 
    # returns tuple of list items taken by weight and total value
    sorted_items = sorted(steal, key = Valuables.get_value, reverse=True)

    hull = []
    total_value = 0.0
    capacity = max_capacity
    i = 0
    while capacity > 0:
        if sorted_items[i].get_amount() <= capacity:
            total_value += sorted_items[i].get_amount() * sorted_items[i].get_value()
            hull.append((sorted_items[i].get_name(), sorted_items[i].get_amount()))
            capacity -= sorted_items[i].get_amount()
        else:
            total_value += sorted_items[i].get_value() * capacity
            hull.append((sorted_items[i].get_name(), capacity))
            sorted_items[i].set_amount_left(capacity)
        
            capacity -= capacity
        i += 1
    
    return (hull, total_value)

def main():
    # list indicates which items are available to steel
    items = ['gold', 'silver', 'raisins', 'books']
    # value of items
    values = [53.27,0.49,0.01, 0.5]
    # how much (weight) of each item
    amount = [2, 5000, 15, 2] 
    # units of mass... 
    units = ['kg', 'g', 'lb', 'kg']

    # initalize instance that catalogs items available
    steal_items = build_raid(items, values, amount, units)

    # execute greedy routine to fill 
    # knapsack of specified max capacity
    print(greedy(steal=steal_items, max_capacity=5000))

#run
main()