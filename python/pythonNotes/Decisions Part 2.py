'''lec11_Decisions Part 2'''



'''help with debugging'''
n = int(input("Enter a positive integer ==> "))
total = 0 #from 0 to n-1 加起来
i = 0
while i != n:
    total += i
    i += 1
print('Sum is', total)


#n=5 total=10 加起来0-4
#4 3 2 1 0
#有一个问题，n如果是负数，永不停止


#breakpoint 红色圆圈先点在total+=i这行，debug然后会运行然后停在这里，然后点掉之前的breakpoint再breakpoint最后一行print，
#再continue execution until next breakpoint，再到下一个地方看variable


if __name__ == "__main__":
    print("你的测试案例：")
    # Put the main body of the program below this line

'''random walk'''

import random 

# Print three numbers randomly generated between 0 and 1.
print(random.random()) #随机0-1的float
print(random.random())
print(random.random())

# Print a random integer in the range 0..5
print(random.randint(0,5)) #随机0-5的整数，包括5
print(random.randint(0,5))
print(random.randint(0,5))

'''
1---------N//2---------N
假设1-N （整数）总共这么多steps，我们从N//2中间开始走，我们可以向1走，也可向N走,如果我们的数<1 or >N，会摔落悬崖
goal:how many steps it takes to 摔落
'''


random.random() #随机0-1小数，大于0.5，小于0.5      returns a value less than 0.5 step backward; otherwise step forward. 都是走一步
random.randint(0,1) #从0-1的整数    returns 1 then step forward; otherwise, step backward.
random.choice([-1,1]) #从列表中选择内容 returns (it will return either -1 (step backward) or 1 (step forward)).


import random
def simulate_walk(N):
    start_pos=N//2 #从中间开始
    steps=0 #统计走了几步
    
    current_pos=start_pos

    Fallen=False #flag 一般false,然后loop里面true了就停下
    
    while not Fallen:
        val=random.randint(0,1)
        if val==0:
            current_pos-=1  #向左一步
            print("Step back")
        else:
            current_pos+=1 #向右边一步
            print("Step forward")
        steps+=1 #统计步数+1
        
        if current_pos <1 or current_pos > N:
            Fallen=True #摔落，退出
    return steps #返回最后的步数
 
if __name__=='__main__':
    N=int(input("Enter N:"))
    print("The steps you take to fall:",simulate_walk(N))



'''Review of Boolean Logic'''
'''

 and  双T/1
 or 有T/1
 

DeMorgan’s Laws Relating and, or, not
疑似无人在意哈
not (ex1 and ex2) == (not ex1) or (not ex2)
not (ex1 or ex2) == (not ex1) and (not ex2)
ex1 and (ex2 or ex3) == (ex1 and ex2) or (ex1 and ex3)
ex1 or (ex2 and ex3) == (ex1 or ex2) and (ex1 or ex3)



Short-Circuited Boolean Expressions

x1 and ex2 有一个F了，就已经F,不执行了
ex2 will not be evaluated if ex1 evaluates to False. Think about why.


ex1 or ex2 有一个T了，就已经T
ex2 will not be evaluated if ex1 evalues to True.


if ex1:
    if ex2:
       blockA
    elif ex3:
       blockB (ex1=T ex2=T ex3=F)
elif ex4:
    blockD
else:
    blockE (ex1=F)



if x>5 and y<10:
    if x<5 or y>2: #y>2
        if y>3 or z<3:
            print 1   #x>5, 2<y<10
    else:
        print 2
'''


f = float(input("Enter a Fahrenheit temperature: "))
is_below_freezing = f < 32.0 #create a boolean 然后assign再用它
if is_below_freezing:
    print("Brrr.  It is cold")


bmi=int(input("BMI: "))
age=int(input("Age: "))
slim = bmi < 22.0
young = age <= 45

if slim and young:
    print("low")
elif not(slim) and young:
    print("Medium")
else:
    print("剩下的")
    
    
    
    
'''
自学重要！！
'''
'''list解包'''
# 创建一个列表
my_list = [1, 2, 3]

# 解包列表
a, b, c = my_list

print(a)  # 输出: 1
print(b)  # 输出: 2
print(c)  # 输出: 3

'''tuple 解包'''

my_tuple = (4, 5,6)

# 解包列表
a, b, c = my_tuple

print(a)  # 输出: 4
print(b)  # 输出: 5
print(c)  # 输出: 6

(a,b,c)=(7,8,9)
print(a)  # 输出:7
print(b)  # 输出: 8
print(c)  # 输出:9


'''区分'''
a,b=1,2 #这是同时赋值，不是tuple
a,b,c=1,2,3


# 左对齐，字段宽度10
print("{:<10}".format("text"))  # 'text      '

# 右对齐，字段宽度10
print("{:>10}".format("text"))  # '      text'

# 居中对齐，字段宽度10
print("{:^10}".format("text"))  # '   text   '


# 固定宽度10，右对齐整数
print("{:>10}".format(123))  # '       123'

# 浮点数保留两位小数，宽度12，右对齐
print("{:>12.2f}".format(123.456))  # '     123.46'

# 浮点数保留一位小数，宽度6，居中对齐
print("{:^6.1f}".format(7.89))  # '  7.9 '

