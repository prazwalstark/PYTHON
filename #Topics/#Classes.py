#Classes basically include the information about group of instances.object
#While Objects are simply the representation of indivual 
# for example Dog is a class and Dog named 'CR7' is an instance or object of class
class Car():
    '''A simple attempt to represent a car.'''
    def __init__(self,make,model,year):
        '''Initialize attributes to describe a car.'''
        self.make = make
        self.model= model
        self.year= year
        self.odometer_reading=0
    
    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name.'''
        long_name = str(self.year)+' '+self.make +' ' +self.model
        return long_name.title()
    
    def read_odometer(self):
        '''Print a statement showing the car's mileage.'''
        print('This car has '+ str(self.odometer_reading)+' miles on it.')
    
    def update_odometer(self,mileage):
        ''' 
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        '''
        if self.odometer_reading == 0:
            self.odometer_reading = mileage
        if mileage> self.odometer_reading:
            self.odometer_reading = mileage
            print('You cant roll back an odometer!')
    def increment_odometer(self,miles):
        '''Add the given amount to the odometer reading.'''
        self.odometer_reading +=miles

my_new_car= Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

my_used_car= Car('subaru','outback',2013)
print(my_used_car.get_descriptive_name())
mileage=3400
my_used_car.update_odometer(mileage)
my_used_car.increment_odometer(1000)
my_used_car.update_odometer(mileage)
my_used_car.read_odometer()

#Inheritance and class
#Inheritance allows the user to extract the attributes from a class and pass it on to a new class
#Basically, the newly created class is called sub class or child class while the class from which data is
#extracted is called parent or super class.
#Inheritance is useful when the users need of methods is already in another class. In such case the user can extract the methods from super class.
#Also, the user can also add new attributes to the child or sub class.