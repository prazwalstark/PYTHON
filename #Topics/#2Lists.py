from sre_constants import RANGE_UNI_IGNORE
team = ["messi","    neymar    ","mbappe",'donnaramu']
#for is used for looping in python and along with lists we can print all the elements of lists in print statement
for players in team:
    print(players.lstrip())
#for loop for in numerical lists 
for num in range(1,10):
    print(num)# here the print statement doesn't print the number 10 cause for loop starts from 1 and stops when reaches 10
#range() function also be used to make lists of numbers
num=list(range(6))#here the range is from 0 to 5 because the initial value isn't mentioned
print(num)
#range(intial value, final value or stopping value, number gap or jump value)
#The program below illustrates the use of range() function in python
work_values=[]
sum=0
for num in range(2,11,2):
    square=num**2
    print(square)
    sum+=square
    work_values.append(square)
print (work_values)
print(sum)
maximum=max(work_values)# similar functions are min() = for minimum and sum()= for summation of the elements of the lists
print(maximum)
#List Comprehensions in Python (example):
cube=[num**3 for num in range(1,6,2)]#in for loop avoid colon at last unlike in other normal statements
print(cube)
#Slicing in python is accessing more than one elements of list and working on them
print(team[-2:])
#Looping in the slice
print("Here are my teammatesm:")
for players in team[:2]:
    print(players.strip())
#List can also be copied to another list variable
legends= team[:3]
legends.append("Ronaldo")
print(legends)
#We can also state legends=team but this statement sets both the varibles with same traits/elements i.e. we can't work on variables differently after copying them
#Tuple is an immutable part of python that can't be changed in the program
#Defining Tuple: It uses parantheses()
#looping in Tuple is similar to list
#We can't edit the variables of tuple but we can redefine tuple
players=(30,10,7,7)
print(players[:2])




