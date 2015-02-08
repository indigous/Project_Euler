def isPrime(val):
    flag = True
    for i in range(2,val):
        if val%i==0:
            flag = False
    return flag

primesList = []
cnt = 2
while True:
    if isPrime(cnt):
        primesList.append(cnt)
    if len(primesList)==10001:
        break
    cnt += 1
    
print primesList, "\n\n\n"
print primesList[-1]