# not multiples in 2 and between 251 to 51
"""
for i in range(251,51,-1):
    if i%2!=0:
        print(i)

print(252%2!=0)
"""
from turtledemo.penrose import start

#
"""start=int(input("enter start number:"))
end=int(input("enter end number:"))
if start>end:
    print("invalid input")
else:
    c=0
    for i in range(start,end):
        if i%11==0:
            print(i)
            c+=1
    else:
        if c==0:
            print("no mutlipes")
"""

# print all even numbers in range 700 to 900
"""
s=int(input("enter start number:"))
e=int(input("enter end number:"))
for i in range(s,e):
    if i%2==0:
        print(i)
"""


# odd number print with ","

"""
s = int(input("enter start number:"))
e = int(input("enter end number:"))
l = 0
if e % 2 != 0:
    l = e
else:
    l = e - 1
for i in range(s, e+1):
    if i == l:
        print(i, end=" ")
    elif i % 2 != 0:
        print(i, end=",")

"""


#odd numbers print with ","
"""
s = int(input("enter start number:"))
e = int(input("enter end number:"))
l = 0
if e % 2 != 0:
    l = e-2
else:
    l = e - 1
for i in range(s, e):
    if i == l:
        print(i, end=" ")
    elif i % 2 != 0:
        print(i, end=",")
"""


#write a program to print the even numbers in a range ,
# if the start>end then swap inputs and print even numbers
"""
s=int(input("enter start number:"))
e=int(input("enter end number:"))
if s>e:
    s,e=e,s
for i in range(s,e+1):
    if i%2==0:
        print(i,end=" ")

"""

"""
s=int(input("enter start number:"))
e=int(input("enter end number:"))
c=0
for i in range(s,e):
    if i%2==0:
        c+=1
if c==0:
    print("no mutlipes")
else:
    print(c)
"""

"""
s=int(input("enter start number:"))
e=int(input("enter end number:"))
c=0
for i in range(s,e):
    if i%2==0:
        c+=1
        if c%2==1:
            print(i,end=" ")
"""


s=int(input("enter start number:"))
e=int(input("enter end number:"))
c=0
for i in range(s,e):
    if i%2==0:
        c+=1
        if c%2==1:
            if c==1:
                print(i,end=",")
            else:
                print(i,end=",")