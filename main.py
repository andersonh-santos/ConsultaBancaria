import xlrd, os, datetime

PATH = os.path.abspath("data/sheet_money.xlsx")
WORKBOOK = xlrd.open_workbook(PATH)
RECORDS_WORKSHEET = WORKBOOK.sheet_by_index(0)
ACCOUNTS_WORKSHEET = WORKBOOK.sheet_by_index(1)

def accounts_list():
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

    client_object_list = list()

    for i in range(len(account_names)):
        client_object_list.append(
            {
                'account_name': account_names[i],
                'client': clients[i],
                'acronym': acronyms[i],
            }
        )

    return client_object_list

accounts_list()

def records_list():
    dates = list()
    values = list()
    descriptions = list()
    account_names = list()
    for row in range(1, RECORDS_WORKSHEET.nrows):
        evaluated_row = RECORDS_WORKSHEET.row(row)
        for col in range(RECORDS_WORKSHEET.ncols):
            if col == 0 and row != 0:
                date = evaluated_row[0].value
                converted_date = xlrd.xldate_as_tuple(date, WORKBOOK.datemode)
                to_print_date = datetime.datetime(*converted_date).strftime("%d/%m/%y")
                
        value = evaluated_row[1].value
        if value == "":
            arq = open("error_log.txt","w")
            arq.write(f"Célula sem valor na linha {row +1}, coluna {col -1}, portanto a linha será ignorada.\n")
            continue
        description = evaluated_row[2].value
        account_name = evaluated_row[3].value
        if account_name == "":
            arq = open("error_log.txt","a")
            arq.write(f"Célula sem conta na linha {row +1}, coluna {col +1}, portanto a linha será ignorada.\n")
            continue

        dates.append(to_print_date)
        values.append(value)
        descriptions.append(description)
        account_names.append(account_name)

    records_object_list = list()

    for i in range(len(dates)):
         records_object_list.append(
            {
                'date': dates[i],
                'value': values[i],
                'description': descriptions[i],
                'account_name': account_names[i]
            }
        )

    return records_object_list

records_list()
    

def read_error_log():
    arq = open("error_log.txt")
    linhas = arq.readlines()
    print("Lista de logs: \n")
    for linha in linhas:
        print(linha)

def menu():
    print("Consulta WLC. Selecione uma das opções abaixo:")
    print("1 - Para consultar o saldo total por pessoa;")
    print("2 - Para consultar o saldo total por conta;")
    print("3 - Para consultar o total de todas as contas por data;")
    print("4 - Para consultar o log de erros;")
    print("5 - Para sair")

while True:

    menu()
    
    try:
        authentication = int(input("Digite uma opção válida para consulta: "))
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Insira um valor válido.")
        continue

    if authentication == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
#TODO
    elif authentication == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
#TODO
    elif authentication == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
#TODO        
    elif authentication == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        read_error_log()
    elif authentication == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Encerrando a consulta...")
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Opção inválida! Favor inserir uma opção válida.")
        continue