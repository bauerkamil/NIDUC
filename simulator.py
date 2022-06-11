import komm
import numpy
import sys
sys.setrecursionlimit(10000)
from Sender import Sender
from Receiver import Receiver
from Chanel import Chanel
from Generator import Generator
from resultsToFile import ResultsToFile


class Simulator:

    def __init__(self, msgLen, probability, numOfIter):
        self.msgLen = msgLen  # bit message length
        self.packetLen = 20  # packet length
        self.checksumLen = int(self.packetLen/4)
        self.numOfPackets = int(msgLen/self.packetLen)
        self.probability = probability  # probability
        self.numOfIter = numOfIter  # number of iterations
        self.data = []
        self.originalPackets = []
        self.sentPackets = []

        print(
            ' 1.Bit parzystosci\n 2.Suma kontrolna\n')
        choice1 = int(input("Wprowadz swoj wybor: "))
        if choice1 == 1:
            self.codeChoice = "parity_bit"
            self.packetLen += 1
        elif choice1 == 2:
            self.codeChoice = "check_sum"
            self.packetLen += self.checksumLen
        else:
            print('Wrong choice')
            return

        print(' 1.BSC\n 2.BEC\n 3.BSC i BEC\n')
        choice2 = int(input("Wprowadz swoj wybor: "))
        if choice2 == 1:
            self.channelChoice = "BSC"
        elif choice2 == 2:
            self.channelChoice = "BEC"
        elif choice2 == 3:
            self.channelChoice = "BSC_BEC"
        else:
            print('Wrong choice')
            return

        self.csvWriter = ResultsToFile(
            self.codeChoice, self.channelChoice, msgLen, self.packetLen, probability, numOfIter)

        self.generator = Generator(self.msgLen)

        self.sender = Sender(self.packetLen, self.msgLen, self.numOfPackets, self.checksumLen, self.data)
        self.chanel = Chanel(self.originalPackets, self.probability)
        self.receiver = Receiver(self.packetLen, self.checksumLen)

        for i in range(0, self.numOfIter):
            self._sendNew_()
            print(i)


    def _sendNew_(self):
        self.sender.data = self.generator.generate_data()  # generowanie ciągu 0 i 1
        
        self.originalPackets = self._encode_()
        # print(self.originalPackets)
        self.csvWriter.originalPackets = self.originalPackets

        self.sentPackets = self.originalPackets.copy()
        self.receiver.packets = self.sentPackets

        for i in range(0, self.numOfPackets):
            self._send_(i)
        
        self.csvWriter._printToCsv_(self.sentPackets)


    def _send_(self, packetNum):
        # print("Wysłany:")
        # print(self.originalPackets[packetNum])

        # self.chanel.packets = self.originalPackets

        self.csvWriter._addRep_()

        self._addNoise_(packetNum)  # zaklocenia

        # print("Otrzymany:")
        # print(self.sentPackets[packetNum])

        self.receiver.packets[packetNum] = self.sentPackets[packetNum]

        answear = self._decode_(packetNum)
        
        if answear == False:
            self._send_(packetNum)


    def _encode_(self):
        if self.codeChoice == "parity_bit":
            return self.sender.coder_parity_bit()
        if self.codeChoice == "check_sum":
            return self.sender.coder_check_sum()

    def _addNoise_(self, packetNum):
        if self.channelChoice == "BSC":
            self.sentPackets[packetNum] = self.chanel.BSC(self.probability, self.sentPackets[packetNum])

        if self.channelChoice == "BEC":
            self.sentPackets[packetNum] = self.chanel.BEC(self.probability, self.sentPackets[packetNum])

        if self.channelChoice == "BSC_BEC":
            self.sentPackets[packetNum] = self.chanel.BSC(self.probability, self.sentPackets[packetNum])
            self.sentPackets[packetNum] = self.chanel.BEC(self.probability, self.sentPackets[packetNum])


    def _decode_(self, packetNum):
        if self.codeChoice == "parity_bit":
            return self.receiver.decoder_parity_bit(packetNum)
        if self.codeChoice == "check_sum":
            return self.receiver.decoder_check_sum(packetNum)
        # dekodowanie
