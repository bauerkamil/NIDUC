import numpy


class Receiver:

    def __init__(self, packets, n):
        self.packets = packets
        self.n = n

    def decoder_parity_bit(self):                       #bit parzystosci - dekodowanie
        is_correct = True
        for i in range(0, numpy.shape(self.packets)[0]):
            parity_bit = self.packets[i][self.n - 1]
            packet_str = str(self.packets[i])
            packet_str = packet_str[:-2]
            if packet_str.count("1") % 2 != parity_bit:
                is_correct = False
        return is_correct

    def decoder_check_sum(self):                       #suma kontrolna - dekodowanie
        check_sum_from_packets = self.packets[numpy.shape(self.packets)[0]-1]
        is_correct = True
        check_sum_int = 0

        for i in range(0, numpy.shape(self.packets)[0]-1):      #sumowanie pakietow
            packet_str = ""
            # print("REC: " + str(self.packets[i]))
            for j in range(0, self.n):
                packet_str = packet_str + str(self.packets[i][j])
            check_sum_int += int(packet_str, 2)

        check_sum_bin = bin(check_sum_int)                      #dodanie przeniesienia
        if len(check_sum_bin) > self.n:
            x = len(check_sum_bin)-self.n
            check_sum_bin = bin(int(check_sum_bin[0:x], 2) + int(check_sum_bin[x:], 2))[2:]
        if len(check_sum_bin) < self.n:
            check_sum_bin = '0'*(self.n - len(check_sum_bin)) + check_sum_bin

        check_sum_from_packets_str = ""                         #sprawdzenie sumy obliczonej z otrzymana
        for j in range(0, self.n):
            check_sum_from_packets_str = check_sum_from_packets_str + str(check_sum_from_packets[j])

        check_sum_bin = check_sum_bin.replace('0', 'a')
        check_sum_bin = check_sum_bin.replace('1', '0')
        check_sum_bin = check_sum_bin.replace('a', '1')
        if check_sum_bin != check_sum_from_packets_str:
                is_correct = False
        return is_correct

    def decoder_parity_bit_and_check_sum(self):                   #bit parzystości i suma konrtolna

        is_correct = True
        is_correct = self.decoder_check_sum()
        for i in range(0, numpy.shape(self.packets)[0]-1):
            parity_bit = self.packets[i][self.n - 1]
            packet_str = str(self.packets[i])
            packet_str = packet_str[:-2]
            if packet_str.count("1") % 2 != parity_bit:
                is_correct = False
        return is_correct