# テクニック型: parity
n = int(input())
prev_t = 0
prev_x = 0
prev_y = 0
is_available = True
for i in range(n):
    t, x, y = map(int, input().split())
    if abs(x - prev_x) + abs(y - prev_y) > t - prev_t or (abs(x - prev_x) + abs(y - prev_y))%2 != (t - prev_t)%2:
        is_available = False
    prev_x = x
    prev_y = y
    prev_t = t
if is_available:
    print("Yes")
else:
    print("No")