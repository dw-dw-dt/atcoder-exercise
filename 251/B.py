# listではなくsetを使う
# 愚直なやり方でも、pypyなら通った
n, w = map(int, input().split())
a_list = list(map(int, input().split()))
a_list.sort()

a_set = set(a_list)

a2_set = set()
for i in range(n):
    a = a_list[i]
    if a > w/2.0:
        break
    for j in range(i+1, n):
        b = a_list[j]
        if a + b > w:
            break
        a2_set.add(a + b)

a3_set = set()
for i in range(n):
    a = a_list[i]
    if a > w/3.0:
        break
    for j in range(i+1, n):
        b = a_list[j]
        if a + b > w/3.0*2.0:
            break
        for k in range(j+1, n):
            c = a_list[k]
            if a + b + c > w:
                break
            a3_set.add(a + b + c)

ans = 0
for i in range(1, w+1):
    # 1つ
    if i in a_set:
        ans += 1
        continue
    # 2つ
    if i in a2_set:
        ans += 1
        continue
    # 3つ
    if i in a3_set:
        ans += 1
        continue

print(ans)
