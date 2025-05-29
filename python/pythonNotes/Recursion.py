'''Lecture 23 — Recursion
When a function calls itself, it is known as a recursive function 自己叫自己'''


'''First example'''
#点火发射
def blast(n):
    if n > 0:
        #打出这个n，作为倒计时
        print(n)
        #自己叫自己，n递减1
        blast(n-1)
        
    #n<=0时
    else:
        #发射
        print("Blast off!")
    return

blast(5)
'''
5
4
3
2
1
Blast off!
'''

'''practice problem to illustrate Python’s Call Stack Mechanism'''
#L 是 list, i是index
'''print first,call next 一个个把list里的元素打出来，i+1来指向下一个 '''
def rp1( L, i ):
    #i<5？
    if i < len(L):
        print(L[i], end=' ')
        rp1( L, i+1 )
    else:
        print()
        
'''call first,print next 

When a function ends, Python looks at the top of the stack
从后往前回溯


i
0  rp2(L,1) 6.等待打出2
1  rp2(L,2) 5.等待打出3
2  rp2(L,3) 4.等待打出5
3  rp2(L,4) 3.等待打出7
4  rp2(L,5) 2.等待打出11
5  1.打出空行


'''
def rp2( L, i ):
    if i < len(L):
        rp2( L, i+1 )
        print(L[i], end=' ')
    else:
        print()

L = [ 2, 3, 5, 7, 11 ]
rp1(L,0)
#2 3 5 7 11 

rp2(L,0)
#11 7 5 3 2 
print()

'''Factorial
n!=n(n−1)(n−2)⋯1
n!=n⋅(n−1)!
0!=1

5!
5*fact4
5*4*fact3
...
5*4*3*2*1*fact(0) 也就是1
'''
def fact(n):
    #base case，终止recursion（不再叫自己）
    if n == 0:
        return 1
    #recursive part
    else:
        return n*fact(n-1)
    
print(fact(5))
#120

'''fibonacci
0,1,1,2,3,5,8,13,21,34,55
fn=fn−1+fn−2

5
f4+f3
f3+f2 + f2+f1
f2+f1 f1+f0 f1+f0 f1
f1+f0 +f1 f1+f0 f1+f0 f1
5
'''
def fib(n):
    #fixed first number 0
    if n == 0:
       return 0
    #fixed second number 1
    if n == 1:
       return 1
    #sum of the previous two
    return fib(n - 1) + fib(n - 2)

print(fib(5))
#5
print(fib(7))
#13




'''Final Example: Merge Sort'''
""" 

We rewrite merge_sort using recursion and compare to the 
iterative version. The recursive version is natural to write 
and does not require a list/loop to maintain sublists. As a 
result, it is slightly more efficient.


"""

import time
import random


def time_function(L, func):
    """ Illustrates how you can send a function as an argument
    to another function as well. Runs the function called func,
    and returns the time.

    """

    L1 = list(L)
    start = time.time()
    func(L1)
    end = time.time()
    print("Method: {:s} took {:f} seconds".format((func.__name__).ljust(20), end-start))


def merge(L1, L2):
    """ Assume L1 and L2 are sorted.
    Create a new list L that is the merged
    version of L1&L2.
    
    This is the efficient version of merge
    that does not modify the input lists, as pop 
    is costly, even though it is a constant time operation.

    """
    
    L = []
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            val = L1[i]
            L.append( val )
            i += 1
        else:
            val = L2[j]
            L.append( val )
            j += 1
    ## at this point, either L1 or L2 has run out of values
    ## add all the remaining values to the end of L.
    L.extend(L1[i:]) 
    L.extend(L2[j:])
    return L


    
def merge_sort_iterative(L):
    """ Complexity: O(n* log n)
        See earlier version of this code for explanation.

    """

    L1 = []
    for val in L:
        L1.append( [val] )
    
    while len(L1) > 1:
        L2 = []
        for i in range(0, len(L1)-1, 2):
            Lmerged = merge( L1[i], L1[i+1] )
            L2.append( Lmerged )
            
        if len(L1)%2 == 1:
            L2.append( L1[-1] )
        L1 = L2
    return L1[0]


def merge_sort_recursive(L):
    """ Complexity: O(n logn)
        The function calls itself recursively logn times,
        and each time about n elements are merged.

    """
    if len(L) == 1:
        #没什么好sort的
        return L
    
    length = len(L)
    #list切一半
    mid = length // 2
    #左边的数merge sort
    left = merge_sort_recursive(L[:mid])
    #右边的数merge sort
    right = merge_sort_recursive(L[mid:])
    #最后把左边和右边的合体merge sort
    return merge(left,  right)

if __name__ == "__main__":
    ##Testing code
    k = 100000
    L = list(range(k))
    random.shuffle(L)
    
    time_function( L, merge_sort_iterative )
    time_function( L, merge_sort_recursive )
    time_function( L, list.sort )
    
    
    
'''Flattening a Nested List'''
def flatten(L):
    result = []
    for x in L:
        if type(x) == list:
            result.extend( flatten(x) )
        else:
            #不是list的时候就直接把数传进来
            result.append(x)
    return result

def flatten2(L):
    
    if type(L) != list:
        return [L]
    else:
        result = []
        for x in L:
            #不断的去皮，call自己直到最后变成[L]时，把L传进去
            result.extend( flatten2(x) )
            print(result)
        return result

    
if __name__ == "__main__":
    v = [[1,5], 6, [[2]], [3, [7, 8, [9,10], [11,12] ]]]
    print(v)
    #[[1, 5], 6, [[2]], [3, [7, 8, [9, 10], [11, 12]]]]
    print(flatten(v))
    #[1, 5, 6, 2, 3, 7, 8, 9, 10, 11, 12]
    print(flatten2(v))
    #[1, 5, 6, 2, 3, 7, 8, 9, 10, 11, 12]
    '''
    print(flatten2(2))
    print(flatten(2))
    '''
    
'''Recursive triangles'''
"""
Example program shows the use of recursion to create fractals, 
in this case, the Sierpinski Triangle. See function:

draw_triangles

for the recursion. The rest is TkInter program allowing the
user to change properties of the Sierpinski triangle drawn.

"""


from tkinter import *
import math

class MyApp(object):
    def __init__(self, parent):
        ##Function local to init to simplify repetitive button creation process
        def put_button(parent, name, functionname, placement):
            newbutton = Button(parent, text=name, command=functionname)
            newbutton.pack(side=placement)
            newbutton.configure(width=button_width,\
                                padx=button_padx, pady=button_pady )
            return newbutton
        
        ## constants used  in the initialization
        button_width = 10
        button_padx = "3m"
        button_pady = "3m"

        ## variables used in the program
        self.maxlevel = 6
        self.size = 600  #3**self.maxlevel
        self.maxy = int(self.size*math.sqrt(3)/2)
        self.stopped = False
        self.depth = 2
        self.wait_time = 1
        self.parent = parent
        
        ## interface elements
        ## all frames
        self.main_frame = Frame(parent)
        self.main_frame.pack()
        self.top_frame = Frame(self.main_frame)
        self.top_frame.pack(side=TOP)
        self.bottom_frame = Frame(self.main_frame)
        self.bottom_frame.pack(side=BOTTOM)

        ## canvases: top for info, buttom for drawing Triangles
        self.infocanvas = Canvas(self.top_frame, \
                                 width=self.size, height=30)
        self.infocanvas.pack(side=TOP)
        self.text_area = self.infocanvas.create_text(30,10,anchor='nw')
        self.canvas = Canvas(self.top_frame, \
                             width=self.size, height=self.maxy)
        self.canvas.pack(side=BOTTOM)

        ## buttons: for controlling the program
        self.drawbutton = put_button(self.bottom_frame, 'Draw', self.draw, LEFT)
        self.clearbutton = put_button(self.bottom_frame, 'Clear', self.clear, LEFT)
        self.fasterbutton = put_button(self.bottom_frame, \
                                         "Faster", self.faster, LEFT)
        self.slowerbutton = put_button(self.bottom_frame, \
                                         "Slower", self.slower, LEFT)
        self.increasebutton = put_button(self.bottom_frame, \
                                         "Depth+1", self.increase, LEFT)
        self.decreasebutton = put_button(self.bottom_frame, \
                                         "Depth-1", self.decrease, LEFT)
        self.quitbutton = put_button(self.bottom_frame, \
                                     "Quit", self.quit, RIGHT)
        ## display settings for the program on the info canvas
        self.put_info()

    def put_info(self):
        """ Function for displaying the settings for the program, 
            depth and wait time for the animation effect.

        """
        
        info = "Wait time: %d ms" %(self.wait_time)
        if self.depth == self.maxlevel+3:
            info += " "*10+ "Depth: %d (max level reached)" %self.depth 
        elif self.depth == 0:
            info += " "*10+ "Depth: 0 (min level reached)"
        else:
            info += " "*10+ "Depth: %d" %self.depth
        self.infocanvas.itemconfigure(self.text_area, text=info)

    def clear(self):
        """ Clear the drawing (used in self.clearbutton). """
        self.canvas.delete("all")
        
    def faster(self):
        """ Make the animation faster (used in self.fasterbutton). """
        self.wait_time //= 2
        if self.wait_time <= 0:
            self.wait_time = 1
        self.put_info()

    def slower(self):
        """ Make the animation slower (used in self.slowerbutton). """
        self.wait_time *= 2
        self.put_info()
        
    def increase(self):
        """ Increases the depth for recursion (used in self.fasterbutton). """
        if self.depth < self.maxlevel+3: 
            self.depth += 1
            self.put_info()
        
    def decrease(self):
        """ Decreases the depth for recursion (used in self.slowerbutton). """
        if self.depth > 0:
            self.depth -= 1
            self.put_info()
            
    def draw(self):
        """ Clear the canvas and draws the Sierpinksi triangles (used in self.drawbutton). """
        padding = 20 ##just leave some space off the corners
        if not self.stopped:
            self.clear()
            self.draw_triangles(0+padding,self.maxy-padding,self.size-2*padding, 1)
            
    def draw_triangles(self, x, y, length, depth):
        """ Draws two triangles: one with x,y as the bottom left corner,
            in red and a second inverted one inside between the midpoints
            of the outside triangle, in white.

        """
        ## Triangle 1: Outside Triangle
        mid = length/2
        self.canvas.create_polygon(x, y, \
                                   x+length, y, \
                                   x+mid, y-math.sqrt(3)*mid,\
                                   fill = "red")
            
        if depth <= self.depth:
            ## Triangle 2: Inside Triangle
            leftmid = ( x+(mid)/2, y-(math.sqrt(3)*mid)/2 )
            rightmid = (  x+(length+mid)/2, y-(math.sqrt(3)*mid)/2 )
            bottommid = ( x+mid, y )
            
            self.canvas.create_polygon( leftmid[0], leftmid[1], \
                                        rightmid[0], rightmid[1], \
                                        bottommid[0], bottommid[1], \
                                        fill = "white" )
            self.draw_triangles(x, y, length/2, depth+1)
            self.draw_triangles(leftmid[0], leftmid[1], length/2, depth+1)
            self.draw_triangles(x+length/2, y, length/2, depth+1)
            ## Add animation effect
            self.canvas.update()
            self.canvas.after(self.wait_time)
            
    def quit(self):
        self.stopped = True
        self.parent.destroy()

if __name__ == "__main__":
    root = Tk()
    root.title("Recursion Example with Sierpinski Triangles")
    myApp = MyApp(root)
    root.mainloop()
    
    

def recursive_max_impl( L, i ):
    '''
    The actual recursive function.
    '''
    if i == len(L)-1:
        #最后一位
        return L[i]
    else:
        #不断把下一位拿进来找最大值
        return max(L[i], recursive_max_impl(L,i+1) )

def recursive_max( L ):
    '''
    The driver for the recursive function.  This handles the special
    case of an empty list and otherwise makes the initial call to the
    recursive function.
    '''
    if len(L) == 0:
        return -99999    # By convention
    else:
        return recursive_max_impl( L, 0 )

if __name__ == "__main__":
    L1 = [ 5 ]
    print(recursive_max( L1 ))
    L2 = [ 24, 23.1, 12, 15, 1 ]
    print(recursive_max( L2))
    L2.append( 55 )
    print(recursive_max( L2 ))