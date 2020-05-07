import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')  # Красивые графики

def data_search(m):
    """ищет в файле показатель и его значения, формирует массив значений за все периоды"""
    table = pd.read_csv(m, delimiter=',', header = 0, parse_dates = ['moment'])
    dataset = pd.DataFrame(table[table.name == item_name][['moment', 'name', 'iz_fiz', 'long_position', 'short_position']])
    dataset.query('iz_fiz == @fiz', inplace = True)
    dataset[['long_position', 'short_position']].astype(float)
    show_frame(dataset)

def show_frame(dataset):
    """визуализирует long_position и short_position на отрезке времени, добавляет подписи по оси Х"""
    lines_ds = pd.DataFrame(dataset, columns=['moment', 'long_position', 'short_position'])
    lines_ds.set_index('moment', inplace=True)
    lines_ds.plot()
    plt.show()

item_name = "Фьючерсный контракт на Индекс РТС"
fiz = ('1.0')
data_search ('moex\\output_MOEX_FUT.csv')



# "Фьючерсный контракт на курс доллар США - российский рубль"
# "Фьючерсный контракт на Индекс РТС"
# "Фьючерсный контракт на нефть BRENT"

# "Фьючерсный контракт на обыкновенные акции ПАО \"НК \"Роснефть\""
# "Фьючерсный контракт на обыкновенные акции ПАО Сбербанк"
# "Фьючерсный контракт на обыкновенные акции ПАО \"Газпром\""