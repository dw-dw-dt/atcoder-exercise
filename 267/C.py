m, n = map(int, input().split())
a_list = list(map(int, input().split()))


for i in range(m):
    if i == 0: 
        ans = a_list[0] * 1
        for j in range(1, n):
            ans += a_list[j] * (j+1)
        prev_sum = ans
    else:
        _ans = prev_sum
        if i + n - 1 >= m: break
        if i == 1:
            delta = sum(a_list[i-1:i+n-1])
        else:
            delta += a_list[i+n-2] - a_list[i-2] 
        # for j in range(n):
        #     _ans -= a_list[i-1+j]
        # _ans += a_list[i+n-1]*n
        _ans += a_list[i+n-1]*n - delta
        if _ans > ans:
            ans = _ans
        prev_sum = _ans

print(ans)
