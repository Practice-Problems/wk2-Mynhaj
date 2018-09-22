def sherlock(a , b):
    return len([i for i in range(a,b+1) if (i**0.5-int(i**0.5)==0)])
def encrypt(s):
    p = "".join(s.split(" "));
    rows = columns = int(len(p)**0.5)
    if (len(p)**0.5 - rows)>0: rows += 1;
    if (len(p)**0.5 - columns)>0.5: columns += 1;
    k = [p[i:rows+i] for i in range(0,len(p),rows)]
    p = [[k[i][j] for i in range(columns) if j < len(k[i])] for j in range(rows)]
    for i in p: print(''.join(i),end=' ')


