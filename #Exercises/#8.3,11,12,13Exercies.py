#Exercise 8.3
def shirt_print(size,message):
    print('You have selected "'+size+'" size of shirt. \n THe message to be printed is:')
    print('\n'+message)
shirt_print('Medium','Messi The GOAT')
print('\n\n')
shirt_print(message='Ronaldo is an Asshole',size='Large')

#Exercise 8.11
new_list=[]
def show_magicians(magicians):
    for magician in magicians:
        print('-'+magician)
def make_great(magicians):
    for magician in magicians:
        magician= 'The Great' + magician
        new_list.append(magician)
    return new_list

magicians=['Jonathan Todd','Michael Carbonaro','Chris Angel','Siegfried & Roy']
magicians = make_great(magicians)
show_magicians(magicians)

#Exercise 8.12
sandwiches=[]
def make_sandwich(sandwiches):
    print('\n\nThe items in your Sandwiche are: \n')
    for sandwich in sandwiches:
        print('-'+ sandwich)
def ask_customer():
    print('What would you want in you sandwich sir?')
    print('Note: Please, Enter the items followed by Enter key after each items and when finished press enter on blank line! ')
    while True:
        topping = input()
        if topping:
            sandwiches.append(topping)
        else:
            break
    return sandwiches
sandwiches = ask_customer()
make_sandwich(sandwiches)


#Exercise 8.13
import modulefor8
print(modulefor8.build_profile('Prazwal D.', 'Stark',Address= 'Kathmandu',Roll_No='55',Sec='BCT CD'))
from modulefor8 import build_profile
print(build_profile('Prazwal D.', 'Stark',Address= 'Kathmandu',Roll_No='55',Sec='BCT CD'))
from modulefor8 import build_profile as bp
print(bp('Prazwal D.', 'Stark',Address= 'Kathmandu',Roll_No='55',Sec='BCT CD'))
import modulefor8 as m8
print(m8.build_profile('Prazwal D.', 'Stark',Address= 'Kathmandu',Roll_No='55',Sec='BCT CD'))
from modulefor8 import *
print(build_profile('Prazwal D.', 'Stark',Address= 'Kathmandu',Roll_No='55',Sec='BCT CD'))




