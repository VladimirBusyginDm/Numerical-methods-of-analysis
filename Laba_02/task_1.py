from numpy import log, arange

# TODO: Неявный метод Эйлера с реализацией метода Ньютона

a = 1
b = 2
N = 10
h = (b - a) / N

f = lambda x, u: (u*u*log(x) - u) / x
x = [i for i in arange(a, b + h, h)]
y = [0.0 for i in range(0, N + 1)]
y[0] = 1    # начальное условие

df = lambda x, u: (2*u*log(x) - 1) / x
F = lambda y_l, j : y_l - y[j - 1] - h * f(x[j], y_l)
dF = lambda y_l, j: 1 - h * df(x[j], y_l)


def Nuton(y: float, j: float) -> float:
    return y - F(y, j) / dF(y, j)


def method() -> list:
    for j in range(1, N + 1):
        start = y[j - 1]
        end = Nuton(start, j)
        while abs(start - end) >= h**4:
            start = end
            end = Nuton(end, j)
        y[j] = y[j - 1] + h * f(x[j], end)
    return y