#Lists in python means multiple datas can be stored inside single variable within square breackets[]
team = ["messi","    neymar    ","mbappe",'donnaramu']
#lstrip or rstrip or simply strip can remove whitespaces from the variables or particular variable in lists
print(team[1].lstrip())
#append adds items to lists in last position where the list is previously left
team.append('icardi')
print(team)
#Insert is similar to append but insert variable in particular index i.e. position
team.insert(1,'paredes')
print(team)
#del removes the items from the list from particular position or index
del team[1]
print(team)
#Remove simply removes particular listed item from the lists
team.remove('mbappe')
print(team)
#Pop removes the last item from the list but also provides an opportunity to use the removed item by pop
pop_team = team.pop()
print(team)
print(pop_team + ' is a substitute')
#Sort is used to arrange the items in the lists
team.sort()
print(team)
#(reverse=True) : reverses the sorting of data
team.sort(reverse=True)
print(team)
#reverse has the same function as that of (reverse=True)
team.reverse()
print(team)
#This is all about list and organizing lists in Python. In next chapter we will discuss working with lists!
