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
    set_tuple1= set(tuple(sorted(word)) for word in words1)
    set_tuple2 = set(tuple(sorted(word)) for word in words2)
    common_tuples = set_tuple1 & set_tuple2
    list_tuple1 = [ word for word in words if tuple(sorted(word)) in common_tuples]
    list_tuple2 = [word for word in words if tuple(sorted(word)) in common_tuples]
    out_put = []
    for word1 in list_tuple1:
        for word2 in list_tuple2:
            if tuple(sorted(word1)) == tuple(sorted(word2)):
                out_put.append((word1, word2))

    return out_put
lists1 =["bat", "tab", "apple", "mango"]
lists2 = ["act", "cat", "banana", "tab"]
print(anagram_find(lists1, lists2))

#using dictionary to find anagram
def anagram_find1(lists_1, lists_2):
    #create a dictionary to hold lists
    dict_list1 = defaultdict(list)
    for word in lists_1:
        sorted_list = tuple(sorted(word)) #create a list of duplicated elements
        dict_list1[sorted_list].append(word)
    map_list2 = defaultdict(list)
    for word2 in lists_2:
        sorted_tuple = tuple(sorted(word2))
        map_list2[sorted_tuple].append(word2)
    common_tuples = set(dict_list1.keys()) & set(map_list2.keys())
    output = []
    for anagram in common_tuples:
        for word1 in dict_list1[anagram]:
            for word2 in map_list2[anagram]:
                output.append((word1, word2))
    return output
lists1 = ["cinema", "iceman"]
list2= ["iceman", "cinema"]
print(anagram_find1(lists1, list2))
#Returning  anagram from two list
def find_anagram(list_1, list_2):
    """The function returns a list of unique word from list 1 that are in list 2"""
    map1 = defaultdict(list)
    for word in list_1:
        sorted_tuple1  = tuple(sorted(word))
        map1[sorted_tuple1].append(word)

    map2 = defaultdict(list)
    for word2 in list_2:
        sorted_tuple2 = tuple(sorted(word2))
        map2[sorted_tuple2].append(word2)

    #intersection
    common_tuples = set(map1.keys()) & set(map1.keys())

    output = set() #set to store unique words
    for anagram in common_tuples:
        output.update(map1[anagram])
        output.update(map2[anagram])

    return list(output)

lists1 = ["cinema", "iceman"]
list2= ["iceman", "cinema"]
print(find_anagram(lists1, list2))

