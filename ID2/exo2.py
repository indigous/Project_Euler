fibim1 = 2
fibim2 = 1
sum = 2

while True:
    fibi = fibim1 + fibim2
    fibim2 = fibim1
    fibim1 = fibi
    
    if fibi>4e6:
        break
    
    if fibi%2==0:
        sum += fibi

print sum