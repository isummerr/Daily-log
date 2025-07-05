#input and output
name = input("enter your name: ")
age = int(input("enter your age: "))
print(f"Hello {name}, you are {age} years old.") #output here alwasy is a string, so we use f-string to format the output
print(type(name), type(age))  # type of name is str and age is int