def main():
    target = int(input("What is the number your would like to factor? "))
    #target = 600851475143
    factorNum = 2
    primeNumbers = []

    while(target>1):
        if target % factorNum == 0:
            primeNumbers.append(factorNum)
            target = target/factorNum
        else:
            factorNum += 1
    print(primeNumbers)    

main()
