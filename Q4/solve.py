# coding: utf-8
def solve(n, m, L):
    import numpy as np
    n_iter = 5000
    mobiles = []
    for i in range(n_iter) :
        n_mob = 0
        for j in range(m) :
            rr = np.random.rand()
            if rr < L[n_mob] and n_mob > 0 : 
                n_mob -= 1 
            elif rr >= L[n_mob] and n_mob < n : 
                n_mob += 1
        mobiles.append(n_mob)
    return sum(mobiles)/len(mobiles)
