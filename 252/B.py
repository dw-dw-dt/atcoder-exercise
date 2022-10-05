n, k = map(int, input().split())

a_list = [int(_) for _ in input().split()]
b_list = [int(_) for _ in input().split()]

max_a = max(a_list)
for i in b_list:
    if a_list[i-1] == max_a:
        print('Yes')
        exit()
print('No')