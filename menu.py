import komm
import numpy
from Sender import Sender
from Receiver import Receiver
from Chanel import Chanel
from Generator import Generator


class Menu:

    def __init__(self, msgLen, packetLen, probability, numOfIter):
        self.msgLen = msgLen  # bit message length
        self.packetLen = packetLen  # packet length
        self.probability = probability  # probability
        self.numOfIter = numOfIter  # number of iterations
        self.data = [0]
        self.packets = [0]

        print(' 1.Bit parzystosci\n 2.Suma kontrolna\n 3.Bit parzystosci i suma kontrolna\n')
        self.choice = int(input("Wprowadz swoj wybor: "))

        print(' 1.BSC\n 2.BEC\n 3.BSC i BEC\n')
        self.choice2 = int(input("Wprowadz swoj wybor: "))

        self.generator = Generator(self.msgLen)

        self.sender = Sender(self.packetLen, self.msgLen, self.data)
        self.chanel = Chanel(self.packets, self.probability)
        self.receiver = Receiver(self.packets, self.packetLen)

        self._sendNew_()

    def _sendNew_(self):
        self.sender.data = self.generator.generate_data()  # generowanie ciągu 0 i 1

    def _send_(self):
        self.packets = self._encode_()

        print("Wyslany:")
        print(self.packets)

        self.chanel.packets = self.packets
        self._addNoise_() # zaklocenia

        print("Otrzymany:")
        print(self.packets)

        self.receiver.packets = self.packets
        answear = self._decode_()
        if answear:
            print("Odpowiedz: Zaakceptowano")
        else:
            print("Odpowiedz: Odrzucono")
            self._send_()

    def _encode_(self):
        if self.choice == 1:
            return self.sender.coder_parity_bit()
        if self.choice == 2:
            return self.sender.coder_check_sum(self.msgLen, self.data)
        if self.choice == 3:
            return self.sender.coder_parity_bit_and_check_sum()

    def _addNoise_(self): 
        if self.choice2 == 1:
            for i in range(0, numpy.shape(self.chanel.packets)[0]):
                self.packets[i] = self.chanel.BSC(
                    self.chanel.p, self.chanel.packets[i])

        if self.choice2 == 2:
            for i in range(0, numpy.shape(self.chanel.packets)[0]):
                self.packets[i] = self.chanel.BEC(
                    self.chanel.p, self.chanel.packets[i])

        else:
            for i in range(0, numpy.shape(self.chanel.packets)[0]):
                self.packets[i] = self.chanel.BSC(
                    self.chanel.p, self.chanel.packets[i])
            for i in range(0, numpy.shape(self.chanel.packets)[0]):
                self.packets[i] = self.chanel.BEC(
                    self.chanel.p, self.chanel.packets[i])

    def _decode_(self):
        if self.choice == 1:
            return self.receiver.decoder_parity_bit()
        if self.choice == 2:
            return self.receiver.decoder_check_sum()
        if self.choice == 3:
            return self.receiver.decoder_parity_bit_and_check_sum()
        # dekodowanie
