name="gk"
age=18
color="red"
count= 30.02
variables = [name, age, color, count]
# The variables are stored in a list []
variables = tuple(variables)  # Convert the list to a tuple [] to () to make it immutable
# This code defines several variables and stores them in a tuple
print(variables)


#arithmetic operations
a=10
b=20
print(a+b)  # Addition
print(a-b)  # Subtraction
print(a*b)  # Multiplication
print(a/b)  # Division
print(a//b)  # Floor Division # (returns the largest integer less than or equal to the division result)
print(a%b)  # Modulus- remainder using %(modulo operator)
print(a**b)  # Exponentiation- a raised to the power of b 


#relational operations
a=10
b=20
print(a==b)  # Equal to - checks if a is equal to b and returns T/F- False
print(a!=b)  # Not equal to
print(a>b)   # Greater than
print(a<b)   # Less than
print(a>=b)  # Greater than or equal to
print(a<=b)  # Less than or equal to    


#assignment operations
a=10
b=20            
a+=b  # a = a + b
print(a)  # 30
a-=b  # a = a - b
print(a)  # -10
a*=b  # a = a * b
print(a)  # -200
a/=b  # a = a / b
print(a)  # -10.0
a//=b  # a = a // b
print(a)  # -1.0
a%=b  # a = a % b
print(a)  # -1.0
a**=b  # a = a ** b
print(a)  # 1.0e-20 (1.0 * 10** -20)


#logical operations
a=True
b=False
print(a and b)  # Logical AND - returns True if both a and b are True
print(a or b)   # Logical OR - returns True if either a or b is True
print(not a)    # Logical NOT - returns True if a is False, and vice versa      
a=10
b=20
print(not (a > b))  # Logical NOT - returns True if a is not greater than b 


#type conversion- done automatically by python
# but can also be done explicitly using the built-in functions int(), float(), str()
a = 10
b = 20.5
c = "30"
# Convert integer to float
a_float = float(a)
print(a_float)  # 10.0
print(type(a), type(b))
print(a+b)
# Convert float to integer      

#type casting- done manually by the user but needs same value type as the variable.
a= "10"
b= 20
# Convert string to integer
a_int = int(a)
print(a_int)  # 10
print(type(a), type(b))
#print(a+b)  # This will raise an error because a is a string and b is an integer
print(a_int+b)


#

#practice 1
a=5
b=10
sum = a+b
print(sum)

a= int(input("enter first number: "))  # This will raise a syntax error because variable names cannot contain spaces
b = int(input("enter second number: "))  # Corrected variable name
print(a>=b)  # This will print the sum of the two numbers