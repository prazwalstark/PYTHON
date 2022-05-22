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