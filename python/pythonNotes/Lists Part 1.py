'''
列表
int, float, string, boolean, tuple 可以包括各种type
it is just a container, tuple 也是


values can be updated
'''

#index从0开始, indices是index的复数


# [ ] square brackets ( )parentheses

scores = [ 59, 61, 63, 63, 68, 64, 58 ]
planets = [ 'Mercury', 'Venus', 'Earth', 'Mras', 'Jupiter',
 'Saturn', 'Neptune', 'Uranus', 'Pluto' ]

''' Hello Venus! '''
print(planets[1]) #Venus
print(len(planets)) #9 长度
#index 0-8  (9-1)


print(planets[-1])
print(planets[len(planets)-1])
#pluto, 最后的一项  9-1=8 

print(planets[-2])
#Uranus, 最后的第二项 9-2=7

planets[3] = 'Mars' #可更改
print(planets) #Mars被修改了

s = 'abc'
print(s[0])
#'a'
print( s[1])
#'b'

import math
#help(math)

#help(str)




print(planets)
planets.sort()
#按照·字母顺序排序
print(planets)


scores = [ 59, 61, 63, 63, 68, 64, 58 ]
print(scores)
#cores.sort() #just a function, does not return value
#从小到大排序了
print(scores) #直接改变scores

#存下来排序后的list，也keep original list scorea
new_scores = sorted(scores)
print(new_scores)


#sum((1,2,3)) sum([1,2,3])
print("Average Scores = {:.2f}".format( sum(scores) / len(scores) ))
#Average Scores = 62.29
print("Max Score =", max(scores)) #最大
#Max Score = 68
print("Min Score =", min(scores)) #最小
#Min Score = 58

'''
append, insert, pop, remove 都是只能处理一个元素
'''


my_list = [1, 2, 3]
my_list.append(4) #append 在列表的末尾添加一个元素。
print(my_list)  # 输出: [1, 2, 3, 4]

my_list = [1, 2, 3]
my_list.insert(1, "apple")  # insert 在索引1的位置插入"apple"
print(my_list)  # 输出: [1, 'apple', 2, 3]


my_list = [1, 2, 3, 4]
last_element = my_list.pop()  # pop()   return, 移除最后一个元素
print(last_element)  # 输出: 4
print(my_list)  # 输出: [1, 2, 3]

second_element = my_list.pop(1)  # pop(1)   return, 移除索引1的元素
print(second_element)  # 输出: 2
print(my_list)  # 输出: [1, 3]


my_list = [1, 2, 3, 2]
my_list.remove(2)  # list.remove(2) 移除第一次出现的2
print(my_list)  # 输出: [1, 3, 2]

#lists of lists/nested list
L = [ 'Alice', 3.75, ['MATH', 'CSCI', 'PSYC' ], 'PA' ]
'''
L[0] is the name,
L[1] is the GPA
L[2] is a list of courses
L[2][0] is the 0th course, 'MATH'
L[3] is a home state abbreviation
'''
print(L[2][1]) #CSCI


'''
Python list memory model
'''
my_string='hello world' #my_string is a pointer 指针


a = [1, 2, 3]
c = a  #pointing to the same thing
c[0] = 10
print(a)  # 输出: [10, 2, 3]，a 也被改变了
print(c)  # 输出: [10, 2, 3]

a = [1, 2, 3]
c = a.copy() #副本
c[0] = 10
print(a)  # 输出: [1, 2, 3]，a 没有被改变
print(c)  # 输出: [10, 2, 3]

l1 = [ 6, 12, 13, 'hello' ]
print(l1[1], l1[-2]) #12 13
l1.append( 15 ) #6 12 13 'hello' 15
print( len(l1) ) # 5
print( len(l1[3]) ) #hello的length = 5位
l1.pop(3) #移除hello
l1.sort() #6 12 13 15
l1.insert(2, [14, 15] ) #6 12 [14，15] 13 15
l1[3] += l1[4] # 6 12 [14，15] 28 15
l1[3] += l1[2][1] # 6 12 [14，15] 43 15
print(l1[3])# 43
l1.pop() # 6 12 [14，15] 43
l1[2].remove(14) 
print(l1) # [6 12 [15] 43] 打出来加上brackets别忘记
