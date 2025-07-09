#dictionary - used to store data in key:value pairs.
# Dictionaries are mutable, meaning you can change their content after creation but unordered
# and do not allow duplicate keys.
# A dictionary is defined using curly braces {} and can contain elements of different data types.
information = {
    "key" : "value",
    "marks" : 90.2,
    "name" : "hello",
    "subjects" : ["a", "b", "c"], #list can also be used as a value in dictionary
    "tuple" : ("x", "y", "z"), #tuple can also be used as a value in dictionary
    "age" : 20,
    "is_student" : True
} #accepts all type of value types. but keys accpeets only strings, integers, boolean or tuples.
#print(information["key"])
information["key"] = "apple" #instead of creating a new key, we can change the value of an existing key- by overwriting it  
print(information["key"])

null_dict = {}
# To create an empty dictionary, you can use either of the following methods:
empty_dict = {}  # Using curly braces
empty_dict2 = dict()  # Using the dict() constructor    

nulldict = {}
null_dict["name"] = "John"
print(nulldict)
print(null_dict)

#nested dictionary- a dictionary inside a dictionary
student = {
    "name" : "John",
    "subjects" : {
        "math" : 90,
        "science" : 85,
        "english" : 88  #nested dictionary
    }
}
print(student["name"],["subjects"])


#dictionary methods
# 1. keys() - returns a view object that displays a list of all the keys
print(student.keys())
print(len(student.keys()))  #length of keys

# 2. values() - returns a view object that displays a list of all the values
print(student.values())

# 3. items() - returns a view object that displays a list of all the key-value pairs
print(student.items())

# 4. get() - returns the value for the specified key if key is in dictionary
print(student.get("name"))  #returns value of key "name"

# 5. update() - updates the dictionary with the specified key-value pairs
student.update({"age": 20})  #adds a new key-value pair
print(student["age"])



#SETS # A set is an unordered collection of unique elements, meaning it does not allow duplicate values.
#sets are mutable - add, remove, but elements of sets are immutable - cannot change the value of an element
# A set is defined using curly braces {} or the set() constructor and can contain elements of different data types.
# Sets are useful for membership testing, removing duplicates from a sequence, and performing   
#collection of unordered unique elements. and immutable.
collection = {1,2,3,"hello"}
print(collection)
collection1 = {1,2,2,2,3,"hello", "bye",3,"world"}
print(collection1) #duplicates are removed - as sets have unique elements only
# To create an empty set, you can use the set() constructor:
empty_set = set() # Using the set() constructor , {} creates an empty dictionary, not a set
print(empty_set)
print(type(collection))
print(len(collection1))

#set methods
# 1. add() - adds an element to the set
collection.add("wow")
print(collection)

# 2. remove() - removes the specified element from the set
print(collection.remove(2)) #will return None, as remove does not return anything but removes what element you had asked for.
collection.remove(1) 
print(collection) #will print the set after removing 1
# If you try to remove an element that is not in the set, it will raise a KeyError.
# To avoid this, you can use the discard() method, which does not raise an error if the element is not found.
#unhashable type - immutabke values which cannot be changed so the output can be executed without error caused due to mutable changes.

# 3. clear() - removes all elements from the set
print(collection.clear())# same logic wont print anything but will clear ar=nd output will return none
collection.clear() #here it first executes the command.
print(collection) #will print an empty set as clear command has been executed priorly.
#but it wont print empty - it will give set(), which is the correct way to print empty sets

#set.pop() - removes and returns an arbitrary element from the set
# This method is useful when you want to remove an element without specifying which one.
# Note that the element removed is arbitrary, meaning it could be any element from the set.
# If the set is empty, it will raise a KeyError. It can be used when we are trying to generate a random value out of a dataset more of like lottery
#collection.pop() #will give error as we have emptied the set earlier by using .clear

set = {1,2,3,"my","name","is","Gauri" ,"hello","world"}
print(set.pop())

#set.union() - returns a new set with all elements from both sets - also by |
set1= {4,5,6,"new","set"}
set2 = {7,8,9,"another","set"}
unionset = set1.union(set2)
print(unionset)
# You can also use the | operator to perform union
unionset2 = set1 | set2
print(unionset2)

# set.intersection() - returns a new set with elements that are common to both sets - also by &
set3 = {1,2,3,}
set4={2,3,4}
intersect = set3.intersection(set4)
print(intersect)
# You can also use the & operator to perform intersection
intersect2 = set3 & set4
print(intersect2)

#practice 4
dict = {
    "table" : ["a piece of furniture", "list of facts & figures"],
    "cat" : "a small animal",
}
print(dict)


classinfo = {"python", "java","c++", "javascript", "java", "python", "java", "c++","c"}
print(len(classinfo))

dict = {}
#sub1 = input("Enter subject 1: ")
#sub2 = input("Enter subject 2: ")
#sub3 = input("Enter subject 3: ")
dict.update()
#dict = {
    #"subject1": sub1,
    #"subject2": sub2,
    #"subject3": sub3
#}
#print(dict)

set0 = {9,"9.0"} # have to make it a string cause otherwise set give 9 and 9.0 same hash values meaning it wont repeat and gets print only once
print(set0)
#or the other possible way is
set0 = {
    ("float", 9.0),
    ("int",  9)
}
print(set0)