# for else

"""
for i in range(1,11):
    if i%2==0:
      print(i,end=" ")
else:
    print("anu")
"""
from itertools import count
from operator import index

# break

"""
for i in range(8):
    if i==7:
        break
    print(i, end=" ")
else:
    print("anu")


#continue
for i in range(9):
    if i==7:
        continue
    print(i, end=" ")
else:
    print("anu")
"""

# pass
"""
for i in range(9):
    if i==7:
        pass
    print(i, end=" ")
else:
    print("anu")
"""

"""
#strings

# 1)'',2)" ",3)""" """

print("hello\'anu" ,end=" ")
print("world")

a=""""""
print(a)
print(type(a))

a='anu'
print(a)
print(type(a))

a="anu"
print(a)
print(type(a))

#streams

a=b'7'
print(a)
print(type(a))

#raw text

a=r"anu\nDurga"
b=R"anu\tDurga"
print(a)
print(type(a))
print(b)
print(type(b))

#f string

first=input("enter first ")
second=input("enter second ")
print(f'this {first} ,{second} very time')

x=99.8341360
print(f"anu is {x:.2f}")


#{}
name="nnn"
age=18
print("hi,welcome to is {}".format("cv corp"))
print("hi,{1} welcome to is {0}".format(name,age))


#format %s,%r
name="tttt"
age=18
print("hi,welcome %r to is %s"%(name,age))
"""

"""
#string slicing
a="anu durga"
b="ffiiaaa"
print(a[0:6:2])
print(b)


#index
a="anu"
print(a[2])

#length
a="anu durga adapa"
print(len(a))

#upper
a="anuDurga"
print(a.upper())

#lower
a="anuDiuraga"
print(a.lower())

#title
a="anu,Durga dddd ffafaaf"
print(a.title())

#reverse
a="anudurga"
print(a[ : :-1])


#strip,rstrip,lstrip
a="...anu durga adapa is the good..."
print(a.strip())
a="...anu durga adapa is the good..."
print(a.strip("."))

a="...anu durga adapa is the good..."
print(a.rstrip())
a="...anu durga adapa is the good..."
print(a.rstrip("."))

print(a.lstrip())
a="...anu durga adapa is the good..."
print(a.lstrip("."))
a="...anu durga adapa is the good..."


#concenation
a="anu durga adapa "
b="annnnn bbababaab"
print(a+b)


#join
l=["anu","Durga","kkkk"]
jo=",".join(l)
print(jo)

l=["anu","Durga"]
jo=" ".join(l)
print(jo)


#split

#deafault split space
a="anu durga adapa is the good..."
b=a.split()
print(b)

#specific separator
a="anu,durga,adapa,is,the,good..."
p=a.split(",")
print(p)

#newline
a="anu\ndurga\nadapa\nis\nthe\ngood..."
b=a.split("\n")
print(b)

#split with limit==>maxslpit
a="anu,durga,adapa,is,the,good..."
b=a.split(",",2)
print(b)


#opposite of join()
#split ---- breaks string into list
#join ---- combines list into string
a="I Love Python"
b=a.split()
print(b)

c=" ".join(b)
print(c)


#find
a="anu djjj jjd  djdhdd"
print(a.find("u"))
print(a.find("jj"))

#index
a="anuhhd dhdhhded dhdh"
b=a.index("h")
print(b)


#rfind==>starts at index 4 but rfind() gives 20 last one
a="anu djjj kkkkdjdhdd djjj"
b=a.rfind("djjj")
print(b)


a="anu djjj kkkkdjdhdd djjj"
b=a.rfind("djjj",0,14)
print(b)
"""

# reverse number
""""
x=int(input("enter number:"))
rev=0
while x!=0:
    rem=x%10
    rev=rev*10+rem
    x=x//10
    print(rem,end="")


print(3//10)
print(3%10)"""

# find all the values and
# number of values for each of 6 and 9 divisible by '6' and '9' in the range 10 to 100
"""
count_6 = 0
count_9 = 0
count_both = 0
for i in range(10, 101):
    if i%6==0 and i%9==0:
        print(i,end="\n")
        count_both += 1
    if i%6==0:
        count_6 += 1
    if i%9==0:
        count_9 += 1
print("both count:",count_both)
print("count6:",count_6)
print("count9:",count_9)
"""

#prime or not prime
"""
x=int(input("enter number:"))
c=0
for i in range(1,x+1):
    if x%i==0:
        c+=1
if c==2:
    print("prime")
else:
    print("not prime")
"""

#print the series till "z"
#a c e g i k m o q
"""
x=int(input("enter number:"))
for i in range(0,x,2):
    print(chr(97+i),end=" ")
"""

#print the series 'z'
# a c f j o u
pos=1
step=2
x=int(input("enter number:"))
for i in range(0,x+1):
    print(chr(pos+96),end=" ")
    pos+=step
    step=step+1
