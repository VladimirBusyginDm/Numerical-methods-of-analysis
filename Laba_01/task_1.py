import matplotlib.pyplot as plt
from numpy import arange, exp

f = lambda x: exp(x/2) / (x + 1)**(1/2)
I_precise = 1.11832273845302
df = lambda x: exp(x/2) / (2*(x + 1)**(1/2)) - exp(x/2) / (2*(x+1)**(3/2))
a = 0
b = 1.05
epsilon = 10**-5


def graphics() -> None:
    plt.plot([x for x in arange(a, b, 0.05)], [f(x) for x in arange(a, b, 0.05)],
             [x for x in arange(a, b, 0.05)], [df(x) for x in arange(a, b, 0.05)])
    plt.grid()
    plt.show()

# TODO :
#   1)Правило Рунге, сост квадр формула левых прямоугольников, шаг разб h?


def I(h: float) -> float:
    sum = 0
    N = int ((b - a) / h)
    for k in range(0, N):
        sum += f(a + k*h)
    return sum*h


def R(h1: float, h2: float) -> float:
    return h1**2 * (I(h2) - I(h1)) / (h1**2 - h2**2)


def Runge_h() -> tuple:
    h1 = b
    h2 = b/2
    N = 2
    while abs(R(h1, h2)) > epsilon:
        N += 1
        h1 = b / N
        h2 = h1 / 2
    return N, h2


def print_result() -> None:
    N, h = Runge_h()
    print('Левых прямоугольников : \nI : ', I(h), '\nN : ', N, '\nh : ', h, '\nНевязка : ', I_precise - I(h))
