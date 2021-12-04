import builtins


file = "03\Input.txt"


def readFile(file):
    list = []
    f = open(file)
    for x in f:
        list.append(x.replace("\n", ""))
    f.close()
    return list


def separateBitsList(listi):
    lista = []
    for x in listi:
        lista.append(list(x))
    return lista


def mostCommonBit(list, columna):
    bit = 0
    apariciones1 = 0
    for x in list:
        if(x[columna] == 1):
            apariciones1 += 1
    if(apariciones1 > len(list)/2):
        bit = 1
    else:
        bit = 0
    return bit

def generateGamma(list):
    gamma = ""
    
    return gamma

print(mostCommonBit(separateBitsList(readFile(file)),0))
