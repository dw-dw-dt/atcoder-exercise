# re.finditer(), itertools.combinations()の使い方
import re
import itertools
n = int(input())

if n == 0:
    print(0)
    exit()

bin_n = format(n, 'b') # str
n_list = [bin_n]

res_iter = re.finditer('1', bin_n)
res_list = []
for res in res_iter:
    res_list.append(res.start())

res_len = len(res_list)
res_list_list = []
for i in range(res_len):
    for pair in itertools.combinations(res_list, i+1):
        res_list_list.append(list(pair))

for item in res_list_list:
    tmp = bin_n
    for i in item: # item : [0, 2]
        tmp = tmp[:i] +'0'+ tmp[i+1:]
    n_list.append(tmp)

ans_list = []
for item in n_list:
    ans_list.append(int(item, 2))
ans_list = sorted(ans_list)
for ans in ans_list:
    print(ans)