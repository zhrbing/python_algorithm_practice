# -*- codding:utf-8 -*-


import xlwt
import xlrd
import os
import time


code_list= [{"KlTm": 1522070100,"TrdDy": "20180327","OpPri": 3354,"PreClPri": 3363,"HiPri": 3378,"LoPri": 3353},
            {"KlTm": 1522071000,"TrdDy": "20180327","OpPri": 3373,"PreClPri": 3363,"HiPri": 3376,"LoPri": 3368},
            {"KlTm": 1522071900,"TrdDy": "20180327","OpPri": 3370,"PreClPri": 3363,"HiPri": 3376,"LoPri": 3364}]
filename="读写excel"+".xls"
#===================================================================================================    
data_keys=[]
for data_key in code_list[0].keys():
    data_keys.append(data_key)
print(data_keys)   
#===================================================================================================
def write_to_xls():
    book=xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet=book.add_sheet("sheet1",cell_overwrite_ok=True)

    for title in range(len(code_list[0])):  #第一行，写标题
            sheet.write(0,title,data_keys[title])

    for row in range(len(code_list)):
        for column in range(len(code_list[0])):
            if data_keys[column]=='KlTm':    #判断并转换Unix时间戳
                sheet.write(row+1,column,time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(code_list[row]['KlTm'])))
            else:        
                sheet.write(row+1,column,code_list[row][data_keys[column]])

    book.save(filename)
#===================================================================================================
def read_from_xls():
    book=xlrd.open_workbook(filename)
    sheet1=book.sheet_by_index(0)
    rows=sheet1.nrows
    cols=sheet1.ncols
    
    for r in range(rows):
        for c in range(cols):
            cell_value=sheet1.cell_value(r,c)
            print(cell_value,end='\t')
        print()
#===================================================================================================
# write_to_xls()
read_from_xls()
print(os.path.abspath('.'))
os.system(filename)

