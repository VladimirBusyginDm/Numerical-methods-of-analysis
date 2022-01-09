from numpy import log, arange, array

# TODO : Метод Рунге-Кутты

a = 1
b = 2
N = 10
h = (b - a) / N

A = [1/2, 1/2]      # q + 1
alfa = [1, 0]       # q + 1
beta = [[1, 0],     # q x q
        [0, 0]]
q = 1

f = lambda x, u: (u*u*log(x) - u) / x
x = [i for i in arange(a, b + h, h)]
y = [0.0 for i in range(0, N + 1)]
y[0] = 1    # начальное условие


def method1() -> list:
    for j in range(0, N):
        fi = [h for i in range(0, q + 1)]
        fi[0] *= f(x[j], y[j])
        y[j + 1] = y[j] + A[0]*fi[0]

        for i in range(1, q + 1):
            temp_y = y[j]
            for k in range(0, i):
                temp_y += beta[i][k]*fi[k]
            fi[i] *= f(x[j] + alfa[i]*h, temp_y)
            y[j + 1] += A[i]*fi[i]
    return y


def method() -> list:
    for j in range(0, N):
        k1 = f(x[j], y[j])
        k2 = f(x[j] + 2*h/3, y[j] + 2*h*k1/3)
        y[j+1] = y[j] + h*(k1 + 3*k2)/4
    return y

