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
