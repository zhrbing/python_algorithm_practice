# -*- codding:utf-8 -*-

mylist=['Michael','Sarah','Tracy','Bob','Jack']
print(mylist[0:3])  #取前3个元素,如果第一个索引是0，还可以省略，mylist[:3]
print(mylist[-1])   #取最后一个元素
print(mylist[-2:])  #取最后两个元素

numlist=list(range(1,101))
print(numlist)
print(min(numlist),max(numlist),sum(numlist))
print(numlist[:10]) #取前10个数
print(numlist[-10:])    #后10个数
print(numlist[10:20])   #前11-20个数
print(numlist[:10:2])   #前10个数，每2个取1个
print(numlist[::5])     #所有数，每5个取1个
print(numlist[:])       #复制一个list
print((0,1,2,3,4,5)[:3])    #tuple切片，取前3个
print('abcdefghijkl'[::2])  #字符串切片

del numlist[-1]     #通过索引移除元素
numlist.remove(1)   #通过值移除元素


#====================================================================================================
alphalist=['x','a','r','z']

alphalist.sort()      #永久排序，按字母表顺序
print(alphalist)

alphalist.sort(reverse=True)    #永久排序，按字母表反向顺序
print(alphalist)

print(sorted(alphalist))        #临时排序，返回一个原list的排序拷贝，原list顺序不变
print(sorted(alphalist,reverse=True))   #临时排序，返回一个原list的字母表反向排序拷贝，原list顺序不变

alphalist.reverse()     #将原list倒序
print(alphalist)