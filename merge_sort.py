def merge_sort(arr1,arr2):
    i,j=0,0
    merged=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
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