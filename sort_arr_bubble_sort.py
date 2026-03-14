def bubble_sort(arr):
    n=len(arr)
    # outerloop(i) : [how many rounds to run]
    for i in range(n):
        # start each round assuming the list is sorted
        swapped=False
        # inner loop(j) : [compare neighbors]
        # n-i-1 ensures we don't re-check locked numbers at the end
        for j in range (0, n-i-1):
            # comparison : left>right ?
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]          # TUPLE UNPACKING
                swapped=True
            # if no swap happens in a full pass , the list is perfect.
        if not swapped:
                break
    return arr
num=[5,2,8,1]
sorted_numbers = bubble_sort(num)
print(f"Final sorted array : {sorted_numbers}")


# initial state : [5,2,8,1]
# n=4
# ROUND 1 (i=0)
# range of j : 0to2 (n-0-1)
# j=0 : [5,2,8,1] -> 5>2 yes, swap[2,5,8,1]
# j=1 : [2,5,8,1] -> 5>8 no swap
# j=2 : [2,5,8,1] -> 8>1 yes swap[2,5,1,8]
# result : [2,5,1,8] (8 is locked)
# swapped : true

# ROUND 2 (i=1)
# range of j : 0to1 (n-1-1)
# j=0 : [2,5,1,8] -> 2>5 no swap
# j=1 : [2,5,1,8] -> 5>1 yes swap[2,1,5,8]
# result : [2,1,5,8] (5 is locked)
# swapped : true

# ROUND 3 (i=2)
# range of j : 0to0 (n-2-1)
# j=0 : [2,1,5,8] -> 2>1  yes swap[1,2,5,8]
# result : [1,2,5,8] (2 is locked)
# swapped : true

# round 4(i=3)
# range of j : None (n-3-1=0)
# check no pairs left 
# swapped : false -> break  




