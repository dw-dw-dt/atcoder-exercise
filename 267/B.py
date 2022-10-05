s = list(input())

s = { i+1: v for i, v in enumerate(s) }

def is_split(s):
    if s[1] == '1': return False
    col1 = '1' if s[7] == '1' else '0'
    col2 = '1' if s[4] == '1' else '0'
    col3 = '1' if s[2] == '1' or s[8] == '1' else '0'
    col4 = '1' if s[5] == '1' else '0'
    col5 = '1' if s[3] == '1' or s[9] == '1' else '0'
    col6 = '1' if s[6] == '1' else '0'
    col7 = '1' if s[10] == '1' else '0'
    if col2 == '0' and col1 == '1' and ('1' in [col3, col4, col5, col6, col7]):
        return True
    elif col3 == '0' and ('1' in [col1, col2]) and ('1' in [col4, col5, col6, col7]):
        return True
    elif col4 == '0' and ('1' in [col1, col2, col3]) and ('1' in [col5, col6, col7]):
        return True
    elif col5 == '0' and ('1' in [col1, col2, col3, col4]) and ('1' in [col6, col7]):
        return True
    elif col6 == '0' and ('1' in [col1, col2, col3, col4, col5]) and col7 == '1':
        return True
    else: False

if is_split(s):
    print('Yes')
else:
    print('No')