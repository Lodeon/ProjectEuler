def primeCheck(sentNum):
    for num in range(3,int(sentNum**0.5)+1,2):
        if sentNum%num == 0:
            return False
    return True

def main():
    prime = 11
    primeSum = 0
    primeList = [2, 3, 5, 7]
    while prime < 2000000:
        if primeCheck(prime) is True:
            primeList.append(prime)
        prime += 2
    print(sum(primeList))
    
main()
