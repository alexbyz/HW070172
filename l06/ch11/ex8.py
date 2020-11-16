import random

def getData():
    nums = []
    xStr = input("enter data or <Enter> to quit ")
    while xStr != "":
        x = xStr
        nums.append(x)
        xStr = input("enter data or <Enter> to quit ")
    return nums

def count(myList, x):
    c = 0
    for i in myList:
        if i == x:
            c = c+1
    return c

def isin(myList, x):
    if count(myList, x) != 0:
        return True
    else:
        return False

def index(myList, x):
    c = 0
    for i in myList:
        if i == x:
            return c
        c = c + 1
    return False

def reverse(myList):
    revList = []
    for entry in range(len(myList)-1,-1,-1):
        revList.append(myList[entry])
    return revList

def sort(myList):
    sortList = []
    bufferList = myList
    for i in range (len(bufferList)):
        x = min(bufferList)
        sortList.append(x)
        bufferList.remove(x)
    return sortList

def shuffle(myList):
    shuffeledList = []
    for i in range(len(myList)):
        shuffeledList.append(False)

    i = 0

    while isin(shuffeledList, False):
        r = random.randrange(0,len(myList),1)
        if shuffeledList[r] == False:
            shuffeledList[r] = myList[i]
            i = i + 1
    return shuffeledList

def removeDup(myList):
    trimmedList = []

    for i in range(len(myList)):
        if isin(trimmedList, myList[i]) == False:
            trimmedList.append(myList[i])
       
    return trimmedList


def main():

    data =getData()
    
    countCar = 'a'

    #print("{0} in date is {1}".format(countCar, isin(data, countCar)))
    #print("the first index of {0} is {1}".format(countCar, index(data, countCar)))
    #print("the entered date contained {0} times the element {1}".format(count(data, countCar), countCar))
    #print(reverse(data))
    #print(sort(data))
    #print(shuffle(data))
    print(removeDup(data))

main()
