'''
Weight  ---less
Value   ---Maximum

1. Calculate the value per unit weight of all the items.
2. Select the items which has more V/W ratio greedily.

'''
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value/weight

def frac_knapsack(items, capacity):
    items.sort(key=lambda x:x.ratio, reverse = True)
    used_capacity = 0
    value = 0
    for i in items:
        if used_capacity + i.weight <= capacity:
            used_capacity += i.weight
            value += i.value
        else:
            unused_capacity = capacity - used_capacity
            value += i.ratio * unused_capacity
            used_capacity += unused_capacity
            print(value)
            return 
        
item1 = Item(100,20)
item2 = Item(120, 30)
item3 = Item(60, 10)
my_list = [item1, item2, item3]
frac_knapsack(my_list, 50)