from calendar import c


a = int(input())
b = int(input())
c = int(input())
x = int(input())

cnt = 0
for a_i in range(0, a+1):
    for b_i in range(0, b+1):
        for c_i in range(0, c+1):
            if a_i*500 + b_i*100 + c_i*50 == x:
                cnt += 1
print(cnt)