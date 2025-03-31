from collections import defaultdict
def find_unique_string(words):
    """This function implements a mechanism of finding a unique
    string in a  list"""
    seen = set() #set to hold seen words
    duplicate = set() #holds duplicate words
    for word in words:
        if word in seen:
            duplicate.add(word)
        seen.add(word)
    #iterate through word to find unique word
    for word in words:
        if word not in duplicate:
            return word
    return "" #no unique word found
words = ["apple", "banana", "apple"]
print(find_unique_string(words))
print(find_unique_string([]))

def anagram_find(words1, words2):
    """this function finds anagram pairs in a two list pairs"""
    #converting words to string
    #words1 = [str(word) for word in words1]
    #words2 = [str(word1) for word1 in words2]
    sort_tuple = set(tuple(sorted(word)) for word in words1) #sorting words alphabetically
    sorted_tuple2 = set(tuple(sorted(word)) for word in words2) #sorting words in list2 alphabeticallly
    common_tuples = sort_tuple & sorted_tuple2 #getting the common words from two tuples
    list_1 = [ word for word in words1 if tuple(sorted(word))in common_tuples]
    list_2 = [word for word in words2 if tuple(sorted(word)) in common_tuples]

    output = []
    for word1 in list_1:
        for word2 in list_2:
            if tuple(sorted(word1)) == tuple(sorted(word2)):
                output.append((word1, word2))
    return output
lists1 =["bat", "tab", "apple", "mango"]
lists2 = ["act", "cat", "banana", "tab"]
print(anagram_find(lists1, lists2))

#using dictionary to find anagram
def anagram_find1(lists_1, lists_2):
    #create a dictionary to hold lists
    dict_lis1 = defaultdict(list)
    for word in lists_1:
        sorted_list = tuple(sorted(word))