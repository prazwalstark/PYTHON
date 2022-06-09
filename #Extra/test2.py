from numpy import delete


path="D:/Programs/#Python/#Extra/test2.txt"
with open(path,'a') as fuck:
    fuck.write('I love you.\n\n') 
    fuck.write('Asshole')
for i in range (-1,5):
    try:
        div=10/i
        print (div)
    except:
        print('Division isn\'t possible')
    #else:
        #print (div)
with open(path,'r') as asshole:
    for line in asshole.readlines():
        print(asshole.count('love'))

delete(path)
