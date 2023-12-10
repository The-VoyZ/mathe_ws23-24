import seaborn as sns 
import sympy
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")
#print(df.loc[613])

df = sns.load_dataset("iris")
df.value_counts("species")

#sns.displot(df,x="petal_width",hue="species")
#plt.show()

def nr8(time,percentage):
    #geg:f(x) = anfangsbestand*e^(-a*x) // t in min
    x = sympy.symbols("x",real=True)
    eqation = sympy.Eq(1*sympy.exp(x*time),percentage)
    a = sympy.nsolve(eqation,x,0)
    print(a)
    equation2 = sympy.Eq(1*sympy.exp(a*x),0.00001)
    b = sympy.nsolve(equation2,x,0)
    print(b)
nr8(39,0.1)

def nr10(time,square):
    x = sympy.symbols("x",real=True)
    equation = sympy.Eq(1*sympy.exp(x*11),2)
    a = sympy.nsolve(equation,x,0)
    equation2 = sympy.Eq(x*sympy.exp(a*time),square)
    b = sympy.nsolve(equation2,x,0)
    print(b)

nr10(6,10)