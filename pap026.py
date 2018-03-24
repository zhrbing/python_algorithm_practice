# -*- codding:utf-8 -*-

#求1+2!+3!+...+10!的和
#方法一：
def fact(i):
    sum=0
    if i==0:
        sum=1
    else:
        sum=i*fact(i-1)
    return sum

print([fact(i) for i in range(10)])  
s=0  
for j in range(1,11):
    s+=fact(j)

print(s)    

#方法二：
n,s2,t=0,0,1
for n in range(1,11):
    t*=n
    s2+=t
print(s2)    