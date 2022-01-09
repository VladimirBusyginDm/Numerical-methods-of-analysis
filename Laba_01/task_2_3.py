import matplotlib.pyplot as plt
from numpy import arange, exp

f = lambda x: exp(x/2) / (x + 1)**(1/2)
I_precise = 1.11832273845302
df = lambda x: exp(x/2) / (2*(x + 1)**(1/2)) - exp(x/2) / (2*(x+1)**(3/2))
a = 0
b = 1.05
epsilon = 10**-5

# TODO :  Определить шаги h для заданной точности
#   2.a) Составная формула трапеций
#   2.б) Составная формула средних прямоугольников


ddf = lambda x: (1 - 2/(x + 1) + 3/((x + 1)**2))*exp(x/2) / (4*((x + 1)**(1/2)))
M = ddf(a)


def graphic_ddf() -> None:
    plt.plot([x for x in arange(a, b, 0.05)], [ddf(x) for x in arange(a, b, 0.05)])
    plt.xlabel('x')
    plt.ylabel('f \'\' (x)')
    plt.grid()
    plt.show()


def trapeze() -> tuple:
    N = int(((((b - a)**3)*M / (12*epsilon))**(1/2)))
    h = (b - a) / N
    return N, h


def I_trapeze() -> float:
    result = (f(a) + f(b)) / 2
    N, h = trapeze()
    for k in range(1, N):
        result += f(a + k*h)
    return result * h


def middle_rectangles() -> tuple:
    N = int(((((b - a) ** 3) * M) / (24 * epsilon)) ** (1 / 2))
    h = (b - a) / N
    return N, h


def I_middle_rectangles() -> float:
    N, h = middle_rectangles()
    result =  0
    for k in range(0, N):
        result += f(a + (k + 1/2)*h)
    return result * h


def print_result() -> None:
    N_t, h_t = trapeze()
    I_t = I_trapeze()
    N_m_r, h_m_r = middle_rectangles()
    I_m_r = I_middle_rectangles()
    print('КФ трапеции : \nI : ', I_t, '\nh : ', h_t, '\nN : ', N_t, '\nНевязка : ', I_precise - I_t)
    print('КФ средних прямоугольников : \nI : ', I_m_r, '\nh : ', h_m_r, '\nN : ', N_m_r, '\nНевязка : ', I_precise - I_m_r)
