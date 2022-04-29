#In this segement we will learn IF Statement in Python!!
team=['Messi','pedri','gavi','foden','fati','torres']
for players in team:
    if players.lower() == 'messi':
        print(players.upper()+' is the best player in the world.')
    else:
        print(players.title())
#'==' is to check whether both the values are same or not while
#'!=' is to check if both values aren't equal.
#Numerical Comparisons has operators '>=' '<=' '<' '>' 
#Multpiple conditions can be checked by 'and' 'or' opearators
if 'Messi' or 'Fati' in team:
    print('God is here to save us.')
else:
    print('We are doomed')
#PEP8 : 'age == 4:' statement is better than 'age==4:'


