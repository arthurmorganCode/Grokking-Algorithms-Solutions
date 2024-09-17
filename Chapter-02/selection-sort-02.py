def selectionsort(arr):
    for i in range(len(arr)):
        myHand = i
        for j in range (myHand + 1, len(arr)):
            if arr[j] < arr[myHand]:
                myHand = j

        (arr[i], arr[myHand]) = (arr[myHand], arr[i]) # Swap the found minimum element with the first element



list = [4,5,7,891,243,2546,23,6,61,1]
selectionsort(list)
print (list)