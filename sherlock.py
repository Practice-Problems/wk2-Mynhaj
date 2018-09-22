def sherlock(a , b):
    return len([i for i in range(a,b+1) if (i**0.5-int(i**0.5)==0)])
def encrypt(s):
    p = "".join(s.split(" "));
    rows = 0;
    columns = 0;
    w = len(p)**0.5
    if (w - int(w))>0:
        columns = int(w);
        rows = columns + 1;
    return [p[i:rows+i] for i in range(0,len(p),rows)]

    
        
        
    
    
