'''Lecture 21 — Sorting'''
'''lec21_class 就好'''


'''selection sort 学生不需要知道这个'''
def sel_sort( v ):
    '''
    O(N^2) N-size of list   v是list 
    cur_min 初始最小值->目前最小值-> final最小值 然后重复
    
    
    
    2 8 5 3 9 4 1
    cur_min = 2
    遍历一遍找更小的minimum，找到1
    swap 2 and 1
    
    1 8 5 3 9 4 2
    1已sort，cur_min = 8
    遍历一遍找更小的minimum，找到2
    swap 8 and 2
    
    1 2 5 3 9 4 8
    1,2已sort，cur_min = 5
    遍历一遍找更小的minimum，找到3
    swap 5 and 3
    
    1 2 3 5 9 4 8
    1,2,3已sort，curr_min = 5
    遍历一遍找更小的minimum，找到4
    swap 5 and 4
    
    1 2 3 4 9 5 8
    1,2,3,4已sort，curr_min = 9
    遍历一遍找更小的minimum，找到5
    swap 9 and 5
    
    1 2 3 4 5 9 8
    1,2,3,4,5已sort，curr_min = 9
    遍历一遍找更小的minimum，找到8
    swap 9 and 8
    
    1 2 3 4 5 8 9
    结束
    
    
    '''
    #第0项到倒数第二项，倒数第一项不能swap
    for i in range(0, len(v)-1):
        #初始最小值 index，第i项
        jMin = i
        #从邻居开始，遍历到末尾
        for j in range(i+1,len(v)):
            #不断更新比初始最小值 更小的 最小值index
            if v[j] < v[jMin]:
                jMin = j
        
        #swap 初始最小值 and 找到的更小最小值
        v[i],v[jMin] = v[jMin],v[i]

if __name__ == "__main__":
    v = [ 6.4, 18.5, 5.7, 18.8, 9.4 ]
    sel_sort(v)
    print(v)
    #[5.7, 6.4, 9.4, 18.5, 18.8]

'''Insertion sort -上课学的
O(N^2) N-size of list
从左到右， 比较每个数与左边的数
把数insert到正确的位置

2 8 5 3 9 4

8开始，i=1
j=0
j=0 and v[0] #2 < 8 不进while
v[j+1] = 8  #放进
v[:i+1] #打出到i的list 
2 8

5开始，i=2
2 8 5
j=1 and v[1] #8 > 5 进
v[2] = v[1]#8
2 8 8
j=0 and 2 < 5 不进
v[j+1] = 5  #放进
2 5 8


3开始，
2 5 8 3 
2 5 8 8   #右移8
2 5 5 8   #右移5   
2 3 5 8   #2比3小，在旁边放进来  

9开始
2 3 5 8 9  #9比8小，在旁边放进来

4开始，
2 3 5 8 9 4 
2 3 5 8 9 9   #右移9
2 3 5 8 8 9   #右移8
2 3 5 5 8 9   #右移5
2 3 4 5 8 9   #3比5小，放进来
结束
'''



def ins_sort( v ):
    '''
    O(N^2)
    The Insertion Sort algorithm
    '''
    #i 从index1开始
    for i in range(1,len(v)):
        #每个开始的数
        x = v[i]
        #开始数 左边的一个数的 index
        j = i-1
        #当开始数左边还有数 and 左边的数大于开始数时
        while j >= 0 and v[j] > x:
            #右移左边的数+1
            v[j+1] = v[j]
            #Decrement j 直到开始数大于等于左边数， j是放进来左边一个index
            j -= 1
        #现在x大于等于左边的数，在左边数+1的位置放进来x
        v[j+1] = x
        #v[:i+1] 打出i从0-i的sorted list
        print("i = {}, j = {}, sorted = {}".format(i,j, v[:i+1]))

if __name__ == "__main__":
    v = [2, 8, 5, 3, 9, 4 ]
    
 
    ins_sort(v)
    print(v)
    print()
    '''
    i = 1, j = 0, sorted = [2, 8]
    i = 2, j = 0, sorted = [2, 5, 8]
    i = 3, j = 0, sorted = [2, 3, 5, 8]
    i = 4, j = 3, sorted = [2, 3, 5, 8, 9]
    i = 5, j = 1, sorted = [2, 3, 4, 5, 8, 9]
    [2, 3, 4, 5, 8, 9]
    '''
    v = [ 6.4, 18.5, 5.7, 18.8, 9.4 ]
    ins_sort(v)
    print(v)
    print()
    '''
    i = 1, j = 0, sorted = [6.4, 18.5]
    i = 2, j = -1, sorted = [5.7, 6.4, 18.5]
    i = 3, j = 2, sorted = [5.7, 6.4, 18.5, 18.8]
    i = 4, j = 1, sorted = [5.7, 6.4, 9.4, 18.5, 18.8]
    [5.7, 6.4, 9.4, 18.5, 18.8]
    '''
    v =  [ 10, 5, 3, 2, -4 ]
    ins_sort(v)
    print(v)
    print()
    '''
    i = 1, j = -1, sorted = [5, 10]
    i = 2, j = -1, sorted = [3, 5, 10]
    i = 3, j = -1, sorted = [2, 3, 5, 10]
    i = 4, j = -1, sorted = [-4, 2, 3, 5, 10]
    [-4, 2, 3, 5, 10]
    '''
    v = []
    ins_sort(v)
    print(v)
    print()
    v = [ 5, 6, 7, 6, 5, 5]
    ins_sort(v)
    print(v)
    '''
    i = 1, j = 0, sorted = [5, 6]
    i = 2, j = 1, sorted = [5, 6, 7]
    i = 3, j = 1, sorted = [5, 6, 6, 7]
    i = 4, j = 0, sorted = [5, 5, 6, 6, 7]
    i = 5, j = 1, sorted = [5, 5, 5, 6, 6, 7]
    [5, 5, 5, 6, 6, 7]
    '''
    
    



'''Merging two sorted lists 怎么合并两个sortedlists变成一个sortedlist呢'''
L1 = [ 9, 12, 17, 25 ]
L2 = [ 3, 5, 11, 13, 16 ]
#[ 3, 5, 9, 11, 12, 13, 16, 17, 25 ]

def merge(L1,L2):
    
    #从index 0开始，初始化新list
    i1 = 0
    i2 = 0
    L = []
    
    #i1+=1或i2+=1后若超出range，会停下
    while i1 < len(L1) and i2 < len(L2):
        #L1的元素更小
        if L1[i1] < L2[i2]:
            #放进来
            L.append( L1[i1] )
            #指向下一个L1的元素
            i1 += 1
            
        #L2的元素更小，或L2元素等于L1，#等于放这里或者上面<=都行
        else:
            #放进来
            L.append( L2[i2] )
            #指向下一个L2的元素
            i2 += 1
            
            
            
    '''当其中一个list全部加入L后, 把另一个list剩下的加进去'''        
    #L += L1[i1:]一样的 extend把可迭代对象tuple,list里的元素一个个加进去
    L.extend(L1[i1:])   #  copy remaining items from L1, if any
    print("L1 remaining: " , L1[i1:])
    L.extend(L2[i2:])   #  copy remaining items from L2, if any
    print("L2 remaining: " , L2[i2:])
    return L


if __name__ == "__main__":
    v1 = [ 26, 35, 145]
    v0 = [ 0, 0, 9, 9, 9.4, 9.6, 15, 21 ]
    print(merge(v0,v1))
    '''
    L1 remaining:  []
    L2 remaining:  [26, 35, 145]
    [0, 0, 9, 9, 9.4, 9.6, 15, 21, 26, 35, 145]
    '''
    
    
    
    L1 = [ 2, 7, 9, 12, 17, 18, 22, 25 ]
    L2 = [ 1, 5, 6, 8, 13, 14, 15, 18, 19, 23, 25 ]
    merged_L = merge(L1, L2)
    print(merged_L)
    '''
    L1 remaining:  [25]
    L2 remaining:  []
    [1, 2, 5, 6, 7, 8, 9, 12, 13, 14, 15, 17, 18, 18, 19, 22, 23, 25, 25]
    '''
    
    
    
    L1 = [1, 2, 3, 4]
    L2 = [1, 2, 3, 4]
    merged_L = merge(L1, L2)
    print(merged_L)
    '''
    L1 remaining:  [4]
    L2 remaining:  []
    [1, 1, 2, 2, 3, 3, 4, 4]
    '''

    L1 = [1, 2, 3, 4]
    L2 = [5, 6]
    merged_L = merge(L1, L2)
    print(merged_L)
    '''
    L1 remaining:  []
    L2 remaining:  [5, 6]
    [1, 2, 3, 4, 5, 6]
    '''
    
    L1 = [44, 55, 66, 77]
    L2 = [1, 10, 44, 55]
    merged_L = merge(L1, L2)
    print(merged_L)
    '''
    L1 remaining:  [55, 66, 77]
    L2 remaining:  []
    [1, 10, 44, 44, 55, 55, 66, 77]
    '''



'''merge sort -上课学的'''
def merge_sort(v):
    '''
    O(NlogN)
    Implementation of the merge sort algorithm.
    合并排序
    '''
    #就1个元素不能sort
    if len(v) <= 1:
        return
    
    #初始化lists
    lists = []
    #list里面的元素
    for item in v:
        #元素自成一个list存入大lists
        lists.append([item])
    
    #lists=[[9.1], [17.5], [9.8], [6.3], [12.4], [1.7]]
    
    
    i = 0
    
    while i < len(lists)-1:
        #每两个list按合成1个sortedlist，用之前写的merge
        new_list = merge(lists[i], lists[i+1])
        #尾部放入合成好的list，所以是不断越来越大
        lists.append(new_list)
        i += 2
        print(lists)
    
    #使用切片赋值 v[::] = ... 表示替换 v 中的所有元素
    #最后一个已经合并并sort好了
    v[::]= lists[-1]
    
    
'''切片赋值'''
v = [1, 2, 3]

v[:] = [4, 5, 6]
print(v)  # 输出: [4, 5, 6]

v[::] = [7, 8, 9]
print(v)  # 输出: [7, 8, 9]

'''copy 不影响原列表'''
v = [1, 2, 3]
copy_v = v[:]
copy_v = [3.3]
print(v)
#[1, 2, 3]

if __name__ == "__main__":

    v = [ 9.1, 17.5, 9.8, 6.3, 12.4, 1.7 ]
    merge_sort(v)
    print(v)
    '''
    [[9.1], [17.5], [9.8], [6.3], [12.4], [1.7], [9.1, 17.5]]
    
    [[9.1], [17.5], [9.8], [6.3], [12.4], [1.7], [9.1, 17.5], [6.3, 9.8]]
    
    [[9.1], [17.5], [9.8], [6.3], [12.4], [1.7], [9.1, 17.5], [6.3, 9.8], [1.7, 12.4]]
    
    [[9.1], [17.5], [9.8], [6.3], [12.4], [1.7], [9.1, 17.5], [6.3, 9.8], [1.7, 12.4], [6.3, 9.1, 9.8, 17.5]]
    
    [[9.1], [17.5], [9.8], [6.3], [12.4], [1.7], [9.1, 17.5], [6.3, 9.8], [1.7, 12.4], [6.3, 9.1, 9.8, 17.5], [1.7, 6.3, 9.1, 9.8, 12.4, 17.5]]
    
    [1.7, 6.3, 9.1, 9.8, 12.4, 17.5]
    '''
    
    
    
    #[1.7, 6.3, 9.1, 9.8, 12.4, 17.5]
    
'''去重的merge'''
    
def merge(L1,L2):
    '''
    Merge the contents of two lists, each of which is already sorted
    into a single sorted list.
    '''
    i1 = 0
    i2 = 0
    L = []

    '''
    Repeated choose the smallest remaining item from the lists until one
    list has no more items that have not been merged.
    '''
    while i1 < len(L1) and i2 < len(L2):
        if L1[i1] < L2[i2]:
            L.append( L1[i1] )
            i1 += 1
        elif L2[i2] < L1[i1]:
            L.append( L2[i2] )
            i2 += 1        
        #当等于时，不加进去，仍然迭代index
        elif L2[i2] == L1[i1]:
            i2 += 1
            
    L.extend(L1[i1:])   #  copy remaining items from L1, if any
    L.extend(L2[i2:])   #  copy remaining items from L2, if any
    return L



if __name__ == "__main__":
    L1 = [ 2, 7, 9, 12, 17, 18, 22, 25 ]
    L2 = [ 1, 5, 6,  8, 13, 14, 15, 18, 19, 23, 25 ]

    merged_L = merge(L1, L2)
    print(merged_L) #没有2个18或25了
    #[1, 2, 5, 6, 7, 8, 9, 12, 13, 14, 15, 17, 18, 19, 22, 23, 25]
    
    
'''谁更快！Final Comparison Across All Sorts

1. python 内置排序最快
2. Merge sort O(NlogN)
3. Selection sort and insertion sort O(N^2)

When almost sorted,
insertion sort 比selection sort快多了


FinalExam说要记住逻辑不是code
'''