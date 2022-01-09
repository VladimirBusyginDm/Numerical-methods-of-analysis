import Laba_02.task_1 as task1
import Laba_02.task_2 as task2
import Laba_02.task_3 as task3
import Laba_02.task_4 as task4
import pandas as pd
import numpy as np

a = 1
b = 2
N = 10
h = (b - a) / N
x = [i for i in np.arange(a, b + h, h)]

a = task1.method()
b = task2.method()
c = task3.method()
d = task4.method()


r1 = [d[i] - a[i] for i in range(0, N + 1)]
r2 = [d[i] - b[i] for i in range(0, N + 1)]
r3 = [d[i] - c[i] for i in range(0, N + 1)]

col1 = ['x[i]', 'Метод Эйлера', 'Метод последовательнго повышения порядка точности', 'Метод Рунге-Кутта', 'Экстраполяционный метод Адамса']
data1 = pd.DataFrame(data=np.array([x, a, b, c, d]).transpose(), columns= col1)

col2 = ['x[i]', 'Метод Эйлера', 'Метод последовательнго повышения порядка точности', 'Метод Рунге-Кутта']
data2 = pd.DataFrame(data=np.array([x, r1, r2, r3]).transpose(), columns=col2)

def print_full(x):
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 2000)
    pd.set_option('display.float_format', '{:20,.6f}'.format)
    pd.set_option('display.max_colwidth', None)
    print(x)
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns')
    pd.reset_option('display.width')
    pd.reset_option('display.float_format')
    pd.reset_option('display.max_colwidth')

print_full(data1)
print('Таблица невязок')
print_full(data2)