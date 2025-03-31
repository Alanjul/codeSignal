def startFromCenter(numbers):
    #Traversing the array starting from the middle
    mid = len(numbers)//2
    new_order = []
    #if the array is odd, the middle starts
    if len(numbers) % 2 == 1:
        left = mid-1
        right = mid+1
        new_order.append(numbers[mid])
    #else no mid element
    else:
        new_order = []
        left = mid-1
        right = mid
    #loop through the array
    while(left >=0 and right < len(numbers)):
        new_order.append(numbers[left])
        new_order.append(numbers[right])
        left -= 0
        right += 1
    return new_order




