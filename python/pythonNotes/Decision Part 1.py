
#去除输入内容首尾的空格
user_input = float(input("Enter float: ").strip())
print(user_input)





#比较身高~
#输入数据
chris_height = float(input("Enter Chris's height (in cm): "))
sandy_height = float(input("Enter Sandy's height (in cm): "))

#max(variable_a, variable_b, variable_c) 会选出最大的值
print("The greater height is", max(chris_height,sandy_height))

#用if - else 语句
'''
if a > b:
    ...
else:
    ...
'''

chris_height = float(input("Enter Chris's height (in cm): "))
sandy_height = float(input("Enter Sandy's height (in cm): "))

if chris_height > sandy_height:
    print("Chris is taller")
else:
    print("Sandy is taller")
   
    
   
# True False and or   
age = 20
has_id = True

#if 语句后面的条件表达式必须为 True，代码块才会执行。
if age >= 18 and has_id:
    print("You are allowed to enter.")
else:
    print("You are not allowed to enter.")

if age >=18 or has_id:
    print("Perhaps you may come in")




#比大小~
x = 17
y = 15.1
print( x < y)
#False
print( x <= y)
#False
print( x <= 17)
#True
print( y < x)
#True

'''
ABC..abc...
大写在小写前面，所以大写<小写
A在M前面， A<M
大写Art在小写music前面
大写Music在小写art前面

'''
s1 = 'art'
s2 = 'Art'
s3 = 'Music'
s4 = 'music'
print( s1 < s2)
#False
print(s2 < s3)
#True
print( s2 < s4)
#True
print(s1 < s3)
#False


#！= 不等于  ==等于  < > <= >= Boolean              注意！！  = 赋值 

#lec6 ex1
a = 1.6
b = -1.7
c = 15
s = 'hi'
t = "good"
u = "Bye"
v = "GOOD"
w = "Bye"
y = 15.1

print(a < b)          # A 1.6>-7    False
print(a < abs(b) )       # B 1.6<1.7    True
print(a >= c )           # C 1.6<15     False
print(s < t )            # D abcdefgh g<h t<s   False
print(t == v )           # E v<t 或者说 v!=t    False
print(u == w )           # F u==w   True
print(b < y )            # G -1.7<15.1  True

#这样上交
#B
#F
#G

#身高比较
name1 = "Dale"
print("Enter the height of", name1, "in cm ==> ", end='') #end='' 不想让他自动换行，到下一行才能输入, 默认end='\n'
#不要忘记int套input外面
height1 = int(input())

name2 = "Erin"
print("Enter the height of", name2, "in cm ==> ", end='')
height2 = int(input())

if height1 < height2:
    print(name2, "is taller")
    #給高的人颁max_height奖
    max_height = height2
    
 #== 两个等号！！   elif=else if
elif height1 == height2:
    print(name1,"and", name2, "is at same height")
    max_height = height2
#else 在if 或者elif 后面
else: 
    print(name1, "is taller")
    max_height = height1

print("The max height is", max_height)


'''
如果你使用 elif，函数只会执行第一个匹配的条件，而不会继续检查后面的条件。
'''

#不要用int() 来取整浮点数！不四舍五入 ，要用round()
#整除a//b = int (a/b)
#string*2 怎么换行
print(('#...#'+'\n')*2+"#####")



#format形式跟在"后面，print括号里面

#注意区别 format形式输出的是字符串，round是个值112.1他把0省略了
print("{:.2f}".format(112.099))  # 输出: "112.10" (字符串)
print(round(112.099, 2))         # 输出: 112.1 (浮点数)

#天气怎么样
cel_today = 12
cel_yesterday = -1
#and 两个都是！
if cel_today > 0 and cel_yesterday > 0:
    print("above 0 celsius both of these days")
#or a-true或者b-true，或者a和b 都true 
if cel_today > 0 or cel_yesterday > 0:
    print("above 0 celsius one of these days")
if cel_today > 0 or cel_yesterday < 0:
    print("a or b or both ab")

'''
and or 逻辑

T and T == true 双1才成立
T and F == false  1,0 不行
F and T == false  0,1 不行
F and F == false  0，0 不行

T or T == true 双1  有1就行
T or F == true  1,0  有1就行
F or T == true  0,1  有1就行
F or F == false  0，0  没1不行


not(T and T)==false
'''





#not
a = 5
b = 10

is_greater = not (a < b) #a<b 是true， not取反
print(is_greater)  # 输出: False


a = 15
b = 20
if not a<b: 
    print("a is not less than b")
else:
    print("a is less than b")
    
    
    
#这是矩形的四个点
'''
x0 ____________ x1
y0|            |
  |            |
  |            |
y1|            |
   ————————————
'''
x0 = 10
x1 = 16
y0 = 32
y1 = 45
x=int(input("Enter x:"))
y=int(input("Enter y:"))


if(x0<x<x1) and (y0<x<y1):
    print(x,y,"are on the rectangle")
else:
    print(x,"or",y,"is not on it")
    
    
    

