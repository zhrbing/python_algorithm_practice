# -*- codding:utf-8 -*-

'''
"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
'''

import math

for num in range(100,1000):
    i=math.floor(num/100)  #math.floor(x)返回小于等于x的最大整数值
    j=(math.floor(num/10))%10
    k=num%10
    if num==i**3+j**3+k**3:
        print(num,end='\t')
          
       
      