def binary_search(list, target):
    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess < target:
            low = mid + 1
        elif guess > target:
            high = mid - 1
        else:
            return mid
    return None


list = [1,3,5,7,9,10,23]
print (binary_search(list,23))



