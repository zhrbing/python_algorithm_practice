# -*- codding:utf-8 -*-

import datetime
import time

a=datetime.date.today()
print(a,a.year,a.month,a.day)

#两个日期相差天数，x.__sub__(y)==>x-y,x.__rsub__(y)==>y-x
#a.__sub__(b),返回值类型为datetime.timedelta
a=datetime.date(2018,3,1)
b=datetime.date(2018,3,30)
print(a.__sub__(b))
#a.__sub__(b).days,返回值为整数类型
print(a.__sub__(b).days)

#isocalendar(...)*:返回一个包含三个值的元组，依次为：
# year年份，week number周数，weekday星期数（周一为1…周日为7)
c=datetime.date(2018,3,24)
d=c.isocalendar()
print(d)
for e in d:
    print(e,end='\t')

#isoformat(...): 返回符合ISO 8601标准 (YYYY-MM-DD) 的日期字符串
print(datetime.date(2018,3,24).isoformat())    #==>2018-03-24

#isoweekday(...): 返回符合ISO标准的指定日期所在的星期数（周一为1…周日为7) 
print(datetime.date(2018,3,24).isoweekday())    #==>6

#与isoweekday(...)相似的还有一个weekday(...)方法，
#只不过是weekday(...)方法返回的周一为 0, 周日为 6 
print(datetime.date(2018,3,24).weekday())   #==>5

#fromtimestamp(...)：根据给定的时间戮，返回一个date对象
print(datetime.date.fromtimestamp(time.time()))     #==>2018-03-24

#today(...)：返回当前日期
print(datetime.date.today())        #2018-03-24
print(datetime.date.today().__str__())  #获得日期的字符串

a=datetime.datetime.now()
print(a,'\n',a.date(),'\n',a.time())

mytoday=datetime.date.today()
mlastday=datetime.date(mytoday.year,mytoday.month,1)-datetime.timedelta(1)
print(mlastday)     #获取上个月最后一天的日期
mfirstday=datetime.date(mlastday.year,mlastday.month,1)
print(mfirstday)    #获取上个月第一天的日期