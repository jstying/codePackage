'''Controlling Loops'''

'''Part 1: Ranges and For Loops— A Review'''

for i in range(10):
    print(i) #print 0-9 每行换行
print()



for i in range(3,8):
    print(i) #print 3-7 每行换行
print()
    
for i in range(4,21,3):
    print(i) #print 4,7,10,13,16,19 递增3，终于21 
    
#convert range into list
print(list(range(-1,-10,-1)))
#[-1, -2, -3, -4, -5, -6, -7, -8, -9]

lc=list(range(1,10))
print(lc)
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

print(tuple(range(-1,-10,-1)))
#(-1, -2, -3, -4, -5, -6, -7, -8, -9)



planets = [ 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter',
    'Saturn', 'Uranus', 'Neptune', 'Pluto' ]
for i in range(len(planets)):
    print(planets[i]) #print each planet in the list
    
print()    

#how to reverse the order and print
for i in range(len(planets)-1,-1,-1):
    print(planets[i])
print()    

#reverse the order and print, last first, -1 到 -9， 终止于-10
for i in range(-1,-len(planets)-1,-1):
    print(planets[i])
print()    
#pluto uranus jupiter earth Mercury 
for i in range(-1,-len(planets)-1,-2):
    print(planets[i])
print()     
for i in range(-1,-len(planets)-1,-2):
    print(i)    # print the index -1,-3,-5,-7,-9
print()    
    
'''
aabbcc
'''


#为什么len(s)-5
#确保至少6个char可以检查，i+5不会超出范围,i+5必须小于len, 终于len-5,0到len-6

def has_three_doubles(s):
    for i in range(0, len(s)-5):
        if s[i] == s[i+1] and s[i+2] == s[i+3] and s[i+4] == s[i+5]:
            return True
    return False

print(has_three_doubles("xyaabbcc"))
#True




'''Use a range and a for loop to print the positive, 
even numbers less than the integer value associated with n.'''



n=10
for i in range(2,n,2):
    print(i)





#Suppose we want a list of the squares of the digits 0..9. 
squares = list(range(10))
final=[]
for s in squares:
    s = s*s
    final.append(s)
print(final)


'''Part 2: Nested Loops'''


#0-9 0-9 每两个数之间相乘的等式， times table 乘法表
digits = range(10)
for i in digits:
    for j in digits:
        print("{} x {} = {}".format(i,j,i*j))


#Finding the Two Closest Points
points = [ (1,5), (13.5, 9), (10, 5), (8, 2), (16,3) ]

from math import sqrt


dist = 1000


# 使用两层循环比较每一对点之间的距离
for i in range(len(points)):
    for j in range(i + 1, len(points)):  # 避免重复计算距离
        # 计算两点之间的距离
        distance = sqrt((points[j][1] - points[i][1]) ** 2 + (points[j][0] - points[i][0]) ** 2)
        
        # 如果计算出的距离比当前的最小距离小，则更新最小距离和对应的点
        if distance < dist:
            dist = distance
            point1 = points[i]
            point2 = points[j]

            
print("The closest distance is {:.2f} between points {} and {}".format(dist, point1, point2))






#list of lists, find the maximum average
temps_at_sites = [ [ 12.12, 13.25, 11.17, 10.4],
                   [ 22.1, 29.3, 25.3, 20.2, 26.4, 24.3 ],
                   [ 18.3, 17.9, 24.3, 27.2, 21.7, 22.2 ],
                   [ 12.4, 12.5, 12.14, 14.4, 15.2 ] ]


averages = [] #存储每个avg
for site in temps_at_sites: #每个里面的list
    avg = sum(site) / len(site)
    averages.append(avg)

max_avg = max(averages)
max_index = averages.index(max_avg) #index of 小list that has maximum avg
print("Maximum average of {:.2f} occurs at site {}".format(max_avg, max_index))

'''using a break'''
#while true一直循环，直到break，退出循环
sum = 0
while True:
    x = int(input("Enter an integer to add (0 to end) ==> "))
    if x == 0:
        break #退出
    sum += x

print(sum)#不停加的值



mylist = [3, -1, 5, -7, 0, 9, -3, 4] 

for item in mylist:
    if item < 0:  
        continue  # 跳过当前项，不打印
    print(item)  # 打印非负数的项
    
#continue 跳过这次循环，进入下一次循环



for i in range(5):
    if i == 2:
        continue  # 不打印2
    print(i) #0 1 3 4



import math
x = float(input("Enter a positive number -> "))
while x > 1:
    x = math.sqrt(x)
    print(x, flush=True)
#This loop will terminate when x becomes less than or equal to 1.

    
    
import math
x = float(input("Enter a positive number -> "))
while x >= 1:
    x = math.sqrt(x)
    #立即输出内容
    print(x, flush=True)
#This loop causes an infinite loop if x becomes exactly 1, because math.sqrt(1) is always 1,\
    #so the loop condition x >= 1 will never become false.
    
    
    
    
    
    
total = 0
for i in range(10):
    for j in range(10):
        total += 1
print(total) #100 10x10



total = 0
for i in range(10):
    for j in range(i+1,10):
        total += 1
print(total) #45 
'''
i=0 j=1,2,3,4,5,6,7,8,9
i=1, j=2-9
2  3-9
3 4-9
4 5-9
5 6789
6 789
7 89
8 9
9 none

9+8+7+6+..+1=45
'''

total = 0
for i in range(10):
    total += 1
for j in range(10):
    total += 1
print(total) #20





 #initialize 同样的值
sum_up=sum_low=0
 
 #initialize 不同的值
a,b=0,1