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
#Nesting or List of Dictionaries
alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

#making an empty list for storing alien.
aliens=[]
#Making 30 green aliens:
alien={'color':'green','points':15,'speed':'slow'}
for a in range(30):
    aliens.append(alien)
#show the first 5 aliens:
for aliens_created in aliens[:5]:
    print(aliens_created)
print("...\n\n")
print('Total number of aliens:' + str(len(aliens)))

