def checkPrime(x):
    i = 2
    sqroot = x**0.5

    while i <= sqroot:
        if int(x % i) != 0:
            i = i+1
        else:
            return False
    return True

def main():
    n = int(input("enter a number "))

    primeList = []

    for i in range(2,n+1,1):
        primeList.append(i)

    i = 0

    while len(primeList) != 0:
        if checkPrime(primeList[i]) == True:
            #print(primeList[i])
            removedN = primeList[i]
            del primeList[i]
            i = i+1
                    
            try:
                for x in range(len(primeList)):
                    if primeList[x] % removedN == 0:
                        del primeList[x]    
            except:
                primeList     
                                   

main()