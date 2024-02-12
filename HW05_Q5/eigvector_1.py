# coding: utf-8
def eigvector_1 (T):
    import numpy as np
    I = np.identity(len(T))
    T = T - I
    
    for i in range(len(T-1)) : 
        for j in range(i+1,len(T)) : 
            if T[j][i] != 0 : 
                k = T[j][i] / T[i][i]
                T[j] -= (k*T[i])
    res = [ 0 for i in range(len(T))]
    res[-1] = 1
    for i in range(len(T)-2,-1,-1) : 
        s = 0 
        ff = T[i] / (-1 * T[i][i])
        for j in range(len(T)-1,i,-1) : 
            s += (ff[j] * res[j])
        res[i] = s
    jam = sum(res)
    k = 100 / jam
    for i in range(len(res)) : 
        res[i] *= k
    V = res 
    return V    
