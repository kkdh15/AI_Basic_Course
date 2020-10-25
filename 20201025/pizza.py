#module
def make_pizza(size, *toppings):
    print("pizza size : {} inch".format(size))
    for topping in toppings:
        print(f"{topping}", end=' ')
    print()

def get_pizza_name():
    print('abcd pizza')

if __name__ == '__main__':
    make_pizza(18, 'peperoni', 'orion', 'potato', 'cheese')