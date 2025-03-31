#inital string
input_str = "Hello dear user123"
#split the string into words
words = input_str.split()
print(words)
#reverse each word
reverse_words = [''.join(reversed(word)) for word in words]
print(reverse_words)
def solution(input_st):
    #split the string into words
    words1 = input_st.split()
    #reverse each words
    reverse_word = [''.join(reversed(word1)) for word1 in words1]
    #join the words back together with space
    result = " ".join(reverse_word)
    return result
print(solution("Hello neat pthonistas_123"))