# 逆引き辞書

N,Q = map(int,input().split())
 
number = [0] * (N+1)
idx = [0] * (N+1)
for i in range(1,N+1):
    number[i] = i #インデックスが入るリスト
    idx[i] = i #値が入るリスト
 
for i in range(Q):
    x = int(input())
    cnt_idx = number[x] #xのインデックス
 
    if cnt_idx <N:
        next_idx = cnt_idx + 1
        cnt_number = idx[next_idx] #xの移動先にあった数字
        number[x] = next_idx #xの移動先のindex
        idx[next_idx] = x
        number[cnt_number] = cnt_idx
        idx[cnt_idx] = cnt_number
    
    if cnt_idx == N:
        next_idx = cnt_idx - 1
        cnt_number = idx[next_idx] #xの移動先にあった数字
        number[x] = next_idx
        idx[next_idx] = x
        number[cnt_number] = cnt_idx
        idx[cnt_idx] = cnt_number
 
ans = []
 
for i in range(1,N+1):
    ans.append(idx[i])
 
print(*ans)