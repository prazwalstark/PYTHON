'''In this program we will take input(number) from the user and sum all the digits of a number until the resutant sum is in single digit.'''
def example(num):
    if num < 10 :
        return num
    else:
        return example((num%10 + example(int(num/10))))
num=int(input())
n = example(num)
print (n)

