myList = []


def divs(n):
    global myList
    if n == 1:
        myList.append(1)
        return 1
    i = 2
    while True:
        if n % i == 0:
            myList.append(i)
            return n/i
        else:
            i += 1


trian = 0
count = 1

while True:
    trian += count
    count += 1
    n = trian
    while True:
        val = divs(n)
        if val == 1:
            myList.append(1)
            break
        else:
            n = val
    print "Triangular number = ", trian
    print "List of factors = ", myList, "\n"
    myList = []
    if count > 10:
        break
