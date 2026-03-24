# while loop
s=0
n=int(input('enter the number : '))
while n>0:
    m=n%10
    s = s+m
    n=n//10
print('the sum of digits is : ',s)


# for loop with string
N=input('enter the no : ')
digit_sum=0
for digit in N:
    digit_sum = digit_sum + int(digit)
print('sum of digits : ',digit_sum)

# recursion based sum of digits
def sum_digit(n):
    if n==0:
        return 0
    return n%10 + sum_digit(n//10)
n = 4538
print('recursion based sum of digits',sum_digit(n))