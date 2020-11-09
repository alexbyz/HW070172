#exercise 7
#pi fibonacci

def fib(n):
    f_old = 1
    f_new = 0

    for i in range(n):     
        sum = f_old + f_new        
        f_old , f_new = f_new, sum
    return sum

def main():
    print("this programm prints a fibonacci sequence\n")

    n = int(input("Which Fibonacci-number should be printed?:"))  

    print(fib(n))
            
    input("Press a key to end the programm")
main()