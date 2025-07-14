print("hello world")
x=10
y=20
x=y
y=30
print(x)

a = 5
b = 2
a += b * 3
print(a)
#BODMAS
#2*3=6 = 5+6 =11

num = "100.5"
converted = float(num)
print(int(converted))
# concept of truncate is used here 
#Truncate = Chop off the decimal part, keep only the whole number
#Compare Truncate vs Round:
#Operation	Input	Output
#int(4.9)	4.94  (truncated)
#round(4.9)	4.95  (rounded)

list = [1,2,3,4]
print(len(list)) #unlike indexing it wont start from 0 - counts as a whole element

data = ('n', 'o', 'o', 'n')
if data == data[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

a = {1, 2, 3}
b = {3, 4, 5}
print(a.intersection(b))
a.update(b)
print(a)


t = (1, 2, 3, 4)
print(t[-3:])

name = "Awesome"
print(name[::-2])#here every second element is skipped


colors = ["red", "blue", "green"]
colors.insert(1, "yellow")
print(colors) #it would print yellow at 1st index and not 1 in the list

#name = input("Enter your name: ")
#print(f"Welcome, {name}!")


d = {"x": 10, "y": 20}
d["z"] = 30
print(d)

data = {"stu1": {"name": "Maui"}, "stu2": {"name": "Arya"}}
print(data["stu2"]["name"])


# #Write a Python program that asks the user to input numbers in a loop. If a number is a multiple of 7, print "Found a multiple of 7!" and break the loop. Otherwise, continue asking for numbers.
# num = int(input("enter a number : "))
# while num >= 0:
#     if num // 7 == 0:
#         break
#     print("Found a multiple of 7!")
#     if num // 7 != 0:
#         continue


# while True:
#     word = input("enter a word")
#     if word == "stop":
#         break
#     print(word)

i = 0
while i <= 5:
    print(i)
    i += 1

a = 0
while a <= 5:
    print(a*a)
    a +=1

i = 1
total = 0

while i <= 5:
    total += i
    i += 1

print("Sum =", total)


i = 1
sum = 0
while i <= 5:
    sum +=i
    i +=1
print(sum)


i = 5
while i>=1:
    print(i)
    i -= 1

i = 0
while i<=10:
    if i % 2==0:
        print(i)
    i += 1


i = 1
factorial = 1
while i <= 5:
    factorial = factorial * i
    i +=1
print(factorial)



sum = 0
while True:
    num = int(input("enter a number: "))
    
    if num == 0:
        break
    sum += num
print(sum)

attempt = 0
while attempt <3:
    password = input("enter password: ")
    if password == "open123":
        print("access granted")
        break
    else:
        print("wrong password")
        attempt +=1
    if attempt == 3:
        print("Too many attempts. access denied.")