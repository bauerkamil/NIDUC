from menu import Menu
import csv

fileName = "results.csv"
row = ['codeChoice','channel','msgLen','packetLen','probability','iterations','resendNum','mistakesApproved','ber','equalSend']
with open(fileName, 'w') as csvfile:
            # creating a csv writer object
    csvwriter = csv.writer(csvfile)

            # writing the data rows
    csvwriter.writerow(row)

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

    menu = Menu(msgLen, packetLen, probability, iterNum)

    print(' Chcesz kontynuować? [y/n]\n')
    yn = input("Wprowadz swoj wybor: ")
    
    if yn == 'n':
        continueBool = False
