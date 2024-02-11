# coding: utf-8
def integral(f, a, b):
    import numpy as np #‌ If needed
    step = 0.01
    n_samples = int((b-a)/step)
    x = np.linspace(start=a , stop=b , num=n_samples)
    S = 0
    for i in x : 
        S += (step*f(i))
    return S
