# coding: utf-8
def solve(numb):
    import random
    import numpy as np
    L = [1/24 , 1/12 , 1/6 , 1/2 , 1/8 , 1/12]
    n_iter = 10000
    res = []
    for i in range(n_iter) :
        n_1 = 0
        n_2 = 0
        a1 = np.random.randint(24)
        a2 = np.random.randint(24)
        n_1 = get_dice(a1)
        n_2 = get_dice(a2)
        mult = n_1 * n_2 
        res.append(mult>numb)
    return sum(res)/len(res)
