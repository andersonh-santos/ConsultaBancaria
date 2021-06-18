import xlrd
import os

PATH = os.path.abspath("data/sheet_money.xlsx")
WORKBOOK = xlrd.open_workbook(PATH)
RECORDS_WORKSHEET = WORKBOOK.sheet_by_index(0)
ACCOUNTS_WORKSHEET = WORKBOOK.sheet_by_index(1)


def accounts_client_acronym():
    account_names = list()
    clients = list()
    acronyms = list()
    for row in range(1, ACCOUNTS_WORKSHEET.nrows):
        evaluated_row = ACCOUNTS_WORKSHEET.row(row)
        account_name = evaluated_row[0].value
        client = evaluated_row[1].value
        acronym = evaluated_row[2].value

        account_names.append(account_name)
        clients.append(client)
        acronyms.append(acronym)


    # print(f'Nomes: {account_names}')
    # print(f'Clientes: {clients}')
    # print(f'Siglas: {acronyms}')


    client_object_list = list()

    for i in range(len(account_names)):
        client_object_list.append(
            {
                'account_name': account_names[i],
                'client': clients[i],
                'acronym': acronyms[i],
            }
        )

    print(client_object_list)

accounts_client_acronym()