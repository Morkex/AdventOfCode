file = "02\Input.txt"


def readFile(file):
    list = []
    f = open(file)
    for x in f:
        list.append(x.replace("\n", ""))
    f.close()
    return list


def listOfLists(list):
    lista = []
    for x in list:
        tupla = x.split(" ")
        lista.append(tupla)
    return lista


def calculaCoordenadas(lista):
    hori = 0
    depth = 0
    for x in lista:
        if(x[0]) == "forward":
            hori += int(x[1])

        if(x[0]) == "up":
            depth -= int(x[1])

        if(x[0]) == "down":
            depth += int(x[1])
    lista = [hori, depth]
    return lista


def calculaCoordenadasAim(lista):
    hori = 0
    depth = 0
    aim = 0
    for x in lista:
        if(x[0]) == "forward":
            hori += int(x[1])
            depth += aim*int(x[1])

        if(x[0]) == "up":
            #depth -= int(x[1])
            aim -= int(x[1])
        if(x[0]) == "down":
            #depth += int(x[1])
            aim += int(x[1])
    lista = [hori, depth]
    return lista


def multiplication(lista):
    return lista[0] * lista[1]


print("Part1: " + str(multiplication(calculaCoordenadas(listOfLists(readFile(file))))))
print("Part2: " + str(multiplication(calculaCoordenadasAim(listOfLists(readFile(file))))))

