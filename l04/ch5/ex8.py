#ex 8 ch 5
#ceasar chipher

def main():
    print("This programm is a ceaser chipher n")
    name = (input("enter a Name\n")).lower()
    key = int(input("Key: "))

    newN =""
    abc = "abcdefghijklmnopqrstuvwxyz"

    for ch in name:  
        newN = newN + abc[(ord(ch)-97) + (key % 52)] 

    print(newN)              

main()