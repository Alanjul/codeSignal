def usual_traversal(arrays):
    """Return a array of  new array traversing from the beginning, for each
    subsequent pair of elements"""
    n = len(arrays)
    mid = n//2
    new_arr = [arrays[mid]]
    left = mid -1
    right = mid + 1
    #loop through the array for left to right
    while left >= 0 or right < n:
        left_array = []
        #alternate left in two steps
        for _ in range(2):
            if left >= 0:
                left_array.append(arrays[left])
                left -=1

        new_arr.extend(left_array[::-1])

        #alternate right in 2 steps
        for _ in range(2):
            if right < n:
                new_arr.append(arrays[right])
                right += 1

    return new_arr
arr = [1, 2, 3,4, 5, 6,7]
solutions =usual_traversal(arr)
print(solutions, ' ')
