#prime or not
"""
x=int(input("Enter x:"))                     #prime number or not
if x>1:                                      #x=2==>2>1
    for i in range(2,x-1):
        if x%i==0:                           #2%2==0:
            print("not prime")
            break
    else:
        print("prime")

else:
    print("not a prime")

print(2%2==0)
for i in range(2,1):
   print(i)


#multiples of 3 given range

s=int(input("Enter s:"))
e=int(input("Enter e:"))
for i in range(s,e):
    if i%3==0:
        print(i)
"""
from os import write

#write even numbers in the given range

"""
s=int(input("Enter s:"))
e=int(input("Enter e:"))
for i in range(s,e):
    if i%2==0:
        print(i)"""


#write a program to print the two numbers after swapping

"""
a=int(input("Enter a:"))
b=int(input("Enter b:"))
#temp=a
#a=b
#b=temp

a=a+b
b=a-b
a=a-b
print(a,b)
"""

#write a program to print the multiples of 5
#case 1: if starting range is greater than end range than print "invalid range"

"""
s=int(input("Enter s:"))
e=int(input("Enter e:"))
if s>e:
    print("invalid range")
else:
    for i in range(s,e):
        if i%5==0:
            print(i)"""


#write a program to convert kgs into grams
"""
kg=float(input("Enter a:"))
grams= int(kg*1000)
print(grams)
"""

#write a program to convert celsius temperature  into fahrenheit
"""
cc=int(input("Enter a:"))
ff=float(cc*1.8)+32
print(ff)
"""

#delare and initialize 3 varaiables and print the biggest number
"""
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
if a>b and a>c:
    print(a)
elif b>c and b>a:
    print(b)
else:
    print(c)
"""



#write a program that performs the following tasks
#a.store numbers in a variable
#b.if value is not in range 100-1000 print wrong number else follow the steps
#c.check even or odd
#d.if even divide by 3 print remainder
#e.if odd divide number by 2 and print thr remainder

"""
a=int(input("Enter a:"))
if (a>100 and a<1000):
    if a%2==0:
        print(a%3)

    else:
        print(a%2)
else:
    print("wrong")
"""


#declare and initialize a number .check whether the number is in range (0-100) or not
#if not in range print invalid input.else-if number is in range 90-100 then print super smart,80-90 smart,70-80
#print smart enough,60-70 print just smart print just smart 35-60 print no smart,0-35 print dump

"""
x=int(input("Enter x:"))
if x>=0 and x<=100:
    if x>=90 and x<=100:
        print("super smart")
    elif x>=80 and x<=89:
        print("smart")
    elif x>=70 and x<=79:
        print("smart enough")
    elif x>=60 and x<=69:
        print("just smart")
    elif x>=35 and x<=59:
        print("no smart")
    else:
        print("dump")
else:
        print("invalid")
"""



#in java we are using switch but donot use in python
#we are using the "match" keyword
"""
c=input("Enter c:")
a=int(input("Enter a:"))
b=int(input("Enter b:"))

match c:
    case '+':
      print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b)
    case '/':
        print(a/b)
"""

"""
a=int(input("Enter a:"))
for i in range(1,a,1):
     print("cv corp")
"""

#multiples in 11 between 250 to 550
"""
for i in range(250,550):
    if i%11==0:
        print(i)

print(11*23)
"""

#multiples in 2 between 700 to 900
"""
for i in range(700,900):
    if i%2==0:
        print(i)
"""

"""

#sum of  numbers in a given range
a=int(input("Enter a:"))
b=int(input("Enter b:"))
sum=0
for i in range(a,b):
    sum+=i
print(sum)
"""





