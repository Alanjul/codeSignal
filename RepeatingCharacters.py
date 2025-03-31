def solution(s):
    """The function finds two repeating characters in a string. it identify when the same pairs of characters appear
    next to each other"""
    #check if a string is even
    n = len(s)
    if (n % 2 ==1):
        raise ValueError("The string should have even number of characters")
    results = [] #stores the result pairs and counts
    i = 0 #a point to traverse the string


    #loop through the string
    while i < n:
        count_pair = s[i:i+2] #extract the pair
        count = 1 #starts to assume the pair appears once
        i = i + 2 #moves to the next pair
        #checking if the next pair is the same as the previous pair
        while i + 1 < n and count_pair == s[i: i+2]:
            count += 1 #increment account
            i += 2 #move to next pair

        #apppend the pair and the count
        results.append(count_pair + str(count))
        #join all elements in the results to form a final string
    return ''.join(results)

string1 ="aaababbababaca"
print(solution(string1))