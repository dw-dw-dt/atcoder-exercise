# オーバーフローが生じないように p * q ** 3 > N を変形して p > N / (q**3) のようにする
n_ori = int(input())
n = min(n_ori, 1000000)

import math
from numba import njit
import numpy as np

def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False

    return prime

# 素数の列挙
prime = sieve_of_eratosthenes(n)
s_list = [0 for _ in range(sum(prime))]
cnt = 0
for p in range(n+1):
    if prime[p]:
        s_list[cnt] = p
        cnt += 1
        
@njit
def func(s_list, n_ori):
    ans = 0
    n = s_list.shape[0]
    for i in range(n):
        p = s_list[i]
        for j in range(i+1, n):
            q = s_list[j]
            if p > n_ori/(q ** 3): break
            else: ans += 1
    return ans


out = func(np.array(s_list), n_ori)
print(out)

