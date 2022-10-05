# listの重複削除
n = int(input())
l = list(0 for _ in range(n))
for _ in range(n):
    l[_] = int(input())
print(len(set(l)))