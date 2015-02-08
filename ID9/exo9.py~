import math

count = 0


def isPyt(a,b):
    global count
    if math.sqrt(a**2+b**2)%1==0:
        count += 1
        return True
    else:
        return False

a = 1
b = 1
c = 0
flag = False

for i in range(1,500):
    for j in range(1,500):
        if isPyt(a,b) and a+b+math.sqrt(a**2+b**2)==1000:
            c = int(math.sqrt(a**2+b**2))
            print "I broke the inner for loop!"
            flag = True
            break
        b += 1
    if flag:
        print "I broke the outer for loop!"
        break
    a += 1
    b = a + 1

print "a = ", a, "  b = ", b, "  c = ", c, "  a + b + c = ", a+b+c
print "a*b*c = ", a*b*c