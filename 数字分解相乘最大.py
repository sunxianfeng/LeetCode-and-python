# -*- coding:utf-8 -*-
import time
memo = [-1 for _ in range(25)]
def breakinteger(n):
    if n == 1: return 1
    if memo[n] != -1: return memo[n]
    res = -1
    for i in range(1,n):
       res = max(res, max(i * breakinteger(n-i),i * (n-i)))
    memo[n] = res
    return memo[n]



if __name__ == "__main__":
    start_time = time.time()
    res = breakinteger(20)
    print time.time() - start_time
    print res