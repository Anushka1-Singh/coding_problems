a=5
b=10
print(f"before swapping a={a}, b={b}")
a=a+b     # a becomes 15 (the sum)
b=a-b     # b becomes 5 (sum - original b = original a)
a=a-b     # a becomes 10 ( sum - new b = original b)
print(f"after swapping a={a}, b={b}")

# test cases
# works fine with postive integers , negative integers , mixed sign integers, floating point(small rounding errors), either no. is zero 
# program crash when strings are used , concatenation , output - typeError
# a=none , b=5 , cannot add none to a integer , crash (type error)
