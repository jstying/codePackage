
x = "red! Let's go red! Go red! Go red!"


print(x.strip("red!"))  # 去除左右两边的 "red!" 这个字符组合
# 输出: " Let's go red! Go red! Go "

print(x.strip("edr!"))  # 去除左右两边的 "edr!" 字符组合, red! 就是一种组合
# 输出: " Let's go red! Go red! Go "


print(x.lstrip("red!"))  # lstrip去除左边的 "red!" 字符组合
# 输出: " Let's go red! Go red! Go red!"


print(x.rstrip("red!"))  # rstrip去除右边的 "red!" 字符组合
# 输出: "red! Let's go red! Go red! Go "


print("    Go red!      ".strip())  # 默认，去除前后的空格
# 输出: 'Go red!'


print(" \n   Go red!    \t  ".strip())  #默认，去除前后的空白字符，包括\n和\t
# 输出: 'Go red!'

# strip() with only space as argument
print(" \n   Go red!    \t  ".strip(' '))  #strip(' ') 只去除空格，不去除\n,\t
# 输出: '\n   Go red!    \t'


x = "Let's go red! Let's go red! Go red! Go red!"


print(x.split()) #以空白字符作为切割
# 输出: ["Let's", 'go', 'red!', "Let's", 'go', 'red!', 'Go', 'red!', 'Go', 'red!']

print(x.split("!")) #以！作为切割， 
# 输出: ["Let's go red", " Let's go red", ' Go red', ' Go red', '']

x = "! 2 !"
print(x.split("!"))
#['', ' 2 ', ''] 切割线在str最前或最后，会产生空''

print(x.split("red!")) #以red!作为切割
# 输出: ["Let's go ", " Let's go ", ' Go ', ' Go ', '']

print("Let's go red! \n Let's go    red! Go red! \t Go red!".split(" ")) #以单个空格作为切割，\t \n不被切
# 输出: ["Let's", 'go', 'red!', '\n', "Let's", 'go', '', '', '', 'red!', 'Go', 'red!', '\t', 'Go', 'red!']
print("Let's go red! \n Let's go    red! Go red! \t Go red!".split()) #以单个空格作为切割，\t \n不被切
#["Let's", 'go', 'red!', "Let's", 'go', 'red!', 'Go', 'red!', 'Go', 'red!']

x = " Let's go red! \n Let's go    red! Go red! \t Go red!   "
print(x.split(" "))  # 以单个空格作为分隔符
#['', "Let's", 'go', 'red!', '\n', "Let's", 'go', '', '', '', 'red!', 'Go', 'red!', '\t', 'Go', 'red!', '', '', '']



print("Let's go red! \n Let's go    red! Go red! \t Go red!".split()) #以空白字符作为切割，\t \n被切
# 输出: ["Let's", 'go', 'red!', "Let's", 'go', 'red!', 'Go', 'red!', 'Go', 'red!']



x = "Let's go red! Let's go red! Go red! Go red!"

print(x.find('red'))      # 输出: 9  ,index of r
print(x.find('Red'))      # 输出: -1 , not found
print(x.find("edr!"))     # 输出: -1 , not found
print(x.find('red', 10))  # 输出: 23 , the first red found after index 10
print(x.find('red', 10, 12)) # 输出: -1 , not found
print('red' in x)         # 输出: True , found 'red'  - Boolean
print('Red' in x)         # 输出: False , not found  - Boolean



#open file 在后台
f = open('abc.txt')
f = open('abc.txt','r') #r-reading from the file, same as default, 读取模式

line = f.readline() #read the first line of the file, line is str, f始终指向第一行
print(line) 
 
s = f.read() #read the remainder contents of the file, s is str，f指到最后一行
print(s)
'''
kinchanna

kombawa
naiyougisuo
yichana

'''
#可以去掉空行，由于print到txt里的换行符了
print(line.strip())
print(s)
'''
kinchanna
kombawa
naiyougisuo
yichana
'''

'''
When you are at the end of a file, f.read() and f.readline()
will both return the empty string: ""    
#e.g. line='' s='' 到最后一行时
'''

#一行行打出来,file name有引号
f = open('abc.txt')
line1 = f.readline() 
line2 = f.readline()
print(line1.strip()) #kinchanna
print(line2.strip()) #kombawa

print()

''' Read contents of a file'''
f = open('abc.txt')
for line in f:
    print(line.strip())
    
'''
kinchanna
kombawa
naiyougisuo
yichana
'''
#把f替代进去，简化一点
for line in open('abc.txt'):
    print(line)
    
    
''' open and close'''
f = open('abc.txt')

#...

f.close() #关掉 
f = open('abc.txt') #再打开，f重新指向第一行

'''Example: Computing the Average Score'''

file_name = input("Enter the name of the scores file: ") #scores.txt
file_name = file_name.strip()    # Elminate extra white space that the user may have typed
print(file_name)



num_scores = 0
sum_scores = 0

#s 是每行的数值，但是是string
for s in open(file_name):
    #转化成int
    sum_scores += int(s)
    #计有几个
    num_scores += 1

print("Average score is {:.1f}".format( sum_scores / num_scores ))

open(file_name).close() #手动关闭

'''Writing to a File'''

#以 write mode写入模式，创建一个新文档
#或者打开已有，擦除文档之前的所有内容
f_out = open("outfile.txt","w")

#不会自动换行，所以文档里面是Fine fine fineDreamlike
#f_out.write("Fine fine fine")
#f_out.write("Dreamlike")


#手动加上\n
f_out.write("Fine fine fine \n")
f_out.write("Dreamlike {} {}".format('yes', 'baby'))
#Fine fine fine 
#Dreamlike

#要close才能有变化
f_out.close()


'''Appending to a file'''
#如无，帮我创建; 如有，原内容保留，新的不断在末尾加上
f_out2 = open("outfile2.txt","a")
#write()里面是str,末尾有个\n
f_out2.write("This line is appended to the file.\n")
f_out2.write("keep adding\n")
f_out2.close()

'''Parsing - reading a data file/web page 解析数据'''


'''Opening Static Web Pages'''
import urllib.request  #处理URL的模组
word_url = 'http://www.greenteapress.com/thinkpython/code/words.txt'
word_file = urllib.request.urlopen(word_url) #后台打开URL，word_file是里面获取的数据
line = word_file.readline()  # 读取文件第一行
print(line.decode('utf-8').strip())  # 解码并去掉换行符后打印
#aa

'''Data formats'''
'''
HTML -Hypertext Markup Language 

<html>
   <head>
      <title>HTML example for CSCI-100</title>
   </head>
   <body>
      This is a page about <a href="http://python.org">Python</a>.
      It contains links and other information.
   </body>
</html>


<html><head><title>HTML   example for CSCI-100</title>
</head> <body> This is a page about <a
href="http://python.org">Python</a>.  It contains   links
and other   information. </body> </html>
____________________________________________________________________________________
JSON -JavaScript Object Notation
{
   "class_name": "CSCI 1100"
   , "lab_sections" : [
          { "name": "Section 01"
             , "scheduled": "T 10AM-12PM"
             , "location": "Sage 2704"
          }
          , { "name": "Section 02"
             , "scheduled": "T 12PM-2PM"
             , "location": "Sage 2112"
          } ]

 }

'''
import json  

x = ' [ "a", [ "b", 3 ] ] '  # 定义一个 JSON 格式的字符串
result = json.loads(x)  # 把字符串解析为 Python 对象
print(result)  
#['a', ['b', 3]] 变成python里的list

'''Parsing ad-hoc data formats - Regular tabular data'''

'''
CSV comma separated values



chicken noodle, 2
clam chowder, 3
tomato soup, 2
'''

'''Practice Problem: write a simple parser for the soup list that returns a list of the form:
["chicken noodle", "chicken noodle", "clam chowder", "clam chowder", "clam chowder"]
'''

file_name = 'soup.txt' 

# 初始化一个空列表来存储结果
soup_list = []
soup_list2 = []

file = open(file_name, 'r')  


for line in file:
    #去掉两边空格，以逗号分隔开
    parts = line.strip().split(',') # ["chicken noodle" , "2"]
    soup_name = parts[0].strip()  
    count = int(parts[1].strip())  
    
   #concatenate
    soup_list+=[soup_name] * count
    #[str]*2   [str,str]
    
    #append方法
    for i in range(count):
        soup_list2.append(soup_name)
    
    
    
# 手动关闭文件
file.close()

# 打印结果
print(soup_list)
print(soup_list2)

    
'''
Lecture 13 Practice Problem: Parse the yelp.txt data file to create a
list of lists of names and averages. This demonstrates parsing an
irregularly formatted file.  We have to know that the 0th entry on
each line and the 6th are the scores.

Prof. Stewart

Meka’s Lounge|42.74|-73.69|407 River Street+Troy, NY 12180|http://www.yelp.com/biz/mekas-lounge-troy|Bars|5|2|4|4|3|4|5

Information after column 5 are all reviews
'''

def yelp_averages( yelp_name ):
    averages = [] #intialize list large
    for line in open(yelp_name):
        line = line.split('|') #以竖线分隔，每个放进list
        name = line[0]
        scores = line[6:]    # after column 5=From entry 6 on are the scores ... till the end ; scores -list

        if len(scores) == 0:
            # Handle the special case of an empty scores list
            averages.append( [ name, -1 ] ) #append small list into large list
        else:
            # Compute the average when there is at least one score
            sum_score = 0
            for s in scores:
                sum_score += int(s)
            avg = sum_score / len(scores)
            avg=round(avg,2)
            averages.append([name,avg]) 
    return averages

avgs = yelp_averages('yelp.txt')
print( avgs[0:3] ) #只打出来index 0，1，2的前三小list组成的list
#[["Meka's Lounge", 3.86], ['Tosca Grille', 2.5], ['Happy Lunch', 3.5]]
print( avgs[0:8] ) 
#[["Meka's Lounge", 3.86], ['Tosca Grille', 2.5], ['Happy Lunch', 3.5], 
#['Hoosick Street Discount Beverage Center', 4.67], ["Uncle Ricky's Bagel Heaven", 4.14],
# ['Confectionery House', 4.5], ['Uncle John Diner', 4.67], ['China Wok', 1.5]]


#tips： len不能测int的长度，转成str先！

'''Lec13_ex'''

'''
census_data.txt
l1:Location    2000    2011
l2:New York State  18,976,811  19,378,102
l3:New York City   8,008,686   8,175,133
l4:




'''
f = open("census_data.txt")
line1 = f.readline() #Location 2000 2011\n
line1 = line1.strip()  #Location 2000 2011
line2 = f.read()  
#New York State  18,976,811  19,378,102\n
#New York City   8,008,686   8,175,133\n
line3 = f.readline() #啥也没有


print(line1) #Location 2000 2011
print(line2)
#New York State  18,976,811  19,378,102
#New York City   8,008,686   8,175,133
# 这个空行是由NYC的\n与print的\n组成
print(line3) #光标从这里开始，空的
#
f.close()

f = open("census_data.txt")
s = f.read()#读全部
line_list = s.split('\n') #3个\n分开 4个块
print(len(line_list)) #4个
line_list = s.strip().split('\n') #前后空格全清，把最后个\n弄掉了, 只剩2个\n
#['Location    2000    2011', 'New York State  18,976,811  19,378,102', 'New York City   8,008,686   8,175,133']
print(len(line_list))#3个



'''Given a file containing test scores, one per line, we want to have a new file that contains
 the scores in increasing order. To do this, write a Python program that asks the user 
 for two file name strings, one for the input scores and the second for the output, sorted scores. 
 The program should open the first file (to read), read the scores, sort them, open the second file 
 (to write), and output to this file the scores in increasing order. There should be one score 
 per line, with the index on each line.
75
98
75
100
21
66
83
15

0:  15
1:  21
2:  66
3:  75
4:  75
5:  83
6:  98
7: 100

'''
 
 
 
#scores.txt 
f_name=input("Enter the scores file: ").strip()
print(f_name)
#scores_sorted.txt
f_name2=input("Enter the output file: ").strip()
print(f_name2)

#open the scores file
f1=open(f_name,'r')

#intialize list
ls=[]

for line in f1:
    ls.append(int(line.strip())) #store the int into the list

f1.close()
#sorted list [15, 21, 66, 75, 75, 83, 98, 100]
sort_list=sorted(ls)

#open write mode output file
f2= open(f_name2,'w')
for i in range(len(sort_list)):
    #write() 里面必须是str，不是int; int没有len()
    f2.write("{}{}:{}{}\n".format(' '*(2-len(str(i))),i, " "*(4-len(str(sort_list[i]))),str(sort_list[i])))
f2.close()