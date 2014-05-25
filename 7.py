def primeCheck(sentPrime):
    for i in range(3,int(sentPrime**0.5)+1,2):
        if sentPrime%i == 0:
            return False
    return True

def main():
    count = 4 # Start count one step back due to location of +=
    prime = 11 # Start 5th prime due to lower primes' problems with above
    while count < 10002:
        if primeCheck(prime) is True:
            count += 1
            if count == 10001:
                print(prime)
                return
            else:
                prime += 2
        else:
            prime += 2
    
main()
