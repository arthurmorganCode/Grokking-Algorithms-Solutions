def quicksort(arr):
    if len(arr) < 2 :
        return arr
    else:
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        mid = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

    return quicksort(left) + quicksort(mid) + quicksort(right)


print(quicksort([4,6,7,2,8,9,1,3]))