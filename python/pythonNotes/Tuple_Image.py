tuple #元组 秃剖
x = (4, 5, 10)   # note the parentheses ()
print(x[0]) 
#4
print(x[2])
#10
len(x) #里面有3项
#3

# 定义一个元组, ()
my_tuple = (1, "apple", 3.5)

# 访问元组的元素
print(my_tuple[1])  # 输出 "apple"

# 尝试修改元组会报错
#my_tuple[1] = "banana"  # 会引发错误，因为元组不可变


#string不是元组，但也能根据索引打出来
s = 'abc'
print(s[0])
#'a' 
print(s[1])
#'b'
#print(s[3])  #报错，string out of index

'''
immutable 不变的
string内部和tuple内部不可更改

>>> x[1] = 2
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

>>> s[1] = 'A'
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
'''

x=(2,3)
a=x
print(a)
#(2,3)
y=(4,5)
print(x+y)
#连结tuple (2,3,4,5)


def split(n):
    ''' Split a two-digit number into its tens and ones digit '''
    tens = int(n / 10 )  # n//10
    ones = n % 10
    return (tens, ones) #return (8,3)    return tuple

x = 83
ten,one = split(x)
print( x, "has tens digit", ten, "and ones digit", one )
#83 has tens digit 8 and ones digit 3


def combine( digits ):
    return digits[0]*100 + digits[1]*10 + digits[2]

d = (5, 2, 7)
print( combine(d)) #527 反向操作 tuples进去，返回原数字


import math

def circle(radius):
    ''' Compute and return the area of a circle '''
    return math.pi * radius**2

def cylinder(radius,height):
    ''' Compute and return the surface area of a cylinder '''
    circle_area = circle(radius)
    height_area = 2 * radius * math.pi * height
    return 2*circle_area + height_area

def sphere(radius):
    '''  Compute and return the surface area of a sphere '''
    return 4 * math.pi * radius**2

if __name__ =="__main__":
    #我的test code, 别人import后就没有下面的东西，见lec7_area.py 有main这行字的人，每次运行都会跑下面protected内容
    r=float(input("Enter radius (float) => "))
    h=float(input("Enter height (float) => "))
    print("Surface area cylinder is: {:.2f}".format(cylinder(r,h)))
    print("Surface area sphere is: {:.2f}".format(h*sphere(r)))
    
    
    
'''
? not sure
(width,height)
(0,0) ------ (w-1,0)
(0,h-1)------(w-1,h-1)

比如（100，200）as width and height   (0,0) （99，0） （0，199） (99,199)
'''
'''
Black

(0,0,0)

Red

(255,0,0)

Green

(0,255,0)

Blue

(0,0,255)

White

(255,255,255)

Light Gray

(122,122,122)
'''
#PIL/PILLOW — Python Image Library
#import PIL

from PIL import Image
#要在同一个文件夹里才能打开

#文件名
filename = "chipmunk.jpg"
im = Image.open(filename) #assign图片
im.show()#打开图片
print('\n' '********************')
print("Here's the information about", filename)
#im.size告诉大小（560，417），mode=RGB,format=JPG
print(im.format, im.size, im.mode)

#convert('L')
gray_im = im.convert('L') #变成灰度照片gray scale
#resize(300,230) convert into size of 像素单位
scaled = gray_im.resize( (128,128) ) #resize里要括号里加括号的
print("After converting to gray scale and resizing,")
print("the image information has changed to")
print(scaled.format, scaled.size, scaled.mode)
#RGB mode->L mode 灰度模式, format不再保留原来的格式jpg了, None

scaled.show()#打开图片
#im.save(filename)保存图片，filename eg ('image1.jpg')
scaled.save(filename + "_scaled.jpg") #更改文件名后面跟上新的名称和格式

im2 = Image.open('swarm.jpg')
print(im2.size, im2.format, im2.mode)
#(600,800), 'JPEG', 'RGB' 只有size是tuple，其他是string
im2.show()
im4=im2.crop((100,100,300,400)) #截取图片，左上角坐标，右下角坐标,200x300
im4.show()
#create an empty new image， 默认黑色
im3=Image.new('RGB',(200,200))
im3.show()
# 创建自定义颜色图像 (蓝色)
im_blue = Image.new('RGB', (200, 200), color=(0, 0, 255))
im_blue.show()
# 创建自定义颜色图像 (蓝色)
im_blue = Image.new('RGB', (200, 200), color=(0, 0, 255))
im_blue.show()


im1 = Image.open('sheep.jpg')
print(im1.size)
#(600, 396) (width, height)
im1.show()

im5 = Image.new('RGB', (600, 396*2)) #创建新的黑色同宽，双倍高的图
im5.paste( im1, (0,0))   #把sheep粘到从左上角（0，0）起的图片（上部分）
im5.show()
#bg.paste(pastedimg,(location))
im5.paste( im1, (0, 396))#把sheep粘到下半部分（0，396）起的图片
im5.show()#黑色图片上贴满了2张sheep一上一下

'''
This example crops three boxes from an image, 
creates a new image and pastes the boxes 
at different locations of this new image.
'''
from PIL import Image

im = Image.open("lego_movie.jpg")
im.show()
#a,b=(100,200) 可以这样写 to assign a and b value
w,h = im.size#获取width height im.size 
print(w,h)

## Crop out three columns from the image
## Note: the crop function returns a new image
part1 = im.crop((0,0,w//3,h)) #左上角右下角裁剪
part1.show()
part2 = im.crop((w//3,0,2*w//3,h))#整除确保坐标不出错
part2.show()
part3 = im.crop((2*w//3,0,w,h))
part3.show()

## Create a new image same size as original one
newim = Image.new("RGB",(w,h))

## Paste the image in different order
## Note: the paste function changes the image it is applied to
newim.paste(part3, (0,0)) #粘在左上角
newim.paste(part2, (w//3,0))#粘在左中上角
newim.paste(part1, (2*w//3,0))#粘在右边一点的左上角
newim.show()


