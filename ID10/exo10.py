import math

def isPrime(val):
    flag = True
    for i in range(2,int(math.sqrt(val))+1):
        if val%i==0:
            flag = False
    return flag

sumPrimes = 5
i = 5

while i<int(2e6):
    if isPrime(i):
        sumPrimes += i
    if (i+1)%100==0:
        print i
    i += 2

print "The sum of all the prime numbers below two million is : ", sumPrimes