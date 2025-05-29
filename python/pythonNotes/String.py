# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 14:09:44 2024

@author: yingj
"""

s="hello"
t='goodbye'

s='He said, "hello, world"'
print(s,t)

a = "Many single quotes here '''''''  and here ''' but correct."
print(a)

s1 = """This
is a multi-line
string."""


s1=''' e
a
d'''

print(s1)


s0='oh \n no'
print(s0)


j='i dont know \\'
print(j)

x = "*\t*\n**\t**\n***\t***\n"
print(x)

y = 'oh no, what\'s going on? '
print(y)

q="zeng \t zeng?"
print(q)


ss = "Hello!"
print(len(ss))
print(ss*8)


ee="23"
ee=int(23)
print(ee)


sac="23"
sac=float(sac)
print(sac)

#'abc' 'def' legal 
print('apple', 'banana', 'cherry', sep=' x ')
print('cat', 'dog', 'bird', sep=' | ', end='!\n')


print("Enter a number")
x = float(input())
print('The square of', x, 'is', x*x)

sp=" 'a b' ' " 'ok'
print(sp)

xx=input("Enter love:")
print(xx)


xy = input("Enter an integer ")
xy = int(xy)
print(xy+2)





#type 64, ''no space
x = int(input('Enter an integer ==> '))
y = x // 10
z = y % 10
print(x, ',', y, z, sep='')

n=int(input("Enter 4: \n"))
s1='10'
s2=s1*(n-1)+'1'
print(s2)
