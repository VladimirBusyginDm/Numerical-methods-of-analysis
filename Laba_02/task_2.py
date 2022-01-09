from numpy import log, arange

# TODO: 2.Метод последовательного повышения точности 2-го порядка q = 0

a = 1
b = 2
N = 10
h = (b - a) / N

f = lambda x, u: (u*u*log(x) - u) / x
x = [i for i in arange(a, b + h, h)]
y = [0.0 for i in range(0, N + 1)]
y[0] = 1    # начальное условие


def method() -> list:
    for j in range(0, N):
        y_half = y[j] + h * f(x[j], y[j]) / 2
        y[j + 1] = y[j] + h * f(x[j] + h / 2, y_half)
    return y

