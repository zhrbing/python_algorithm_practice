# -*- codding:utf-8 -*-

nums=[]
for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        nums.append(i)

print(nums)            
'''
for else语句可以总结成以下话:
如果我依次做完了所有的事情(for正常结束)，我就去做其他事(执行else)，
若做到一半就停下来不做了（中途遇到break），我就不去做其他事了(不执行else)。

***只有循环完所有次数(for循环正常退出)，才会执行 else 。
***break 可以阻止 else 语句块的执行(中途从break跳出，则连else一起跳出)。
'''