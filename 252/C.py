n = int(input())

s_list = ['a' for _ in range(n)]
for i in range(n):
    s_list[i] = input()

ans_dict = {i: 0 for i in range(10)}
for k in range(10):
    t_list = [None for _ in range(n)]
    for i in range(n):
        word = list(s_list[i])
        t = s_list[i].index(f'{k}')
        while t in t_list:
            t += 10
        t_list[i] = t
    ans_dict[k] = max(t_list)

min_ans  = min(ans_dict.values())
print(min_ans)