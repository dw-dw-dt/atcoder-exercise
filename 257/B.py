n, k, q = map(int, input().split())
a_list = [int(i) for i in input().split()]
l_list = [int(i) for i in input().split()]

for i in range(q):
    l = l_list[i]
    if a_list[l-1] == n:
        pass
    elif l < k and a_list[l-1] + 1 == a_list[l]:
        pass
    else:
        a_list[l-1] += 1
a_list = map(str, a_list)
print(' '.join(a_list))
        