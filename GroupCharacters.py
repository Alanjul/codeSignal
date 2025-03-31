def solution(s):
    groups=[] #keeps grouping of the strings
    current_char = None
    group_length = 0 #tracks the length
    #loop the string to process it
    for char in s:
        if char.isdigit() or char.isalpha():
            if char == current_char:
                #increment the group length
                group_length += 1

            else:
                if current_char is not None:
                    groups.append((current_char, group_length))
                current_char = char
                group_length = 1

    if current_char is not None:
        groups.append((current_char, group_length))
    return groups

s= 'aaabbcccaae'
answer = solution(s)
print(answer)

#implement the Run_length Encoding considering all numerica and alpha characters
def encode_rle(string1):
    group = []
    current = None
    length = 0 #length of the group
    #iterate through the string
    for char in string1:
        if char.isalpha() or char.isdigit():
            if char == current:
                length += 1
            else:
                if current is not None:
                    group.append(f"{current}{length}")
                current = char
                length = 1
    if current is not None:
        group.append(f"{current}{length}")
    return "".join(group)

string2 ="aaa@bb!!c#d**e"
result2 = encode_rle(string2)
answer2 = 'a3b2c1d1e1'
#Testing
if result2 == answer2:
    print("correct answer was provided")
else:
    print("You solution does not work")