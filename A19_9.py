# Loop through numbers from 1 to 10
for i in range(1, 11):  # Generates numbers: 1,2,3,4,5,6,7,8,9,10
    # If the number is 10, print it without a trailing comma and end with a dot
    if i == 10:
        print(i, end=".")  # Prints 10.
    # If the number is even (2,4,6,8), print it followed by a comma
    elif i % 2 == 0:
        print(i, end=",")  # Prints even numbers with a comma



"""
solution 1

#2,4,6,8,10.
x=int(input("Enter x:"))  #4  #7
for i in range(1,x):  #1,2,3  #1,2,3,4,,6,7
    if x%2==0:            #4%2==0: ,4%2==0:
        if i == x - 2:  # step1-->1==4-2 ,step2--->2==4-2
            print(i, end=".") #.
        elif i % 2 == 0:  # 1%2==0: ,2%2==0:,3%2==0:,4%2==0:
            print(i, end=",") #.
    else:
        if i == x - 1:  # 1==7-1,2==7-1,3==7-1,4==7-1,5==7-1,6==7-1
            print(i, end=".") #.
        elif i % 2 == 0:  # 1%2==0 ,2%2==0:,3%2==0:,4%2==0:,5%2==0:,6%2==0:
            print(i, end=",") #2,4,6
"""



"""
solution 2
answer:2,4,6,8,10.

x=int(input("Enter x:"))
if x%2==0:
    for i in range(1,x):
        if i==x-2:
            print(i,end=".")
        elif i%2==0:
            print(i,end=",")
else:
    for i in range(1,x):
        if i==x-1:
            print(i,end=".")
        elif i%2==0:
            print(i,end=",")

solution 3
answer:2,4,6,8,10.
x=int(input("Enter x:"))
x=int(input("Enter x:"))
l=0
if x%2==0:
    l=x-2
else:
    l=x-1
for i in range(1,x):
    if i==l:
        print(i,end=".")
    elif i%2==0:
        print(i,end=",")
"""
#solution 4

a=2
b=0
x=int(input("Enter x:"))
if x%2==0:
    b=x-2
else:
    b=x-1
for i in range(a,b,2):
    print(i,end=",")
print(b,end=".")


#odd number
a=int(input("Enter a number: "))
l=0
if a%2!=0:
    l=a-2  
else:
    l=a-1
for i in range(1,a):
    if i==l:
        print(i,end=".")
    elif i%2!=0:
        print(i,end=",")        










""""
a=int(input("Enter a:"))
for i in range(1,a):
    if a%2==0:
        if i==a-2:
            print(i,end=".")
        elif i%2==0:
            print(i,end=",")
    else:
        if i==a-1:
            print(i,end=",")
        elif i%2==0:
            print(i,end=",")


a=int(input("Enter a:"))
if a%2==0:
    for i in range(1,a):
        if i==a-2:
            print(i,end=".")
        elif i%2==0:
            print(i,end=",")
else:
    for i in range(1,a):
        if i==a-1:
            print(i,end=".")
        elif i%2==0:
            print(i,end=",")



a=int(input("Enter a:"))
b=0
if a%2==0:
    b=a-2
else:
    b=a-1
for i in range(1,a):
    if i==b:
        print(i,end=".")
    elif i%2==0:
        print(i,end=",")


#alternative number even
a=int(input("Enter a:"))
c=0
for i in range(4,a+1,2):
    if c%2==0:
        print(i,end=" \n")
    c+=1


#alternative number odd
a=int(input("Enter a:"))
c=0
for i in range(1,a+1,2):
    if c%2!=0:
        print(i,end=" \n")
    c+=1

print(0%2!=0) #false
print(1%2!=0)  #true
print(2%2!=0)  #false
print(3%2!=0) #true"""

""""

# answer ===> 1 a @ 1 a @
a=int(input("Enter a:"))
for i in range(0,a):
    if i%3==0:
        print("1",end=" ")
    elif i%3==1:
        print("a",end=" ")
    elif i%3==2:
        print("@",end=" ")"""
"""
print(0%3)
print(1%3)
print(2%3)
print(3%3)
print(4%3)
print(5%3)"""

#answer  1 a @ 1 a @
a=int(input("Enter a:"))
c="1"
for i in range(0,a):
    print(c,end=" ")
    if c=="1":
        c="a"
    elif c=="a":
        c="@"
    else:

        c="1"

