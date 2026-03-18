n=10 #number of terms
n1=0
n2=1
print(n1,n2,end=' ')
for i in range(2,n):   # 8 iterations
    n3=n1+n2
    print(n3,end=' ')
    n1=n2
    n2=n3
print(n)
# while condition
num=int(input('enter no. of terms : '))
num1=0
num2=1
count=2
if num<=0:
    print('invalid input')
elif num==1:
    print(num1,num2,end=' ')
else:
    print(num1,num2,end=' ')
    while count<num:
        num3=num1+num2
        print(num3,end=' ')
        num1=num2
        num2=num3

        count+=1
        
