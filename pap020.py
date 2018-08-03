import json
from openpyxl import Workbook


filename="/home/zhbing/Documents/feixun.txt"
savefile="/home/zhbing/Documents/feixun.xlsx"
with open(filename,encoding='utf-8') as file:
    contents=file.read()

ctsjson=json.loads(contents)    
kcodeList=ctsjson['object'][0]['kcodeExchangePlanList']

titlelist=[]
for dkey in kcodeList[0].keys():
    titlelist.append(dkey)
    
print(titlelist)

wb=Workbook()
sheet=wb.active
sheet.append(titlelist)

for kcode in kcodeList:
    rowdata=[]
    for v in kcode.values():
        rowdata.append(v)
    sheet.append(rowdata)

wb.save(savefile)
