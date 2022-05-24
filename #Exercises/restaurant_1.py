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