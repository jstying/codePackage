'''Lecture 19  Classes, Part 2'''

'''详见 lec19_restaurant_exercise.py 
Restaurant.py
'''



'''Circle — A new Circle Class 半成品'''
#导入math module
import math

class Circle(object):
    def __init__(self, x=0, y=0, r=1):
        '''
        x坐标，y坐标，r半径
        Returns
        -------
        A new circle definition centered at point
        (x, y) and having radius r

        x - x coordinate of the center
        y - y coordinate of the center
        r - Radius of the circle

        '''
        self.x = x
        self.y = y
        self.r = r
    
    def __str__(self):
        '''
        str形式
        Return a printable string representing the circle
        '''
        return "Circle at {} with radius {}".\
                    format(self.center(), self.r)
                    
    def center(self):
        '''
        返回带xy坐标的tuple
        Return a tuple representing the center of the circle
        '''
        return self.x, self.y
    
    def __lt__(self, other):
        '''self < other
        
        lexicographical order 序列
        A B C ... Z a b c ... z
        大写的 小于 小写字母
        
        
        (1, 2) < (1, 3)  # 比较第一个元素，1 == 1；比较第二个元素，2 < 3 -> True
        (1, 2) > (0, 99)  # 比较第一个元素，1 > 0 -> True
        (1, 2) == (1, 2)  # 两个元组完全相等 -> True
        (1, 2, 3) < (1, 2, 4)  # 逐个比较，前两个元素相等；比较第三个元素 3 < 4 -> True
        
        (1, "apple") < (1, "banana")  # 不同类型的元素无法比较，会报错：TypeError
        
        '''
        self_c = self.center()
        other_c = other.center()
        
        
        if self_c < other_c:
            return True
        elif other_c < self_c:
            return False
        
        #坐标相同，就比较半径
        else:
            return self.r < other.r
    

   
    def __add__(self, val):
        '''加上一个半径长度，返回新obj'''
        return Circle(self.x, self.y, self.r + val)
    
    
    def area(self):
        '''返回pi r 平方'''
        return math.pi * self.r ** 2
    
    
    def increase(self, val):
        '''自身增加半径，返回self obj 和__add__一样'''
        self.r += val
        return self
        
    def report_area(self):
        '''打出一句带有坐标tuple和面积的str'''
        print("This circle at {} has an awesome area {} ...".format(self.center(), self.area()))

if __name__ == "__main__":
    c1 = Circle(3, 5, 7)
    print(c1)
    c2 = Circle(4, 6)
    print(c2)
    c3 = Circle(5)
    print(c3)
    c4 = Circle()
    print(c4)
    '''
    Circle at (3, 5) with radius 7
    Circle at (4, 6) with radius 1
    Circle at (5, 0) with radius 1
    Circle at (0, 0) with radius 1
    '''
    
    
    print()
    print(c1 < c2)
    print(c2 < c1)
    print(c2 < c2)
    print(c2 < Circle(4, 6, 2))
    print(Circle(4, 6, 2) < c2)
    '''
    True
    False
    False
    True
    False
    '''
   
    print()
    print(c1+7)
    #Circle at (3, 5) with radius 14
    print("Area:", c4.area())
    #Area: 3.141592653589793
    
    print(c1)
    c12 = c1.increase(12)
    print(c1)
    print(c12)
    c12.increase(2)
    print(c12)
    print(c1)
    c1.report_area()
    '''
    Circle at (3, 5) with radius 7
    Circle at (3, 5) with radius 19
    Circle at (3, 5) with radius 19
    Circle at (3, 5) with radius 21
    Circle at (3, 5) with radius 21
    This circle at (3, 5) has an awesome area 1385.4423602330987 ...
    '''
    