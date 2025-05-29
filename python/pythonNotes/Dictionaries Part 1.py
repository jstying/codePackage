'''Lecture 16 — Dictionaries, Part 1'''

'''count the movies for each person 法1'''
#hanks.txt
#imdb_2010-12.txt

imdb_file = input("Enter the name of the IMDB file ==> ").strip()
#计数的list of lists [[hanks,1][bob,2]...]
count_list = []
for line in open(imdb_file, encoding = "ISO-8859-1"):
    #Hanks, Jim               | Seymour Sally Rufus         |            2011
       
    #一行去除两边的空格，用|分开成三个词存进words 的list里面                                                                                                                        |            2014
    words = line.strip().split('|')
    #第一项就是名字
    name = words[0].strip()
    
    #initialize flag
    found = False
    
    #每个小list
    for pair in count_list:
        #已有名字
        if pair[0] == name:
            #增加电影数
            pair[1] += 1
            #更新flag
            found = True
            #退出这个循环，然后就不到下面初始化一个小list了
            break
        
    #若没有名字，第一个名字存进去，初始化1部电影，初始化一个小list[hanks,1]
    if not found:
        new_pair = [name, 1]
        count_list.append(new_pair)

#把每个小list的内容打出来，作者名，作品数
for pair in count_list:
    print("{} appeared in {} movies".format(pair[0], pair[1]))
    
'''
Hanks, Jim appeared in 6 movies
Hanks, Colin appeared in 10 movies
Hanks, Bethan appeared in 1 movies
Hanks, Tom appeared in 41 movies
Hanks, Zach appeared in 2 movies
Hanks, Bridget appeared in 1 movies
Hanks, Scott appeared in 1 movies
Hanks, Mark appeared in 1 movies
Hanks, Brad appeared in 1 movies
Hanks, Steve appeared in 1 movies
Hanks, Christopher appeared in 1 movies
Hanks, Mike appeared in 1 movies
Hanks, Paul appeared in 1 movies
'''

'''法2 Faster version using sorting'''
#hanks.txt
#imdb_2010-12.txt
imdb_file = input("Enter the name of the IMDB file ==> ").strip()
#存名字
count_list = []
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    found = False
    #把名字全部放进去
    count_list.append(name)

#排序，同名的靠在一起
count_list.sort()

index = 0
#指针遍历每个名字
while index < len(count_list):
    #获取当前名字
    name = count_list[index]
    #初始化此作家作品计数器
    count = 0
    
    #先检查index是否out of range，在检查是不是同一个作者名字
    while index < len(count_list) and count_list[index] == name:
        #增加作品数
        count += 1
        #看看下个名字还是同个人名吗，不是的话就跳出这个while，回到大while重新开始
        index += 1
    #flush 它确保输出立即显示在控制台上，而不是被缓冲
    print("{} appeared in {} movies".format(name, count), flush=True)



'''法3  The fastest version using dictionaries'''
#hanks.txt
#imdb_2010-12.txt
imdb_file = input("Enter the name of the IMDB file ==> ").strip()
#创建字典
counts = dict()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    #如果名字已经在字典中
    if name in counts:
        #key=名字，update value
        counts[name] += 1
    #名字还没进字典
    else:
        #字典key=名字，value=1
        counts[name] = 1

#把字典的key排序，储存为list  注意！dict和set没有.sort， 但可以通过sorted转成list排序      
names = sorted(counts)
#最多限制为100个
limit = min(100, len(names))
#0-99
for index in range(limit):
    #每个名字
    name = names[index]
    #counts[name]对应名字的计数
    print("{} appeared in {} movies".format(name, counts[name]))   








'''dictionaries'''
#初始化字典
heights=dict()
print(heights) #{}
heights={}
print(heights) #{}


#dictionary_name[key]=value
'''key hashable=immutable 可以是字符串、小数，整数、元组, boolean(就True,False两个key)
dict, set, list不可以
value 可以是任何boolean,int,float,string,list,tuple,set,other dictionaries

多个key可以指向相同的值
key name必须独一无二
heights = {
    'belgian horse': 162.6,
    'indian elephant': 280.0,
    'tiger': 91.0,
    'lion': 91.0  # 'tiger' 和 'lion' 都对应 91.0
}
'''




heights['belgian horse'] = 162.6
heights['indian elephant'] = 280.0
heights['tiger'] = 91.0
heights['lion'] = 97.0

print(heights)
#{'belgian horse': 162.6, 'indian elephant': 280.0, 'tiger': 91.0, 'lion': 97.0}

#update value
heights['lion'] = 93.0
print(heights)
#{'belgian horse': 162.6, 'indian elephant': 280.0, 'tiger': 91.0, 'lion': 93.0}

#有键tiger吗
print('tiger' in heights)
#True

#没这个键哈
print('giraffe' in heights)
#False


#heights 中是否存在键 91.0
print(91.0 in heights)
#False

#有这个值吗
print(91.0 in heights.values())
# True



print(heights.keys())
#dict_keys(['belgian horse', 'indian elephant', 'tiger', 'lion'])
print(heights.values())
#dict_values([162.6, 280.0, 91.0, 93.0])
print(list(heights.values()))
#[162.6, 280.0, 91.0, 93.0]
print(sorted(heights.values()))
#[91.0, 93.0, 162.6, 280.0]

people = dict()
#key ='Hanks, Tom'  value={'Splash', 'Big', 'Forest Gump'}
people['Hanks, Tom'] = set()
#set里面放'big'
people['Hanks, Tom'].add('Big')
people['Hanks, Tom'].add('Splash')
people['Hanks, Tom'].add('Forest Gump')
#值的长度，也就是set的
print(len(people['Hanks, Tom']))
#3
print(people)
#{'Hanks, Tom': {'Splash', 'Big', 'Forest Gump'}}


countries = dict()
countries.clear()
print(countries)
 #{}
 
countries['Algeria'] =  (37100000, 'Africa')
countries['Canada'] = (34945200, 'North America' )
countries['Uganda'] = (32939800, 'Africa')
countries['Morocco'] = (32696600, 'Africa')
countries['Sudan'] = (30894000, 'Africa')
print(countries)
#{'Algeria': (37100000, 'Africa'), 'Canada': (34945200, 'North America'), 'Uganda': (32939800, 'Africa'), 'Morocco': (32696600, 'Africa'), 'Sudan': (30894000, 'Africa')}


name = "Canada"
print("The population of {} is {}".format(name, countries[name][0]))
#The population of Canada is 34945200
print("It is in the continent of", countries[name][1])
#It is in the continent of North America


'''
Removing Values: Sets and Dictionaries

For a set: 集合
discard removes the specified element, and does nothing if it is not there  没找到，无事发生-discard
remove removes the specified element, but fails (throwing an exception) if it is not there 没找到，报错-remove
'''
#discard

my_set = {1, 2, 3, 4, 5}
# 移除元素 3
my_set.discard(3)
print(my_set)  
#{1, 2, 4, 5}

# 尝试移除一个不存在的元素 10, 不会引发错误
my_set.discard(10)  
print(my_set)  
#{1, 2, 4, 5}


#remove
my_set = {1, 2, 3, 4, 5}
my_set.remove(3) #和discard一样
print(my_set)
#{1, 2, 4, 5}
my_set.remove(10)  # 这将引发 KeyError
print(my_set)  #打不出来啊



'''
For a dictionary 字典, it is the del function. delete 没找到，key error
'''
# 创建一个字典
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# 删除键为 'age' 的key value pair
del my_dict['age']

print(my_dict)  # 输出: {'name': 'Alice', 'city': 'New York'}

del my_dict['country']  # 这将引发 KeyError


'''Lecture 16 — Exercises'''

'''Write a Python program that forms a dictionary called countries that associates the population 
with each of the following countries (in millions):

Algeria 37.1

Canada 3.49

Uganda 32.9

Morocco 32.7

Sudan 30.9

Canada 34.9 # a correction to the error above.

and then prints the length of the countries dictionary, the sorted list of the keys in countries 
and a sorted list of the values in countries. There should be six assignment statements in your program
 (seven if you include initializing the dictionary) and three lines of output from your program. 
 Please initialize your dictionary using dict() rather than {}
'''

countries=dict()
countries['Algeria']=37.1
countries['Canada']=3.49
countries['Uganda']=32.9
countries['Morocco']=32.7
countries['Sudan']=30.9
#update Canada value
countries['Canada']=34.9


#return key numbers
print(len(countries)) 
#5

#the sorted list of the keys in countries 
print(sorted(countries))
#['Algeria', 'Canada', 'Morocco', 'Sudan', 'Uganda']

#a sorted list of the values in countries
print(sorted(countries.values())) 
#[30.9, 32.7, 32.9, 34.9, 37.1]




'''Lecture 16 — Exercises'''

'''Our solution to the IMDB problem thus far has not actually told us who is 
the busiest individual in the Internet movie database. Your job in this part is 
to complete this task. Starting from the code produced in class, which will be immediately 
posted on the course website (in the Code written in class area), 

write a program that finds and prints the name of the individual who appears the most times 
in the IMDB file you are given. 

Also, count and output the number of individuals who appear only 1 time in the IMDB.


For example if the answer were Thumb, Toni and this person had appeared 100 times, 
and if 2,000 people had only appeared once, then your output should be

Enter the name of the IMDB file ==> imdb_data.txt
Thumb, Toni appears most often: 100 times
2000 people appear once
We strongly suggest that you test your solution on the hanks.txt dataset first! 
We will test on multiple files. You do not need to worry about the possibility 
of a tie for the most commonly occuring name. Please initialize your dictionary using dict() rather than {}
'''
#imdb_data.txt
#hanks.txt
#imdb_2010-12.txt
imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)
#创建字典
counts = dict()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    #如果名字已经在字典中
    if name in counts:
        #key=名字，update value
        counts[name] += 1
    #名字还没进字典
    else:
        #字典key=名字，value=1
        counts[name] = 1




#initialize count for one time
num_1=0
#initialize max value and key
max_Value=0
max_Key=''

#go through all keys
for key in counts:
    #if larger
    if counts[key]>max_Value:
        #update largest
        max_Value=counts[key]
        max_Key=key
    if counts[key]==1:
        #increment count
        num_1+=1
        
print("{} appears most often: {} times".format(max_Key, max_Value))
print("{} people appear once".format(num_1))

    