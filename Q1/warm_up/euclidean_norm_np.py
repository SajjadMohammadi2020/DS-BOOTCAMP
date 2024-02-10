# coding: utf-8
def euclidean_norm_np(mylist):
    import numpy as np
    res = np.sum(np.array(mylist)**2)
    res = np.sqrt(res)
    return res
