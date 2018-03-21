# -*- codding:utf-8 -*-


input_data=input("请输入年月日，以-隔开：")
date_data=input_data.split('-')
year=int(date_data[0])
month=int(date_data[1])
day=int(date_data[2])

months=(0,31,59,90,120,151,181,212,243,273,304,334)
if 0<month<=12:
    sum=months[month-1]
else:
    print('请输入正确月份！')    
    
sum+=day

leap=0
if (year%400==0) or ((year%4==0) and (year%100!=0)):
    leap=1
if(leap==1) and (month>2):
    sum+=1

print(input_data+"是"+date_data[0]+"年的第【"+str(sum)+"】天。")            