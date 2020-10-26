#ex12.py
#calculator
#by Alexander Huber
#exercises 12

def main():
    total = eval(input("how many calcualtions do you want to make? "))
    for i in range(total):
        print("enter an expression to be calculated:\t") 
        ans = eval(input())   
        print(ans)
    input("press any key to end the program\n")
main()