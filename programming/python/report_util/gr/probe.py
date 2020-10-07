import openpyxl
import os.path
from win32com.client import Dispatch

file_1 = f'{os.path.abspath("")}\\data\\register.xlsx'
file_2 = f'{os.path.abspath("")}\\data\\file.xlsx'

exel = Dispatch('Excel.Application')

open_f1 = exel.Workbooks.Open(Filename=file_1)
open_f2 = exel.Workbooks.Open(Filename=file_2)

chuse_sheet = open_f1.Worksheets(4)
chuse_sheet.Copy(Before=open_f2.Worksheets(1))

open_f2.Close(SaveChanges=True)
exel.Quit()

print('Успех')






#
# work_file = openpyxl.load_workbook(filename='data/register.xlsx')
# work_sheet = work_file['complex']
#
# new_file = openpyxl.load_workbook(filename='data/for_new.xlsx', read_only=False)
# new_sheet = new_file['complex']
#
# for row in work_sheet:
#     for cell in row:
#         new_sheet[cell.coordinate].value = cell.value
#
# new_file.save('data/for_new.xlsx')
# print('Успех')

