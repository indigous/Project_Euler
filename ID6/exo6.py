sqSum = (sum(range(1,101)))**2
sumSq = sum([a*b for a,b in zip(range(1,101),range(1,101))])

print "sqSum = ", sqSum, "  sumSq = ", sumSq, "    sum = ", sqSum-sumSq