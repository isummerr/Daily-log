#list is a built in data structure in python that allows you to store multiple items in a single variable.
# It is mutable, meaning you can change its content after creation.
#Lists are defined using square brackets [] and can contain elements of different data types, including numbers, strings, and even other lists.
# Lists can be manipulated using various methods, such as append(), remove(), and sort().
marks = [67, 56, 34, 45.2] # A list containing integers and a float
print(marks)  # Output: [67, 56, 34, 45.2]
print(type(marks))  # Output: <class 'list'> - because it is a list
print(marks[2])  # Accessing the third element in the list (index 2) - Output: 34
#list can have different data types - says strings and int in same list
list = [34, "ok", 34.2]
print(list)  # Output: [34, 'ok', 34.2]
#strings are immutable, meaning once created, their content cannot be changed. but lists are mutable, meaning you can change their content after creation.
list1 = [2,3,4, "hello"]
list1[3] = "world"  # Changing the fourth element in the list
print(list1)  # Output: [2, 3, 4, 'world'] - The fourth element has been changed to "world"
#similarly we can change int, float, or any other data type in the list too.
#list1[4] = 5.5  # Changing the fifth element in the list
#print(list1)  # Output: [2, 3, 4, 'world', 5.5] - The fifth element has been changed to 5.5 - will raise an error because there is no fifth element in the list     

#list slicing
# Slicing allows you to extract a portion of the list using the colon : operator.
# Slicing syntax: list[start:end] - extracts elements from index 'start' to 'end-1'it will not include the last index.
# If 'start' is omitted, it defaults to 0. If 'end' is omitted, it defaults to the length of the list.
# Negative slicing works similarly,
# allowing you to slice from the end of the list with -1 as the last element.
list2 = [2,3,4,"thank", "you", 4]
print(list2[2:5]) # Output: [4, 'thank', 'you'] - Slicing from index 2 to 4 (end index is not included)
print(list2[-4:-1])  # Output: ['thank', 'you', 4] - Slicing from the fourth last to the second last element


#list methods
list3 = [13, 2, 33, 4, 5]

# list.append() - Adds an element to the end of the list.
list3.append(6) # Adding 6 to the end of the list - mutating the list
print(list3)  # Output: [1, 2, 3, 4, 5, 6]

# list.remove(value) - Removes the first occurrence of a specified value from the list.
print(list3.remove(33))  # Output: None - removes the first occurrence of 33 from the list
list3.remove(2)  # Removing 2 from the list

# list.pop(index) - Removes and returns the element at the specified index (default is the last element).
print(list3.pop(2))  # Output: 4 - Removes and returns the element at index 2 (which is 4)
print(list3)  # Output: [1, 2, 5, 6] - The list after removing the element at index 2

# list.sort() - Sorts the elements of the list in ascending order.
print(list3.sort()) #gives none as output
print(list3)  # Output: [1, 2, 3, 4, 5, 6] - ascending order

# list.reverse() - Reverses the order of the elements in the list.
print(list3.reverse())  # Output: None - reverses the list in place
print(list3)  # Output: [6, 5, 4, 3, 2, 1] - The list is now reversed

# list.sort(reverse=True) - Sorts the elements of the list in descending order.
print(list3.sort(reverse=True))  # Output: None - sorts the list in descending order
print(list3)  # Output: [6, 5, 4, 3, 2, 1] - The list is now sorted in descending order

# list.insert(index, value) - Inserts a value at a specified index in the list.
list3.insert(2, 10)  # Inserting 10 at index 2
print(list3)  # Output: [6, 5, 10, 4, 3, 2, 1] - The value 10 is inserted at index 2


#Tuples
# Tuples are similar to lists, but they are immutable, meaning once created, their content cannot be changed.
# Tuples are defined using parentheses () and can also contain elements of different data types.
# Tuples can be used to store related data that should not be modified, such as coordinates- immutable data.
tuple = (1,4,23,89)
print(tuple)  # Output: (1, 4, 23, 89)
print(type(tuple))  # Output: <class 'tuple'> - because it is a tuple
print(tuple[2])  # Accessing the third element in the tuple (index 2) - Output: 23

#tuples can have different data types - says strings and int
#we can not change the value of a tuple, but we can access its elements.
#tuple[2] = 45  # This will raise an error because tuples are immutable

#we can also print empty tuple or a single value tuple with a comma and without a comma code will consider it as integer not a tuple.
empty_tuple = ()  # Empty tuple
print(empty_tuple)  # Output: ()
single_value_tuple = (5,)  # Single value tuple with a comma
print(single_value_tuple)  # Output: (5,)
not_a_tuple = (5)  # Not a tuple, just an integer
print(not_a_tuple)  # Output: 5 - This is just an integer, not a tuple

# tuple slicing
# Slicing works similarly to lists, allowing you to extract a portion of the tuple.
tuple2 = (1, 2, 3, "hello", "world",1)
print(tuple[2:4])  # Output: (3, 'hello') - Slicing from index 2 to 3 (end index is not included)

#tuple methods
# tuple.index(value) - Returns the index of the first occurrence of a specified value in the tuple.
print(tuple.index(1))  # Output: 2 - The index of the first occurrence of 23 in the tuple  

# tuple.count(value) - Returns the number of occurrences of a specified value in the tuple.
print(tuple.count(1))  # Output: 1 - The number of occurrences of  1 in the tuple

# tuple length - The length of a tuple can be determined using the len() function.
print(len(tuple))  # Output: 4 - The length of the tuple is 4   

# tuple unpacking - allows you to assign the elements of a tuple to multiple variables in a single line.
a, b, c, d = tuple  # Unpacking the tuple into variables a, b, c, and d
print(a, b, c, d)  # Output: 1 4 23 89 - The values of the tuple are assigned to the variables      

# tuple concatenation - allows you to combine two or more tuples into a new tuple.
tuple3 = tuple + tuple2  # Concatenating two tuples
print(tuple3)  # Output: (1, 4, 23, 89, 1, 2, 3, 'hello', 'world') - The two tuples are combined into a new tuple           

# tuple repetition - allows you to repeat the elements of a tuple a specified number of times.
tuple4 = tuple * 2  # Repeating the tuple twice     
print(tuple4)  # Output: (1, 4, 23, 89, 1, 4, 23, 89) - The tuple is repeated twice 


#practice3
#movie1 = input("Enter the name of the first movie: ")
#movie2 = input("Enter the name of the second movie: ")
#movie3 = input("Enter the name of the third movie: ")
#list = [movie1, movie2, movie3]  # Creating a list of movies
#print("Your favorite movies are :", list)


#palindrome check - # A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.
list = [1,2,3,2,1]
list2 = [1, "abc", 2, 6, "abc", 1]
# Check if the list is a palindrome
copy_list = list.copy()
copy_list.reverse()  # Reversing the copied list
print(copy_list)  # Output: [1, 2, 3, 2, 1] - The reversed list is the same as the original list
if (list == copy_list):
    print("list is palindrome")
else:
    print("not palindrome")  # Output: True - The original list and the reversed list are equal, so it is a palindrome

copy_list2 = list2.copy()
copy_list2.reverse()
if (list2 == copy_list2):
    print("list2 is palindrome")
else:
    print("not palindrome")

tup = ("C", "D", "A", "A", "B", "B", "A")
print(tup.count("A"))
#tuple to list conversion
tup = ["C", "D", "A", "A", "B", "B", "A"]
tup.sort()
print(tup)  # Output: ['A', 'A', 'A', 'B', 'B', 'C', 'D'] - The list is sorted in ascending order