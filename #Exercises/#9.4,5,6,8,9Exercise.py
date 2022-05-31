#Exercise 9.4
class Restaurant():

    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name= restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served=20000
    def describe_restaurant(self):
        print(self.restaurant_name.title() + ' cooks '+ self.cuisine_type.title() +'.')
    def open_restaurant(self):
        print(self.restaurant_name.title()+'is Open!')
    def set_number_served(self,serves):
        self.number_served += serves
        print('The Total Serves made are: '+ str(self.number_served))
restaurant1 = Restaurant('A Cafe Restaurant','Chinese Cuisine')
print(restaurant1.restaurant_name.title())
print(restaurant1.cuisine_type.title())
print('\n\n')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant1.set_number_served(200)

#Exercise 9.5
class User():
    def __init__(self,first_name,last_name,address,email,phone_number):
        self.first_name= first_name
        self.last_name = last_name
        self.address= address
        self.email= email
        self.phone_number = phone_number
        self.login_attempts=0
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
    def describe_user(self):
        print("\n\nUser's information:\n")
        print('First Name: '+ self.first_name.title())
        print('Last Name: '+ self.last_name.title())
        print('Address: '+ self.address)
        print('Phone NO: '+ self.phone_number)
        print('Email: '+self.email.lower())
    def greet_user(self):
        print('Hello! '+ self.first_name.title() + ' ' + self.last_name+ ', Thank You For Participating in Our Survey')
    def login_attempt(self):
        print('The total login attempts made by you are: '+ str(self.login_attempts))
person1= User('Prazwal D.','Stark','Pulchowk, Nepal','prazwaldstark@gmail.com','9845632882')
person1.describe_user()
person1.greet_user()
for i in range(1,5):
    person1.increment_login_attempts()
person1.login_attempt()
person1.reset_login_attempts()
person1.login_attempt()

#Exercise 9.6
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors=[]
    def icecream_flavors(self):
        self.flavors=['Chocolate','Vanilla',"Strawberry",'Mix-Fruit']
        print('The Flavors of Ice-Cream available in this restaurant are:')
        for flavor in self.flavors:
            print('-'+flavor)
icecreamstand1= IceCreamStand('Bagelarium & STG Gelateria Broken Arrow','Desert')
print(icecreamstand1.restaurant_name.title())
print(icecreamstand1.cuisine_type.title())
icecreamstand1.icecream_flavors()

#Exercise 9.8
class Admin(User):
    def __init__(self,first_name,last_name,address, email,phone_number,Privilege):
        super().__init__(first_name,last_name,address, email,phone_number)
        self.Privilege = Privileges(Privilege)
class Privileges():
    def __init__(self,Privilegee):
        self.Privilegee= Privilegee
    def show_privileges(self):
        print('The administrative privilege of user are:\n')
        for privilege in self.Privilegee:
            print('-'+privilege)
prazwal = Admin('Prazwal','D. Stark','Pulchowk','prazwaldstark@gmail.com','9845632882',Privilege=['can add post','can delete post','can ban user'])
prazwal.Privilege.show_privileges()

#Exercies 9.9
"""A set of classes that can be used to represent electric cars."""

from car import Car 

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")  
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85
        
class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year,battery):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery(battery)

car1= ElectricCar('Tesla','Model S','2016',60)
car1.battery.get_range()
print('Upgrading...')
car1.battery.upgrade_battery()
car1.battery.get_range()

#For exercise 9.10 I have created two python files 
#restaurant_1 and restaurant_2 
#all the exercise related stuffs are written well there!
#Go Check It out
#As for exercise 9.11,12 I have done similar to what I did before and stored codes in admin_1,admin_2 and admini_3 