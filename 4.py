p1 = 999
p2 = 999
answer = 0

while p2 > 99:
    p3 = p1*p2
    p4 = str(p3)
    if str(p3) == p4[::-1] and p3 > answer:
            answer = p3
    if p1 == 100:
        p1 = 999
        p2 -= 1
    else:
        p1 -= 1

print('The palindrome is:', answer)
