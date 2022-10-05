# listのsortとスライス
n = int(input())
l = list(map(int, input().split()))

print(sum(sorted(l, reverse=True)[::2])-sum(sorted(l, reverse=True)[1::2]))