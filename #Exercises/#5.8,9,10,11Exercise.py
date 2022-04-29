#Exercise 5.8
usernames=['Admin','Prazwal','Stark','Neo','John']
for names in usernames:
    if names.lower()=='admin':
        print('**Hello! '+ names + '**\nWould you like to see a status report?')
    else:
        print('**Hello! '+ names + '**\nThank YOu for loging in again.')



#Exercise 5.9
print('\n\n\n')
usernames=[]
if usernames:
    for names in usernames:
        print('Welcome! '+ names)
else:
    print('We need to find some users!')

#Exercise 5.10
print('\n\n\n')
current_users=['Mbappe','Lazano','Neymar','Pedri','Coutinho']
current_user=[]
for users in current_users:
    current_user.append(users.lower())
new_users=['Messi','Salah','NeYmar','MANE','CouTinHo']
for users in new_users:
    if users.lower() in current_user:
        print(users + ' is already used. Try other names!')
    else:
        print(users + ' is avaible!')

#Exercise 5.11
print('\n\n\n')
num=[value for value in range(1,10)]
for numbers in num:
    if numbers == 1:
        print('1st')
    elif numbers == 2:
        print('2nd')
    elif numbers == 3:
        print('3rd')
    else:
        print(str(numbers) +'th')