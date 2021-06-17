import xlrd, os
from zipfile import Path


PATH = os.path.abspath("data/sheet_money.xlsx")
WORKBOOK = xlrd.open_workbook(PATH)
RECORDS_WORKSHEET = WORKBOOK.sheet_by_index(0)
ACCOUNTS_WORKSHEET = WORKBOOK.sheet_by_index(1)

def account_records():
    for row in range(ACCOUNTS_WORKSHEET.nrows):
        for col in range(ACCOUNTS_WORKSHEET.ncols):
                print(ACCOUNTS_WORKSHEET.cell_value(row, col), end = '')
                print('\t', end = '')
        print()

account_records()

def register_records():
    for row in range(RECORDS_WORKSHEET.nrows):
        for col in range(RECORDS_WORKSHEET.ncols):
                print(RECORDS_WORKSHEET.cell_value(row, col), end = '')
                print('\t', end = '')
        print()

register_records()