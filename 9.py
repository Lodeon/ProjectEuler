b = 2
end = 0

while end == 0:
    for a in range(1, b):
        c = (a**2 + b**2)**0.5
        if c%1 == 0 and (a + b + c) == 1000:
            print(a*b*c)
            end = 1
    b += 1
