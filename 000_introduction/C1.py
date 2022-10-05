# a+b+c=nの制約下でのforループ入れ子
# forループでゴリ押す場合はnjit
n, y = map(int, input().split())

def solve(n, y):
    for i in range(n+1):
        for j in range(n-i+1):
            k = n - i - j
            if i*10 + j*5 + k == y/1000:
                return i, j, k
    return -1, -1, -1

i, j, k = solve(n, y)
print(i, j, k)