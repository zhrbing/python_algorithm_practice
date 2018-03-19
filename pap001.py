# -*- codding:utf-8 -*-

'''
简述：这里有四个数字，分别是：1、2、3、4 
提问：能组成多少个互不相同且无重复数字的三位数？各是多少？ 
Python解题思路分析：可填在百位、十位、个位的数字都是1、2、3、4。
组成所有的排列后再去掉不满足条件的排列。
'''
count=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j) and (j!=k) and (k!=i):
                count+=1
                print('{:0>2}'.format(count)+'\t'+str(i*100+j*10+k))