# -*- codding:utf-8 -*-

'''
简述：任意三个整数类型，x、y、z 
提问：要求把这三个数，按照由小到大的顺序输出
Python解题思路分析：可考虑用list
'''

output_list=[]
input_list=input("请输入若干个整数，用空格隔开：").split(' ')
for data in input_list:
    output_list.append(int(data))
output_list.sort()
for data in output_list:
    print(data,end='\t')