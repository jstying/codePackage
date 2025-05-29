'''Lecture 14 Problem Solving and Design, Part 1'''

'''Find all pair of indices those elements whose
difference is k. Return a list of tuples for each pair'''

L=[-1,5,10,9,6,2,-3]
k=int(input("Please enter the number k => "))

#我需要nested for loop, index 0与1，0与2...这样比较

'''
1. create empty list
2. scan thrugh the list and find absolute difference between every pair - nested for loop
3. check diff is equal to k or not
4. If match, put it in the list, append((i,j)) 把一个元组放进去

corner cases: k is negative, zero
'''

x=[]
for i in range(len(L)):
    for j in range(i+1,len(L)):
        if abs(L[i] - L[j]) == k:
            x.append((i,j))
            
print(x)


'''找所有tuple里的最高分'''

scores = [(3, 2), (2, 1), (9, 1), (8, 7), (2, 0), (0,4), (1,7), \
          (29, 6), (27, 29), (30, 29), (2, 29)]

#set to be the first element 
high = scores[0][0]
#每个 tuple, looking for the highest score in the list
for score in scores:
    #tuple第一位比较
    if score[0] > high:
        #update highest
        high = score[0]
    #tuple第二位比较
    if score[1] > high:
        high = score[1]
print(high)



'''统计每个分数的达成次数 0-30/high high+1个位置'''
#[0]*2 [0,0]

#创建high+1个长度的list里面放了这么多个0，因为L1[30]要存在index30那里，所以加一格长度
L1 = (high+1) * [0]
print("Initialize L1:")
print(L1)
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for score in scores:
    #在相应score的index加1计数 e.g. L1[3]+=1
    L1[score[0]] += 1
    L1[score[1]] += 1
print("After counting:")
print(L1)
#[2, 3, 4, 1, 1, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 4, 1]


'''找到次数最多的次数'''
most = max(L1)
#4
print("Max occurence: {}".format(most))

if most == 1:
    #没有众数
    print("No Mode")
else:
    for index in range(len(L1)):
        #返回众数存在的index
        if L1[index] == most:
            print("Mode is at: {}".format(index))
            #Mode is at: 2
            #Mode is at: 29
            #说明2分，29分都是众数
            
            
            
L2 = []
for score in scores:
    #把所有分数存入L2, score是每个tuple
    L2.append(score[0])
    L2.append(score[1])

#自己排序一下    
L2.sort()           
print(L2)            
#[0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 4, 6, 7, 7, 8, 9, 27, 29, 29, 29, 29, 30]            


curr = 0   #初始化当前最大出现次数，不断比较刷新
index = 0  #L2的第一项开始
prev = -1  # 初始化前一项score
count = 0  #初始化当前score的出现次数
modes = [] # 显示出现最多的score

#scan the entire L2，遍历
while index < len(L2):
    
    #当前元素与上一个元素不同
    if L2[index] != prev:
        #目前出现次数比最大出现次数多
        if count > curr:
            #把目前看起来最多次的前一项数字，作为众数
            modes = [prev]
            #更新最多次数
            curr = count
        #同样最多次数的数字出现
        elif count == curr:
            #把那个数字也存进去，作为众数
            modes.append(prev)
        #把当前元素当成下一项的前一项
        prev = L2[index]
        #计数为出现1次
        count = 1
    #相同元素出现时
    else:
        #计数+1
        count += 1
    #move to next one
    index += 1
    
#将最后一项比较完
if count > curr:
    modes = [prev]
    curr = count
elif count == curr:
    modes.append(prev)
print(modes)












# 将 range 转换为列表
my_list = list(range(1, 10, 2))  # 生成[1, 3, 5, 7, 9]
print(my_list)  # 输出: [1, 3, 5, 7, 9]

# 将 range 转换为元组
my_tuple = tuple(range(1, 10, 2))  # 生成(1, 3, 5, 7, 9)
print(my_tuple)  # 输出: (1, 3, 5, 7, 9)






