
# A TUPLE in python is an ordered and immutable sequence of elements , written using commas (usually inside parantheses()) , which can store value 
# of the same or different data types . 
# important - IMMUTABLE(unchangeable) , if you try to change point[0] =7 , python will give you an error.
# TUPLE HAVE INDEXING , YOU CAN ACCESS IT ELEMENT USING INDEXING . INDEX STARTS FROM ZERO 
# EVEN IT SUPPORTS INDEXING , YOU CANNOT CHANGE VALUE USING INDEXING. 

# without tuple unpacking
point=(5,10)
x=point[0]
y=point[1]
print(x,y)

t=(10,20,30,40)
print(t[0])
print(t[1])
print(t[2])
print(t[3])

# TUPLE UNPACKING - 
# tuple unpacking is a fancy way of saying taking items out of the bag and giving them their own names.
# instead of accessing items one by one using numbers like point[0], you can assign them to variables in one go. 
point=(5,10)
x,y=point     # python unpacks 5 into x and 10 into y

a=5
b=10
print(f'before swapping : a={a} , b={b}')
a,b = b,a                                   # a tuple is created on the right side of the assignment => (b,a)->(10,5) => a,b=(10,5) [tuple unpack]
print(f"after swapping : a={a} , b={b}")
# tuple unpacking happens because the right hand side automatically becomes a tuple , even if you don't write parantheses
# in python b,a already means a tuple even without parentheses

# TEST CASES 
# 1! swapping different data types - 
# name,age= 'alice',22
# name,age=age,name
# output = name=25, age='alice'    [ python doesnot care about the type , only the pposition ]
# 2! too many variables / too many values
# a,b,c=10,20 / a,b=10,20,30
# output : value error : too many values to unpack