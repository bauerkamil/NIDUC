import komm
import numpy
from Sender import Sender
from Receiver import Receiver
from Chanel import Chanel
from Generator import Generator
from resultsToFile import ResultsToFile


class Menu:

    def __init__(self, msgLen, packetLen, probability, numOfIter):
        self.msgLen = msgLen  # bit message length
        self.packetLen = packetLen  # packet length
        self.probability = probability  # probability
        self.numOfIter = numOfIter  # number of iterations
        self.data = []
        self.packets = []

        print(
            ' 1.Bit parzystosci\n 2.Suma kontrolna\n 3.Bit parzystosci i suma kontrolna\n')
        choice1 = int(input("Wprowadz swoj wybor: "))
        if choice1 == 1:
            self.codeChoice = "parity_bit"
            # self.packetLen=self.packetLen-1
        elif choice1 == 2:
            self.codeChoice = "check_sum"
        elif choice1 == 3:
            self.codeChoice = "parity_bit_check_sum"
            # self.packetLen=self.packetLen+1
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
            self.codeChoice, self.channelChoice, msgLen, packetLen, probability, numOfIter)

        self.generator = Generator(self.msgLen)

        self.sender = Sender(self.packetLen, self.msgLen, self.data)
        self.chanel = Chanel(self.packets, self.probability)
        self.receiver = Receiver(self.packets, self.packetLen)

        for i in range(0,self.numOfIter):
            self._sendNew_()

    def _sendNew_(self):
        self.sender.data = self.generator.generate_data()  # generowanie ciągu 0 i 1

        self._send_()

    def _send_(self):
        self.packets = self._encode_()

        # print("Wyslany:")
        # print(self.packets)

        self.chanel.packets = self.packets
        self.csvWriter.sentPackets = self.packets.copy()

        self._addNoise_()  # zaklocenia

        # print("Otrzymany:")
        # print(self.packets)

        self.receiver.packets = self.packets
        answear = self._decode_()
        if answear:
            self.csvWriter._printToCsv_(self.packets)
            # print("Odpowiedz: Zaakceptowano")

        else:
            # print("Odpowiedz: Odrzucono")
            self.csvWriter._addRep_()
            self._send_()

    def _encode_(self):
        if self.codeChoice == "parity_bit":
            return self.sender.coder_parity_bit()
        if self.codeChoice == "check_sum":
            return self.sender.coder_check_sum(self.msgLen, self.data)
        if self.codeChoice == "parity_bit_check_sum":
            return self.sender.coder_parity_bit_and_check_sum()

    def _addNoise_(self):
        if self.channelChoice == "BSC":
            for i in range(0, numpy.shape(self.chanel.packets)[0]):
                self.packets[i] = self.chanel.BSC(
                    self.chanel.p, self.chanel.packets[i])

        if self.channelChoice == "BEC":
            for i in range(0, numpy.shape(self.chanel.packets)[0]):
                self.packets[i] = self.chanel.BEC(
                    self.chanel.p, self.chanel.packets[i])

        if self.channelChoice == "BSC_BEC":
            for i in range(0, numpy.shape(self.chanel.packets)[0]):
                self.packets[i] = self.chanel.BSC(
                    self.chanel.p, self.chanel.packets[i])
            for i in range(0, numpy.shape(self.chanel.packets)[0]):
                self.packets[i] = self.chanel.BEC(
                    self.chanel.p, self.chanel.packets[i])

    def _decode_(self):
        if self.codeChoice == "parity_bit":
            return self.receiver.decoder_parity_bit()
        if self.codeChoice == "check_sum":
            return self.receiver.decoder_check_sum()
        if self.codeChoice == "parity_bit_check_sum":
            return self.receiver.decoder_parity_bit_and_check_sum()
        # dekodowanie
