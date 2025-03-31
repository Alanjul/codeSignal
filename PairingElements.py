def solution(numbers):
    """The array creates a tuple of pairs , pairing each element with each other"""
    mid = len(numbers)//2

    #check if the arr has odd length
    new_arr = []
    if len(numbers) % 2 == 1:
        left = mid -1
        right = mid +1
        new_arr.append((numbers[mid], 0))#append tuples
    else:
        new_arr.append((numbers[mid-1], numbers[mid]))
        left = mid -2
        right = mid +1
    #loop through the array both left and right
    while left >= 0 and right < len(numbers):
        new_arr.append((numbers[left], numbers[right]))
        left -=1
        right +=1
    return new_arr

arr = [1, 2, 3, 4, 5]
new_arr = solution(arr)
for num in new_arr:
    print(num , " ")