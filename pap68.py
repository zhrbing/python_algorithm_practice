# -*- codding:utf-8 -*-

import random
import string

#方法一
def generate_code(count=6):
    forSelect=string.ascii_letters+string.digits
    ra=""
    for x in range(count):
        ra+=random.choice(forSelect)
    print(ra) 


#方法二
def generate_code2(len=6):
    code_list=[]
    for i in range(10):  #0-9
        code_list.append(str(i))
    for i in range(65,91):  #A-Z
        code_list.append(chr(i))
    for i in range(97,123):  #a-z
        code_list.append(chr(i))
    myslice=random.sample(code_list,len)
    code=''.join(myslice)  #list转成string
    print(code)

generate_code()
generate_code2()    