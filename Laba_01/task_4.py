from numpy import exp
from scipy.special import legendre, roots_legendre

f = lambda x: exp(x/2) / (x + 1)**(1/2)
I_precise = 1.11832273845302
df = lambda x: exp(x/2) / (2*(x + 1)**(1/2)) - exp(x/2) / (2*(x+1)**(3/2))
a = 0
b = 1.05
epsilon = 10**-5
n = 5
x_new = lambda x_old: (b - a)*x_old/2 + (a+b)/2

# TODO: Гаусс-НАСТ
#   1.Применить формулу Гаусса НАСТ
#   2.Оценить погрешность Rn

legendre_x = roots_legendre(n=n + 1, mu=False)[0]       # корни Pn+1(x)
dif_poly_legendre_coefficients = legendre(n=n + 1).deriv()    #коэф dPn+1(x):


def A(k: int) -> float:
    return 2 / ( (1 - legendre_x[k]**2)*(dif_poly_legendre_coefficients(legendre_x[k])**2) )


def I_Gauss() -> float:
    result = 0
    for i in range(0, n + 1):
        result += A(i)*f(x_new(legendre_x[i]))
    return result*(b-a)/2


def print_result() -> None:
    print('КФ НАСТ Гаусс : \nI : ', I_Gauss(), '\nНевязка : ', I_precise - I_Gauss())
