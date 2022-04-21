import numpy
import random

class Sender:

    def __init__(self, n, m, data):
        self.n = n
        self.m = m
        self.data = data

    def coder_parity_bit(self):                     #dodanie bitu parzytości do pakietów
        number_of_packets = int(numpy.ceil(self.m/(self.n-1)))
        data = self.data.reshape(number_of_packets, self.n-1)
        packets = numpy.arange(self.m + number_of_packets).reshape(number_of_packets, self.n)

        for i in range(0, number_of_packets):
            packet_str = str(data[i])
            packet = data[i]
            if packet_str.count("1") % 2:
                packet = numpy.append(packet, [1])
            else:
                packet = numpy.append(packet, [0])
            packets[i] = packet
        return packets

    def coder_check_sum(self, m, data):                         #dodanie sumy kontrolnej
        number_of_packets = int(numpy.ceil(m / self.n))
        data = data.reshape(number_of_packets, self.n)
        packets = numpy.arange(m + self.n).reshape(number_of_packets+1, self.n)
        check_sum_int = 0

        for i in range(0, number_of_packets):                       #sumowanie pakietow
            packet_str = ""
            # print("SEN: " + str(data[i]))
            for j in range(0, self.n):
                packet_str = packet_str + str(data[i][j])
            packets[i] = data[i]
            check_sum_int += int(packet_str, 2)

        check_sum_bin = bin(check_sum_int)                            #dodawanie przeniesienia
        if len(check_sum_bin) > self.n:
            x = len(check_sum_bin)-self.n
            check_sum_bin = bin(int(check_sum_bin[0:x], 2) + int(check_sum_bin[x:], 2))[2:]
        if len(check_sum_bin) < self.n:
            check_sum_bin = '0'*(self.n - len(check_sum_bin)) + check_sum_bin

        check_sum = numpy.array(list(check_sum_bin), dtype=int)        #zamiana bitów na przeciwne
        for x in range(0, len(check_sum_bin)):
            if check_sum[x] == 1:
                check_sum[x] = 0
            else: check_sum[x] = 1
        packets[number_of_packets] = check_sum
        return packets

    def coder_parity_bit_and_check_sum(self):                   #bit parzystości i suma konrtolna

        m = int(numpy.ceil(self.m / (self.n - 1))) + self.m
        return self.coder_check_sum(m, self.coder_parity_bit())
