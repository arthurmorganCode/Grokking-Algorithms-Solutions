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