''' Assignment 3
Anirudh Ralhan, bt21107091'''
from math import *

# Question 1

print("Question 1")
num = int(input("Enter an integer : "))
binnum = str(bin(num))
print("The given integer in binary is : ",binnum[2:])
print("----------------------------------------------------")

# Question 2

print("Question 2")
inpstr = str(input("Enter Expression to be evaluated : "))
evalstr = eval(inpstr)
print("Evaluated expression equals ",evalstr)
print("----------------------------------------------------")

# Question 3

print("Question 3")
print("(a) : ", (3*4)*5)
n = float(input("Enter value of n : "))
print("(b) : ", (n*(n-1))/2)
r = float(input("Enter value of r : "))
print("(c) : ",4*pi*(r*r))
r_2 = float(input("Enter value of r : "))
a = float(input("Enter value of a in radians : "))
b = float(input("Enter value of b in radians : "))
print("(d) : ", sqrt((r_2*(cos(a))*(cos(a))))+(r_2*(sin(b))*(sin(b))))
y2 = float(input("Enter value of y2 : "))
y1 = float(input("Enter value of y1 : "))
x2 = float(input("Enter value of x2 : "))
x1 = float(input("Enter value of x1 : "))
print("(e) : ",(y2-y1)/(x2-x1))
print("----------------------------------------------------")

# Question 4

print("Question 4")

alist = []
for i in range(5):
    alist.append(i)
print("a : ",alist)

blist = []
for i in range(3,10):
    blist.append(i)
print("b : ",blist)

clist = []
for i in range(4,13,3):
    clist.append(i)
print("c : ",clist)

dlist = []
for i in range(15,5,-2):
    dlist.append(i)
print("d : ",dlist)

elist = []
for i in range(5,3):
    elist.append(i)
print("e : ",elist)

print("----------------------------------------------------")

# Question 5

print("Question 5")
catoms = int(input("Enter number of carbon atoms : "))
oatoms = int(input("Enter number of oxygen atoms : "))
hatoms = int(input("Enter number of hydrogen atoms : "))
molwt = (catoms*12.0107)+(hatoms*1.00794)+(oatoms*15.9994)
print("Molecular weight is : ",molwt)
print("----------------------------------------------------")
    
