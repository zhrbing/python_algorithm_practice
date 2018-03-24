# -*- codding:utf-8 -*-

import string

'''
关于用Python方法辨别数据类型可以用python type()方法，
那么想要查看字符串中每一项的类型，并逐一输出要怎么来处理呢？
要求：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
Python解题思路分析： 利用while语句,条件为输入的字符不为'\n'
'''

s=input("请输入一个字符串:\n")
letters,space,digit,others=0,0,0,0
for c in s:
    if c.isalpha():
        letters+=1
    elif c.isspace():
        space+=1
    elif c.isdigit():
        digit+=1
    else:
        others+=1

print("英文字母："+str(letters),"空格："+str(space),
        "数字："+str(digit),"其他："+str(others))        