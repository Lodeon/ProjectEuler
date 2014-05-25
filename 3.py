# Wade Polo
# Project Euler #3

count = 2
sumCount = 0
prime = 600851475143

while count <= prime:
    if prime%count == 0:
        prime = prime/count
        sumCount = count
    else:
        count += 1

print('The largest prime factor is:', sumCount)
