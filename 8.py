def readFile(txt):
    infile = open(txt, 'r')
    digits = infile.read().replace('\n', '')
    infile.close()
    return digits

def main():
    lrgst = 0
    count = 1
    prod = 1
    lst = readFile('1000Digits.txt')
    while count < len(lst):
        num = lst[count:(count+13)]
        for i in num:
            prod *= int(i)
        if prod > lrgst:
            lrgst = prod
        prod = 1
        count += 1
    print(lrgst)

main()
