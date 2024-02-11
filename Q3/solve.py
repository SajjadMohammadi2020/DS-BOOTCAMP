# coding: utf-8
def solve(arr):
    import numpy as np
    import scipy as sp
    import math
    SSB = 0 
    k = len(arr)
    all_extend = []
    for i in range(len(arr)) : 
        all_extend.extend(arr[i])
    all_mean = np.array(all_extend).mean()
    for i in range(len(arr)) : 
        SSB += ((len(arr[i]))*(np.mean(arr[i])-all_mean)**2)
    SSE = 0
    for i in range(len(arr)) : 
        mean_gr = np.array(arr[i]).mean()
        for j in range(len(arr[i])) : 
            SSE += ((arr[i][j]-mean_gr)**2)
    SST = SSE + SSB
    N = len(all_extend)
    df1 = k - 1 
    df2 = N - k
    df3 = N - 1
    MSB = SSB / (k-1)
    MSE = SSE / (N-k)
    f_value = MSB / MSE
    pvalue = 100 * (sp.stats.f.cdf(f_value , df1 , df2))        
    return pvalue
