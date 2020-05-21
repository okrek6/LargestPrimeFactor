import time

def main():
    startTime = time.time()
    target = 600851475143
    factorNum = 2
    primeNumbers = []

    while(target>1):
        if target % factorNum == 0:
            primeNumbers.append(factorNum)
            target = target/factorNum
        else:
            factorNum += 1
    print(primeNumbers)
    print('{} seconds completed' .format(time.time() - startTime))

main()
