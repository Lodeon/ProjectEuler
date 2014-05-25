step = 3
end = 0
x = 3

while end == 0:
    if step == 20:
        print(x)
        end = 1
    elif x%step == 0:
        step += 1
    else:
        if step%2 == 0:
            x = x*2
        elif step%3 == 0:
            x = x*3
        else:
            x = x*step
