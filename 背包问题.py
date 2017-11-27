# -*- utf-8 -*-
import time

def beibao(w,v,n,c):
    if n < 0 or c <= 0 : return 0

    res = beibao(w,v,n-1,c)
    if c >= w[n]:
        res = max(res,v[n] + beibao(w,v,n-1,c-w[n]))
    return res

if __name__ == "__main__":
    w = [1,2,3,4,5,6]
    v = [6,10,12,15,18,24]
    n = 5
    memo = [[-1 for _ in range(16)] for _ in range(5)]
    start_time = time.time()
    res = beibao(w,v,5,15)
    print res
    print time.time()-start_time