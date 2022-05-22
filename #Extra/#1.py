#Sum of Even Fibonacci numbers.
def fibonacci():
    sum = 0
    a=1
    b=1
    temp = 0
    print('How many sum of even fibonacci numbers sum do you want?')
    num = int(input())
    while num==0:
        #print(a)
        if a%2!=0:
            sum+=a
            num-=1
        temp = b
        b = a
        a = temp + b
       
    return sum
#print(fibonacci())



 