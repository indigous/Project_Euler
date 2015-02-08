def isPal(myStr):
    l = len(myStr)
    n = l/2
    flag = True
    for i in range(n):
        if myStr[i]==myStr[l-(1+i)]:
            pass
        else:
            flag = False
            break
    return flag

result = 0

n1 = 999
n2lim = 0
result = 0

while n1>n2lim:
    
    for n in range(n1,n2lim,-1):
        v = str(n1*n)
        l = len(v)
        if isPal(v):
            if int(v)>result:
                result = int(v)
            n2lim = n
            n1 -= 1
            break
    n1 -= 1
    

print result