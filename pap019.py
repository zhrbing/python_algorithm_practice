# -*- codding:utf-8 -*-

filename="E:\Documents\Backup.postman_dump.json"

def read_atonce():
     with open(filename,encoding='utf-8') as file:
        contents=file.read()

     print(contents)


def read_linebyline():
    with open(filename,encoding='utf-8') as file:
        for line in file:
            print(line.rstrip())


def sotre_inalist():
    with open(filename,encoding='utf-8') as file:
        lines=file.readlines()

    for line in lines:
        print(line.rstrip())


# read_atonce()      #一次性读取
# read_linebyline()   #按行读取
# sotre_inalist()     #存储为一个list，再从list中读取
#==================================================================================
write_to_file="E:\write_to_file.txt"

def write_toemptyfile():
    with open(write_to_file,'w',encoding='utf-8') as file:
        file.write('I love programming!\n')
        file.write('I love creating new games.\n')


def append_tofile():
    with open(write_to_file,'a',encoding='utf-8') as file:
        file.write('\nI also love wroking with data.\n')
        file.write('I love making apps as well.\n')


# write_toemptyfile()     #写入空文件        
append_tofile()         #在文件后追加