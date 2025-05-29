'''Lecture 24 — Advanced Python Topics and Functional Programming'''

'''Map: Apply a function to each element of a list
map(func, iterable e.g.list,str,tuple,set,dict,range)
用list() 来看map里的东西

'''
#list of lists
v = [ [2, 3, 5, 7], [11,13,17,19], [23, 29], [31,37] ]
#map(len,v) map v里面每个元素/小list的长度   把map转成list打出来
print( list(map( len, v)) )
#[4, 4, 2, 2]

#把map里的元素加起来 4 4 2 2 
print(sum(map(len,v)))
#12

'''Passing Functions as Parameters'''
#distance from 原点
def dist2D( p ):
    # x平方+y平方 开根号
    return (p[0]**2 + p[1]**2)**0.5



pts = [ (4.5, 3), (2.1,-1), (6.8,-3), (1.4, 2.9) ]
#map pts里面每个元素/小tuple与原点的距离 转成list打出来
print(list( map(dist2D,pts) ))
#[5.408326913195984, 2.3259406699226015, 7.432361670424818, 3.2202484376209237]

#最大距离
print(max( map(dist2D,pts) ))
#7.432361670424818


'''Lambda functions: Anonymous functions
lambda 后面跟的是list里的元素
如果不习惯，还是def function 再用map
'''
#squaring the values of a list， 对于每个list的元素应用function x**2
#lambda parameter: func of that parameter
print(list(map( lambda x: x**2, [ 1, 2, 3, 4 ] )))
#[1, 4, 9, 16]


#平方每个1-100的数，加起来  1^2+2^2+...+100^2
n = 100
print(sum( map( lambda x: x**2, range(1,n+1))))
#338350


#用lamda来简化dist function，还是最大距离
pts = [ (4.5, 3), (2.1,-1), (6.8,-3), (1.4, 2.9) ]
print( max( map( lambda p: (p[0]**2 + p[1]**2)**0.5, pts) ))
#7.432361670424818

'''用map return the maximum x coordinate. 每个点/tuple x,y'''
pts = [ (6,-1), (8,4), (7.5,-3), (4.4,12), (7,2) ]
print(max(map( lambda p: p[0], pts)))
#8


'''Filter: Extract / eliminate values from a list
filter takes boolean  True从list拿取value, False不拿'''
v = [ 1, 9, -4, -8, 10, -3 ]
#大于0吗 True就拿 False就不管
print(list(filter( lambda x: x>0, [ 1, 9, -4, -8, 10, -3 ])))
#[1, 9, 10]

#1+9+10
print(sum(filter( lambda x: x>0, v)))
#20

'''Passing Functions to Sort'''
pts = [ (2,5), (12,3), (12,1), (6,5), (14, 10), (12, 10), \
          (8,12), (5,3) ]
    
'''我们想要sort by y, 降序, y一样的话，大的x在前面
[(8, 12), (14, 10), (12, 10), (6, 5), (2, 5), (12, 3), (5, 3), (12, 1)]
'''

#默认的话sort by x/tuple的第一个元素, 降序
print(sorted( pts, reverse=True ))
#[(14, 10), (12, 10), (12, 3), (12, 1), (8, 12), (6, 5), \
  #  (5, 3), (2, 5)]
  

#key 是个func，决定按什么排的 ， 按照y/tuple的第二个元素来排
'''但是（2，5） （6，5）还不对'''
print(sorted( pts, key = lambda p: p[1], reverse=True))
#[(8, 12), (14, 10), (12, 10), (2, 5), (6, 5), (12, 3), \
    #(5, 3), (12, 1)]  
    
'''正确做法'''
by_x = sorted(pts,reverse=True)
print(by_x)
#[(14, 10), (12, 10), (12, 3), (12, 1), (8, 12), (6, 5), \
  # (5, 3), (2, 5)]
print(sorted( by_x, key = lambda p: p[1], reverse=True))
#[(8, 12), (14, 10), (12, 10), (6, 5), (2, 5), (12, 3), \
  # (5, 3), (12, 1)]

'''法二'''
#它告诉 sorted 按照元组的第二个坐标（p[1]）为主排序；如果第二个坐标相同，再按照第一个坐标（p[0]）
print(sorted( pts, key = lambda p: (p[1], p[0]), reverse=True))
#[(8, 12), (14, 10), (12, 10), (6, 5), (2, 5), (12, 3), \
 # (5, 3), (12, 1)]  
  
  
  
  
'''List Comprehensions'''
#1到8，每个数要平方 把每个i*i 存进list
n = 8
print( [ i*i for i in range(1,n+1) ] )
#[1, 4, 9, 16, 25, 36, 49, 64]
  
  
#对于每个v里的元素，如果大于0， 把每个 x 存进list
v = [ 1, 9, -4, -8, 10, -3 ]
print([ x for x in v if x>0 ])
#[1, 9, 10]  

#大于0的每个元素的平方，存进list,还是 第一项x*x 是要存进去的东西
v = [ 1, 9, -4, -8, 10, -3 ]
print([ x*x for x in v if x>0 ])
#[1, 81, 100]

# i是1-4 j是1-4 只有i不等于j时存 tuple进list
print([ (i,j) for i in range(1,5) for j in range(1,5) if i != j ])
#[(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2),
    #(3, 4), (4, 1), (4, 2), (4, 3)]
    
'''Write a list comprehension statement to generate a list of all pairs of odd positive integer values
 less than 10 where the first value is less than the second value.
 pairs of正奇数，两个数字小于10，i<j
'''
print([(i,j) for i in range(1,10,2) for j in range(1,10,2) if i<j])    
#[(1, 3), (1, 5), (1, 7), (1, 9), (3, 5), (3, 7), (3, 9), (5, 7), (5, 9), (7, 9)]
