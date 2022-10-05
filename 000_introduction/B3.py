# intの各桁の数字の和を求める
n, a, b = map(int, input().split())

ans = 0
for i in range(n+1):
    t = sum(map(int, list(str(i))))
    if t >= a and t <= b:
        ans += i
print(ans)