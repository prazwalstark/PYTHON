#Exercise 7.8
sandwiches = ['chicken','pastrami' ,'egg', 'seafood','pastrami','roast beef','grilled','ham','pastrami', 'nutella','grilled chicken']
finished_sandwiches=[]
for sandwich in sandwiches:
    print('Here is Your Order! Please enjoy your '+ sandwich.title()+' Sandwich. Thank You!')
    finished_sandwiches.append(sandwich)
print('--Order List--')
for sandwich in finished_sandwiches:
    print(sandwich.title() + 'Sandwich')



#Exercise 7.9
sandwiches = ['chicken','pastrami' ,'egg', 'seafood','pastrami','roast beef','grilled','ham','pastrami', 'nutella','grilled chicken']
print('Sorry, For the inconvinience but we have run out of pastrami sandwich!')
num=len(sandwiches)-1
while num!=-1:
    if sandwiches[num] == 'pastrami':
        del sandwiches[num]
    num-=1
print('Updated order list is: ')
for sandwich in sandwiches:
    print(sandwich)

#Exercise 7.10
# I am supposed to ask the user what would be there dream vacation place.
poll_result={}
answer=True
while answer:
    print('Whats your name?')
    name=input()
    print('What would be your dream vacation place?')
    destination=input()
    poll_result[name]=destination
    ans=input('Do you wamt more entries?(Y|N)')
    if ans=='N':
        answer=False
for names,destinations in poll_result.items():
    print(names+' would like to visit '+destinations+'.\n\n')



