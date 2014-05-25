# Wade Polo
# Project Euler #1

count = 0
sumCount = 0

while count < 999:
    count += 1
    if count%3 == 0 or count%5 == 0:
        sumCount += count

print('The sum is:', sumCount)
