#Exercise 6.5 
rivers={'Nepal':'Trishuli','India':'Yamuna','Egypt':'Nile'}
for country,river in rivers.items():
    print('The '+river+' runs through '+country+'.')
print("Rivers:")
for river in sorted(rivers.values()):
    print(river)
print("Countries:")
for country in sorted(rivers.keys()):
    print(country)


#Exercise 6.6
language_poll = {'Prazwol': 'Python','John':'C/C++','Neo':'Machine'}
people = ['Prazwol','Neo','Stark','John','Tony','Strange']
for people_poll in language_poll.keys():
    if people_poll in people:
        print(people_poll + ' Thank you for responding.')
    else:
        print(people_poll +' Please participate in the poll.')


