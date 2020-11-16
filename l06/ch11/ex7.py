def innerP(list1, list2):
    product = []
    if len(list1) == len(list2):
        for i in range(len(list1)):
            product.append(list1[i]*list2[i])
        return product
    else:
        return False

def main():
    list1 = [1,2,4,5,6,7,3,5]
    list2 = [2,34,12,43,54,4,6,23]

    print("inner Product is: ", innerP(list1,list2))

main()