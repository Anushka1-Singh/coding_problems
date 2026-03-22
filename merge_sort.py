def merge_sort(arr1,arr2):
    i,j=0,0
    merged=[]
    while i<len(arr1) and j<len(arr2):       # loop stops after : 3<3 and 2<3, still elements are left so we use merge.extend 
        if arr1[i]<arr2[j]:                  # merge.extend to add remaining elements
            merged.append(arr1[i])
            i +=1
        else:
            merged.append(arr2[j])
            j +=1
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged
arr1=[1,3,5]
arr2=[2,4,6]
result=merge_sort(arr1,arr2)
print('hi your result',result)

# arr1[0]<arr2[0] => 1<2 , True ,       [1]
#i=1 , j=0
#arr1[1]<arr2[0]   =>  3<2  ,     False        [1,2]
#i=1, j=1                                   
#arr1[1]<arr2[1]   =>  3<4  ,     True         [1,2,3]
#i=2, j=1
#arr1[2]<arr2[1]   =>  5<4  ,     False        [1,2,3,4]
#i=2,  j=2                          
#arr1[2]<arr2[2]   =>  5<6  ,     True         [1,2,3,4,5]
#i=3, j=2

#merged.extend(arr1[i:]) → arr1[3:] → []
#merged.extend(arr2[j:]) → arr2[2:] → [6]



def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr3=[5,2,8]
arr4=[1,9,3]
arr3=bubble_sort(arr3)
arr4=bubble_sort(arr4)
merged=arr3+arr4
merged=bubble_sort(merged)
print('merged sort array : ', merged)

