s1 = input()
s2 = input()
s3 = input()
s4 = input()
s5 = input()
s6 = input()
s7 = input()
s8 = input()
s9 = input()
s10 = input()

A = 0
B = 0
C = 0
D = 0

row = 'a'

for i in range(10):
    if '#' in s1:
        A = 1
        row = s1
        break
    elif '#' in s2:
        A = 2
        row = s2
        break
    elif '#' in s3:
        A = 3
        row = s3
        break
    elif '#' in s4:
        A = 4
        row = s4
        break
    elif '#' in s5:
        A = 5
        row = s5
        break
    elif '#' in s6:
        A = 6
        row = s6
        break
    elif '#' in s7:
        A = 7
        row = s7
        break
    elif '#' in s8:
        A = 8
        row = s8
        break
    elif '#' in s9:
        A = 9
        row = s9
        break
    elif '#' in s10:
        A = 10
        row = s10
        break

for i in range(10):
    if '#' in s10:
        B = 10
        break
    elif '#' in s9:
        B = 9
        break
    elif '#' in s8:
        B = 8
        break
    elif '#' in s7:
        B = 7
        break
    elif '#' in s6:
        B = 6
        break
    elif '#' in s5:
        B = 5
        break
    elif '#' in s4:
        B = 4
        break
    elif '#' in s3:
        B = 3
        break
    elif '#' in s2:
        B = 2
        break
    elif '#' in s1:
        B = 1
        break

for i, item in enumerate(list(row)):
    if item == '#':
        C = i + 1
        break

for i, item in enumerate(reversed(list(row))):
    if item == '#':
        D = 10 - i
        break
        

print(f'{A} {B}')
print(f'{C} {D}')