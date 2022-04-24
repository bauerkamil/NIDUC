from menu import Menu

continueBool = True

while continueBool:

    print(' Wprowadź długość wiadomości\n')
    msgLen = int(input("Wprowadz swoj wybor: "))

    print(' Wprowadź długość pakietu\n')
    packetLen = int(input("Wprowadz swoj wybor: "))

    print(' Wprowadź prawdopodobieństwo\n')
    probability = float(input("Wprowadz swoj wybor: "))

    print(' Wprowadź ilość iteracji\n')
    iterNum = int(input("Wprowadz swoj wybor: "))


    menu = Menu(msgLen,packetLen,probability,iterNum)

    print(' Chcesz kontynuować? [y/n]\n')
    yn = input("Wprowadz swoj wybor: ")
    if yn=='n':
        continueBool=False