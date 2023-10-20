import numpy as np 
import math as m

def expformat(num):
    zahl = np.exp(num)
    formatted = f"{zahl:.5e}"
    print(formatted)
    
def natlogfunction(num):
    x = num 
    x = np.log(x)
    print(x)
    
def log10func(num):
    x = num 
    x = np.log10(x)
    print(x)
    
def natlogformat(num):
    x = float(num)
    x = np.log(x)
    print(x)
    
natlogformat(6.1e38)