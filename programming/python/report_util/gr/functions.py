import openpyxl
import os

registry_file = openpyxl.load_workbook(filename='register.xlsx')
request_file = openpyxl.load_workbook(filename='request.xlsx')


def fiscal_and_reg(spec_name, **kwargs):
    data = registry_file['fiscal']
    data['H24'] = spec_name
    for new in kwargs.items():
        data[new[0]] = new[1]
    registry_file.save('register.xlsx')
    os.system('start excel.exe register.xlsx')
    print('Реестр сформирован')


def complex_settings(spec_name, *args, **kwargs):
    data = registry_file[args[0]]
    data[args[1]] = spec_name
    for new in kwargs.items():
        if new[0] == 'H5':
            continue
        data[new[0]] = new[1]
    registry_file.save('register.xlsx')
    os.system('start excel.exe register.xlsx')
    print('Реестр сформирован')


def request_for_work(**kwargs):
    data = request_file['form']
    for new in kwargs.items():
        data[new[0]] = new[1]
    request_file.save('request.xlsx')
    os.system('start excel.exe request.xlsx')
    print('Заявка сформирована')