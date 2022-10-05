# 全探索する必要があるのだけれど、パターン数が多すぎるので、DPで解く（愚直に全探索すると計算負荷が大きくなりすぎる）
# DPは全探索の効率化, 最大最小問題や全部で何パターン問題で頻出。ナップサック問題のように制約条件も入力変数とすることも。
# DPはpypy必須
n, m = map(int, input().split())
a_list = list(map(int, input().split()))

dp = [[0 for i in range(n)] for j in range(m)]
for i in range(n):
    for j in range(m):
        if j > i: dp[j][i] = 0
        elif j == i:
            if j == 0:
                dp[j][i] = a_list[i]
            else:
                dp[j][i] = dp[j-1][i-1] + a_list[i] * (i+1)
        else:
            if j == 0:
                dp[j][i] = max(dp[j][i-1], a_list[i])
            else:
                dp[j][i] = max(dp[j][i-1], dp[j-1][i-1] + a_list[i] * (j+1))

print(int(dp[m-1][n-1]))