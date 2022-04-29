#Exercise 6.8
cat={'name':'Cat','Type':'Domestic','Owner':'Drake'}
dog={'name':'Dog','Type':'Domestic','Owner':'Messi'}
snake={'name':'Snake','Type':'Wild','Owner':'Bear Grills'}
fish={'name':'Fish','Type':'Aquatic','Owner':'Aquaman'}
lion={'name':'Lion','Type':'Wild','Owner':'Stark'}
pets=[cat,dog,snake,fish,lion]
for pet in pets:
        print(pet['Owner']+' is the owner of a '+pet['name']+'. It is '+pet['Type']+' in nature. ')


#Exercise 6.10
fav_num={'Prazwol':[1,0],'Lila':[1,3,5,7,9],'Punam':[2,4,6,8]}
for name,num in fav_num.items():
        print(name+' has favourite numbers:')
        for n in num:
                print(n)


#Exercise 6.11
cities={'Seoul':{'country':'Korea','population':'9.8m','fact':'Its third largest city in the world.'},'Barcelona':{'country':'Spain','population':'1.62m','fact':'It is known for its art and architecture.'},'Kathmandu':{'country':'Nepal','population':'1.44m','fact':'It is one of the most polluted city in the world.'}}
