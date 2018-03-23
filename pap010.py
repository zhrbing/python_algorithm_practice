# -*- codding:utf-8 -*-
import calendar
import time

print("时间戳：",time.time())

print("\n时间元组：",time.localtime())  #返回一个时间元组
slist=[]
for s in time.localtime():
    slist.append(s)

print(slist)  
print("一年中的第几天：",time.localtime()[7])  

print("\n格式化可读时间：",time.asctime(time.localtime()))

print("\n格式化成yyyy-mm-dd hh:mm:ss形式：",time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),end='\n\n')


print(calendar.month(2018,3))

  
