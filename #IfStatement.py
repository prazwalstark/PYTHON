#In this segement we will learn IF Statement in Python!!
team=['messi','pedri','gavi','foden','fati','torres']
for players in team:
    if players == 'messi':
        print(players.upper()+' is the best player in the world.')
    else:
        print(players.title())