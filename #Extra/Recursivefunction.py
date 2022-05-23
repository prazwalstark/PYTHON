#In python recursive funtion allows user to call the same funtion repeatedly by itself so as to solve a problem.
#Recursive functions can have various uses so as to make program simpler and effective.
#Following is an example of recursive function to calculate factorial of a number say 4  has factorial 4*3*2*1=24

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x*factorial(x-1))

print('Input the number whose factorial you want to find!')
x= int(input())
result=factorial(x)
print('\nThe factorial of '+str(x)+' is: '+str(result))

#This example is to find the HCF of two numbers using recursive functioin.
def HCF(num1,num2):
    low= min(num1,num2)
    high = max(num1,num2)
    if high%low == 0:
        return low
    else:
        return HCF(low,high%low)

print('Input the numbers between whom you want to find HCF!\n Note: While giving input, Press enter after 1st Number is entered and enter the 2nd Number!\n')
num1= int(input())
num2= int(input())
result=HCF(num1,num2)
print('\nThe HCF of '+str(num1)+' & '+str(num2)+' is: '+str(result))

#This example is to find a to the power b using recursive functioin.
def HCF(a,b):
    if b == 1:
        return a
    else:
        return (a*HCF(a,b-1))

print('Input the value of a and b! \nNote: While giving input, Press enter after 1st Number is entered and enter the 2nd Number!\n')
a= int(input())
b= int(input())
result=HCF(a,b)
print('\nThe value of '+str(a)+'^'+str(b)+' is: '+str(result))

#Fabionnic Series Using recurssive function
def fibonacci(a,b,x):
    if x !=0:
        print (b)
        return fibonacci(b,b+a,x-1)
a=1
b=1
x=int(input())
fibonacci(a,b,x)
#OR
def fibonacci(a,b,x):
    if x ==1:
      return a
    else:
      return fibonacci(b,b+a,x-1)
a=1
b=1
x=int(input())
print(fibonacci(a,b,x))