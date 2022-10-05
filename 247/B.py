n = int(input())
st = [input().split() for _ in range(n)]

is_available = True
for i in range(n):
    si_available = True
    ti_available = True
    si, ti = st[i]
    for j in range(n):
        if j == i: continue
        if si in st[j]:
            si_available = False
            break
    if si_available:
        pass
    else:
        for j in range(n):
            if j == i: continue
            if ti in st[j]:
                ti_available = False
                break
    if not si_available and not ti_available:
        is_available = False
        break

print('Yes' if is_available else 'No')