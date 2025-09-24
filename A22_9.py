#1,a,@,1,a,@.

"""
x=int(input("enter x "))
for i in range(x-1):
    if i%3==0:
        print(1,end=",")
    elif i%3==1:
        print("a",end=",")

    elif i%3==2:
        print("@",end=",")
if (x-1)%3==0:
    print(1,end=".")
elif (x-1)%3==1:
    print("a",end=".")
elif (x-1)%3==2:
    print("@",end=".")
"""

#1,a,@,1,a,@
"""
x=int(input("enter x "))
for i in range(x):
    if i==x-1:
        if (x - 1) % 3 == 0:
            print(1, end=".")
        elif (x - 1) % 3 == 1:
            print("a", end=".")
        elif (x - 1) % 3 == 2:
            print("@", end=".")
    else:
        if i%3==0:
            print(1,end=",")
        elif i%3==1:
            print("a",end=",")
        elif i%3==2:
            print("@",end=",")
"""

#alternative number even numbers
"""
a=int(input("enter a"))
b=int(input("enter b"))
c=0
for i in range(a+1,b):
    if i%2==0:
        if c%2==0:
            print(i,end=" ")
        c+=1
"""

#1 fit bit fit fitbit fit bit fit bit fitbit
#1  2   3   4    5     6   7   8   9    10
"""
x=int(input("enter x "))
for i in range(1,x+1):
    if i%10==1:
        print(1)
    elif i%5==0:
        print("fitbit")
    elif i%2==0:
        print("fit")
    else:
        print("bit")
"""

#1 fit bit fit fitbit bit fit bit fit fitbit
#1  2   3   4    5     6   7   8   9    10
"""
x=int(input("enter x "))
flag=0
for i in range(1,x+1):
    if i%10==1:
        print(1)
    elif i%5==0:
        print("fitbit")
        if flag==1:
            flag=0
        else:
            flag=1
    elif ii%2==flag:
        print("fit")
    else:
        print("bit")
"""

"""
flag=0
if flag:
    flag = 0
    print(flag)
else:
    flag = 1
    print(flag)
"""


#find the number of steps to convert 'x' input to zero
# if it is odd subtract by '1' or divide by 2
"""
x=int(input("enter x "))
mets=0
while x!=0:
#while x>0:
    if x%2==0:
        x//=2
    else:
        x=x-1
    mets+=1
print(mets)"""


#print 1,2,4,7,11,16,,22,,29 series  till x input
#
#
"""
x=int(input("enter x "))
count=1
print(count,end=" ")
for i in range(1,x):
    count+=i
    if count<=x:
        print(count,end=" ")
"""

##print 1,2,4,7,11,16,,22,,29 series  till x input

x=int(input("enter x "))
new=1
diff=1
while new<=x:
    print(new,end=" ")
    new+=diff
    diff+=1

