#exercise 15
#pi aproximation

def main():
    print("this programm finds an approximation of pi\n")

    n = int(input("how many numbers should the approximation sum up?:"))    
    sum = 0

    for i in range(1,n+1,4):    #the sum has to alternate with + and - 
        sum = sum + (4/i)       #the loop counts 1,5,9,...
        sum = sum - (4/(i+2))   #the sumbtraction modifies the interation count to 1+2=3,5+2=7,9+2=11
               
    print("the approximation of pi is ", sum)

    input("Press a key to end the programm")
main()