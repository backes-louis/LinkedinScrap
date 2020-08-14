import xlrd
import sys


list_of_names = []

location = (r"C:\Users\Louis.backes\Desktop\selenium\file_names.xlsx")
name = []
wb = xlrd.open_workbook(location)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0)

for i in range(sheet.nrows):

    if sheet.row == xlrd.XL_CELL_EMPTY:
        sys.exit()  
    else:
        list_of_names.append(sheet.cell_value(i,0))


                   
                 
                 
                 