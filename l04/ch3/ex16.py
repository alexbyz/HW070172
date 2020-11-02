#exercise 16
#pi fibonacci

def main():
    print("this programm prints a fibonacci sequence\n")

    n = int(input("Which Fibonacci-number should be printed?:"))    

    f_old = 1
    f_new = 0

    for i in range(n):     
        sum = f_old + f_new        
        #f_old = f_new
        #f_new = sum
        f_old , f_new = f_new, sum

    print(f_new)
            
    input("Press a key to end the programm")
main()