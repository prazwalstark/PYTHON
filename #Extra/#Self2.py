'''You are given some input, and you are required to check whether they are valid mobile numbers.

A valid mobile number is a ten digit number starting with 9 , 8 or 7.'''
num = int(input())
numbers=[]
result=[]
for j in range(0,num):
    numbers.append(input())
for inp in numbers:
    empt_num=''
    count = 0
    for i in inp:
        if i.isdigit():
            empt_num += i
            count+=1
    if count == 10:
        empt_num=int(empt_num.strip())
        while empt_num>10:
            empt_num //=10
        if empt_num in [7,8,9]:
            result.append('YES')
        else:
            result.append('NO')
    else:
        result.append('NO')
for results in result:
    print(results)
