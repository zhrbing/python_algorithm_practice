# -*- codding:utf-8 -*-

'''
斐波那契数列（Fibonacci sequence），又称黄金分割数列、因数学家列昂纳多·斐波那契以兔子繁殖为例子而引入，
故又称为“兔子数列”，指的是这样一个数列：1、1、2、3、5、8、13、21、34。
在数学上，斐波纳契数列以如下被以递归的方法定义：
f0=0(n=0)
f1=1(n=1)
fn=f[n-1]+f[n-2](n>=2)
'''

#要求一：输出第10个斐波那契数列
#方法一：
def fib(n):
    a,b=1,1
    for i in range(n-1):
        a,b=b,a+b
        print(a,end='\t')

#方法二：使用递归
def fib2(n):
    if n==1 or n==2:
        return 1
    else:
        return fib2(n-1)+fib2(n-2)

#要求二：需要输出指定个斐波那契数列
def fib3(n):
    if n==1:
        return [1]
    if n==2:
        return [1,1]
    fibs=[1,1]
    for i in range(2,n):
        fibs.append(fibs[-1]+fibs[-2])

    return fibs

print(fib3(10))