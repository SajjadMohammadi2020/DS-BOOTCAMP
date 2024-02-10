# coding: utf-8
def euclidean_norm_list(mylist):
    import math
    res = 0
    for i in range(len(mylist)) : 
        res += (mylist[i]**2)
    res = math.sqrt(res)
    return res
