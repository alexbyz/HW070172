#ex 7 ch 5
#ceasar chipher

def main():
    print("This programm is a ceaser chipher n")
    name = (input("enter a Name\n")).lower()
    key = int(input("Key: "))

    newN =""

    for ch in name:  
        newN = newN + chr((ord(ch)+key))  

    print(newN)              

main()