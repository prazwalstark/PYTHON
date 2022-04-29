players={'Messi' : 10,'Neymar' : 11, 'Mbappe':7,'Pedri':8,'Coutinhno':14,'Inestia':4}
#del players['Messi']
#print(players['Messi'])
#print(players)
for player,num in players.items():
    print(player +' wears Jersey No. ' +str(num))
    if num == 10:
        print('He is the GOAT of football.\n\n')


goat = ['Messi','XAVI']
for player in sorted(players.keys()):#use .values() to access values stored in keys only!
    print(player)
    if player in goat:
        print('Legendary Player!')


#we can use set() like sorted which makes a set of values without repeatation of values
#Nesting