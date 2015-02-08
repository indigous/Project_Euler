__author__ = 'inigo'

import numpy as np

matrixNumbers = np.zeros((100, 50), dtype=np.int)
cnt = 0

with open("numbers.dat", 'r') as numFile:  # Opens the file
    for line in numFile:
        for i in range(50):
            matrixNumbers[cnt, i] = int(line[i])
        cnt += 1


solution = np.zeros(50, dtype=np.int)
carr = 0
for i in range(49, -1, -1):
    if i != 0:
        add = sum(matrixNumbers[:, i]) + carr
        solution[i] = add%10
        carr = add/10
    else:
        solution[i] = sum(matrixNumbers[:, i]) + carr

solutionString = ''
for i in range(50):
    solutionString += str(solution[i])

print solutionString[0:10]

