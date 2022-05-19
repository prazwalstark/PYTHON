# We can input info from user by using input() function
# Similarly, int() can be used along with input() to enter integer value from the user.
#while loop can also be used in place of for loop and its syntax is:
#while condition:
#statements
#We can use flag idea to end the loop or programs at various parts.
#Similarly, break can be used to exit a loop!
#continue is used for leaving for statments to be executed in a loop and moving to the loop part.
#Example
#Start with users that need to be verified 
#and an emptylist to hold confirmed users. 
unconfirmed_users= ['alice','briani','candace']
confirmed_users=[]
#Verify each user until there are no more unconfirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: "+ current_user.title())
    confirmed_users.append(current_user)
print('\nThe following users have beem confirmed:\n')
for users in confirmed_users:
    print(users)
#Filling a Dictionary with User Input 
#For an Instance in this program we will ask user to input there name and which mountain would they like to climb.
responses={}
Res=True
while Res:
    name= input('What is your name?')
    response = input('Which mountain would you like to climb?')
    responses[name] = response
    Question=  input('Would like other people to take the poll as well?(Y/N)')
    if Question == 'N':
        Res = False
print('----The Result of the pole----')
for name,response in responses.items():
    print(name +' would like to climb '+ response +'.')

