'''Lecture 20 — Searching'''
'''lec20_class lec20_ex_start'''


import random

#随机生成0-1000的一个float
print(random.uniform(0, 1000))


my_list = [1, 2, 3, 4, 5]

#打乱顺序用shuffle
random.shuffle(my_list)
print(my_list)  
#输出可能是 [4, 1, 5, 3, 2]，每次运行结果不同

import random
# 生成一个 0 到 9 之间的随机整数（不含 10）
print(random.randrange(10))  # 例如 7

# 生成一个 5 到 15 之间的随机整数（不含 15）
print(random.randrange(5, 15))  # 例如 12

# 生成一个 10 到 50 之间，步长为 5 的随机整数（不含 50）
#10, 15, 20, 25, 30, 35, 40, 45
print(random.randrange(10, 50, 5))  # 例如 25

'''Problem 1: 
找出一个列表中最小的两个value的indices
'''

def find_two_smallest(values):
    #当列表元素小于2个时
    if len(values) < 2:
        return "list should have at least 2 values"
    
    #initialize tracking values and indices
    #最小的
    min1 = values[0]
    #第二小的
    min2 = values[1]
    min1_index = 0
    min2_index = 1
    
    #iterate through the for loop
    for i in range(len(values)):
        #current value pointing
        value = values[i]
        
        #小于最小的
        if value < min1:
            #把曾经的最小 变成 现在的第二小
            min2, min2_index = min1, min1_index
            #update最小的value，index
            min1, min1_index = value, i
        
        #小于第二小的，但没有小于最小的
        elif value < min2:
            #update成第二小的
            min2, min2_index = value, i
            
    #返回值和indices
    return (min1, min1_index),(min2, min2_index)



if __name__ == "__main__":
    values = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    result = find_two_smallest(values)
    print(result) 
    #((1, 1), (1, 3))
    
    
    values = [23, 2, 6, 5 , 7]
    result = find_two_smallest(values)
    print(result) 
    #((2, 1), (5, 3))


'''enumerate for 循环同时追踪 index 和 value'''
fruits = ["apple", "banana", "cherry"]

#tracking index and value while iterating
for index, fruit in enumerate(fruits):
    print("Index: {}, Fruit: {}".format(index,fruit))

'''
Index: 0, Fruit: apple
Index: 1, Fruit: banana
Index: 2, Fruit: cherry
'''


'''code written in class
找出一个列表中最小的两个value的indices   1种写法'''

import random
import time

#法二
def index_two_v2( values ):
    # 整体是O(N)+O(NlogN)=O(NlogN)    O(1)这种可省略
    
    # dict() key-数值 value-list of indices
    val_dict = dict()
    
    #遍历
    for index in range(len(values)): # O(N)
        #如果数值没存进去
        if not values[index] in val_dict:
            #初始化 key-数值 v-空列表
            val_dict[values[index]] = []
        #对应数值的index 存进dict 里面的list
        val_dict[values[index]].append(index)
    
    # sort the keys
    #数值从小到大存进list
    sorted_keys = sorted(val_dict) #O(N log N)
    
    # pick out the indices of the smallest keys
    
    #当最小值有多个indices指向的话，打出前两个indices
    if len(val_dict[sorted_keys[0]]) > 1:
        return val_dict[sorted_keys[0]][0], val_dict[sorted_keys[0]][1]
    #当最小值仅1个index指向的话，打出最小值的index和第二小值的index - 默认测试数据属于这一类
    else:
        return val_dict[sorted_keys[0]][0], val_dict[sorted_keys[1]][0]



if __name__ == "__main__":
    #输入list长度
    n = int(input("Enter the number of values to test ==> "))
    #把range对象转成list， 0到n-1 连续数字
    values = list(range(0,n))
    #打乱排序作为列表
    random.shuffle( values )
    print(values)

    #开始时间戳
    s2 = time.time()
    (j0,j1) = index_two_v2(values)
    #过了一段时间后
    #现在时间戳-开始时间戳 = 用时
    t2 = time.time() - s2
    print("Ver 2:  indices ({},{}); time {:.3f} seconds".format(j0,j1,t2))
    
'''code written
- 找出一个列表中最小的两个value的indices   另1种写法'''
import random
import time



#法二
def index_two_v2( values ):
    #list
    pairs = []
    for i in range(len(values)):
        #把数值和index放进tuple存进去
        pairs.append( (values[i],i) )
    #排序一下，按照数值
    pairs.sort()
    #返回最小index，第二小index
    return pairs[0][1], pairs[1][1]   # indices of the values are in location 1 of each pair



if __name__ == "__main__":
    n = int(input("Enter the number of values to test ==> "))
    values = list(range(0,n))
    random.shuffle( values )
    print(values)


    s2 = time.time()
    (j0,j1) = index_two_v2(values)
    t2 = time.time() - s2
    print("Ver 2:  indices ({},{}); time {:.3f} seconds".format(j0,j1,t2))



'''binary search'''   
#x是要找的数，L是list
def binary_search( x, L):
    '''二分查找  仅适用从小到大排的list'''
    #最小值index
    low = 0
    #最大值index
    high = len(L)
    
    #当low不等于high
    while low != high:
        #取中间值index
        mid = (low+high)//2
        #x大于中间值
        if x > L[mid]:
            #地板更新为中间值+1，上升
            low = mid+1
        #x小于/等于 中间值
        else:
            #天花板更新为中间值，下降
            high = mid
     
    #如果这个x大于list里最大值，而且还不在list里面
    if low >= len(L):    
        return (False,low)
    #x没找到的话，low就不用管他；x找到了，low就是对应的index
    else:
        return (x==L[low],low)
    
if __name__ == "__main__":
    L = [ 1.3, 7.9, 11.2, 15.3, 18.5, 18.9, 19.7 ]
    '''找找value的index'''
    
    print(binary_search( 11.2, L ))
    #找到
    #(True,2)
    
    
    '''
    1st iteration:
    low = 0
    high = 7
    low != high
    mid = (0+7)//2 = 3
    x=11.2  L[3]=15.3
    x < L[3] -> high = 3
    
    继续while
    low = 0 high = 3
    mid = (0+3)//2 = 1
    x=11.2 L[1]=7.9
    x > L[1] -> low = 1+1=2
    
    继续while
    low = 2 high =3
    mid = (2+3)//2 = 2
    x=11.2 L[2]=11.2
    x = L[2] -> high = 2
    
    low = high = 2
    跳出循环
    return 2
    
    成功找到11.2 在 index 2
    '''


    print(binary_search( 19.1, L ))
    #(False, 6)


    print(binary_search( -1, L))
    #(False, 0)
    '''low = 0
    high = 7 -> 3 -> 1 -> 0
    mid = 3 -> 1 -> 0
    '''



    print(binary_search( 25, L))
    #(False, 7)
    
    
    '''
    N 是列表的长度
    N = 512
    N after 1st iteration 256
    2 128
    3 64
    4 32
    5 16
    6 8
    7 4
    8 2
    9 1
    
    #公式法
    log₂(512) = 9
    9 次循环
    
    O(log N) base 2 - binary search
    
    
    if N=1000 or 1,000,000:
    
    log₂(1000) = 9.97 = 10
    log₂(1,000,000) = 19.93 = 20
    
    '''