# -*- codding:utf-8 -*-

'''
乘法口诀表
'''

for i in range(1,10):
    for j in range(1,i+1):
            print("%d*%d=%d" % (j,i,i*j),end='\t')
    print()

#方法二：
print( '\n'.join(['\t'.join(['%s*%s=%-2s' % (j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)]))