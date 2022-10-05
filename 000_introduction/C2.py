s = input()

is_removable = True
while is_removable:
    if len(s) >= 7 and s[-7:] == 'dreamer':
        s = s[:-7]
    elif len(s) >= 6 and s[-6:] == 'eraser':
        s = s[:-6]
    elif len(s) >= 5 and s[-5:] in ('dream', 'erase'):
        s = s[:-5]
    else:
        is_removable = False

if len(s) == 0:
    print('YES')
else:
    print('NO')
