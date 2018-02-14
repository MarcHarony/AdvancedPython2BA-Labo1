    # utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2
from math import sqrt
def fact(n):
    """Computes the factorial of a natural number.
    
    Pre: -
    Post: Returns the factorial of 'n'.
    Throws: ValueError if n < 0
    """
    a = n
    facto = 1
    while a > 0 :
        facto *= a
        a-=1
    return facto

def roots(a, b, c):
    """Computes the roots of the ax^2 + bx + c = 0 polynomial.
    
    Pre: -
    Post: Returns a tuple with zero, one or two elements corresponding
          to the roots of the ax^2 + bx + c polynomial.
    """
    rho = b**2-4*a*c
    if rho >0 :
        root_1 = (-b+ sqtr(rho))/(2*a)
        root_2 = (-b- sqtr(rho))/(2*a)
        return root_1 ,root_2
    elif rho == 0 :
        root = -b/(2*a)
        return (root)
    else :
        return ()

def integrate(function, lower, upper):
    """Approximates the integral of a fonction between two bounds
    
    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <= 'upper',
         'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """
    coconut = 0
    a = lower
    while a < upper :
        coconut += -1+(a+1)**2 #pas le temps de créer une fonction qui interprète un string
        a+=1
    return coconut

if __name__ == '__main__':
    print(fact(5))
    print(roots(1, 0, 1))
    print(integrate('x ** 2 - 1', 0, 3))

#test
