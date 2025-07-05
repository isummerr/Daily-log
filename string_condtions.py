#strings 
# Strings are sequences of characters enclosed in quotes (single or double)
# Strings can be manipulated using various methods and operations   

#escape sequence characters
# Escape sequences are special characters that allow you to include characters in a string that would otherwise be difficult to include, such as newlines, tabs, or quotes.
# Common escape sequences include:
# \n - Newline
# \t - Tab  

#concatenation
# Concatenation is the process of joining two or more strings together using the + operator.
# Example:
first_name = "John"            
last_name = "Doe"
full_name = first_name + " " + last_name  # Concatenation using +
print(full_name)  # Output: John Doe

#length of string
# The length of a string can be determined using the len() function.
# Example:
string_length = len(full_name)  # Length of the string
print(string_length)  # Output: 8- because it also counted space between first and last name



#indexing and slicing
# Indexing allows you to access individual characters in a string using square brackets [].
# Each character in a string has an index, starting from 0 for the first character.
# Negative indexing allows you to access characters from the end of the string, with -1 being the last character.
#indexing only helps to call a single character from the string. we cannot manipulate the string or value within using indexing.

# Slicing allows you to extract a substring from a string using the colon : operator.
# Slicing syntax: string[start:end] - extracts characters from index 'start' to 'end-1'. 
# # If 'start' is omitted, it defaults to 0. If 'end' is omitted, it defaults to the length of the string.
# Negative slicing works similarly, allowing you to slice from the end of the string with -1 as the last character.   
# Example:
sample_string = "Hello, World!"
first_character = sample_string[0]  # Indexing - first character
print(first_character)  # Output: H
substring = sample_string[0:5]  # Slicing - first five characters
print(substring)  # Output: Hello   

string = "hello"
print(string[4])
#negative 
print(string[-3])

#slicing
print(string[1:4])
#negative slicing
print(string[-4:-1]) #output wont be in reverse order, 
#plus the last index wont be included in the output.


#string functions
# Strings in Python have many built-in functions that allow you to manipulate and analyze them.
# Some common string functions include:
string = "This is a sample string."
print(len(string))
# upper() - Converts the string to uppercase.
print(string.upper())  # Output: THIS IS A SAMPLE STRING.
# lower() - Converts the string to lowercase.
print(string.lower())  # Output: this is a sample string.
# strip() - Removes leading and trailing whitespace from the string.
print(string.strip("this")) # Output: This is a sample string. (removes only the leading and trailing spaces, not the word 'this')
# replace(old, new) - Replaces occurrences of 'old' with 'new' in the string.
print(string.replace("sample", "example")) # Output: This is a example string.
# split(separator) - Splits the string into a list of substrings based on the specified separator.
print(string.split()) # Output: ['This', 'is', 'a', 'sample', 'string.']
# join(iterable) - Joins elements of an iterable (like a list or tuple) into a single string, using the string as a separator.
print(" ".join (["Helllo,", string])) # Output: Helllo, This is a sample string. if using string.join(["Hello", string]) # Output will repeat string twice as join works like first_element + string + second_element.
# endswith(suffix) - Checks if the string ends with the specified suffix. Output is True or False.

print(string.endswith("ing."))  # Output: True
# startswith(prefix) - Checks if the string starts with the specified prefix. Output is True or False.
print(string.startswith("Th")) # Output: True
# isdigit() - Checks if all characters in the string are digits. Output is True or False.
print("this".isdigit) # Output: False
# isalpha() - Checks if all characters in the string are alphabetic.
#print(string.isaplha(123)) # Output: False
# isalnum() - Checks if all characters in the string are alphanumeric (letters and digits).
print("hello123".isalnum())  # Output: True
# isspace() - Checks if all characters in the string are whitespace characters (spaces, tabs, newlines).

# title() - Converts the first character of each word to uppercase and the rest to lowercase.
print(string.title()) # Output: This Is A Sample String.
# swapcase() - Swaps the case of each character in the string (uppercase to lowercase and vice versa).
print(string.swapcase()) # Output: tHIS IS A SAMPLE STRING.
# capitalize() - Capitalizes the first character of the string.
print(string.capitalize()) # Output:  This is a sample string.
# find(substring) - Returns the index of the first occurrence of 'substring' in the string, or -1 if not found.
print(string.find("sample")) # Output: 10 (index of the first occurrence of "sample")
print(string.find("good")) # Output: -1 (not found)
# count(substring) - Returns the number of occurrences of 'substring' in the string.
print(string.count("the")) # Output: 0 (not found)
print(string.count("is")) # Output: 2 (occurrences of "is")



#practice 2
#first_name = input("Enter your first name: ")
#print(len(first_name))

string = "this is dollar $$$$"
print(string.count("$"))

#conditional statements - if, elif, else
# Conditional statements allow you to execute different blocks of code based on certain conditions. 
# The basic syntax is:  if-elif-else

#elif is used to check multiple conditions in sequence when if condition turns out false, and else is used as a fallback if none of the previous conditions are met.
#in case if statement turns out to be true, the rest of the conditions are not checked.
mango = 100
if (mango>= 80):
    print("Mangoes sales are high")
elif (mango >= 40):
    print("Maybe buy maybe not")
else:
    print("Dont buy")


age = 21
if (age>=18):
    print("you can vote")
elif (age>=16):
    print("you can drive")
else:
    print("you are too young to vote or drive")



hunger = 50 
if (hunger <=40 and hunger >= 60): #a range condition where 'and' is used to check range in between
    print("You are not too hungry or too full")
elif (hunger>= 40):
    print("You are hungry")
else:
    print("You are full")

marks = 100
if marks>=90:
    print("Grade A")
elif marks>=80:
    print("Grade B")
elif marks>=70:
    print("Grade C")
elif marks>70:
    print("Grade D")

# Nested if statements allow you to check conditions within other conditions.
# Example:
number = 10
if number > 0:
    print("Positive number")
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

# Ternary operator allows you to write a simple if-else statement in a single line.
# Syntax: value_if_true if condition else value_if_false


#practice3
number = 49
if number % 7 == 0:  # Check if the number is divisible by 7
    print("Number is divisible by 7")
else:
    print("Number is not divisible by 7")

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter a third number: "))
if a>b and a>c:
    print("a is the largest number")
elif b>a and b>c:
    print("b is the largest number")
elif c>a and c>b:
    print("c is the largest number")
