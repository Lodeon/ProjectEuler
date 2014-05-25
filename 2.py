# Wade Polo
# Project Euler #2

x, y = 1, 2
sumCount = 0

while y <= 4000000:
    if y%2 == 0:
        sumCount += y
    x, y = y, x+y

print('The sum is:', sumCount)
