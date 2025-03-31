def simple_hash(input_string):
    """Calculating the sum of the unicode by converting an string value between 0 and 9"""
    summation = sum(ord(ch) for ch in input_string)
    print(summation)
    return summation % 10 #we limit our range from 0 to 9
print(simple_hash("Hello"))
print(simple_hash("world"))
#define hash_set
student_ids = set()

#add elements
student_ids.add(13)
student_ids.add(456)
student_ids.add(786)

#check for existence
print(456 in student_ids) #in operation runs in O(1) time complexity, space complexity of hash_set is O(n)
#lookup time complexity is o(1), insertion is O(1), Deletion is O(1) and their west time complexity is O(n)

#Grocery List
Grocery_list = set()
#add items
Grocery_list.add("Milk")
Grocery_list.add("Cheese")
Grocery_list.add('bread')
#try remove the item
Grocery_list.remove('bread')

#creating a new copy
new_list = set(['Eggs', 'Jam', 'Ham'])
copied_list = new_list.copy()
print(copied_list)


"""Finding intersection between list1 and list2"""
def array_intersection(list1, list2):
    set1 = set(list1) # removing duplicate in list1
    set2 = set(list2) # remove duplicate in list2
    intersection = set1 & set2 #returns the intersection between set1 and set2
    return sorted(list(intersection))
list1 = [1, 2, 3,5,7]
list2 = [5,6,1,3,5,2,9]
print(array_intersection(list1, list2))

"""Removing duplicate elements """
#create two sets one to store seen element and one one to store repeated elements
def non_repeating_elements(nums):
    seen, repeated = set(), set()
    for num in nums:
        if num in seen:
            repeated.add(num)
        else:
            seen.add(num)
    return list(seen -repeated)
nums = [1, 2, 3, 4, 5,6, 7, 8,9, 10, 1, 2, 6, 7, 8]
print(non_repeating_elements(nums))

"""The functions finds unique element in a a list1 and they should not be in list 2"""
def unique_elements(lists1, lists2):
    set1 = set(lists1)
    set2 = set(lists2)
    unique1 = sorted(list(set1 -set2))
    unique2 = sorted(list(set2 -set1))
    return (unique1, unique2)
lists1 = [1, 2, 3, 5,8,9,10]
lists2 = [5,6,7,8,9,10,11,12]
print(unique_elements(lists1, lists2))
