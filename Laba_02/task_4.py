from numpy import log, arange

# TODO: 4.Экстраполяцион метод Адамса 3-го порядка с методом повышения точности 3-го порядка

a = 1
b = 2
N = 10
h = (b - a) / N

f = lambda x, u: (u*u*log(x) - u) / x
x = [i for i in arange(a, b + h, h)]
y = [0.0 for i in range(0, N + 1)]
y[0] = 1    # начальное условие

k = 2


def begin_table() -> None:
    for j in range(0, k):
        y_temp = y[j] + h * f(x[j], y[j]) / 3
        y_temp = y[j] + 2 * h * f(x[j] + h / 3, y_temp) / 3
        y[j + 1] = y[j] + h * (f(x[j], y[j]) + 3 * f(x[j] + 2 * h / 3, y_temp)) / 4


def method() -> list:
    begin_table()
    for j in range(k, N):
        y[j + 1] = y[j] + h * (23 * f(x[j], y[j]) - 16 * f(x[j - 1], y[j - 1]) + 5 * f(x[j - 2], y[j - 2])) / 12
    return y