import math

def primality(number):
    temp = int(math.sqrt(number)) + 1
    if number == 1:
        return False
    for i in range(2, temp):
        if number % i == 0:
            return False
    return True

def listFromB(list):
    numberOfnumbers = dict()
    for i in list:
        if i in numberOfnumbers.keys():
            counter = numberOfnumbers.get(i)
            counter = counter + 1
            numberOfnumbers.update({i: counter})
        else:
            numberOfnumbers.update({i: 1})

    listOfPrimalityNumbers = []
    for i in numberOfnumbers.keys():
        if primality(numberOfnumbers.get(i)):
            listOfPrimalityNumbers.append(i)

    return listOfPrimalityNumbers

if __name__ == '__main__':
    A = [2, 3, 9, 2, 5, 1, 3, 7, 10]
    B = [2, 1, 3, 4, 3, 10, 6, 6, 1, 7, 10, 10, 10]
    # C = [2, 9, 2, 5, 7, 10]
    listOfPrimalityNumbers = listFromB(B)
    C2 = []
    for i in A:
        if i not in listOfPrimalityNumbers:
            C2.append(i)

    print("List A: ")
    print(A)
    print("List B: ")
    print(B)
    print("List C: ")
    print(C2)

