#Functions in python are very important in order to avoid writing same piece of code repeatedly for many times as fuction can call a block of code at any part and execute so that user don't have to bother writing that same piece of code repeatedly!
# a simple piece of code is shown below!
def greet():
    '''This is Greeting Messsage'''
    print('Hey!Whats up')

greet()
#Explanation 
# line 3 has def statement to define a fuction named greet and() can be used to define the type of function
#4 has triple quotes for the purpose of Documentation of the function!
#5 has the message written with the help of print statement
#7 here the greet() function is being called and the statements within that function block are to be executed!
def greet(name):
    '''This is Greeting Messsage'''
    print('Hey!Whats up '+name.title())

greet('Prazwal')

def name(first_name, last_name, sex):
    '''Its got making an argument optional, Interesting huh!'''
    full_name= first_name +" "+ last_name
    if sex:
        print(full_name.title()+' has done sex '+ sex +' times.')
    else:
        print(full_name.title()+ ' hasnt done sex yet.')

name(first_name='Tony', last_name='Stark',sex='100')
name(first_name='Prazwal', last_name='Stark',sex='')
# It's just a program and please don't ger offended by the word 'sex', I am feeling a bit sleepy so I just used it huh.
# Returning a Dictionary

