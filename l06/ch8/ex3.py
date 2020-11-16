#futval.py
#future investments
#by Alexander Huber
#ex6, ex7, ex8

def futval(inV, apr):

    principal = inV
    initial = principal

    principal = principal * (1 + apr) 
    return principal

def main():

    inV = 10
    apr = 0.03
    acc = inV
    i = 0

    while acc < inV*2:
        acc = futval(acc, apr)
        i = i + 1
    
    print("it takes {0}years to double".format(i))
    

main()