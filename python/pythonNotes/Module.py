# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 14:02:53 2024

@author: yingj
"""
#绝对值
print(abs(-5))

#2 的三次方
print(pow(2,3))

#int直接去除小鼠，不四舍五入
print(int(5.8)) #5

#四舍五入 是6，精确到个位
print(round(5.5)) #6
print(round(5.2323))

#小数点后太多,精确到小数点后两位 5.56 四舍五入的
print(round(5.555555555555788232738237,2))


-8%3 #-8%3=-3...1 
-9%2 #-9%2=-5...1
-13//2 #-7






#最小值 1
print(min(3,5,6,4,1,96))

#最大值 96
print(max(3,5,6,4,1,96))

#找o, 第一个o,返回index
b="good morning"
print(b.find('o'))  #1
print(b.find('x'))  #-1  因为没有找到
print(b.find('o', 3)) # 6 ,第三个o
b.find("m") #5


#help(str)  //全部的



#大写
name = "Neil Degrasse Tyson"
print(name.lower())
print(name.upper())
print(name.capitalize())
print(name.title())
"""
neil degrasse tyson
NEIL DEGRASSE TYSON
Neil degrasse tyson
Neil Degrasse Tyson
"""
print(name+'!')

#用dr替代br   replace
a="abracadabra".replace("br", "dr")
print(a)


#有几个x
bb="abracadabra".count("x")
print(bb)  #0

#有几个在index3后面的x
bc="abxracaxdabra".count("x",3)
print(bc)  #1

print("  abc s ".strip())  #去掉2边的空格
print("  abc s ".rstrip()) #去掉右边的空格
#lstrip 去掉左边的空格
xb="aaabbbfsassassaaaa".strip("a")
print(xb)
#bbbfsassass，去掉两边的a

"aaabbbfsassassaaaa".replace("a", "")
#去除所有a

#String Format Method
out_string = 'A cylinder of radius {} and height {} has volume {}'.format(1,2,3)
print(out_string)

r=1
h=3
volume=5
out_string = 'A cylinder of radius {0:.2f} and height {1:.2f} has volume {2:.2f}'.format(r, h, volume)
print(out_string)

#help(__builtins__)



#import math lib

import math


print(math.sqrt(43)) #开根号
print(math.trunc(4.5)) # 给你整数，去掉小数 trunc
print(math.ceil(4.1)) # 向上取整 4.0还是4.0 4.1就成5了
print(math.log(1024,2)) #log2 1024=10 2的10次方
#help(math)



from math import sqrt,pi
 #仅import 平方根 和派
print(pi) #这里不需要math.pi了，因为已经from math import pi过了



#Or we can give a new name to the module within our program:

import math as m
print( m.pi)
#3.141592653589793
print( m.sqrt(4))
#2.0




'''
Write a short program to ask the user
 to input height values (in cm) three times. 
 After reading these values (as integers), 
 the program should output the largest, 
 the smallest and the average of the height values.
'''

height1=int(input("Enter height value1: "))
height2=int(input("Enter height value2: "))
height3=int(input("Enter height value3: "))

maxNum=max(height1,height2,height3)
minNum=min(height1,height2,height3)
avg=(height1+height2+height3)/3
#format版本
ans="Largest: {:.2f}, Smallest:{:.2f}, Average:{:.2f}".format(maxNum, minNum,avg)
print(ans)
#f-string 版本
ans=f"Largest: {maxNum:.2f}, Smallest: {minNum:.2f}, Average: {avg:.2f}"
print(ans)




