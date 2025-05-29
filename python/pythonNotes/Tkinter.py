'''Lecture 22 — TKInter   /tikei inter/  Graphical user interface'''


'''TkInter First Program'''

#import entire library from lib_name import *
from tkinter import * ### (1)

#main object root
root = Tk()           ### (2)
#tell the obj to start the loop， waiting for events（但打开的主窗口里啥都没有)
root.mainloop()       ### (3)
#关掉这个主窗口kill the interface，退出loop，做下一行也就是打印
print("Hello")        ### (4)



'''Example use of containers and buttons'''
from tkinter import *

#create main object
root = Tk()
#create a frame attached to the root - container - widget容器，管理各种组件（按钮，标签）
main_frame = Frame(root)
main_frame.pack()


top_frame = Frame(main_frame)
#move it to the top
top_frame.pack(side=TOP)

bottom_frame = Frame(main_frame)
#move it to the bottom 
bottom_frame.pack(side=BOTTOM)

#create 2 buttons in the top frame 在上面的框架
button1 = Button(top_frame, text="Top 1")
#put it in the left
button1.pack(side=LEFT)
button2 = Button(top_frame, text="Top 2")
#put it in the right
button2.pack(side=RIGHT)

#create 2 buttons in the top frame 在下面的框架
button3 = Button(bottom_frame, text="Bottom 1")
button3.pack(side=LEFT)
button4 = Button(bottom_frame, text="Bottom 2")
button4.pack(side=RIGHT)
#打开主窗口，呈现出4个按钮咯，但是按按钮没反应
root.mainloop()


'''Running tkinter programs using classes 和上面一样'''
from tkinter import *

class MyApp(object):
    def __init__(self, parent):
        self.parent = parent
        self.main_frame = Frame(parent)
        self.main_frame.pack()

        self.top_frame = Frame(self.main_frame)
        self.top_frame.pack(side=TOP)
        self.bottom_frame = Frame(self.main_frame)
        self.bottom_frame.pack(side=BOTTOM)

        self.button1 = Button(self.top_frame, text="Top 1")
        self.button1.pack(side=LEFT)
        self.button2 = Button(self.top_frame, text="Top 2")
        self.button2.pack(side=RIGHT)
        self.button3 = Button(self.bottom_frame, text="Bottom 1")
        self.button3.pack(side=LEFT)
        self.button4 = Button(self.bottom_frame, text="Bottom 2")
        self.button4.pack(side=RIGHT)

if __name__ == "__main__":
    root = Tk()
    myapp = MyApp(root)
    root.mainloop()
    
'''Example Program with a Button Click quit按钮关闭主窗口'''
from tkinter import *

class MyApp(object):
    def __init__(self, parent):
        self.parent = parent
        self.main_frame = Frame(parent) 
        self.main_frame.pack()
        self.button = Button(self.main_frame, text="Quit", command=self.terminate_program)#when it is clicked, it will call the function called self.terminate_program.
        self.button.configure(width=12, padx="4m", pady="4m")
        self.button.pack()

    def terminate_program(self):
        print("In terminate program")
        #destroy 关闭
        self.parent.destroy()

if __name__ == "__main__":
    root = Tk()
    myapp = MyApp(root)
    root.mainloop()
   
   
   
   


'''Canvas Widget 画布组件-创建一个椭圆'''
from tkinter import *
root = Tk()
main_frame = Frame(root)
main_frame.pack()

#主窗口200x200， 左上角是0，0
canvas = Canvas(main_frame, height=200, width=200)
canvas.pack()

#形成一个 正方形，左上角坐标是 (40, 40)，右下角坐标是 (80, 80)，
#所以绘制出来的是一个 圆形，其半径为 20 像素，圆心在 (60, 60)
canvas.create_oval((40,40,80,80))
canvas.update()

#一个扁一点的
canvas.create_oval((40,40,120,80))
canvas.update()

root.mainloop()


'''Final Program 漂亮的圆形图案生成，CD唱片一样'''
from tkinter import *

class MyApp(object):
    def __init__(self, parent):
        ## This method is internal to the initializer method
        ## and is used for creating buttons. It shortens the program code
        def new_button(parent, cmd, buttontext, packlocation):
            button = Button(parent, command=cmd)
            button.configure(text=buttontext)
            button.configure(width=button_width,
                  padx=button_padx, pady=button_pady )
            button.pack(side=packlocation)
            return button

        #------ constants for controlling layout ------
        button_width = 10
        #padding - widget 与边界之间的距离
        button_padx = "2m"
        button_pady = "1m"
        buttons_frame_padx =  "3m"
        buttons_frame_pady =  "2m"
        buttons_frame_ipadx = "3m"
        buttons_frame_ipady = "1m"
        # -------------- end constants ----------------

        #---------variables for controlling the function-----
        self.canvas_dimension = 600 ##Canvas will be a square
        #延迟8秒
        self.wait_time = 8
        self.repetitions = 2
        #----------end of variables--------------------------
        #root object
        self.myParent = parent
        #create frame
        self.main_frame = Frame(parent)
        self.main_frame.pack ()

        ## Two frames inside the main frame, one for the canvas
        ## on top and the second one for buttons in the bottom
        #create second frame
        self.draw_frame = Frame(self.main_frame)
        self.draw_frame.pack(side=TOP)

        self.info_canvas = Canvas(self.draw_frame, height=20,
                                   width=self.canvas_dimension)
        self.info_canvas.pack(side=TOP)
        #create text area anchor position northwest
        self.text_area = self.info_canvas.create_text(10,10,anchor='nw')
        self.info_canvas.itemconfigure(self.text_area,text="#circles = {:d}".format(self.repetitions))

        self.main_canvas = Canvas(self.draw_frame, \
                                  height=self.canvas_dimension,
                                  width=self.canvas_dimension)
        self.main_canvas.pack()

        self.button_frame = Frame(self.main_frame)
        self.button_frame.pack(side=BOTTOM)
        
        self.draw_button = new_button(self.button_frame,self.draw, 'Draw', LEFT)
        self.clear_button = new_button(self.button_frame,self.clear, 'Clear', LEFT)
        self.increase_button = new_button(self.button_frame,self.increase, 'Increase', LEFT)
        self.reduce_button = new_button(self.button_frame,self.reduce, 'Reduce', LEFT)
        self.quit_button = new_button(self.button_frame,self.quit, 'Quit', RIGHT)

    def clear(self):
        self.main_canvas.delete("all")

    def reduce(self):
        if self.repetitions > 1:
            self.repetitions //= 2
        self.put_info()

    def increase(self):
        if self.repetitions < 200:
            self.repetitions *= 2
        self.put_info()

    def put_info(self):
        ## Change the text field in the canvas
        self.info_canvas.itemconfigure(self.text_area,text="#circles = {:d}".format(self.repetitions))

    def draw(self):
        boundary_offset = 2
        max_radius = (self.canvas_dimension - 2*boundary_offset) // 2
        xc = self.canvas_dimension//2 + boundary_offset
        r = max_radius/self.repetitions
        inc = r
        for i in range(self.repetitions):
            self.main_canvas.create_oval((xc-r, xc-r, xc+r, xc+r))
            r += inc
            self.main_canvas.update() # Actually refresh the drawing on the canvas.
            # Pause execution.  This allows the eye to catch up
            self.main_canvas.after(self.wait_time)

    def quit(self):
        self.myParent.destroy()

if __name__ == "__main__":
    root = Tk()
    root.title("Drawing a circle") ##Give a title to the program
    myapp = MyApp(root)
    root.mainloop()

'''lec ex'''
from tkinter import *

class MyApp(object):
    def __init__(self, parent):
        print('Initialized!')
        self.parent = parent
        self.main_frame = Frame(parent)
        self.main_frame.pack()
        self.button1 = Button(self.main_frame, text="Launch", command=self.terminate_program)
        self.button1.configure(width=12, padx="4m", pady="4m")
        self.button1.pack()
        self.button2 = Button(self.main_frame, text="C", command=self.c)
        self.button2.configure(width=12, padx="4m", pady="4m")
        self.button2.pack()
        self.rocket = 2

    def d(self):
        self.rocket += 2

    def c(self):
        print("Launching ... counting", end='')
        for i in range(self.rocket):
            print('...{}'.format(self.rocket), end='')
            self.rocket -= 1
        print('...Liftoff!', flush=True)

    def terminate_program(self):
        self.c()
        print('Terminated')
        self.parent.destroy()

if __name__ == "__main__":
    root = Tk()
    print("Countdown ready")
    myapp = MyApp(root)
    myapp.d()  #4个
    root.mainloop()
    myapp.d()
    print(myapp.rocket)
    myapp.c()
    print("Done")