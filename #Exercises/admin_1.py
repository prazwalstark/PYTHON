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