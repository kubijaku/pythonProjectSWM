import math


def isPrime(number):  # Works for number > 0, in our example min number of occuring is 1
    maximumDivisor = int(math.sqrt(number)) + 1
    if number == 1:
        return False
    for i in range(2, maximumDivisor):
        if number % i == 0:
            return False
    return True


def checkRequirements(list):
    numberOfEachNumber = dict()
    for i in list:
        if i in numberOfEachNumber.keys():
            counter = numberOfEachNumber.get(i)
            counter = counter + 1
            numberOfEachNumber.update({i: counter})
        else:
            numberOfEachNumber.update({i: 1})

    listOfFinalNumbers = []
    for i in numberOfEachNumber.keys():
        if isPrime(numberOfEachNumber.get(i)):
            listOfFinalNumbers.append(i)

    return listOfFinalNumbers


if __name__ == '__main__':
    A = [2, 3, 9, 2, 5, 1, 3, 7, 10]
    B = [2, 1, 3, 4, 3, 10, 6, 6, 1, 7, 10, 10, 10]
    # C = [2, 9, 2, 5, 7, 10]
    listOfNumbersAchivingRequirements = checkRequirements(B)
    C2 = []
    for i in A:
        if i not in listOfNumbersAchivingRequirements:
            C2.append(i)

    print("List A: ")
    print(A)
    print("List B: ")
    print(B)
    print("List C: ")
    print(C2)
