sumSq = 0
sqSum = 0

for i in range(101):
    sumSq += i**2
    sqSum += i

print((sqSum**2)-sumSq)
