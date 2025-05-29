# -*- coding: utf-8 -*-


print( len('RPI Puckman'))  #字符串长度 11


"""
y=f(x)
y=f(x,x1,x2,x3)
y-return value    x1,x2-parameter
y1,y2,..ym=f(x1,x2,..)
有时候python可以返回2个值。。。function
"""


#def  name of function (input paramaters):                         冒号-colon， underscore 下划线
#indented 缩进的, 缩进结束是一个function的结束


#a(r)=πr^2
def area_circle (radius):
    pi = 3.14159
    area= pi* radius ** 2
    return area   #stop the function and return value 已经结束了

a1=area_circle(10)  #这一行开始运行，前面的func只是被定义
print("area:", a1)

#+ can only concatenate连结 str, 所以这里只能用逗号

#在def下面第一行设置红点，还有带入数值func的地方点红点，然后debug

a = area_circle(1)
print(a)

print(f'A circle with radius 2 has area {area_circle(2):.2f}')
print('A circle with radius 2 has area {:.2f}'.format(area_circle(2)))
r = 75.1
a = area_circle(r)
print("A circle with radius {:.2f} has area {:.2f}".format(r,a))
print(f"A circle with radius {r:.2f} has area {a:.2f}")    


#F=C * 9/5+32
#C=(F-32)*5/9
#摄氏度华氏度转换

def to_f(c):
    f=c*9/5+32
    return f
print("100 degree of Farenheit is:", to_f(100))


#cylinder的表面积
import math

def area_circle(radius):
    #派r方
    return math.pi * radius ** 2

def area_cylinder(radius,height):
    #直接把func拿过来用
    circle_area = area_circle(radius)
    height_area = 2 * radius * math.pi * height
    return 2*circle_area + height_area



#下面的code叫driver code
#两位小数
'''
语句在 Python 中用于判断当前脚本是直接运行还是作为模块被导入。

当脚本是直接运行时，__name__ 的值会是 "__main__"，所以这个判断语句为真，
里面的代码就会执行。

如果这个脚本是被别的脚本导入的，那么 __name__ 的值不会是 "__main__"，
该块中的代码将不会执行。
'''
if __name__ =="__main__":
    print('The area of a circle of radius 1 is', round(area_circle(1),2))
    r = 2
    height = 10
    print('The surface area of a cylinder with radius', r)
    print('and height', height, 'is', round(area_cylinder(r,height),2))


#计算长方形的面积 ：D
def areaSquare (length, width):
    return length*width
print("Area of square with length  2 and width 1 : {:.2f}".format(areaSquare(2, 1)))
l=2
w=1
print(f"Area of square with length {l:.2f} and width {w:.2f}: {areaSquare(2,1):.2f}")


#计算长方形的面积 ：（
def rect_area(l,w):
    return l*w

def invoke_rect_area(l,w):
    #call 3 次，加起来面积3倍
    y=rect_area(l,w)
    y+=rect_area(l,w)
    y+=rect_area(l,w)
    return y
#if 后面有冒号
if __name__ =="__main__":
    ans=invoke_rect_area(10, 15)
    print(ans)  #450


# y=mx+b

def scale(raw,m,b):  #比例尺
    return raw*m+b

if __name__ == "__main__":
    print(scale(50, 1.75, 25))
    print(scale(0, 2.5, 50))



#复习！
#  优先 4**（2**3） - 4**8
1 + 2 * 3 / 3 * 4**2 **3 - 3 / 3*4
#131069.0
#/除号永远返回float
#所以这一行返回的是float



one = 2
two = 1
three = 4
one += 3 * two #one=one+3*1=5
two -= 3 * one + three   #3*5+4=19   1-19=-18
print(two) #-18


def regenerate_doctor(doctor_number):
    return doctor_number+1

def regenerate_tardis(doctor_number):
    print ("Tardis is now ready for doctor number", doctor_number)
    #无return statement, 打印完上一句就返回none
def eliminate_doctor(doctor_number):
    return 0 #已经return就终止function了，下面一句话打印不出了
    print ("You will be eliminated doctor", doctor_number)
    
if __name__ == "__main__":
    print(regenerate_doctor(3))
    print(regenerate_tardis(4)) 
    print(eliminate_doctor(5))



#celsius to farenheit

def convert2fahren(c, minFar_c):
    c_far= 9*c/5+32
    if c_far < minFar_c:
        return minFar_c
    return c_far

print('0 ->',convert2fahren(0,459.67))
print('32 ->',convert2fahren(32,459.67))
print('100 ->',convert2fahren(100,459.67))
print('1000 ->',convert2fahren(1000,459.67))


#无return的func
def frame_string (str):
    l=len(str)
    print('*'*(l+6))
    print('** '+str+' **')
    print('*'*(l+6))
    

   

if __name__ == "__main__":
    frame_string('Spanish Inquisition')
    print() #空一行
    frame_string('Ni')
    print()
    #怎么打出none，就把无return的func print出来，而不是直接call
    print(frame_string('Euphoria'))
    
    
    



    
import math

def area_circle(radius):
    
    '''
    This function returns the area of a circle with a given radius.
    
    radius is the input parameter
    '''

    area = math.pi * radius ** 2 
    return area 

def area_cylinder(h, r):
    '''
    Give a height h and radius r, return the surface area of a cylinder.
    '''
    cap_area = 2 * area_circle(r)
    rect_area = 2* math.pi * r * h
    return cap_area + rect_area

#Any other function

if __name__ == "__main__": #guard
#driver code
    
    r = float(input("Enter radius (float) => "))
    h = float(input("Enter height (float) => "))
    print("Surface area is: {:.2f}".format(area_cylinder(10,12)))
    print("Volume is: {:.2f}".format(h * area_circle(r)))
    
    
#让用户输入取消两边的空格
name = input('Enter a name ==> ').strip()
print(name)

'''
速输入 速打印
'''
name = input('Enter a name ==> ')
print(name)
email = input('Enter an email ==> ')
print(email)


'''
不要用F string了，忘掉他！！！！！
不要用F string了，忘掉他！！！！！
不要用F string了，忘掉他！！！！！
'''