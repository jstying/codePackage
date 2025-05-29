'''Lecture 17 — Dictionaries, Part 2'''

'''Recap of dictionaries'''


#initialize dict
dictoption = {0:'a', 1: 'b', 2:'c'}



print(dictoption[1])
#'b'

#update dictionary value at key 1
dictoption[1] = 'd'
print(dictoption[1])
#'d'


#加进来了新的key value pair
dictoption[10]='e'
print(dictoption)
#{0: 'a', 1: 'd', 2: 'c', 10: 'e'}


#key - str value-int
d = {'Gru':3, 'Margo':4}
print(d['Gru'])
#3



#key-str value-set
d2 = {'Gru': set( [123,456] ), 'Margo': set( [456] ) }
print(d2['Gru'])
#{456, 123}
print(d2['Margo'])
#{456}

print(d2.keys())
#dict_keys(['Gru', 'Margo'])

l=list(d2)
print(l)
#['Gru', 'Margo']

#把keys储存进list里面
l=list(d2.keys())
print(l)
#['Gru', 'Margo']

l2=list(d2.values())
print(l2)
#[{456, 123}, {456}]

print(d2.values())
#dict_values([{456, 123}, {456}])

print(type(d2.keys())) #<class 'dict_keys'>
print(type(d2.values())) #<class 'dict_values'>


'''d2 和 d2.keys()在循环中一样表示键'''
for key in d2:
    print(key,d2[key]) 
#Gru {456, 123}
#Margo {456}

for key in d2.keys():
    print(key,d2[key]) 
#Gru {456, 123}
#Margo {456}


'''仅值，不推荐'''
for v in d2.values():
    print(v)
#{456, 123}
#{456}


'''键值对，返回成tuple'''
for kvpair in d2.items():
    print(kvpair)
#('Gru', {456, 123})
#('Margo', {456})


'''实用款'''
for k,v in d2.items():
    print("key: {} value: {}".format(k, v))
#key: Gru value: {456, 123}
#key: Margo value: {456}


'''Copying and Aliasing Dictionaries'''

d = dict()
d[15] = 'hi'
print(d)
#{15: 'hi'}

L = []
L.append(d)
print(L)
#[{15: 'hi'}]


d[20] = 'bye'
print(d)
#{15: 'hi', 20: 'bye'}

#d 变化， L也变化
print(L)
#[{15: 'hi', 20: 'bye'}]  


#把d的副本给他放进去
L.append(d.copy())
print(L)
#[{15: 'hi', 20: 'bye'}, {15: 'hi', 20: 'bye'}]

d[15] = 'hello'
#前面的原d会改变，但是copy不会改变L[1]
print(L)
#[{15: 'hello', 20: 'bye'}, {15: 'hi', 20: 'bye'}]

#delete key=20的key value pair
del d[20]
#copy的部分依旧不会影响
print(L)
#[{15: 'hello'}, {15: 'hi', 20: 'bye'}]


for k,v in L[1].items():
    print(k,v)
#15 hi
#20 bye



''''lec_ex1'''


d1 = dict()
l1 = [ 5, 6, 7 ]
#car和l1指向同一个！ car 变，l1变
d1['car'] = l1 #d1 {'car':[5,6,7]}
d1['bus'] = l1.copy() #d1 {'car':[5,6,7],'bus':[5,6,7]}
#l1变，car也变，bus是copy不变
l1.append( [8,9] )#d1 {'car':[5,6,7,[8,9]],'bus':[5,6,7]}
#这两个指向同一个，注意！
d1['truck'] = d1['bus'] #d1 {'car':[5,6,7,[8,9]],'bus':[5,6,7],'truck':[5,6,7]}
#truck也会append
d1['bus'].append(10)  #d1 {'car':[5,6,7,[8,9]],'bus':[5,6,7,10],'truck':[5,6,7,10]}
#bus也会pop
d1['truck'].pop(0)  #d1 {'car':[5,6,7,[8,9]],'bus':[6,7,10],'truck':[6,7,10]}
print("list:", l1)
#list: [5, 6, 7, [8, 9]]
#keys从小到大顺序，bus,car,truck
for v in sorted(d1.keys()):
    print("{}: {}".format( v, d1[v] ))

#bus: [6, 7, 10]
#car: [5, 6, 7, [8, 9]]
#truck: [6, 7, 10]





'''Module: Lec17_movie_actors_most_busy — Use sets to find unique movies.'''
'''
找出大明星-这个人上过最多的电影次数和他的名字，还有过气明星-只上过1部电影的人数
名字-key
电影次数统计max和min - value
key=name value=set of movies
'''
#file name
#imdb_2010-12.txt
#imdb_data.txt
imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)


#创建dict
movies = dict()
#打开文件读取每一行
for line in open(imdb_file, encoding = "ISO-8859-1"):
    #每行左右去除空白，用|分隔开部分，存进list
    words = line.strip().split('|')
    #第一部分除白的就是名字-str
    name = words[0].strip()
    #第二部分就是电影名称
    movie = words[1].strip()
    
    #dict里已有该人名的话,已创建的kv pair
    if name in movies:
        #set里面加入电影名
        movies[name].add(movie)
    #一开始dict啥也没有/没有该人名的话
    else:
        #key=name  value=set() 独创一个kv pair
        movies[name] = set()
        #set里面加入电影名,也就是v
        movies[name].add(movie)


#统计
singlets = 0
most = 0

#以key来迭代
for name in movies:
    #求此人的电影数量
    movie_ct = len(movies[name])
    #只有一部
    if movie_ct == 1:
        #统计过气明星
        singlets += 1
    #不断寻找最多，更新最多数量，更新大明星的名字
    if movie_ct > most:
        most = movie_ct
        person = name
        
print("{} appears most often: {} times".format(person, most))
print("{} people appear once".format(singlets))

#imdb_2010-12.txt
#Madsen, Michael appears most often: 16 times
#17795 people appear once

#imdb_data.txt
#Blanc, Mel appears most often: 338 times
#86735 people appear once

'''lec_ex2'''
'''
Enter the name of the IMDB file ==> imdb_data.txt
2342
Ben Hur
165

找出最多人参演的人数和电影名，以及仅1人参演的电影数量
电影名-key
人数统计max和min - value
 总体来说就是反一反，以key作为movie，set of 人名作为value
 
 
'''
#imdb_data.txt
imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)


#创建dict
movies = dict()
#打开文件读取每一行
for line in open(imdb_file, encoding = "ISO-8859-1"):
    #每行左右去除空白，用|分隔开部分，存进list
    words = line.strip().split('|')
    #第一部分除白的就是名字-str
    name = words[0].strip()
    #第二部分就是电影名称
    movie = words[1].strip()
    
    #dict里已有该电影的话/已创建的kv pair
    if movie in movies:
        #set里面加入参演人
        movies[movie].add(name)
    #一开始dict啥也没有/没有该人名的话
    else:
        #key=movie  value=set() 独创一个kv pair
        movies[movie] = set()
        #set里面加入名字,也就是v
        movies[movie].add(name)

#统计
#最少1人参演的电影
#最多人参演的数量
singlets = 0
most = 0

#以key来迭代
for movie in movies:
    #求此电影的人数量
    person_ct = len(movies[movie])
    #只有1人
    if person_ct == 1:
        #统计
        singlets += 1
    #不断寻找最多，更新最多数量参与人
    if person_ct > most:
        most = person_ct
        large_movie = movie
        
print("{}".format(most))
print("{}".format(large_movie))
print("{}".format(singlets))
#75  75人参演Broken电影，参与人最多
#Broken
#4601 4601部1人参演的小电影






'''Module: Lec17_movie_actors_appearances — 字典转换'''
'''
keys are 演员名称
values are sets of 他的电影名称
转成
keys are 出演电影的片数
values are a list of 同样片数的演员名称
'''
#imdb_data.txt
imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)

'''
keys are 演员名称
values are sets of 他的电影
'''
movies = dict()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    movie = words[1].strip()
    
    if name in movies:
        movies[name].add(movie)
    else:
        movies[name] = set()
        movies[name].add(movie)

'''
Now cycle through the movies dictionary to get the data for a new dictionary. This
time, for every actor, we calculate how many movies they were associated with by
taking the length of the set indicated by movies[name]. This length becomes a 
key in the actors dictionary where everyone who is associated with length number of
movies is stored in a list.
'''
actors = dict()
#key是演员名
for name in movies:
    #这人的电影数量
    movie_ct = len(movies[name])
    #actors里没有这个电影数量
    if movie_ct not in actors:
        #key 作为电影数量，初始化value，是一个list，把演员名装进去
        actors[movie_ct] = []
        actors[movie_ct].append(name)
    #已有这个数量，把人名往里面放
    else:
        actors[movie_ct].append(name)

'''
Sort the actors dictionary from highest (most number of movies) to lowest 
(least number of movies). Print out the top 25 actors by number of movies 
they are associated with.
'''
#字典的keys从高到低排序，dict不能.sort()无序，sorted来变成list了
keys = sorted(actors, reverse=True)
i = 0
count = 0
#找出top25的演员名

keys = sorted(actors, reverse=True)

while count < 25 and i < len(keys): 
    
    
    #从最高次数开始，和dict key对应的值
    print(keys[i], actors[keys[i]])
    #确保打出的名字次数有限
    count += len(actors[keys[i]])
    #迭代成下一个次数
    i += 1
'''
338 ['Blanc, Mel']
205 ['Dunn, John W.']
121 ['Morrison, Tom']
120 ['Maltese, Michael']
93 ['Foster, Warren']
89 ['Lee, Christopher']
87 ['Carradine, David']
86 ['Caine, Michael']
80 ['Madsen, Michael', 'Pierce, Tedd']
79 ['Estevez, Joe', 'Hopper, Dennis']
76 ['Roberts, Eric']
75 ['Pleasence, Donald']
74 ['Fine, Larry', 'Howard, Moe']
72 ['Black, Karen', 'Mitchell, Cameron', 'Wynn, Keenan']
70 ['Cushing, Peter', 'Butler, Daws']
69 ['De Niro, Robert', 'Curtis, Tony']
68 ['Reynolds, Burt', 'Hackman, Gene']
'''


my_dict = {'b': 2, 'a': 1, 'c': 3}

# 排序字典的键
sorted_keys = sorted(my_dict)
print(sorted_keys)
#['a', 'b', 'c']
strin=''
#然后通过loop打出key对应的值
for i in range(len(sorted_keys)):
    strin+="{} ".format(my_dict[sorted_keys[i]])

print(strin)
#1 2 3 




#urllib.request 用于打开并读取 URLs。
#json 用于解析 JSON 数据。

import urllib.request
import json

url = "http://nominatim.openstreetmap.org/"\
      "search?q={}&format=json&polygon_geojson=1&addressdetails=0"\
      .format('Troy,NY')
#打开指定的 URL
f = urllib.request.urlopen(url)
#读取文件中 所有 内容，成str
rawcontent = f.read()
#将字节数据解码为字符串，将 JSON 字符串解析为 Python 对象
content = json.loads(rawcontent.decode("utf-8"))

print(content) #东西太多，不适宜打出来



'''长得真的是很像'''
import json

# JSON 字符串
json_str = '{"name": "Alice", "age": 25, "isStudent": true}'

# 转换为 Python dict
data = json.loads(json_str)
print(data)  
#{'name': 'Alice', 'age': 25, 'isStudent': True}

