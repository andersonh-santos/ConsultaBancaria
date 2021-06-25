import xlrd, os, datetime

PATH = os.path.abspath("data/sheet_money.xlsx")
WORKBOOK = xlrd.open_workbook(PATH)
RECORDS_WORKSHEET = WORKBOOK.sheet_by_index(0)
ACCOUNTS_WORKSHEET = WORKBOOK.sheet_by_index(1)

def read_account_list():
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

    clients_object_list = list()

    for key in range(len(account_names)):
        clients_object_list.append(
            {
                'account_name': account_names[key],
                'client': clients[key],
                'acronym': acronyms[key],
            }
        )

    return clients_object_list


def read_record_list():
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
            file = open("error_log.txt","w")
            file.write(f"Célula sem valor na linha {row +1}, coluna {col -1}, portanto a linha será ignorada.\n")
            continue

        description = evaluated_row[2].value
        account_name = evaluated_row[3].value

        if account_name == "":
            file = open("error_log.txt","a")
            file.write(f"Célula sem conta na linha {row +1}, coluna {col +1}, portanto a linha será ignorada.\n")
            continue


        dates.append(to_print_date)
        values.append(value)
        descriptions.append(description)
        account_names.append(account_name)

    records_object_list = list()

    for key in range(len(dates)):
         records_object_list.append(
            {
                'date': dates[key],
                'value': values[key],
                'description': descriptions[key],
                'account_name': account_names[key]
            }
        )

    return records_object_list

ACCOUNTS = read_account_list() 
RECORDS = read_record_list()

def read_total_by_person(RECORDS, ACCOUNTS):
    people_accounts = dict()

    for account in ACCOUNTS:
        if account["client"] in people_accounts.keys():
            people_accounts[account["client"]].append(account["acronym"])
        else:
            people_accounts[account["client"]] = [account["acronym"]]

    total_by_people = dict()

    for account in ACCOUNTS:
        total_by_people[account["client"]] = 0

    for record in RECORDS:
        for person in people_accounts:
            if record["account_name"] in people_accounts[person]:
                total_by_people[person] += record["value"]

    print("Lista do saldo total por pessoa:")

    for person in total_by_people:
        print(f"O saldo total da {person} é de {total_by_people[person]}")


def read_total_by_account(RECORDS):
    total_by_account = dict()

    for account in RECORDS:
        total_by_account[account["account_name"]] = 0

    for account_name in RECORDS:
        total_by_account[account_name["account_name"]] += account_name["value"]

    print("Lista do saldo total por conta:")

    for account_name in total_by_account:
        print(f"O saldo de todas as contas é {account_name}: {total_by_account[account_name]}")


def read_total_by_date(RECORDS):
    date_dict = dict()

    for date in RECORDS:
        date_dict[date["date"]] = 0

    for date in RECORDS:
        date_dict[date["date"]] += date["value"]

    print("Lista do saldo total por data:")

    for date in date_dict:
        print(f"O saldo de todas as contas na data {date} é de: {date_dict[date]}")


def read_error_log():
    file = open("error_log.txt")
    lines = file.readlines()

    print("Lista de logs: \n")

    for line in lines:
        print(line)


def create_menu():
    print("\nConsulta WLC. Selecione uma das opções abaixo:")
    print("1 - Para consultar o saldo total por pessoa;")
    print("2 - Para consultar o saldo total por conta;")
    print("3 - Para consultar o total de todas as contas por data;")
    print("4 - Para consultar o log de erros;")
    print("5 - Para sair")

while True:

    create_menu()
    
    try:
        authentication = int(input("Digite uma opção válida para consulta: "))
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Insira um valor válido.")
        continue

    if authentication == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        read_total_by_person(RECORDS, ACCOUNTS)
    elif authentication == 2:       
        os.system('cls' if os.name == 'nt' else 'clear')
        read_total_by_account(RECORDS)  
    elif authentication == 3:
        os.system('cls' if os.name == 'nt' else 'clear')  
        read_total_by_date(RECORDS)      
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