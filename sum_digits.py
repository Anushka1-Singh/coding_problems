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
n = 456
print('recursion based sum of digits',sum_digit(n))

# sum_digit(456)
# = 456 % 10 + sum_digit(456//10)
# = 6 + sum_digit(45)
# sum_digit(45)
# = 45 % 10 + sum_digit(45//10)
# = 5 + sum_digit(4)
# sum_digit(4)
# = 4 % 10 + sum_digit(4//10) 
# = 4 + sum_digit(0)
# = sum_digit(0)
# = 0 -> base case reached
