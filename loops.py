#loops 
#while loop 
i = 1
while i <= 5:
    print("hello")
    i +=1

# i is an iterator (A variable that sets the limit foe a loop)
# where i will repeating till it is <= 5 - is iteration - looping same thing for no of times till it is <=5 or till the condition stands true
# if i want a count of my loops:
i = 1
while i <= 5:
    print("hello", i )
    i +=1

j = 1
while j <=5:
    print(j)
    j +=1 #gives 1,2,3,4,5

# or

j = 5
while j >= 1:
    print(j)
    j -= 1 #gives 5,4,3,2,1

k = 100
while k>=50:
    print(k)
    k -=10

a = 1
while a<=100:
    print(a)
    a+=1

b = 100
while b >= 1:
    print(b)
    b-=1

c = 3
i =1
while i<=10:
    print(c*i)
    i+=1

list = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx< len(list):
    print(list[idx]) #how to find square of numbers in a list/tuple
    idx+=1
#moving to each item individually in a list or tuple - traverse


tuple = (1,49,49,16,25,36,49,64,81,100)
x = 49
i = 0 #initialization
while i < len(tuple):
    if(tuple[i] == x):
        print(True, "at" ,i) # how to print all indexes in a singlw line seperate by ,
    i+=1


#break and contine
#break - to terminate loop when encountered
#continue - terminates execution in current iteration and continues loop execution with next iteration.
a = 1
while a<= 5:
    print(a)
    if (a == 3):
        break
    a +=1

b = 1
while b<= 5:
    
    if ( b == 4):
        b += 1
        continue
    
    print(b)
    b += 1