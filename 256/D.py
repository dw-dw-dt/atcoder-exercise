# リストの削除を先頭からするとものすごく時間がかかる
# おそらくindexの再設定などのためか、後ろから削除は問題ない
# https://x1.inkenkun.com/archives/861
import numpy as np
 
n = int(input())
 
lr_array = np.zeros((n, 2))

for i in range(n):
    lr_array[i][0], lr_array[i][1] = map(int, input().split())

lr_array = np.sort(lr_array, axis=0)

l_list_new = [0 for _ in range(n)]
r_list_new = [0 for _ in range(n)]
 
cnt = 0
for i in range(len(lr_array)):
    if i==0:
        l_list_new[cnt] = lr_array[0,0]
        r_list_new[cnt] = lr_array[0,1]
    else:
        if lr_array[i,0] <= r_list_new[cnt] and lr_array[i,1] > l_list_new[cnt]:
            r_list_new[cnt] = lr_array[i,1]
        elif lr_array[i,0] <= r_list_new[cnt] and lr_array[i,1] <= l_list_new[cnt]:
            pass
        else: 
            l_list_new[cnt+1] = lr_array[i,0]
            r_list_new[cnt+1] = lr_array[i,1]
            cnt += 1
 
for i in range(cnt+1):
    print(int(l_list_new[i]), int(r_list_new[i]))
