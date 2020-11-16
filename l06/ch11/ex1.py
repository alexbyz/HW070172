
def getN():
    nums = []
    xStr = input("enter a number <Enter> to quit ")
    while xStr != "":
        x = float(xStr)
        nums.append(x)
        xStr = input("enter a number <Enter> to quit ")
    return nums

def mean(nums):
    total = 0.0
    for num in nums:
        total = total + num
    return total / len(nums)

def sdtDev(nums):
    sumDevSq = 0.0
    xbar = mean(nums)
    for num in nums:
        dev = xbar - num
        sumDevSq = sumDevSq + dev**2
    return (sumDevSq/(len(nums)-1))**0.5

def meanStdDev(nums):
    return mean(nums), sdtDev(nums)

def main():
    data = getN()
    mean, stdD = meanStdDev(data)
    print("mean: {0} stdDev: {1}".format(mean, stdD)) 
main()