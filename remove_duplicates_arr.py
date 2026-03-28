# write a program in python to remove duplicate elements from an array
arr=[10,20,10,30,30,40,20]
unique=[]
for i in range(len(arr)):
    if arr[i] not in unique:
        unique.append(arr[i])
print("original : ",arr)
print("without duplicates : ",unique)