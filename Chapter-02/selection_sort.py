def findsmallest(arr):
    smallest_index = 0
    smallest = arr[0]

    for i in range (len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def selectionsort(arr):
    newArr = []
    for i in range (0 , len(arr)):
        smallest = findsmallest(arr)
        newArr.append(arr.pop(smallest))

    return newArr




list = [4,5,7,891,243,2546,23,6,61,1]

print (selectionsort(list))