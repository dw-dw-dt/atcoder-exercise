n, a, b = map(int, input().split())

out = "."*b
for k in range(1, n+1):
    if k % 2 == 1:
        if k != 1: out += "."*b
        for j in range(1, a+1):
            if j > 1: out += "."*b
            for i in range(1, n+1):
                if i == 1: continue
                elif i % 2 == 0: 
                    out += "#"*b
                else: 
                    out += "."*b
            out += "\n"
    else:
        out += "#"*b
        for j in range(1, a+1):
            if j > 1: out += "#"*b
            for i in range(1, n+1):
                if i == 1: continue
                elif i % 2 == 0: 
                    out += "."*b
                else: 
                    out += "#"*b
            out += "\n"
if len(out) > 2: out = out[:-1]
print(out)
    
        
