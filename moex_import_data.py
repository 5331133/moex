import pandas as pd

def wday_list (file_name):
    """собирает список аргументов для даты и передает его в file_list"""
    with open(file_name, 'r', encoding='utf-8') as dict:
        dic = [row.strip() for row in dict]
    dict.close()
    print(dic)
    file_list (dic)

def file_list(dic):
    """формирует перечень адресов-ссылок для импорта данных и запускает экспорт данных st_search"""
    for i in dic:
        m = "https://www.moex.com/ru/derivatives/open-positions-csv.aspx?d="+i+"&t=1"
        print(m)
        st_search(m)

def st_search(m):
    """ищет в файле показатель и его значения, формирует массив значений за все периоды"""
    table = pd.read_csv(m, delimiter=',', header = 0, parse_dates = ['moment'])
    col_name = ['moment', 'name', 'iz_fiz', 'long_position', 'short_position']
    dataset = pd.DataFrame(table[table.contract_type == item_name][['moment', 'name', 'iz_fiz', 'long_position', 'short_position']])
    for index, row in dataset.iterrows():
        to_export = []
        for i in col_name:
            to_export.append(row[i])
        base.append(to_export)
    return

def generate_file(base, filename):
    """экспортирует массив данных base в .csv файл filename.csv"""
    df = pd.DataFrame(base)
#    df.to_csv(filename, header=['moment', 'name', 'iz_fiz', 'long_position', 'short_position'], encoding='utf-8') # полная перезапись базы
    df.to_csv(filename, mode='a', header=None, encoding='utf-8') # добавление к существующей базе

base = []
item_name = "F"
wday_list ('moex\\work_days_20200505.txt') # ссылка на БД с перечнем дат к загрузке
generate_file (base, 'moex\\output_MOEX_FUT.csv') # ссылка на бызу для выгрузки/добавления


#for i in base: print(i, '\n') # ---тест корректности выгрузки---

# "Фьючерсный контракт на курс доллар США - российский рубль"
# "Фьючерсный контракт на Индекс РТС"
# "Фьючерсный контракт на нефть BRENT"

# "Фьючерсный контракт на обыкновенные акции ПАО \"НК \"Роснефть\""
# "Фьючерсный контракт на обыкновенные акции ПАО Сбербанк"
# "Фьючерсный контракт на обыкновенные акции ПАО \"Газпром\""

#['moment', 'isin', 'name', 'contract_type', 'iz_fiz', 'clients_in_long', 'clients_in_short', 'short_position',
#'long_position', 'change_prev_week_short_abs', 'change_prev_week_long_abs', 'change_prev_week_short_perc',
#'change_prev_week_long_perc', 'Empty']

# index=False,  - добавить в параметры df.to_csv для генерации без индекса первой строкой

# http://iss.moex.com/iss/history/engines/stock/markets/shares/boards/tqbr/securities/AFLT.csv?date=20200504