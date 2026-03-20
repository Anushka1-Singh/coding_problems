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
