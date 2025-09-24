#a c f j o u
"""
ch=97
i=2
while ord('z')>ch:
    print(chr(ch),end=" ")
    ch+=i
    i+=1
"""

#
#2 1
#3 1 3 2
"""
for i in range(1,10):
    for j in range(1,i):
        print(i,j,end=" ")
    print(" ")
"""
#prime number given range
"""
for i in range(3,19):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        print(i,end=" ")


#prime number
a=int(input("enter a"))
b=int(input("enter b"))
for i in range(a,b+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")
"""


a = int(input("Enter start of range: "))
b = int(input("Enter end of range: "))
count = 0

for num in range(a, b + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            if count % 2 == 0:
                print(num, end=" ")
            count += 1


#print alternative prime numbers in the range of a and b
#2 5 11 17
a = int(input("Enter start of range: "))
b = int(input("Enter end of range: "))
count = 0
for i in range(a, b + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            if count % 2 == 0:
                print(i, end=" ")
            count += 1


#fib

"""
x=int(input("enter x"))
a=0
b=1
print(a,end=" ")
print(b,end=" ")
for i in range(0,x):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
"""

