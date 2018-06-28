# -*- codding:utf-8 -*-


import requests
import json
import time
import csv
import os

data={
    "Ei":"XAU",
    "Period":1,
    "QryTm":0,
    "Sort":"lt",
    "Lmt":0
}

myurl='***' 
headers={'Content-Type':'application/json'}
filename="当日数据查询服务-当日K线查询-"+data['Ei']+".csv"

response=requests.post(url = myurl,json = data,headers = headers)
resp=response.json()

for ks in resp.keys():
    print(ks,end='\t')
print()    

code_list=resp['data']
print("======**数据总条数：【"+str(len(code_list))+"】**======",end='\n\n')
#===================================================================================================    
data_keys=[]
for data_key in code_list[0].keys():
    data_keys.append(data_key)    #表头存储为list
    print(data_key,end='\t')    
#===================================================================================================    
def write_to_csv():    #数据写入csv文件
    
    with open(filename,"w",newline='') as csvfile:  # 设置newline，否则两行之间会空一行
        writer=csv.writer(csvfile)
        writer.writerow(data_keys)   #写入表头
        
        for cl in code_list:
            write_data=[]         
            for data_key in data_keys:
                if data_key=='KlTm':    #判断并转换Unix时间戳
                    write_data.append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(cl['KlTm'])))
                else:
                    write_data.append(cl[data_key])
            
            writer.writerow(write_data)    #按行写入
#===================================================================================================    
def read_from_csv():
    with open(filename,"r") as csvfile:
        reader=csv.reader(csvfile)
        for line in reader:
            for ss in line:
                print(ss,end=',')
            print()
#===================================================================================================            
write_to_csv()    
print('\n当前路径：'+os.path.abspath('.'))
os.system(filename)
# read_from_csv()   
    
