N = input()
a_list = list(map(int, input().split()))

i = 0
while all([i%2 == 0 for i in a_list]):
    a_list = [a // 2 for a in a_list]
    i += 1

print(i)
