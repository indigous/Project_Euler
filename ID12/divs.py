__author__ = 'inigo'

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


def listOfFactors(n):
    global myList
    myList = []
    while True:
        val = divs(n)
        if val == 1:
            break
        else:
            n = val
    return myList


def numberOfDivs(ls):
    oldValue = 0
    listExp = []
    for i in ls:
        if i == oldValue:
            pass
        else:
            listExp.append(ls.count(i)+1)
        oldValue = i
    nbdivs = 1
    for x in listExp:
        nbdivs *= x
    return nbdivs


trian = 0
ndivs = 0
tempMax = 0
count = 1
while ndivs <= 500:
    trian += count
    count += 1
    listFactors = listOfFactors(trian)
    ndivs = numberOfDivs(listFactors)
    if ndivs > tempMax:
        print "triangular number = ", trian, "  -->  number of divisors = ", ndivs
        tempMax = ndivs




