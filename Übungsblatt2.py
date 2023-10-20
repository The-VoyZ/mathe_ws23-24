import sympy
from sympy import log
import numpy as np
def nr1(denom,equal):
    x = sympy.Symbol("x")
    equation = sympy.Eq(x/denom,equal)
    solution = sympy.solve(equation)
    print(f"Die Lösung für X ist {solution[0]}")
    
def nr2 (x):
    solution = np.exp(-x)
    print(f"Die Lösung ist :{solution}")
    
def nr3 (num):
    solution = np.exp(num)
    print(f"Die Lösung ist: {solution:.5e}")

def nr4(minutes, weight):
    A = sympy.Symbol("A",real=True)
    equation = sympy.Eq(weight * sympy.exp(A * minutes), 2*weight)
    solution = sympy.solve(equation, A)
    
    output = float(solution[0])
    return output

def nr5(minutes, weight, numberofDuplication):
    x = sympy.Symbol("x", real=True)
    a = nr4(minutes, weight)
    equation = sympy.Eq(weight * sympy.exp(a * x), numberofDuplication * weight)
    # Using nsolve to get the numerical solution
    solution = sympy.nsolve(equation, x, 0)  # The third argument is an initial guess, I used 0.
    print(f"Lösung ist : {solution}")

def nr6(weight,minutes,a):
    x = sympy.Symbol("x",real=True)
    #geg: f(x) = anfangsgewicht*e^a*x 
    #ges: 100 = x*e^a*30)
    equation = sympy.Eq(x*sympy.exp(a*minutes),weight)
    solution = sympy.nsolve(equation,x,0)
    print(f"Lösung ist: {solution}")
    
#halbwerts zeit berechnung
def nr7(t,endkonzentration):
    #geg:f(x) = anfangsbestand*e^(-a*x) // t in sec
    #ges: 10% vom anfangs bestand. 
    #f(0.50) = 1*e^(-a*36)
    y = sympy.Symbol("a",real=True)
    x = sympy.Symbol("x",real=True)
    equation1 = sympy.Eq(1 * sympy.exp(y * t), 0.5)
    a = sympy.nsolve(equation1,y,0)
    print(a)
    equation2 = sympy.Eq(1*sympy.exp(a*x),endkonzentration)
    solution = sympy.nsolve(equation2,x,0)
    print(f"Lösung ist : {solution}")