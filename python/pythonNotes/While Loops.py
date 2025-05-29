

'''
While loop
'''

print(1)
print(2)
print(3)


#intialize
i=0
#condition while后面加:
while i<=10: #0-10
    #block
    print(i)
    #increment by 1 递增1， decrement是递减 i-=1 就会永不停止
    i+=1
#结束while，结束缩进identation
print("abc")

# 条件如果是false，不会执行 while下面的



i=10

while i>0: #10-1
  
    print(i)
    i-=1

print("abc")



#tuple在list里面

co2_levels = [ (2001, 320.03), (2003, 322.16), (2004, 328.07),\
               (2006, 323.91), (2008, 341.47), (2009, 348.92),\
               (2010, 357.29), (2011, 363.77), (2012, 361.51),\
               (2013, 382.47) ]
#\续行,\后面不能加注释或任何东西

print(co2_levels[0][0], 'had co2 emission: ', co2_levels[0][1])
#2001 had co2 emission:  320.03


#initialize
i=0
#list的长度 一般用i<len 不用i<=len
while i< len(co2_levels): #while i<10  0-9 10次正好
#i 0 每个tuple的year, i 1每个tuple的co2
#console中间的方块停止不停执行的代码

    print( "Year", co2_levels[i][0], \
           "CO2 levels:", co2_levels[i][1])
    #不要忘记increment
    i += 1
    
print()
#怎么反向打这个？
total=0
i=len(co2_levels)-1 #不能out of index range， index 只有0-9， len=10
while i>=0:#print内容不变，i>=0看看要不要等号，这里要打出来index 0的
    print( "Year", co2_levels[i][0], \
           "CO2 levels:", co2_levels[i][1])
    total += co2_levels[i][1]
    i -= 1
print(total)

#怎么算total
co2_levels = [ (2001, 320.03), (2003, 322.16), (2004, 328.07),\
               (2006, 323.91), (2008, 341.47), (2009, 348.92),\
               (2010, 357.29), (2011, 363.77), (2012, 361.51),\
               (2013, 382.47) ]

i=0
total=0
count=0
while i< len(co2_levels): 
    if co2_levels[i][1]>350:
        count+=1
    total += co2_levels[i][1]
    i += 1
    

print("Total co2_levels is", total)
print("The c02 over 350 has: ", count, "times")


    
a=sum((10,9,8,7,6,5,4,3,2,1))
print(a) #55


a=sum((10,9,8,7,6,5,4,3,2,1),2) #加上后面的2
print(a) #57



i=1
total = 0
while i<11:
    total += i
    i += 1
print(total)
#55


co2_levels = [ (2001, 320.03), (2003, 322.16), (2004, 328.07),\
               (2006, 323.91), (2008, 341.47), (2009, 348.92),\
               (2010, 357.29), (2011, 363.77), (2012, 361.51),\
               (2013, 382.47) ]

i=1 #从1开始，不然out of bound, 也不需要2001年的递增量
while i<len(co2_levels):
    print("Percent change in ",co2_levels[i][0],"is" , (co2_levels[i][1]-co2_levels[i-1][1])/co2_levels[i-1][1]*100,"%")
    i+=1



#我只想打出奇数月份
months=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

i=0 
while i<len(months):
    print(months[i])
    i+=2

'''
    *   #4个空格
   ***   #3 空
  *****
 *******
*********
   ***
   ***
   递增2
'''
i=1 
while i<10:
    #因为i递增2，所以整除2来减1空，2空。。。
    print((4-i//2)*" "+i*"*")
    i+=2 
#树根
print(3*" "+3*"*")
print(3*" "+3*"*")






total = 0
end_found = False  #boolean initialize, flag

while not end_found: #while true,不停加，直到0输入，然后false
    x = int( input("Enter an integer to add (0 to end) ==> "))
    if x == 0:
        end_found = True#找到底了 ， while not True 就不执行了，退出这个循环
    else:
        total += x

print(total)



#nested
'''
i负责2，j负责21，12... （2 21, 2 12...)
i负责21，j负责12，8，5...

需要统计所有的两两配对

j受i影响
'''

L = [2, 21, 12, 8, 5, 31]
i = 0
while i < len(L):
    j = i+1 #j永远在i后面开始
    while j < len(L):
        print(L[i], L[j])
        j += 1#找下一个
    #这个j一行负责完就increment i
    i += 1
'''
2 21
2 12
2 8
2 5
2 31
21 12
21 8
21 5
21 31
12 8
12 5
12 31
8 5
8 31
5 31
'''



def bunny (bpop):
    bpop_next = (10*bpop)/(1+0.1*bpop) - 0.05*bpop*fpop
    bpop_next=max(0,bpop_next)
    return int(bpop_next)


def fox (fpop):
    fpop_next = 0.4 * fpop + 0.02 * fpop * bpop
    fpop_next=max(0,fpop_next)
    return int(fpop_next)

bpop=input("Number of bunnies ==> ")
print(bpop)
bpop=int(bpop)
bpop=max(0,bpop)

fpop=input("Number of foxes ==> ")
print(fpop)
fpop=int(fpop)
fpop=max(0,fpop)



print("Year 1: {} {}".format(bpop,fpop))

i=2
while i<6:
    #loop中反复调用函数
    bpop_next=bunny(bpop)
    fpop_next=fox(fpop)
    #更新arguments
    bpop=bpop_next
    fpop=fpop_next
    #loop increment
    i+=1
    print("Year {}: {} {}".format(i,bpop_next,fpop_next))




