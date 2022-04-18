import komm
import numpy

from Generator import Generator


class Chanel:

    def __init__(self, packets, p):
        self.packets = packets
        self.p = p

    def BSC(self, p, packet):
        bsc = komm.BinarySymmetricChannel(p)
        return bsc(packet)

    def BEC(self, p, packet):
        bec = komm.BinaryErasureChannel(p)
        bec_packet = bec(packet)

        for i in range(len(bec_packet)):
            bec_packet[i] %= 2
        return bec_packet

    def data_transmission(self):
        packets_with_noise = self.packets
        for i in range(0, numpy.shape(self.packets)[0]):
            packets_with_noise[i] = self.BSC(self.p, self.packets[i])
            print("BSC: " + str(packets_with_noise[i]))
            packets_with_noise[i] = self.BEC(self.p, self.packets[i])
            print("BEC: " + str(packets_with_noise[i]))