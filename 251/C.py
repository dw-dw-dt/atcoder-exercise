n = int(input())
original = {}
num_dict = {}
for i in range(n):
    k, v = input().split()
    v = int(v)
    if k not in original.keys():
        original[k] = v
    num_dict[str(i)] = k

max_scr = 0
ans = 'a'
for k, v in original.items():
    if v > max_scr:
        max_scr = v
        ans = k

for k, v in num_dict.items():
    if v == ans:
        print(int(k)+1)
        exit()
