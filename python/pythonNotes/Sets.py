'''Lecture 15 — Sets'''

# 使用大括号创建 set
my_set = {1, 2, 3, 4, 5}

# 使用 set() 函数创建 set, 自动去除重复的内容
my_other_set = set([1, 2, 2, 3, 4])
my_other_set = set((1, 2, 2, 3, 4))
print(my_set)  #{1, 2, 3, 4, 5}
print(my_other_set)  #{1, 2, 3, 4}


# 字符串被分解为单个字符，且每个字符只出现一次
my_string = "hello"
my_set = set(my_string)
print(my_set)  #{'h', 'e', 'l', 'o'}

#无意义操作，自己转生成自己
existing_set = {1, 2, 3}
new_set = set(existing_set)
print(new_set)  #{1, 2, 3}

empty_set = set()
print(empty_set) #set()

# 可以包含的类型-不可变（immutable）
valid_set = {1, 2.5, "hello", (1, 2)}
print(valid_set)  #{1, 2.5, 'hello', (1, 2)}

# 不可以包含的类型 list,set, dict
#invalid_set = {[1, 2], {"key": "value"}}  # 会抛出错误：TypeError: unhashable type: 'list'


set_a = {1, 2, 3}
set_b = {3, 4, 5}


#set() 函数将传入的可迭代对象（如列表、元组、range 对象）
s2=set(range(0,11,2))
print(s2) #{0, 2, 4, 6, 8, 10}
print(len(s2)) #6

s3={1,2}
s3.add(2)
print(s3) #{1, 2}

s3.add(3)
print(s3) #{1, 2, 3}

#清空集合
s3.clear()
print(s3)#set()

#初始化空字典，不是空集合！
s4={} 
print(s4) #{}


s1={0,2,5}
s2={0,2,4,6,8,10}
print(s1.difference(s2)) #{5}
print(s1-s2)#s1有的,s2没有, 只能set和set之间

print(s2.difference(s1)) #{8, 10, 4, 6} set是无序的，随机输出顺序
print(s2-s1) #s2有的,s1没有

print(s1.intersection(s2)) #{0, 2} 相交
print(s1&s2)
print(s2&s1)

print(s1.union(s2)) #{0, 2, 4, 5, 6, 8, 10}  并集
print(s1|s2)

print(s1.issubset(s2)) #子集 s1的元素是否都被s2包括
print(s1<=s2)
#False

print(s1.issuperset(s2)) #超集 s1是否包含s2的所有元素
print(s1>=s2)
#False

# 对称差集=两个集合中不重复的元素的集合
print(s1.symmetric_difference(s2))#{4, 5, 6, 8, 10}
print(s2.symmetric_difference(s1))
print(s1 ^ s2)



#lec exercise1
s1 = set([0,1,2]) #s1 {0,1,2}
s2 = set(range(1,9,2)) #s2 {1,3,5,7}
print('A:', s1.union(s2)) #A: {0, 1, 2, 3, 5, 7}   union 并集

print('B:', s1) #B: {0, 1, 2}  s1

s1.add('1') #注意！ 这是str1！ 所以s1 {0,1,2,'1'}
s1.add(0) #已有就不加
s1.add('3') #s1 {0,1,2,'1','3'}
s3 = s1 | s2 #|并集 
print('C:', s3) #C: {0, 1, 2, '1', 3, 5, 7, '3'}  -s3

print('D:', s3 - s1) #D: {3, 5, 7} difference 3有的1没有的



'''
This is the start to the solution to the problem of find all people
named in the Internet Movie Database.  

One important note.  In opening the file we need to specify the
encoding the text.  The default is what's known as utf-8, but this
only handles English characters well.  For the IMDB file, we need to
open with a more language-independent, international standard.  This
is 'ISO-8859-1'.

As we will use the time.time() function to measure how long our
computation takes.  This function tells the seconds since an "epoch",
which is 1/1/1970 on Unix-based systems (including Macs and Linux
machines) and 1/1/1601 on Windows machines.  By recording in the
software the time before the calculations start, the time when the
calculations end, and subtracting we get the elapsed 过去的时间 time.

import time
#当前时间戳
start_time = time.time()
# 执行一些操作后的时间戳
end_time = time.time()
print("操作耗时: {} 秒".format(end_time - start_time))



这个程序从指定的 IMDB 文件中读取数据，提取出唯一的名字，并计算每添加 1000 个名字所用的时间。

'''




'''法1-Using lists to hold unique names'''
#导入time模块
import time

#记录起始时间
start_time = time.time()

#imdb_2010-12.txt
#获取 IMDB 文件名，并去掉输入中的多余空格
imdb_file = input("Enter the name of the IMDB file ==> ").strip()
#用于存储从文件中提取的唯一名字。
name_list = []

#编码 encoding='utf-8'  encoding='ISO-8859-1'
#每行读取
for line in open(imdb_file, encoding = "ISO-8859-1"):
    # Reynolds, Ryan       | Deadpool         | 2014                                                                                                                                 |            2014

    #一行去除两边的空格，用|分开成三个词存进words 的list里面
    words = line.strip().split('|')
    #第一项就是名字
    name = words[0].strip()
    
    #检查元素  是否存在于可迭代对象中(list,tuple,str,set)
    #name in name_list=False 就加入，True就不执行
    #  如果名字查到的不在list中
    if not name in name_list:
        #存进去
        name_list.append(name)
        #每当列表的长度增加到 1000 的倍数时，程序会计算过去 1000 个名字所花费的时间，并输出。
        if len(name_list) % 1000 == 0:
            #1000个到了统计
            end_time = time.time()
            print('After {} added, the last 1000 took {:.2f} seconds'.format(len(name_list), end_time-start_time))
            #再从刚刚结束时间开始重新计算
            start_time = end_time
            
#打出所有名字
print("Number of unique names in the IMDB:", len(name_list)) #20455
for n in name_list:
    #tab加上名字，每行打完换行
    print('\t{}'.format(n))
    
    
    
'''法二 Faster list version using sorting'''
import time

#imdb_2010-12.txt
imdb_file = input("Enter the name of the IMDB file ==> ").strip()

start_time = time.time()

name_list = []
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    #先把每个名字放进list里面
    name_list.append(name)

# Sort the names.重复的名字都排在一起
name_list.sort()


# ["Alice", "Bob", "Bob", "Charlie", "Charlie"]
#      1     2       2        3        3
count = 1
for i in range(1,len(name_list)):
    #找的是有多少组不同的相邻名字
    #第一项已是1，前一项不等于后一项,把后一项计数
    if name_list[i-1] != name_list[i]:
        count += 1
        


end_time = time.time()
print('Total time required {:2f} seconds'.format(end_time-start_time)) #快了不少
print("Number of unique names in the IMDB:", count) #20455


'''法3： set超高速'''
import time
#imdb_2010-12.txt
imdb_file = input("Enter the name of the IMDB file ==> ").strip()

start_time = time.time()

#initialize set
names = set()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    #全部加进去，他会自动去重
    names.add(name)

end_time = time.time()

print("Solution took {:.2f} seconds".format(end_time-start_time))

print("Number of unique names in the IMDB:", len(names))



#假设用法1的list的话，这块代码不要运行！！只是看看句法
#对 names 列表进行排序
ordered_names = sorted(names)
#min(列表长度，100) 就说最多打100个出来，按字母顺序
for i in range(min(len(ordered_names),100)):
    print("{}: {}".format(i, ordered_names[i]))



#split split split 别拼错 str.split()转成list




#lec15_ex2
'''imdb_2010-12.txt
Downey Jr., Robert | Back to School |      1986
Downey Sr., Robert   | Moment to Moment  | 1975
Downey, Elsie    | Moment to Moment     |  1975
'''

#ask file name 
#imdb_2010-12.txt
#imdb_data.txt
imdb_file = input("Data file name: ").strip()
print(imdb_file)

#ask for a start of last name  e.g. Down
prefix = input("Prefix: ").strip()
print(prefix)

'''how many different last names in the file
how many different names that start with prefix str. 
'''

#initialize
names = set()
prefix_names = set()

for line in open(imdb_file, encoding = "ISO-8859-1"):
    #the list stores three section
    words = line.strip().split('|')
    #full name, the index 0th section
    name = words[0].strip()
    #last name, first name, the list stores 2 sections
    l_f = name.split(',')
    #last name
    last_name=l_f[0].strip()
    #add into the set
    names.add(last_name)
    
    
    #when last name starts with 开头是prefix，区分大小写, 如果prefix='Do'不能用in，因为有McDonald
    if last_name.startswith(prefix):
        prefix_names.add(last_name)
    
#print numbers of unique last names    
print("{} last names".format (len(names)))
#print numbers of unique last names with the prefix
print("{} start with {}".format(len(prefix_names),prefix))



full_name = "Robert Downey Jr."

# 区分大小写 in ， 只要在里面就好了，可以是开头出现，或者中间 e.g. do in names : Donut, adonis,oodo
print("downey" in full_name)  # 输出: False
print("Downey" in full_name)   # 输出: True


name = "Adonis"

# 检查是否以 "Ad" 开头
print(name.startswith("Ad"))  # 输出: True

# 检查是否以 "ado" 开头（区分大小写） 
print(name.startswith("ado"))  # 输出: False

# 检查是否以 "A" 开头
print(name.startswith("A"))  # 输出: True

# 检查是否以 "on" 开头
print(name.startswith("on"))  # 输出: False


'''自学'''
# 定义一个包含元组的列表
list_of_tuples = [(5, 'e'), (2, 'a'), (9, 'c'), (1, 'd'), (5, 'b')]

# 升序从小到大 list.sort() 前无
list_of_tuples.sort()
print(list_of_tuples)
#[(1, 'd'), (2, 'a'), (5, 'b'), (5, 'e'), (9, 'c')]

# 倒序从大到小 list.sort(reverse=True) 前无
list_of_tuples.sort(reverse=True)
print(list_of_tuples)
#[(9, 'c'), (5, 'e'), (5, 'b'), (2, 'a'), (1, 'd')]

#只是从后往前
list1=[2,2,9,5,4]
list1.reverse()
print(list1)
#[4, 5, 9, 2, 2]



s = "  Hello   World  "
result = s.split() #会去除首尾的空白
print(result)  # 输出 ['Hello', 'World']

s = " 12 3 "
result = s.split(" ") #最前最后会留下空字符''
print(result)  # 输出 ['', '12', '3', '']


'''怎么去除列表重复value吗？创建一个新的，已有同样的不允许再传入。'''
parse_list=[1, 2, 2, 2, 3]
no_rep_list=[]
for i in parse_list:
   #新列表已有的话，就不加入新列表
   if i not in no_rep_list:
        no_rep_list.append(i)
print(no_rep_list)
#[1, 2, 3]


'''去除list某个元素，防止在loop遍历原列表时 pop(index) remove(value) 这样会出错'''
numbers = [1, 2, 2, 2, 3]
for num in numbers[:]:  # 使用切片创建numbers副本,里面元素都是一样的，看着副本，删着本体
    if num == 2:
        numbers.remove(num)

print(numbers)  
#[1, 3]
   

numbers = [1, 2, 2, 2, 3]
for num in numbers.copy(): #.copy() 也是一样的
    if num == 2:
        numbers.remove(num)

print(numbers)  
#[1, 3]

'''推荐用while来去除'''
numbers = [1, 2, 2, 2, 3]
while numbers.count(2) > 0:   #这个元素还在的话
    numbers.remove(2)   #删
print(numbers)
#[1, 3]

numbers = [1, 2, 2, 2, 3]
while 2 in numbers:   #这个元素还在的话
    numbers.remove(2)   #删
print(numbers)
#[1, 3]
