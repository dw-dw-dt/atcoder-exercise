hw = [int(i) for i in input().split()]

cnt = 0
for c11 in range(1, min(hw[0]-2, hw[3]-2)+1):
    for c12 in range(1, min(hw[0] - c11 -1, hw[4]-2)+1):
        c13 = hw[0] - c11 - c12
        if c13 <= 0 or c13 > hw[5] - 2: continue
        for c21 in range(1, min(hw[1]-2, hw[3]-c11-1)+1):
            for c22 in range(1, min(hw[1]- c21 -1, hw[4]-c12-1)+1):
                c23 = hw[1] - c21 - c22
                if c23 <= 0 or c13 + c23 > hw[5] - 1: continue
                c31 = hw[3] - c11 - c21
                c32 = hw[4] - c12 - c22
                c33 = hw[5] - c13 - c23
                if c31 + c32 + c33 == hw[2]:
                    #print(c11,c12,c13,c21,c22,c23,c31,c32,c33)
                    cnt += 1
print(cnt)