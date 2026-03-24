s=0
n=int(input('enter the number : '))
while n>0:
    m=n%10
    s = s+m
    n=n//10
print('the sum of digits is : ',s)
