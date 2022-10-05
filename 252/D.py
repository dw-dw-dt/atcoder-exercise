# 3重for loopを使う（nC3）くらいなら余事象の利用などを検討
from collections import Counter

n = int(input())
a_list = [int(i) for i in input().split()]

ans = n * (n-1) * (n-2) / 6
count_dict = Counter(a_list)

for k, v in count_dict.items():
    if count_dict[k] >= 3: # 1つの数字を3回取ってきているケース
        ans -= count_dict[k] * (count_dict[k]-1) * (count_dict[k]-2) / 6
    if count_dict[k] >= 2: # 1つの数字を2回取ってきているケース
        ans -= count_dict[k] * (count_dict[k]-1) / 2 * (n - count_dict[k])
print(int(ans))
