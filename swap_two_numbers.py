a=5
b=10
temp=a
a=b
b=temp
print(f"After Swapping : a={a} , b={b}")

#uses a third variable(temp) to store a value of a while while the swap happens
# dry run:
# temp = a , copy of (a) variable value into temp ,    a(5)  b(10) temp(5)
# a = b    , overwrite a variable with b value ,       a(10) b(10) temp(5)
# b=temp   , overwite b variable with with temp value ,a(10) b(5)  temp(5)
# there is no edge cases 
# 1) swapping large numbers ( python variables value can grow as large as your computer 's memory allows)
# 2) python dynamically typed - not declared the data type of a variable explicitly, the type is decided automatically at runtime based on the value assigned.
#