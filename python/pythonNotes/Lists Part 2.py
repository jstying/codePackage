L1 = [ 'RPI', 'WPI', 'MIT' ]
L2 = L1
L3 = [ 'RPI', 'WPI', 'MIT' ]
L2.append( 'RIT' ) #屁股后面加上
L2[1] = 'CalTech' #去除WPI，变成caltech
print(L1)
#['RPI', 'CalTech', 'MIT', 'RIT']
print(L2)
#['RPI', 'CalTech', 'MIT', 'RIT']
print(L3)
#['RPI', 'WPI', 'MIT']


#List Aliasing 两个list相等，改变一个，另一个也会被改变，只是指向同一个

L1 = [1,2,3]
L2 = L1.copy() #list副本
L1.pop() #去除3
L2.append( 4 ) #屁股加4
print(L1) #[1,2]
print(L2) #[1,2,3,4]



def add_two(val1, val2):
    val1 += val2
    return val1

val1 = 10
val2 = 15
print(val1, val2) #10 15
print(add_two(val1,val2)) #25
print(val1, val2) #10 15 局部的不会影响全局的


def smallest_two(mylist):
     mylist.sort() #排序 改变了list本身
     newlist = [] #创建新的list
     if len(mylist) > 0: #有第一位吗
         newlist.append(mylist[0]) 
         if len(mylist) > 1: #还有第二位吗
             newlist.append(mylist[1]) #放进去
     return newlist

values = [35, 34, 20, 40, 60, 30]

print("Before function:", values) #[35, 34, 20, 40, 60, 30]
print("Result of function:", smallest_two(values)) #[20, 30]
print("After function:", values) #[20, 30, 34, 35, 40, 60] 经过排序的


'''
Operations that create new lists 怎么创建新的list copy
'''
#slicing
a = [1, 2, 3, 4]
b = a[:]  # 切片操作，创建一个新的列表
b[0] = 10  # 修改 b 不会影响 a
print(a)  # 输出 [1, 2, 3, 4]
print(b)  # 输出 [10, 2, 3, 4]

#copy()
a = [1, 2, 3]
b = a.copy()  # 复制列表
b[0] = 10  # 修改 b 不会影响 a
print(a)  # 输出 [1, 2, 3]
print(b)  # 输出 [10, 2, 3]



'''
其他的方式
'''

#Concatenation (连接 +)
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b  # 创建一个新的列表 c,链接两个list起来
print(c)  # 输出 [1, 2, 3, 4, 5, 6]
print(a)  #  [1, 2, 3]
print(b)  # [4, 5, 6]

# Replication (重复 *)
a = [1, 2, 3]
b = a * 2  # 生成一个新的列表 b, 内部重复两次
a[0]=99
print(b)  # 输出 [1, 2, 3, 1, 2, 3]
print(a) #[99, 2, 3]
print([1]*3) #[1,1,1]




#list()
a = [1, 2, 3] 
b = list(a)  
a[1]=1
print(a) #[1,1,3]
print(b)  #[1, 2, 3]



animals = ['cat', 'monkey', 'hawk', 'tiger', 'parrot']
cap_animals = []
#for x in list: x可以是任何名称，叫loop variable
for animal in animals:
    #新list内放入首字母大写的每个词
    cap_animals.append( animal.capitalize() )
print(cap_animals) #打出新list

def capitalize_list( names ):
    cap_names = []
    for n in names:
        cap_names.append( n.capitalize() )
    names = cap_names #其实还是指向一个，新旧都指向大写后的
    return names

animals = ['cat', 'monkey', 'hawk', 'tiger', 'parrot']
animals=capitalize_list(animals)
print(animals)


def capitalize_list( names ):
    cap_names = []
    for n in names:
        n = n.capitalize()
        cap_names.append(n)
    return cap_names

animals = ['cat', 'monkey', 'hawk', 'tiger', 'parrot']
animals=capitalize_list(animals)
print(animals)



def capitalize_list( names ):
    i = 0
    cap_names = []
    while i < len(names):
        names[i] = names[i].capitalize()
        cap_names.append(names[i])
        i += 1      
    return cap_names

animals = ['cat', 'monkey', 'hawk', 'tiger', 'parrot']
animals=capitalize_list(animals)
print(animals)



def capitalize_list( names ):
    i = 0
    cap_names = []

    for i in range(len(names)): 
        names[i] = names[i].capitalize()   
        cap_names.append(names[i])
    return cap_names

animals = ['cat', 'monkey', 'hawk', 'tiger', 'parrot']
animals=capitalize_list(animals)
print(animals)





fruits = ('apple', 'banana', 'cherry')
# 使用 for 循环遍历元组
for fruit in fruits:
    print(fruit) #打出每个value

text = "Hello, World!"
# 使用 for 循环遍历字符串
for i  in text:
    print(i) #打出每个char，包含空格和符号



#打出0-4
for i in range(5):
    print(i)
    
#convert a range to an actual list
x = list(range(5))
print(x) #[0, 1, 2, 3, 4]



'''
range( bi, ei, ii )

bi is the initial value (defaults to 0) 起始i
ei is the ending value (never included in the range!) 终止i 但不运行到这个i
ii is the increment, added each time (defaults to 1)  递增/减i
'''



print(list(range(3,10))) #3-9 [3, 4, 5, 6, 7, 8, 9] 不到10的
print(list(range(4, 20, 4))) #[4, 8, 12, 16] 不到20的
print(list(range(10, 2, -2)))# [10, 8, 6, 4] 不到2的


#\没写完，下一行继续
co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
  348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]
three_values = co2_levels[2:5] #创建从index 2-4的，终止于5的list
print(three_values)
#[328.07, 333.91, 341.47]
print( co2_levels)
#[ 320.03, 322.16, 328.07, 333.91, 341.47, 348.92, 357.29, 363.77,
 #  371.51, 382.47, 392.95 ]


'''
L[si:ei:inc] 默认空[:] 0-len [::2]0-len,递增2
起始的：终止的：递增的
'''


#str也可以！！！
text = "Hello, world!"
print(text[7:12])  # 输出 'world'



L1 = ['cat', 'dog', 'hawk', 'tiger', 'parrot']

print(L1[1:-1])
#['dog', 'hawk', 'tiger'] #终止于倒数第一个value
print(L1[1:-2])
#['dog', 'hawk']#终止于倒数第二个
print( L1[1:-4])#始于index1，终止于倒数四，同一个，就是没有
#[]
print( L1[1:0])#始于index1，终止于0，没有哈
#[]
print(L1[1:10]) #从1开始，打完就没了哈
#['dog', 'hawk', 'tiger', 'parrot']



L1 = ['cat', 'dog', 'hawk', 'tiger', 'parrot']
L2 = L1[:] #copy L1
L2[1] = 'monkey' #改index1
L3 = list(L1) #copy L1
L3[1] = 'turtle'#改index1
L4=L1.copy()#copy L1


print( L1)
#['cat', 'dog', 'hawk', 'tiger', 'parrot']
print( L2)
#['cat', 'monkey', 'hawk', 'tiger', 'parrot']
print( L3)
#['cat', 'turtle', 'hawk', 'tiger', 'parrot']
print(L4)
#['cat', 'dog', 'hawk', 'tiger', 'parrot'] 和L1一样


'''
practice 3
'''
x = [6,5,4,3,2,1]\
 + [7]*2
y = x #x=y=[6,5,4,3,2,1,7,7]
x[1] = y[2] #64432177
y[2] = x[3] #64332177
x[0] = x[1] #44332177
print(x)  

y.sort() #[4, 4, 3, 3, 2, 1, 7, 7]
print(x) #[1, 2, 3, 3, 4, 4, 7, 7]
print(y) #[1, 2, 3, 3, 4, 4, 7, 7]
#都一块变的


'''
Write a slicing command to extract values 
indexed by 1, 4, 7, 10, etc from a list L0 .
'''

L0=[1,2,3,4,5,6,7,8,9,10,11,12,13]
#index不要搞错！
ex_L=L0[0:12:3]

for i in ex_L:
    print(i)

'''
Converting Strings to Lists
'''

abc = "Hello world"
e = list(abc)  #list_name=list(string_name)
print(e)#每个char作为一个个体
#['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']


'''spilt前面要有assignment，他不是自己改变就可以print出来'''

s = "Hello world"
a=s.split()#按空格分割成多个字符串的列表
print(a)
#['Hello', 'world']



s = "Hello     worl   d" #5个 3个 空格
print(s.split())#大片空格被删去，所在地作为分隔
#['Hello', 'worl', 'd']

print(s.split(' '))#每个单个空格被删，5个连续的空生成4个'',3个连续的空生成2个''
#['Hello', '', '', '', '', 'worl', '', '', 'd']#
s.split('l')#每个l被删，作为分隔,2个连续的l之间生成一个空字符串''
#['He', '', 'o     wor', '   d']



s = "apple,,banana,orange,,grape"
result = s.split(',')
print(result)
#['apple', '', 'banana', 'orange', '', 'grape']

s = "apple\tbanana\torange\tgrape"
result = s.split('\t')
print(result)
#['apple', 'banana', 'orange', 'grape']

s = "apple|banana|orange|grape"
result = s.split('|')
print(result)
#['apple', 'banana', 'orange', 'grape']

'''concatenate a list of strings into a single string'''

'''错误作法'''
s = "Hello world"
t = list(s)       # ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
s1 = str(t)       #只是外面套了双引号 "['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']"
print(s1)         # 打出来还是['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

'''正确作法 '''
s = "Hello world"
t = list(s)
s1 = "".join(t)  #string_name=''.join(list_name) 每个元素直接链接成str
print(s1) #Hello world
s2 = " ".join(t)  # 每个元素后加上空格，链接成str
print(s2) #H e l l o   w o r l d

L1 = [ 'No', 'one', 'expects', 'the', 'Spanish', 'Inquisition' ]
print(''.join(L1))
#NooneexpectstheSpanishInquisition
print(' '.join(L1))
#No one expects the Spanish Inquisition

'''Indexing and Slicing Strings'''

s = "Hello, world!"
print(s[5])
#,
print(s[-1])
#!
s = "Hello, world!"
#H=0 e=1 l=2 l=3 0=4 ,=5 ''=6 w=7 o=8 r=9 l=10 d=11 !=12   len(s)=13
print(s[:len(s):2]) #从index 0开始，终止于length,递增2,切出这一段来，要02468 10 12
#Hlo ol!

'''
string 每个char不能更改
>>> s[4] = 'c'
TypeError: 'str' object does not support item assignment
'''


'''
Part 4 Practice

Rewrite L so that it is a list of lists, 
with household pets in the 0th (sub)list, zoo animals in the first. 
Using slicing of L to create this new list and assign L to the result.
'''
L = [ 'cat', 'dog', 'tiger', 'lion' ]
house=L[:2] #默认0开始
zoo=L[2:] #默认len（L）终止
L=[]
L.append(house)
L.append(zoo)
print(L) #[['cat', 'dog'], ['tiger', 'lion']]
#L = [L[:2], L[2:]] 这个方式更好

#How can you append an additional list of farm animals
# (e.g. 'horse', 'pig' and 'cow') to L?
L2=['horse', 'pig' ,'cow']
L.append(L2)
print(L) #[['cat', 'dog'], ['tiger', 'lion'], ['horse', 'pig', 'cow']]

L2=['horse', 'pig' ,'cow']
L=L+L2
print(L)#[['cat', 'dog'], ['tiger', 'lion'], ['horse', 'pig', 'cow'], 'horse', 'pig', 'cow']

#Write code to remove 'tiger' from the sublist of zoo animals.
zoo.remove('tiger') #or zoo.pop(0)
print(zoo)#['lion']

'''
Suppose you have the string

>>> s = "cat |  dog  | mouse | rat"
and you’d like to have the list of strings

>>> L = [ "cat", "dog", "mouse", "rat"]
Splitting the list alone does not solve the problem. 
Instead, you need to use a combination of splitting, 
and a loop that strips off the extra space characters from each string and 
appends to the final result. Write this code. It should be at most 4-5 lines of Python.
'''
s = "cat |  dog  | mouse | rat"
s1=s.split('|')
s=[]
for i in s1:
    s.append(i.strip())
print(s) #['cat', 'dog', 'mouse', 'rat']



'''
Write a function that returns a list containing the smallest and largest values
 in the list that is passed to it as an argument without changing the list?
 Can you think of several ways to do this?
'''

#Using min and max
def min_max_values(lst):
    return [min(lst), max(lst)]

#Using sorting (but remember, you can’t change the original list)
def min_max_values_sorted(lst):
    sorted_list = sorted(lst)  # Create a sorted copy of the list
    return [sorted_list[0], sorted_list[len(sorted_list)-1]] #sorted_list[-1]也可

#Using a for loop that searches for the smallest and largest values.
def min_max_values_loop(lst):
    '''
    if not 的作用
    以下对象被视为假值（False）：
    None
    0（任何数字的零值）
    空序列（如 ''、[]、() 等）
    空字典 {}
    '''
    
    
    
    if not lst:  # Check if the list is empty
        return []  # Return an empty list if it is
    smallest = largest = lst[0]  # Initialize both smallest and largest链式赋值
    for item in lst:
        if item < smallest:
            smallest = item
        if item > largest:
            largest = item
    return [smallest, largest]

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

print(min_max_values(my_list))         # Output: [1, 9]
print(min_max_values_sorted(my_list))  # Output: [1, 9]
print(min_max_values_loop(my_list))    # Output: [1, 9]



L1 = [ 1, 5, [5, 2], 'hello' ]
L2 = L1 #[ 1, 5, [5, 2], 'hello' ]
L3 = L1.copy() #[ 1, 5, [5, 2], 'hello' ]
L2.append( 4 ) #[ 1, 5, [5, 2], 'hello' , 4]
L1.append( 3 )#[ 1, 5, [5, 2], 'hello' , 4, 3]
print(L1) #[ 1, 5, [5, 2], 'hello' , 4, 3]
print(L2) #[ 1, 5, [5, 2], 'hello' , 4, 3]
print(L3) #[ 1, 5, [5, 2], 'hello' ]







def head_and_tail(L):
    from_back = L.pop() # [ [1, 2], 6 ]    back=5  这都是要pop的
    from_front = L.pop(0) #[6] front=[1,2]  这都是要pop的
    L.append(from_front)   #  [6,[1,2]]
    L.insert(0,from_back) # [5,6,[1,2]] L1 L2

L1 = [ [1, 2], 3 ]
L3 = L1.copy() #L3 = [ [1, 2], 3 ]
L2 = L1 #[ [1, 2], 3 ]
L2[-1] = 5 #[ [1, 2], 5 ]
L2.insert(1,6) #[ [1, 2], 6, 5 ]
head_and_tail(L1) 

print(L1[0], L1[-1], len(L1)) # 5 [1,2] 3
print(L2[0], L2[-1], len(L2)) #  5 [1,2] 3
print(L3[0], L3[-1], len(L3)) # [1,2] 3 2










