"""Файл, который содержит функции анализа."""
import pathlib
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import pearsonr as sonr
from scipy.stats import spearmanr as manr
from scipy.stats import kruskal
import help_functions

boxplot_scatter_array_1_2 = ['BodyType', 'FuelType', 'GearboxType',
                             'Cylinders', 'Drivetrain', 'Seats', 'Doors',
                             'Air.Conditioner', 'Heater',
                             'AntiLock.Braking.System', 'Central.Locking',
                             'Power.Steering', 'Power.Windows',
                             'Anti.Lock.Braking', 'Brake.Assist',
                             'Central.Locking.1', 'Power.Door.Locks',
                             'Child.Safety.Locks', 'Rear.Seat.Belts',
                             'Door.Ajar.Warning', 'Adjustable.Seats',
                             'Crash.Sensor', 'Engine.Check.Warning',
                             'Rear.Camera', 'Anti.Theft.Device',
                             'Touch.Screen', 'Audio.System.Remote.Control',
                             'Speakers.Front...back', 'Bluetooth.Connectivity',
                             'USB...Auxiliary.Input',
                             'Adjustable.Steering.Column',
                             'Height.Adjustable.Driving.Seat', 'Digital.Clock']

kruskal_fun_array_3 = ['Heater', 'AntiLock.Braking.System', 'Central.Locking',
                       'Power.Steering', 'Power.Windows', 'Anti.Lock.Braking',
                       'Brake.Assist', 'Central.Locking.1', 'Power.Door.Locks',
                       'Child.Safety.Locks', 'Rear.Seat.Belts',
                       'Door.Ajar.Warning', 'Adjustable.Seats', 'Crash.Sensor',
                       'Engine.Check.Warning', 'Rear.Camera',
                       'Anti.Theft.Device', 'Touch.Screen',
                       'Audio.System.Remote.Control', 'Speakers.Front...back',
                       'USB...Auxiliary.Input', 'Adjustable.Steering.Column',
                       'Height.Adjustable.Driving.Seat', 'Digital.Clock']

hist_fun_array_4 = ['Price', 'Powerhp', 'Torquelbft', 'Cylinders', 'MPGCity',
                    'MPGHighway', 'Seats', 'Doors',
                    'Heightin', 'Lengthin', 'Widthin', 'Wheelbasein']


def brands(excel, home):
    """
    Создает график разнообразия брендов новых авто в США.

    Автор: Половников Дмитрий
    """
    save_path = pathlib.Path(home, 'Graphics', 'brands.png')
    data_brand = pd.DataFrame(excel).loc[:, ['Brand']]
    data_brand_np = data_brand.to_numpy()
    data_brand_unique, data_brand_counts = np.unique(data_brand_np,
                                                     return_counts=True)
    fig, ax_1 = plt.subplots()
    ax_1.barh(data_brand_unique, data_brand_counts, linewidth=0.5,
              edgecolor='blue', color='Black')
    fig.set_figheight(14)
    fig.set_figwidth(10)
    ax_1.set_title('Диаграмма разнообразия брендов новых авто в США',
                   fontsize=13, fontweight='bold')
    ax_1.set_xlabel('Количество', fontsize=13, fontweight='bold')
    ax_1.set_ylabel('Марки', fontsize=13, fontweight='bold')
    ax_1.grid(which='major')
    ax_1.grid(which='minor')
    ax_1.minorticks_on()
    bbox_inches = matplotlib.transforms.Bbox.from_extents(0, 0, 10, 14)
    fig.savefig(save_path,
                dpi=300,
                bbox_inches=bbox_inches)
    plt.show()


def countries(excel, home):
    """
    Создает график новых авто в США по странам производства.

    Автор: Половников Дмитрий
    """
    save_path = pathlib.Path(home, 'Graphics', 'countries.png')
    data_country = pd.DataFrame(excel).loc[:, ['Country']]
    data_country_np = data_country.to_numpy()
    data_country_unique, data_country_counts = np.unique(data_country_np,
                                                         return_counts=True)
    fig, ax_2 = plt.subplots()
    ax_2.barh(data_country_unique, data_country_counts, linewidth=0.5,
              edgecolor='red', color='Black')
    fig.set_figheight(14)
    fig.set_figwidth(10)
    ax_2.set_title('Статистика новых авто в США по странам производства',
                   fontsize=13, fontweight='bold')
    ax_2.set_xlabel('Количество', fontsize=13, fontweight='bold')
    ax_2.set_ylabel('Страны', fontsize=13, fontweight='bold')
    ax_2.grid(which='major')
    ax_2.grid(which='minor')
    ax_2.minorticks_on()
    bbox_inches = matplotlib.transforms.Bbox.from_extents(0, 0, 10, 14)
    fig.savefig(save_path,
                dpi=300,
                bbox_inches=bbox_inches)
    plt.show()


def price_dependency_boxplot(excel, arg, home):
    """
    Анализ связи цены с (аргументом).

    Создает график Бокса-Вискера: цена(аргумент)
    Автор: Половников Дмитрий
    """
    save_path = pathlib.Path(home, 'Graphics', 'boxplot.png')
    ax_plt = excel.boxplot(column='Price', by=arg, vert=False, fontsize=15,
                           grid=True, figsize=(10, 6))
    ax_plt.set_title(label='')
    ax_plt.set_xlabel(xlabel='Price')
    ax_plt.set_ylabel(ylabel=arg)
    ax_plt.set_xlim([0, 700000])
    ax_plt.figure.savefig(save_path, dpi=300)
    plt.show()


def price_dependency_scatter(excel, arg, home):
    """
    Анализ связи цены с (аргументом).

    Создает график-разброс: цена(аргумент)
    Автор: Сиротин Артём
    """
    save_path = pathlib.Path(home, 'Graphics', 'scatter.png')
    ax_plt = excel.plot.scatter(x='Price', y=arg)
    ax_plt.set_xlim([0, 700000])
    title = 'Scatter grouped by ' + arg
    ax_plt.set_title(label=title)
    ax_plt.figure.savefig(save_path, dpi=300)
    plt.show()


def correlation(excel, home):
    """
    Корреляция количественных переменных в базе данных.

    Автор: Бородин Илья
    """
    path = pathlib.Path(home, 'Output', 'correlation.xlsx')
    data_corr = excel.select_dtypes(include=['int', 'float'])
    data_corr = data_corr.iloc[:, 3:]
    data_stat = data_corr.describe()
    data_med = data_corr.median()
    data_iqr = data_corr.quantile(q=0.75) - data_corr.quantile(q=0.25)
    data_med_iqr = pd.DataFrame([data_med, data_iqr], index=['median', 'IQR'])
    data_stat = pd.concat([data_stat, data_med_iqr])
    pearson_stats = pd.DataFrame([],
                                 index=data_corr.columns,
                                 columns=data_corr.columns)
    pearson_worth = pd.DataFrame([],
                                 index=data_corr.columns,
                                 columns=data_corr.columns)
    spearman_stats = pd.DataFrame([],
                                  index=data_corr.columns,
                                  columns=data_corr.columns)
    spearman_worth = pd.DataFrame([],
                                  index=data_corr.columns,
                                  columns=data_corr.columns)
    for x_1 in data_corr.columns:
        for y_1 in data_corr.columns:
            pearson_stats.loc[x_1, y_1], pearson_worth.loc[x_1, y_1] = sonr(
                data_corr[x_1], data_corr[y_1])
            spearman_stats.loc[x_1, y_1], spearman_worth.loc[x_1, y_1] = manr(
                data_corr[x_1], data_corr[y_1])

    with pd.ExcelWriter(path, engine='openpyxl') as wrt:
        data_stat.to_excel(wrt, sheet_name='Statistics')

        pearson_stats.to_excel(wrt, sheet_name='Pearson')

        pearson_worth.to_excel(wrt, startrow=pearson_stats.shape[0] + 2,
                               sheet_name='Pearson')

        spearman_stats.to_excel(wrt, sheet_name='Spearman')

        spearman_worth.to_excel(wrt, startrow=spearman_stats.shape[0] + 2,
                                sheet_name='Spearman')


def kruskal_fun(excel, home, arg):
    """
    Корреляция.

    Анализ корреляции между количественной целевой переменной
    и качественной объясняющей.
    Автор: Сиротин Артём
    """
    path = pathlib.Path(home, 'Output', 'kruskal.txt')
    data_yes = excel.loc[excel[arg] == 'Yes', 'Price']
    data_no = excel.loc[excel[arg] == 'No', 'Price']
    price_sig = kruskal(data_yes, data_no)
    with open(path, 'w', encoding='utf-8') as fln:
        print('Критерий Kruskal — Wallis для переменных "Price" и "' + arg
              + '"', file=fln)
        print(price_sig, file=fln)


def correlation_graphic(excel, home):
    """
    Корреляция количественных переменных в базе данных и вывод графика.

    Автор: Половников Дмитрий
    """
    path = pathlib.Path(home, 'Graphics', 'correlation_1.png')
    data_corr = excel.select_dtypes(include=['int', 'float'])
    data_corr = data_corr.iloc[:, 3:]
    pearson_stats = pd.DataFrame([],
                                 index=data_corr.columns,
                                 columns=data_corr.columns)
    for item in data_corr.columns:
        for j_item in data_corr.columns:
            pearson_stats.loc[item, j_item], temp = sonr(data_corr[item],
                                                         data_corr[j_item])
    pearson_stats = pearson_stats.iloc[0:6, 0:6]
    np_pearson = pearson_stats.to_numpy().astype('float')
    df_columns = data_corr.columns[0:6]
    fig, axis = plt.subplots()
    # heatmap() и annotate_heatmap() - функции из папки Library
    image, cbar = help_functions.heatmap(np_pearson, df_columns, df_columns,
                                         ax=axis,
                                         cmap='YlGn',
                                         cbarlabel='Dependence')

    help_functions.annotate_heatmap(image)

    fig.tight_layout()
    print(temp, cbar)
    plt.savefig(path, dpi=300)
    plt.show()


def hist_fun(excel, home, arg='Power.hp', bins=20):
    """
    Гистограмма частот количественных переменных.

    Автор: Бородин Илья
    """
    path = pathlib.Path(home, 'Graphics', 'correlation_2.png')
    excel[arg].hist(bins=bins)
    plt.title('Histogram grouped by ' + arg)
    plt.xlabel(arg)
    plt.ylabel('Frequency')
    plt.savefig(path, dpi=300)
    plt.show()
