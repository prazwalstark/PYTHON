#Pattern 1:
#*
#**
#***
#****
#*****
for p in range(0,5):
    for q in range(0,p+1):
        print("*",end='')
    print('')

#Pattern 2:
#1
#22
#333
#4444
#55555

for p in range(1,6):
    for q in range(1,p+1):
        print(p,end='')
    print('')
    

#Pattern 3:
#11111
#2222
#333
#44
#5
k=1
for p in range(1,6):
    for q in range(6,p,-1):
        print(k,end='')
    print('')
    k+=1

#Pattern 4:
#1
#12
#123
#1234
#12345
for p in range(1,6):
    for q in range(1,p+1):
        print(q,end='')
    print('')
    
#Pattern 5:
#55555
#4444
#333
#22
#1
for p in range(5,0,-1):
    for q in range(0,p):
        print(p,end='')
    print('')

#Pattern 6:
#1 
#21 
#321 
#4321 
#54321
for p in range(0,5):
    for q in range(p+1,0,-1):
        print(q,end='')
    print('')

#Pattern7:
#012345 
#01234
#0123
#012
#01
for p in range(5,0,-1):
    for q in range(0,p+1):
        print(q,end='')
    print('')

#Pattern8:
#1
#234
#56789
k=1
for p in range(1,6,2):
    for q in range(0,p):
        print(k,end='')
        k+=1
    print('')    