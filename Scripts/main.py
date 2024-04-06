"""
Главный файл.

Запускает программу и вытягивает данные для отображения анализа
с main_functions.py.
Интерфейс разрабатывался всеми участниками проекта.
К каждой функции подписан автор. Он писал код, опираясь на мысли и идеи
каждого коллеги.
"""
import sys
import tkinter as tk
from tkinter import ttk
import pathlib
from io import BytesIO
import requests
import pandas as pd
from PIL import Image as Im
from PIL import ImageTk as ImTk
import matplotlib

# если поставить main_functions выше под PEP8, то не будет работать код
sys.path.append('../Library')
import main_functions
# начало до 76 строчки писалось вместе всеми участниками
matplotlib.use('TkAgg')

HOME_DIR = str(pathlib.Path.cwd())[:-8]
PATH_TO_DATA = str(pathlib.Path(HOME_DIR, 'Data', 'Cars_Python.xlsx'))
EXCEL_DATA = pd.read_excel(io=PATH_TO_DATA, sheet_name=0)
columns = list(EXCEL_DATA.columns)
lenCars = len(EXCEL_DATA.Model)
# Listbox

root = tk.Tk()
root.title('Auto')
root.geometry("600x700")
root.config(bg="black")
root.resizable(False, False)
STYLE = ttk.Style()
STYLE.theme_use('classic')

Notebox = ttk.Notebook(root, width=600, height=850)
TabRoot = ttk.Frame(Notebox)
TabGraphic = ttk.Frame(Notebox)
TAB_SETTINGS = ttk.Frame(Notebox)
Notebox.add(TabRoot, text='База')
Notebox.add(TabGraphic, text='Анализ')
Notebox.add(TAB_SETTINGS, text='Настройки')
Notebox.grid(row=0, column=0)

lb = tk.Listbox(TabRoot, width=50, height=20)
lb.grid(row=1, columns=1, rowspan=2, sticky=tk.N)
MODELS = []
for i in range(lenCars):
    MODELS.append((EXCEL_DATA.Model[i], EXCEL_DATA.Number[i]))
for j in range(len(MODELS)):
    lb.insert(tk.END, MODELS[j][0])
scroll = tk.Scrollbar(TabRoot, orient='vertical', command=lb.yview)
scroll.grid(row=1, columns=1, rowspan=2, sticky=tk.N + tk.S + tk.E)
lb["yscrollcommand"] = scroll.set

# Добавляет пространство после listbox

label = ttk.Label(TabRoot, text='---------',

                  font=('Arial', 24, 'bold'),
                  relief=tk.RAISED,

                  justify=tk.LEFT
                  )
label.grid(row=7, column=0, columnspan=2, stick='we')


# Дополнительное окно с фильтрами

def get_filters():
    """
    Получение фильтров из базы данных.

    Автор: Сиротин Артём
    """
    global MODELS
    max_prices = MAX_PRICE.get()
    min_prices = MIN_PRICE.get()
    brand_box = str(COMBOBOX_BRAND.get())
    country_box = str(COMBOBOX_COUNTRY.get())
    petrol_box = str(COMBOBOX_PETROL.get())
    body_box = str(COMBOBOX_BODY.get())
    print(body_box)
    lb.delete(0, tk.END)
    MODELS.clear()

    if not max_prices:
        max_prices = 10000000000
    else:
        max_prices = int(MAX_PRICE.get())
    if not min_prices:
        min_prices = 0
    else:
        min_prices = int(MIN_PRICE.get())
    for item in range(lenCars):
        if min_prices <= EXCEL_DATA.Price[item] <= max_prices:
            if country_box == EXCEL_DATA.Country[item]:
                if petrol_box == EXCEL_DATA.FuelType[item]:
                    if EXCEL_DATA.Brand[item] == brand_box:
                        if body_box == EXCEL_DATA.BodyType[item]:
                            MODELS.append((EXCEL_DATA.Model[item],
                                           EXCEL_DATA.Number[item]))
                        elif body_box == 'Любой кузов':
                            MODELS.append((EXCEL_DATA.Model[item],
                                           EXCEL_DATA.Number[item]))
                    elif brand_box == 'Все марки':
                        if body_box == EXCEL_DATA.BodyType[item]:
                            MODELS.append((EXCEL_DATA.Model[item],
                                           EXCEL_DATA.Number[item]))
                        elif body_box == 'Любой кузов':
                            MODELS.append((EXCEL_DATA.Model[item],
                                           EXCEL_DATA.Number[item]))
                elif petrol_box == 'Любое топливо':
                    if EXCEL_DATA.Brand[item] == brand_box:
                        if body_box == EXCEL_DATA.BodyType[item]:
                            MODELS.append((EXCEL_DATA.Model[item],
                                           EXCEL_DATA.Number[item]))
                        elif body_box == 'Любой кузов':
                            MODELS.append((EXCEL_DATA.Model[item],
                                           EXCEL_DATA.Number[item]))
                    elif brand_box == 'Все марки':
                        if body_box == EXCEL_DATA.BodyType[item]:
                            MODELS.append((EXCEL_DATA.Model[item],
                                           EXCEL_DATA.Number[item]))
                        elif body_box == 'Любой кузов':
                            MODELS.append((EXCEL_DATA.Model[item],
                                           EXCEL_DATA.Number[item]))
            elif country_box == 'Все страны':
                if petrol_box == EXCEL_DATA.FuelType[item]:
                    if EXCEL_DATA.Brand[item] == brand_box:
                        if body_box == EXCEL_DATA.BodyType[item]:
                            MODELS.append((EXCEL_DATA.Model[item],
                                           EXCEL_DATA.Number[item]))
                        elif body_box == 'Любой кузов':
                            MODELS.append((EXCEL_DATA.Model[item],
                                           EXCEL_DATA.Number[item]))
                    elif brand_box == 'Все марки':
                        if body_box == EXCEL_DATA.BodyType[item]:
                            MODELS.append((EXCEL_DATA.Model[item],
                                           EXCEL_DATA.Number[item]))
                        elif body_box == 'Любой кузов':
                            MODELS.append((EXCEL_DATA.Model[item],
                                           EXCEL_DATA.Number[item]))
                elif petrol_box == 'Любое топливо':
                    if EXCEL_DATA.Brand[item] == brand_box:
                        if body_box == EXCEL_DATA.BodyType[item]:
                            MODELS.append((EXCEL_DATA.Model[item],
                                           EXCEL_DATA.Number[item]))
                        elif body_box == 'Любой кузов':
                            MODELS.append((EXCEL_DATA.Model[item],
                                           EXCEL_DATA.Number[item]))
                    elif brand_box == 'Все марки':
                        if body_box == EXCEL_DATA.BodyType[item]:
                            MODELS.append((EXCEL_DATA.Model[item],
                                           EXCEL_DATA.Number[item]))
                        elif body_box == 'Любой кузов':
                            MODELS.append((EXCEL_DATA.Model[item],
                                           EXCEL_DATA.Number[item]))
    for j_item in range(len(MODELS)):
        lb.insert(tk.END, MODELS[j_item][0])
    FILTERS.destroy()


def new_window_filters():
    """
    Создание окна с фильтрами.

    Автор: Сиротин Артём
    """
    global FILTERS
    global MIN_PRICE
    global MAX_PRICE
    global COMBOBOX_COUNTRY
    global COMBOBOX_PETROL
    global COMBOBOX_BRAND
    global COMBOBOX_BODY
    FILTERS = tk.Tk()
    FILTERS.title('Filters')
    FILTERS.geometry('600x300')
    FILTERS.resizable(False, False)
    label_min_price_name = ttk.Label(FILTERS, text='Минимальная цена',
                                     font=('Arial', 10, 'bold'),
                                     relief=tk.RAISED,
                                     justify=tk.LEFT)
    label_min_price_name.grid(row=0, column=0, pady=10, sticky=tk.E + tk.W)
    MIN_PRICE = ttk.Entry(FILTERS)
    MIN_PRICE.grid(row=0, column=1, pady=10)

    label_max_price_name = ttk.Label(FILTERS, text='Максимальная цена',
                                     font=('Arial', 10, 'bold'),
                                     relief=tk.RAISED,
                                     justify=tk.LEFT)
    label_max_price_name.grid(row=1, column=0, pady=10, sticky=tk.E + tk.W)
    MAX_PRICE = ttk.Entry(FILTERS)
    MAX_PRICE.grid(row=1, column=1)

    button_accept = ttk.Button(FILTERS, text='accept', command=get_filters)
    button_accept.grid(row=4, column=0, columnspan=2, sticky=tk.E + tk.W)
    label_country = ttk.Label(FILTERS, text='Страна производства',
                              font=('Arial', 10, 'bold'),
                              relief=tk.RAISED,
                              justify=tk.LEFT)
    label_country.grid(row=0, column=3, pady=10, padx=10, sticky=tk.E + tk.W)

    country = ['Все страны', 'Japan', 'Germany', 'South Korea', 'USA', 'UK',
               'Italy', 'France', 'Sweden', 'Czech', 'China']

    COMBOBOX_COUNTRY = ttk.Combobox(FILTERS, state="readonly", values=country)
    COMBOBOX_COUNTRY.current(0)
    COMBOBOX_COUNTRY.grid(row=0, column=4)

    label_petrol = ttk.Label(FILTERS, text='Тип топлива',
                             font=('Arial', 10, 'bold'),
                             relief=tk.RAISED,
                             justify=tk.LEFT)
    label_petrol.grid(row=1, column=3, pady=10, padx=10, sticky=tk.E + tk.W)

    label_brand = ttk.Label(FILTERS, text='Марка авто:',
                            font=('Arial', 10, 'bold'),
                            relief=tk.RAISED,
                            justify=tk.LEFT)
    label_brand.grid(row=3, column=0, pady=10, padx=10, sticky=tk.E + tk.W)

    label_body = ttk.Label(FILTERS, text='Кузов:',
                           font=('Arial', 10, 'bold'),
                           relief=tk.RAISED,
                           justify=tk.LEFT)
    label_body.grid(row=3, column=3, pady=10, padx=10, sticky=tk.E + tk.W)

    brand_list = ['Все марки', 'Honda', 'BMW', 'Lexus', 'Hyundai', 'Toyota',
                  'KIA', 'Nissan', 'Audi', 'Chevrolet', 'Ford', 'Mercedes',
                  'Porsche', 'Infiniti', 'Jaguar', 'Cadillac', 'Land Rover',
                  'Jeep', 'Volkswagen', 'Maserati', 'Subaru', 'Dodge', 'Mazda',
                  'Chrysler', 'Aston Martin', 'Ferrari', 'Lamborghini',
                  'Bugatti', 'Bentley', 'Rolls Royce', 'Mclaren', 'Lincoln',
                  'Alfa Romeo', 'Volvo', 'MINI', 'Fiat', 'Acura', 'Genesis',
                  'Buick', 'GMC', 'Koenigsegg', 'Lotus', 'Suzuki', 'MG',
                  'Skoda', 'JAC', 'Changan']

    COMBOBOX_BRAND = ttk.Combobox(FILTERS, state="readonly", values=brand_list)
    COMBOBOX_BRAND.current(0)
    COMBOBOX_BRAND.grid(row=3, column=1)

    petrol = ['Любое топливо', 'Petrol', 'Hybrid', 'Diesel', 'Electric']
    COMBOBOX_PETROL = ttk.Combobox(FILTERS, values=petrol)
    COMBOBOX_PETROL.current(0)
    COMBOBOX_PETROL.grid(row=1, column=4)

    body = ['Любой кузов', 'Convertible', 'Coupe', 'Hatchback',
            'Sedan', 'SUV', 'Truck', 'Van', 'Wagon']
    COMBOBOX_BODY = ttk.Combobox(FILTERS, state="readonly", values=body)
    COMBOBOX_BODY.current(0)
    COMBOBOX_BODY.grid(row=3, column=4)


def reset():
    """
    Очистка фильтров.

    Автор: Сиротин Артём
    """
    MODELS.clear()
    lb.delete(0, tk.END)
    for item in range(lenCars):
        MODELS.append((EXCEL_DATA.Model[item], EXCEL_DATA.Number[item]))
    for j_item in range(len(MODELS)):
        lb.insert(tk.END, MODELS[j_item][0])


buttonFilters = ttk.Button(TabRoot, text='Фильтры', command=new_window_filters)
buttonFilters.grid(row=7, column=0, sticky=tk.E)

ResetFilters = ttk.Button(TabRoot, text='Сбросить фильтры', command=reset)
ResetFilters.grid(row=7, column=1, sticky=tk.W)

# Начальное приветствие
label_1 = ttk.Label(TabRoot, text='Выберите авто для просмотра характеристик',
                    font=('Arial', 16, 'bold'),
                    relief=tk.RAISED,
                    justify=tk.LEFT)
label_1.grid(row=0, column=0, columnspan=2, stick='we')


# Model = 'qwe'

def select():
    """
    Вывод характеристик выбранного автомобиля во вкладке база.

    Автор: Половников Дмитрий
    """
    global MODEL
    global EXCEL_DATA
    global MODELS
    lb_current = lb.curselection()
    MODEL = lb.get(lb_current)
    for item in range(len(MODELS)):
        if MODEL in MODELS[item]:
            price = EXCEL_DATA.Price[MODELS[item][1] - 1]
            LabelPrice.config(text=f'Цена ($): {price}')

            country = EXCEL_DATA.Country[MODELS[item][1] - 1]
            LabelCountry.config(text=f'Страна производства: {country}')

            brand = EXCEL_DATA.Brand[MODELS[item][1] - 1]
            LabelBrand.config(text=f'Марка авто: {brand}')

            engine_type = EXCEL_DATA.EngineType[MODELS[item][1] - 1]
            LabelEngineType.config(text=f'Двигатель: {engine_type}')

            body_type = EXCEL_DATA.BodyType[MODELS[item][1] - 1]
            LabelBodyType.config(text=f'Кузов: {body_type}')

            fuel_type = EXCEL_DATA.FuelType[MODELS[item][1] - 1]
            LabelFuelType.config(text=f'Тип топлива: {fuel_type}')

            gearbox = EXCEL_DATA.GearboxType[MODELS[item][1] - 1]
            LabelGearboxType.config(text=f'Тип коробки передач: {gearbox}')

            power_hp = EXCEL_DATA.Powerhp[MODELS[item][1] - 1]
            LabelPowerhp.config(text=f'Лошадиные силы: {power_hp}')

            torque = EXCEL_DATA.Torquelbft[MODELS[item][1] - 1]
            LabelTorquelbft.config(text=f'Крутящий момент (фунт-фут): \
{torque}')

            cylinders = EXCEL_DATA.Cylinders[MODELS[item][1] - 1]
            LabelCylinders.config(text=f'Цилиндры: {cylinders}')

            drive_train = EXCEL_DATA.Drivetrain[MODELS[item][1] - 1]
            LabelDrivetrain.config(text=f'Привод: {drive_train}')

            city = EXCEL_DATA.MPGCity[MODELS[item][1] - 1]
            LabelMPGCity.config(text=f'Расход по городу (галлоны-мили): \
{city}')

            highway = EXCEL_DATA.MPGHighway[MODELS[item][1] - 1]
            LabelMPGHighway.config(text=f'Расход по трассе (галлоны-мили): \
{highway}')

            seats = EXCEL_DATA.Seats[MODELS[item][1] - 1]
            LabelSeats.config(text=f'Кол-во сидений: {seats}')

            doors = EXCEL_DATA.Doors[MODELS[item][1] - 1]
            LabelDoors.config(text=f'Кол-во дверей: {doors}')

            height = EXCEL_DATA.Heightin[MODELS[item][1] - 1]
            LabelHeightin.config(text=f'Высота (дюйм): {height}')

            length = EXCEL_DATA.Lengthin[MODELS[item][1] - 1]
            LabelLengthin.config(text=f'Длина (дюйм): {length}')

            width = EXCEL_DATA.Widthin[MODELS[item][1] - 1]
            LabelWidthin.config(text=f'Ширина (дюйм): {width}')

            wheel_base = EXCEL_DATA.Wheelbasein[MODELS[item][1] - 1]
            LabelWheelbasein.config(text=f'Колесная база (дюйм): {wheel_base}')

            resl = (290, 200)
            res = requests.get(EXCEL_DATA.Photo[MODELS[item][1] - 1]).content
            photo = ImTk.PhotoImage(Im.open(BytesIO(res)).resize(resl,
                                                                 Im.LANCZOS))
            LabelPhoto.config(image=photo)
            LabelPhoto.image = photo
    LabelCur.config(text=f'Характеристики модели: {MODEL}')


# Автор: Бородин Илья до 513 строчки
buttonSelect = ttk.Button(TabRoot, text='Выбрать', command=select)
buttonSelect.grid(row=8, column=0, columnspan=2)

LabelCur = ttk.Label(TabRoot, text='Характеристики модели:',
                     font=('Arial', 10, 'bold'),
                     relief=tk.RAISED,
                     anchor='w',
                     justify=tk.LEFT, )
LabelCur.grid(row=9, column=0, columnspan=3, sticky=tk.W + tk.E)

LabelPrice = ttk.Label(TabRoot, text='Цена ($): ',
                       font=('Arial', 10, 'bold'),
                       relief=tk.RAISED,
                       anchor='w',
                       justify=tk.LEFT)
LabelPrice.grid(row=10, column=0, sticky=tk.W + tk.E)

LabelBrand = ttk.Label(TabRoot, text='Марка авто: ',
                       font=('Arial', 10, 'bold'),
                       relief=tk.RAISED,
                       anchor='w',
                       justify=tk.LEFT)
LabelBrand.grid(row=10, column=1, sticky=tk.W + tk.E)

LabelCountry = ttk.Label(TabRoot, text='Страна производства: ',
                         font=('Arial', 10, 'bold'),
                         relief=tk.RAISED,
                         anchor='w',
                         justify=tk.LEFT)
LabelCountry.grid(row=11, column=0, sticky=tk.W + tk.E)

LabelEngineType = ttk.Label(TabRoot, text='Двигатель: ',
                            font=('Arial', 10, 'bold'),
                            relief=tk.RAISED,
                            anchor='w',
                            justify=tk.LEFT)
LabelEngineType.grid(row=11, column=1, sticky=tk.W + tk.E)

LabelBodyType = ttk.Label(TabRoot, text='Кузов: ',
                          font=('Arial', 10, 'bold'),
                          relief=tk.RAISED,
                          anchor='w',
                          justify=tk.LEFT)
LabelBodyType.grid(row=12, column=0, sticky=tk.W + tk.E)

LabelFuelType = ttk.Label(TabRoot, text='Тип топлива: ',
                          font=('Arial', 10, 'bold'),
                          relief=tk.RAISED,
                          anchor='w',
                          justify=tk.LEFT)
LabelFuelType.grid(row=12, column=1, sticky=tk.W + tk.E)

LabelGearboxType = ttk.Label(TabRoot, text='Тип коробки передач: ',
                             font=('Arial', 10, 'bold'),
                             relief=tk.RAISED,
                             anchor='w',
                             justify=tk.LEFT)
LabelGearboxType.grid(row=13, column=0, sticky=tk.W + tk.E)

LabelPowerhp = ttk.Label(TabRoot, text='Лошадиные силы: ',
                         font=('Arial', 10, 'bold'),
                         relief=tk.RAISED,
                         anchor='w',
                         justify=tk.LEFT)
LabelPowerhp.grid(row=13, column=1, sticky=tk.W + tk.E)

LabelTorquelbft = ttk.Label(TabRoot, text='Крутящий момент (фунт-фут): ',
                            font=('Arial', 10, 'bold'),
                            relief=tk.RAISED,
                            anchor='w',
                            justify=tk.LEFT)
LabelTorquelbft.grid(row=14, column=0, sticky=tk.W + tk.E)

LabelCylinders = ttk.Label(TabRoot, text='Цилиндры: ',
                           font=('Arial', 10, 'bold'),
                           relief=tk.RAISED,
                           anchor='w',
                           justify=tk.LEFT)
LabelCylinders.grid(row=14, column=1, sticky=tk.W + tk.E)

LabelDrivetrain = ttk.Label(TabRoot, text='Привод: ',
                            font=('Arial', 10, 'bold'),
                            relief=tk.RAISED,
                            anchor='w',
                            justify=tk.LEFT)
LabelDrivetrain.grid(row=15, column=0, sticky=tk.W + tk.E)

LabelMPGCity = ttk.Label(TabRoot, text='Расход по городу (галлоны-мили): ',
                         font=('Arial', 10, 'bold'),
                         relief=tk.RAISED,
                         anchor='w',
                         justify=tk.LEFT)
LabelMPGCity.grid(row=15, column=1, sticky=tk.W + tk.E)

LabelMPGHighway = ttk.Label(TabRoot, text='Расход по трассе (галлоны-мили): ',
                            font=('Arial', 10, 'bold'),
                            relief=tk.RAISED,
                            anchor='w',
                            justify=tk.LEFT)
LabelMPGHighway.grid(row=16, column=0, sticky=tk.W + tk.E)

LabelSeats = ttk.Label(TabRoot, text='Кол-во сидений: ',
                       font=('Arial', 10, 'bold'),
                       relief=tk.RAISED,
                       anchor='w',
                       justify=tk.LEFT)
LabelSeats.grid(row=16, column=1, sticky=tk.W + tk.E)

LabelDoors = ttk.Label(TabRoot, text='Кол-во дверей: ',
                       font=('Arial', 10, 'bold'),
                       relief=tk.RAISED,
                       anchor='w',
                       justify=tk.LEFT)
LabelDoors.grid(row=17, column=0, sticky=tk.W + tk.E)

LabelHeightin = ttk.Label(TabRoot, text='Высота (дюйм): ',
                          font=('Arial', 10, 'bold'),
                          relief=tk.RAISED,
                          anchor='w',
                          justify=tk.LEFT)
LabelHeightin.grid(row=17, column=1, sticky=tk.W + tk.E)

LabelLengthin = ttk.Label(TabRoot, text='Длина (дюйм): ',
                          font=('Arial', 10, 'bold'),
                          relief=tk.RAISED,
                          anchor='w',
                          justify=tk.LEFT)
LabelLengthin.grid(row=18, column=0, sticky=tk.W + tk.E)

LabelWidthin = ttk.Label(TabRoot, text='Ширина (дюйм): ',
                         font=('Arial', 10, 'bold'),
                         relief=tk.RAISED,
                         anchor='w',
                         justify=tk.LEFT)
LabelWidthin.grid(row=18, column=1, sticky=tk.W + tk.E)

LabelWheelbasein = ttk.Label(TabRoot, text='Колесная база (дюйм): ',
                             font=('Arial', 10, 'bold'),
                             relief=tk.RAISED,
                             anchor='w',
                             justify=tk.LEFT)
LabelWheelbasein.grid(row=19, column=0, columnspan=2, sticky=tk.W + tk.E)

LabelPhoto = ttk.Label(TabRoot)
LabelPhoto.grid(row=1, column=1, rowspan=2, sticky=tk.N + tk.S + tk.W)

# Длина для всех колонок
TabRoot.grid_columnconfigure(1, weight=300)

# Второе окно
Label = ttk.Label(TabGraphic, text='Графические данные: ',
                  font=('Arial', 14, 'bold'),
                  relief=tk.RAISED,
                  anchor='w',
                  justify=tk.LEFT)
Label.grid(row=0, column=0, columnspan=2, stick='we')

LabelBrand2 = ttk.Label(TabGraphic, text='Создает график разнообразия \n'
                                         'брендов новых авто в США: ',
                        font=('Arial', 10, 'bold'),
                        relief=tk.RAISED,
                        anchor='w',
                        justify=tk.LEFT)
LabelBrand2.grid(row=1, column=0, stick='we')


def brand():
    """
    Вызов функции из main_functions.

    Автор: Половников Дмитрий
    """
    global HOME_DIR
    global EXCEL_DATA
    main_functions.brands(EXCEL_DATA, HOME_DIR)


ButtonBrand = ttk.Button(TabGraphic, text='Brand', command=brand)
ButtonBrand.grid(row=2, column=0, stick='we')

LabelCountry2 = ttk.Label(TabGraphic, text='Создает график новых авто \n'
                                           'в США по странам производства: ',
                          font=('Arial', 10, 'bold'),
                          relief=tk.RAISED,
                          anchor='w',
                          justify=tk.LEFT)
LabelCountry2.grid(row=1, column=1, stick='we')


def countries():
    """
    Вызов функции из main_functions.

    Автор: Бородин Илья
    """
    global HOME_DIR
    global EXCEL_DATA
    main_functions.countries(EXCEL_DATA, HOME_DIR)


ButtonCountries = ttk.Button(TabGraphic, text='Countries', command=countries)
ButtonCountries.grid(row=2, column=1, stick='we')

LabelSpace = ttk.Label(TabGraphic, text='',
                       font=('Arial', 10, 'bold'),
                       anchor='w',
                       justify=tk.LEFT)
LabelSpace.grid(row=3, column=0, columnspan=2, stick='we')
# combobox1
LabelCombobox = ttk.Label(TabGraphic, text='Выберите параметр:',
                          font=('Arial', 10, 'bold'),
                          relief=tk.RAISED,
                          anchor='w',
                          justify=tk.LEFT)
LabelCombobox.grid(row=4, column=0, columnspan=2, stick='we')

Params1 = main_functions.boxplot_scatter_array_1_2
COMBOBOX_PARAMS_1 = ttk.Combobox(TabGraphic, state="readonly", values=Params1)
COMBOBOX_PARAMS_1.current(0)
COMBOBOX_PARAMS_1.grid(row=4, column=1)


def combobox_params_1():
    """
    Вызов функции из main_functions.

    Автор: Сиротин Артём
    """
    global COMBOBOX_PARAMS_1
    combobox = COMBOBOX_PARAMS_1.get()
    main_functions.price_dependency_boxplot(EXCEL_DATA, combobox, HOME_DIR)


LabelCombobox1 = ttk.Label(TabGraphic, text='Создает график Бокса-Вискера:\n'
                                            'цена(аргумент):',
                           font=('Arial', 10, 'bold'),
                           relief=tk.RAISED,
                           anchor='w',
                           justify=tk.LEFT)
LabelCombobox1.grid(row=5, column=0, stick='we')

LabelCombobox2 = ttk.Label(TabGraphic, text='Создает график-разброс:\n'
                                            'цена(аргумент):',
                           font=('Arial', 10, 'bold'),
                           relief=tk.RAISED,
                           anchor='w',
                           justify=tk.LEFT)
LabelCombobox2.grid(row=5, column=1, stick='we')

ButtonCombobox = ttk.Button(TabGraphic,
                            text='Boxplot',
                            command=combobox_params_1)
ButtonCombobox.grid(row=6, column=0, sticky=tk.E + tk.W)


# Combobox2

def combobox_params_2():
    """
    Вызов функции из main_functions.

    Автор: Сиротин Артём
    """
    global COMBOBOX_PARAMS_1
    combobox = COMBOBOX_PARAMS_1.get()
    main_functions.price_dependency_scatter(EXCEL_DATA, combobox, HOME_DIR)


ButtonCombobox2 = ttk.Button(TabGraphic,
                             text='Scatter',
                             command=combobox_params_2)
ButtonCombobox2.grid(row=6, column=1, sticky=tk.E + tk.W)

LabelSpace1 = ttk.Label(TabGraphic, text='',
                        font=('Arial', 10, 'bold'),
                        anchor='w',
                        justify=tk.LEFT)
LabelSpace1.grid(row=7, column=0, columnspan=2, stick='we')
LabelSpace12 = ttk.Label(TabGraphic, text='',
                         font=('Arial', 10, 'bold'),
                         anchor='w',
                         justify=tk.LEFT)
LabelSpace12.grid(row=15, column=0, columnspan=2, stick='we')
# кнопка
LabelText = ttk.Label(TabGraphic, text='Текстовые данные:',
                      font=('Arial', 14, 'bold'),
                      relief=tk.RAISED,
                      anchor='w',
                      justify=tk.LEFT)
LabelText.grid(row=16, column=0, stick='we')
LabelCor = ttk.Label(TabGraphic,
                     text='Корреляция количественных '
                          'переменных в базе данных.',
                     font=('Arial', 10, 'bold'),
                     relief=tk.RAISED,
                     anchor='w',
                     justify=tk.LEFT)
LabelCor.grid(row=17, column=0, columnspan=2, stick='we')


def text_file():
    """
    Вызов функции из main_functions.

    Автор: Половников Дмитрий
    """
    global HOME_DIR
    global EXCEL_DATA
    main_functions.correlation(EXCEL_DATA, HOME_DIR)


ButtonCountries = ttk.Button(TabGraphic, text='Correlation', command=text_file)
ButtonCountries.grid(row=18, column=0, columnspan=2, stick='we')

LabelSpace1 = ttk.Label(TabGraphic, text='',
                        font=('Arial', 10, 'bold'),
                        anchor='w',
                        justify=tk.LEFT)
LabelSpace1.grid(row=19, column=0, columnspan=2, stick='we')
# Combobox
LabelCombobox3 = ttk.Label(TabGraphic, text='Выберите параметр:',
                           font=('Arial', 10, 'bold'),
                           relief=tk.RAISED,
                           anchor='w',
                           justify=tk.LEFT)
LabelCombobox3.grid(row=20, column=0, columnspan=2, stick='we')

Params2 = main_functions.kruskal_fun_array_3
COMBOBOX_PARAMS_2 = ttk.Combobox(TabGraphic, state="readonly", values=Params2)
COMBOBOX_PARAMS_2.current(0)
COMBOBOX_PARAMS_2.grid(row=20, column=1)


def combobox_params_3():
    """
    Вызов функции из main_functions.

    Автор: Бородин Илья
    """
    global COMBOBOX_PARAMS_2
    combobox = COMBOBOX_PARAMS_2.get()
    main_functions.kruskal_fun(EXCEL_DATA, HOME_DIR, combobox)


LabelCorrelation = ttk.Label(TabGraphic,
                             text='Анализ корреляции между\n'
                             'количественной целевой переменной'
                                  'и \nкачественной объясняющей.',
                             font=('Arial', 10, 'bold'),
                             relief=tk.RAISED,
                             anchor='w',
                             justify=tk.LEFT)
LabelCorrelation.grid(row=21, column=0, sticky=tk.E + tk.W + tk.S + tk.N)

ButtonCombobox = ttk.Button(TabGraphic,
                            text='Kruskal',
                            command=combobox_params_3)
ButtonCombobox.grid(row=21, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

# Кнопка
LabelCorrelation = ttk.Label(TabGraphic,
                             text='Корреляция количественных '
                                  'переменных в базе данных.',
                             font=('Arial', 10, 'bold'),
                             relief=tk.RAISED,
                             anchor='w',
                             justify=tk.LEFT)
LabelCorrelation.grid(row=8,
                      column=0,
                      columnspan=2,
                      sticky=tk.E + tk.W + tk.S + tk.N)


def correlation_graphic():
    """
    Вызов функции из main_functions.

    Автор: Половников Дмитрий
    """
    global HOME_DIR
    global EXCEL_DATA
    main_functions.correlation_graphic(EXCEL_DATA, HOME_DIR)


ButtonCor = ttk.Button(TabGraphic, text='CorGraph',
                       command=correlation_graphic)
ButtonCor.grid(row=9, column=0, columnspan=2, sticky=tk.E + tk.W)

LabelSpace2 = ttk.Label(TabGraphic, text='',
                        font=('Arial', 10, 'bold'),
                        anchor='w',
                        justify=tk.LEFT)
LabelSpace2.grid(row=10, column=0, columnspan=2, stick='we')

LabelHist = ttk.Label(TabGraphic, text='Выберите параметры:',
                      font=('Arial', 10, 'bold'),
                      relief=tk.RAISED,
                      anchor='w',
                      justify=tk.LEFT)
LabelHist.grid(row=11, column=0, columnspan=2, stick='we')

Params3 = main_functions.hist_fun_array_4
COMBOBOX_PARAMS_3 = ttk.Combobox(TabGraphic, state="readonly", values=Params3)
COMBOBOX_PARAMS_3.current(0)
COMBOBOX_PARAMS_3.grid(row=11, column=1)


def combobox_params_4():
    """
    Вызов функции из main_functions.

    Автор: Сиротин Артём
    """
    global COMBOBOX_PARAMS_3
    global SCALE
    combobox = COMBOBOX_PARAMS_3.get()
    bins = SCALE.get()
    main_functions.hist_fun(EXCEL_DATA, HOME_DIR, combobox, bins)


var = tk.IntVar()


# Автор: Сиротин Артём до 902 строки
def on_scale(val):
    """Дополнительная функция для bins."""
    variable = int(float(val))
    var.set(variable)


SCALE = tk.Scale(TabGraphic, from_=10, to=300,
                 command=on_scale, orient='horizontal')
SCALE.grid(row=12, column=0, columnspan=2, sticky=tk.E + tk.W)

LabelHist1 = ttk.Label(TabGraphic,
                       text='Гистограмма частот количественных переменных.',
                       font=('Arial', 10, 'bold'),
                       relief=tk.RAISED,
                       anchor='w',
                       justify=tk.LEFT)
LabelHist1.grid(row=13, column=0, columnspan=2, stick='we')
ButtonHist = ttk.Button(TabGraphic, text='Hist', command=combobox_params_4)
ButtonHist.grid(row=14, column=0, columnspan=2, sticky=tk.E + tk.W)

TabGraphic.grid_columnconfigure(0, weight=300)
TabGraphic.grid_columnconfigure(1, weight=300)

# Настройки

LabelFont = ttk.Label(TAB_SETTINGS, text='Выберите тему:',
                      font=('Arial', 20, 'bold'),
                      relief=tk.RAISED,
                      anchor='w',
                      justify=tk.LEFT)
LabelFont.grid(row=0, column=0, sticky=tk.E + tk.W, padx=10)

Font = ['White', 'Black']
COMBOBOX_FONT = ttk.Combobox(TAB_SETTINGS, state="readonly", values=Font)
COMBOBOX_FONT.current(0)
COMBOBOX_FONT.grid(row=0, column=1, padx=10)

STYLE.theme_create('Black', parent='classic', settings={
    ".": {
        "configure": {
            "background": 'black',  # All except tabs
            "font": 'white'
        }
    },
    "TNotebook": {
        "configure": {
            "background": '#474747',  # Your margin color
            "tabmargins": [0, 2, 0, 0],  # margins: left, top, right, separator
        }
    },
    "TNotebook.Tab": {
        "configure": {
            "background": '#fafafa',  # tab color when not selected
            "padding": [2, 0],
            # [space between text and horizontal tab-button border,
            # space between text and vertical tab_button border]
            "font": "white"
        },
        "map": {
            "background": [("selected", '#474747')],  # Tab color when selected
            "expand": [("selected", [1, 1, 1, 0])]  # text margins
        }
    },
    "TButton": {
        "configure": {
            "background": '#18171C',
            'foreground': 'white',
            'relief': [tk.RAISED],
            "anchor": "center",
            "padx": 10,
            "pady": 10
        },
        "map": {
            "background": [("active", '#474747')],  # Tab color when selected
            'relief': [('pressed', tk.SUNKEN)],
        }

    },
    "TLabel": {
        "configure": {
            "background": 'black',
            'foreground': 'white'
        }
    }
})


def settings():
    """Дополнительная вкладка с настройками интерфейса."""
    global STYLE
    global COMBOBOX_FONT
    global TAB_SETTINGS
    font_setting = COMBOBOX_FONT.get()
    if font_setting == "White":
        STYLE.theme_use('classic')
    elif font_setting == "Black":
        STYLE.theme_use(font_setting)


ButtonSettings = ttk.Button(TAB_SETTINGS, text='Принять', command=settings)
ButtonSettings.grid(row=1, column=0, columnspan=2, sticky=tk.E + tk.W)

root.mainloop()
