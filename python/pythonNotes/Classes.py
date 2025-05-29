'''Lecture 18 — Classes, Part 1'''

'''Objects 解释，可不看

Time: 2:09 PM -> time

Point = (x,y)

Data representation
Interaction

Student = (Name,ID,GPA)
method - to access Student object

Restaurant object -> ratings, locations
methods -> food that a restaurant serves

'''

'''
#定义Point2d 类
class Point2d(object):
    pass #在class、func、loop或if中使用 pass，表示暂时什么都不做。 或者代码还没写
'''   





from math import sqrt
class Point2d(object):
    # __init__ 是初始化方法
    #self 是object自己。(self,x,y) x,y是要赋予的初始值  也可以(self,x=0,y=0) 默认设置个初始
    def __init__(self, x=0, y=0):
        '''
        Initialization  x,y要作为参数传入
        创建一个obj
        obj1=Point2d()
        obj2=Point2d(5,7)   
        obj3=Point2d(4,6)
        '''
        #self的x属性赋值初始的x0
        self.x = x
        self.y = y

        
    def magnitude(self):
        '''
        Distance from the origin 根号下x^2+y^2
        括号内无需参数
        
        length=obj.magnitude()
        
        '''
        return sqrt(self.x**2 + self.y**2)

    def dist(self, o):
        '''
        Distance between 2 points / objs
        另一个obj作为参数 一般用 o
        
        dist=obj1.dist(obj2)
        
        '''
        return sqrt( (self.x-o.x)**2 + (self.y-o.y)**2 )
    
    #lec ex
    def scale(self,s):
        '''scale the object's x and y by int s, 会修改self的x和y属性,改变自身obj，不创建新obj,不返回如何东西
        传入参数s，作为倍数
        
        obj.scale(6)
        print(obj.x)
        #30
        print(obj.y)
        #42
        
        '''
        self.x *= s
        self.y *= s
        
    #lec ex        
    def dominates(self, o):
        '''check self object has larger x y than the other object
        与另一个obj 比较xy属性大小，返回boolean
        
        print(p.dominates(q))
        #True
        
        '''
        return self.x > o.x and self.y > o.y
    
    #加法
    def __add__(self,other):
        '''
        Add two points and return a new object
        把x y属性分别加起来， 创建一个新的obj
        __add__ "+"
        
        p=Point2d(5,7)   
        q=Point2d(4,6)   

        pq = p + q
        print(pq.x,pq.y)
        #9 13
        '''
        return Point2d(self.x + other.x, self.y+other.y)       
    
    #lec ex
    def __str__(self):
        '''return in the format of a tuple
        str(obj)
        
        
        p=Point2d(5,7)   
        q=Point2d(4,6)   

        print(str(p))
        #(5,7)
        print(str(q))
        #(4,6)
        
        
        '''
        
        return "({},{})".format(self.x, self.y)
    
    
    #减法
    def __sub__(self,other):
        '''
        subtract two points and return a new object
        "-"
        p=Point2d(5,7)   
        q=Point2d(4,6)   
        p_q = p - q
        print(p_q.x,p_q.y)
        #1 1
        
        '''
        return Point2d(self.x - other.x, self.y-other.y)     
    
    
    #lec ex
    def __mul__(self,s):
        '''
        multiplication by 倍数s and return a new object
        '*'
        p=Point2d(5,7)   
        pt3 = p*3
        print(pt3.x,pt3.y)
        #15 21
        '''
        return Point2d(self.x*s, self.y*s)  
    
    #equal
    def __eq__(self, o):
        '''check whether two objects have the same x and y
        == 两个等号
        
        p=Point2d(5,7)   
        q=Point2d(4,6)   

        bo = p == q
        print(bo)
        #False
        
        '''
        return self.x==o.x and self.y==o.y
    
    
    #not equal
    def __ne__(self, o):
        '''!=
        两个obj xy属性不同
        
        bo2 = p!=q
        print(bo2)
        #True
        '''
        return self.x!=o.x and self.y!=o.y
        
    
    def __neg__(self):
        '''把x，y属性搞负,返回一个新obj
        g=Point2d(2,9)  
        neg_g = -g
        print(neg_g.x,neg_g.y)
        #-2 -9
        
        '''
        
        return Point2d(-self.x,-self.y)
    
    
#create object with 默认数值 Point2d(0,0)  
a=Point2d()  
print(a.x,a.y)
#0 0 

g=Point2d(2,9)  
neg_g = -g
print(neg_g.x,neg_g.y)
#-2 -9


p=Point2d(5,7)   
q=Point2d(4,6)   

'''str format形式obj放进去就变成了str（obj）的模样'''
print(" {}  {} ".format(p, q))
# (5,7)  (4,6) 

print(str(p))
#(5,7)
print(str(q))
#(4,6)

bo = p == q
print(bo)
#False

bo2 = p!=q
print(bo2)
#True

pq = p + q
print(pq.x,pq.y)
#9 13

p_q = p - q
print(p_q.x,p_q.y)
#1 1

p=Point2d(5,7)   
pt3 = p*3
print(pt3.x,pt3.y)
#15 21

length=p.magnitude()
print(length)
#8.602325267042627

#call 的时候不需要传入self了
dist=p.dist(q)
print(dist)
#1.4142135623730951

print(p.dominates(q))
#True

p.scale(6)
print(p.x)
#30
print(p.y)
#42


'''Operators and other special Functions'''
#__add__ 像这样前后有两个underscores就是特殊，不用这么obj.__add__调用，直接通过+
p.__init__(0,0)
print(p.x,p.y)
#0 0

q2=Point2d(4,6)
print(q.__eq__(q2))
#True





'''
相同的用法
leng = q.magnitude()
leng = Point2d.magnitude(q)

dist = p.dist(q)
dist = Point2d.dist(p, q)

sum = p+q
sum = Point2d.__add__(p, q)

5 + 6
int.__add__(5, 6)

str(13)
int.__str__(13)






obj特殊方法列举：
__add__	+ (加)
__sub__	- (减)
__mul__	* (乘)
__truediv__	/ (真除法)
__floordiv__	// (整除)
__mod__	% (取模)
__pow__	** (幂运算)
__neg__	- (取负)
__pos__	+ (取正)


__eq__	== (相等)
__ne__	!= (不相等)
__lt__	< (小于)
__le__	<= (小于等于)
__gt__	> (大于)
__ge__	>= (大于等于)

__int__	转为整数（int(obj)）
__float__	转为浮点数（float(obj)）
__str__	转为字符串（str(obj)）
__bool__	转为布尔值（bool(obj)）

'''


""" 
Class for storing time. Time is maintained as seconds since midnight

"""

class Time(object):
    def __init__(self, hr, min, sec):
        '''传入参数小时，分钟，秒
        t2 = Time(10, 29, 37)
        转成秒数-属性
        '''
            
        if hr > 24:
            hr = hr%24        
        self.seconds = hr*60*60 + min*60 + sec
        
    def convert(self):
        hr = self.seconds//3600
        min = (self.seconds - hr*3600)//60
        sec = self.seconds - hr*3600 - min*60
        #返回 的是一个元组 return a,b,c
        '''
        t2 = Time(10, 29, 37)
        print(t2.convert())
        (10, 29, 37)
        '''
        return hr, min, sec
        
    def __str__(self):
        '''obj转成str'''
        hr, min, sec = self.convert()
        #return '{:02d}:{:02d}:{:02d}'.format(hr, min, sec) 等同于下面老式的写法, {:02d} 不足两位用0补充
        return '%02d:%02d:%02d' \
               %(hr, min, sec)
    
    def __add__(self, other):
        '''obj1+obj2 属性加起来后 返回新的obj'''
        total = self.seconds + other.seconds
        hr = total/3600
        min = (total - hr*3600)/60
        sec = total - hr*3600 - min*60
        return Time(hr, min, sec)
    
    def __sub__(self, other):
        '''obj1-obj2 属性相减后 返回新的obj'''
        total = self.seconds - other.seconds
        if total < 0:
            total += 24*3600
        hr = total/3600
        min = (total - hr*3600)/60
        sec = total - hr*3600 - min*60
        return Time(hr, min, sec) 

        
if __name__ == '__main__':
    t2 = Time(10, 29, 37)
    
    print(t2.convert())
    
    print(str(t2))
    t3 = Time(23, 59, 59)
    print(str(t3))    

""" 
Class for storing time. Time is reported on a military (24 hour) clock. We
use a list to store hours minutes and seconds as list[0], list[1] and list[2]
explicitly
"""

class Time1(object):
    def __init__(self, hr=0, minute=0, sec=0):
        '''参数传入hr,minute,sec
        用list作为time属性'''
        self.time = [hr, minute, sec]
        
    def convert(self):
        pass
        
    def __str__(self):
        '''调用obj也即是self的time属性  转成str'''
        return "{:02d}:{:02d}:{:02d}".format(self.time[0],self.time[1],self.time[2])       
    
    def __add__(self, other):
        '''obj1 + obj2 返回新obj'''
        
        #先全部加起来各个
        new_hrs = self.time[0] + other.time[0]
        new_mins = self.time[1] + other.time[1]
        new_secs = self.time[2] + other.time[2]
        
        #整除出秒数多余的分钟，取余剩下的作为新秒数
        add_minutes = new_secs // 60
        new_secs = new_secs % 60
        
        #加上多余的分钟成为新分钟，但是整除出多余的小时，取余剩下的成为新分钟
        new_mins += add_minutes
        add_hours = new_mins // 60
        new_mins = new_mins % 60
        
        #多余小时加到小时总数，总数取余24小时一天剩下新的小时结束
        new_hrs += add_hours
        new_hrs = new_hrs % 24
        
        return Time(new_hrs, new_mins, new_secs)
    
    def __sub__(self, other):
        '''self - other 返回新obj'''
        
        seconds = self.time[2] + 60 * self.time[1] + 60*60*self.time[0]
        other_seconds = other.time[2] + 60 * other.time[1] + 60*60*other.time[0]
        #总差值小时
        new_seconds = seconds-other_seconds
        
        # if the subtraction makes us go negative, then add 24 hours to 
        # make it positive
        if new_seconds < 0:
            new_seconds += 3600 * 24
        
        
        #先整除归出小时数
        new_hrs = new_seconds // 3600
        #取余出剩下的
        new_seconds = new_seconds % 3600
        #再整除归出分钟数
        new_mins = new_seconds // 60
        #取余出剩下的作为秒数，结束
        new_seconds = new_seconds % 60
        
        return Time(new_hrs, new_mins, new_seconds)
        


if __name__ == '__main__':
    t1 = Time1()
    print(str(t1))
    t2 = Time1(10, 29, 37)
    print(str(t2))
    t3 = Time1(23, 59, 59)
    print(str(t3))
    '''
    00:00:00
    10:29:37
    23:59:59
    '''
    
    
    print("{} + {} = {}".format(t3, t3, t3 + t3))
    print("{} - {} = {}".format(t1, t2, t1 - t2))
    print("{} - {} = {}".format(t2, t1, t2 - t1))
    print("{} - {} = {}".format(t2, t3, t2 - t3))
    print("{} - {} = {}".format(t3, t2, t3 - t2))
    '''
    23:59:59 + 23:59:59 = 23:59:58
    00:00:00 - 10:29:37 = 13:30:23
    10:29:37 - 00:00:00 = 10:29:37
    10:29:37 - 23:59:59 = 10:29:38
    23:59:59 - 10:29:37 = 13:30:22
    '''
    