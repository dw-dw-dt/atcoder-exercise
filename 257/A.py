n, x = map(int, input().split())

d, m = divmod(x, n)
a_list = [chr(i) for i in range(65, 65+26)]

if m == 0:
    print(a_list[d-1])
else:
    print(a_list[d])
