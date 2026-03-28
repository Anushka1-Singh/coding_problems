# write a program in python to remove duplicate elements from an array
arr=[10,20,10,30,30,40,20]
unique=[]
for i in range(len(arr)):
    # membership operator('in','not in' , not in - "checks if x is not present in the collection(list,string,etc.)")
    if arr[i] not in unique:
        unique.append(arr[i])
print("original : ",arr)
print("without duplicates : ",unique)
# dry run 
# arr[0]=10 not in unique[] : true|append , unique[10]
# arr[1]=20 not in unique[] : true|append , unique[10,20]
# arr[2]=10 not in unique[] : false|skip, unique[10,20]
# arr[3]=30 not in unique[] : true|append, unique[10,20,30]
# arr[4]=30 not in unique[] : false|skip, unique[10,20,30]
# arr[5]=40 not in unique[] : true|append , unique[10,20,30,40]
# arr[6]=20 not in unique[] : false|skip, unique[10,20,30,40]