from admin_1 import User
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