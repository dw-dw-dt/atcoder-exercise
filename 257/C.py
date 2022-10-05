# 都度、負荷のある計算をするのではなく前回の値を利用できないかどうかを検討する
n = int(input())
s = list(input())
s = list(map(int, s))
w_list = [int(i) for i in input().split()]

maps = [(w_list[i],s[i]) for i in range(n)]

a_list = [i[1] for i in sorted(maps)]
sorted_maps = sorted(maps)

best_ans = 0
for i in range(n):
    if i == 0: 
        ans = sum(a_list)
    elif sorted_maps[i][0] == sorted_maps[i-1][0]: 
        if a_list[i-1] == 1:
            ans -= 1
        else:
            ans += 1
        continue
    else:
        if a_list[i-1] == 1:
            ans -= 1
        else:
            ans += 1
    if best_ans < ans:
        best_ans = ans
ans = n - sum(a_list)
if best_ans < ans:
    best_ans = ans
print(best_ans)
