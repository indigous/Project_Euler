myList = []

def divs(n):
    global myList
    i = 2
    while True:
        if n%i==0:
            myList.append(i)
            return n/i
        else:
            i += 1   

n = 600851475143

while True:
    val = divs(n)
    if val==1:
        break
    else:
        n = val

print max(myList)
    