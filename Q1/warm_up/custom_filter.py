# coding: utf-8
def custom_filter(arr,L):
    import numpy as np
    arr = np.array(arr)
    L = np.array([L])
    arr = np.append(arr , L , axis = 0 )
    arr = arr.T
    rem = []
    for i in range(len(arr)) : 
        if sum((arr[i]<=1) | (arr[i]>=10)) != 0 : 
            rem.append(i)
    arr = np.delete(arr, rem , 0)
    arr = arr.T
    if arr.size == 0 : 
        return "NULL"
    else : 
        return arr
