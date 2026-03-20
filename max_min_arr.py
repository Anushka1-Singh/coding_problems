def min_max(arr):
    if not arr:
        return None, None
    minimum = maximum =arr[0]
    for x in arr:
        if x<minimum:
            minimum=x
        elif x>maximum:
            maximum=x
    return minimum, maximum
arr=[64,34,25,12,22,11,90]
low,high=min_max(arr)
print(f"min:{low},max:{high}")

# using bubble sort algorithm
def bubble_sort_min_max(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr[0],arr[n-1]
data=[64,34,25,12,22,11,90]
low,high=bubble_sort_min_max(data)
print(f'Min: {low}, Max:{high}')