def make_pizza(size,*toppings):
    '''Making a Pizza'''
    print('Making a '+ str(size) + '-inch pizza with the following toppings.' )
    for topping in toppings:
        print('-' + topping)