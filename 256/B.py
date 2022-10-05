n = int(input())
a_list = [int(i) for i in input().split()]

cnt = 0
for i in range(n):
    if sum(a_list[i:]) >= 4: cnt += 1
print(cnt)