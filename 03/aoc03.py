file = "03\Input.txt"


def readFile(file):
    list = []
    f = open(file)
    for x in f:
        list.append(x.replace("\n", ""))
    f.close()
    return list


def separateBitsList(listaCompleta):
    listaDeListas = []
    for x in listaCompleta:
        listaDeListas.append(list(x))
    return listaDeListas


def listaDeColumnas(listadeListas, columna):
    listaDeColumna = []
    for x in listadeListas:
        listaDeColumna.append(x[columna])
    return listaDeColumna


def mostCommonBit(listaDeColumna):
    bitMasComun = ""
    if(listaDeColumna.count("0") > listaDeColumna.count("1")):
        bitMasComun = "0"
    if(listaDeColumna.count("0") < listaDeColumna.count("1")):
        bitMasComun = "1"
    return bitMasComun


def leastCommonBit(listaDeColumna):
    bitMenosComun = ""
    if(listaDeColumna.count("0") < listaDeColumna.count("1")):
        bitMenosComun = "0"
    if(listaDeColumna.count("0") > listaDeColumna.count("1")):
        bitMenosComun = "1"
    return bitMenosComun


def generateGammaBits(listaDeListas):
    gamma = ""
    columna = 0
    for columna in listaDeListas[0]:
        gamma += mostCommonBit(listaDeColumnas(listaDeListas, int(columna)))
    return gamma[::-1]


def generateEpsilonBits(listaDeListas):
    epsilon = ""
    columna = 0
    for columna in listaDeListas[0]:
        epsilon += leastCommonBit(listaDeColumnas(listaDeListas, int(columna)))
    return epsilon[::-1]


listaFile = readFile(file)
listaDeListasFile = separateBitsList(listaFile)

print(generateGammaBits(listaDeListasFile))
print(generateEpsilonBits(listaDeListasFile))

print(int(generateGammaBits(listaDeListasFile), 2))
print(int(generateEpsilonBits(listaDeListasFile), 2))

print(int(generateGammaBits(listaDeListasFile), 2) *
      int(generateEpsilonBits(listaDeListasFile), 2))
print("Tiene que dar 4118544")
