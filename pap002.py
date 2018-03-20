# -*- codding:utf-8 -*-

'''
简述：企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时，高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%；
高于100万元时，超过100万元的部分按1%提成。
提问：从键盘输入当月利润I，求应发放奖金总数？ 
玩蛇网Python解题思路分析：请利用数轴来分界及定位。并要注意定义时需要把奖金定义成长整型的数据类型。
'''
i=float(input("请输入净利润："))

arr=[1000000,600000,400000,200000,100000,0]
rat=[0.01,0.015,0.03,0.05,0.075,0.1]
r=0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        print((i-arr[idx])*rat[idx])
        i=arr[idx]

print(r)        
print("============================================================================")

'''方法二
'''
j=float(input("请输入净利润："))
if j>0 and j<=100000:
    rr=j*0.1
elif j<=200000:
    rr=(j-100000)*0.075+100000*0.1
elif j<=400000:
    rr=(j-200000)*0.05+100000*0.1+100000*0.075
elif j<=600000:
    rr=(j-400000)*0.03+200000*0.05+100000*0.1+100000*0.075
elif j<=1000000:
    rr=(j-600000)*0.015+200000*0.03+200000*0.05+100000*0.1+100000*0.075
else:
    rr=(j-1000000)*0.01+400000*0.015+200000*0.03+200000*0.05+100000*0.1+100000*0.075  
print(rr)           