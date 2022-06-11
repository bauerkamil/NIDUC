import numpy
import random

class Sender:

    def __init__(self, packet_len, msg_len, packet_num, checksum_len, data):
        self.packet_len = packet_len
        self.msg_len = msg_len
        self.packet_num = packet_num
        self.checksum_len = checksum_len
        self.data = data

    def coder_parity_bit(self):                     #dodanie bitu parzytości do pakietów
        number_of_packets = self.packet_num
        data = self.data.reshape(number_of_packets, self.packet_len-1)
        packets = numpy.arange(self.msg_len + number_of_packets).reshape(number_of_packets, self.packet_len)

        for i in range(0, number_of_packets):
            packet_str = str(data[i])
            packet = data[i]
            if packet_str.count("1") % 2:
                packet = numpy.append(packet, [1])
            else:
                packet = numpy.append(packet, [0])
            packets[i] = packet
        return packets

    def coder_check_sum(self):                         #dodanie sumy kontrolnej
        number_of_packets = self.packet_num
        data = self.data.reshape(number_of_packets, self.packet_len - self.checksum_len)
        packets = numpy.arange(self.msg_len + (self.checksum_len*number_of_packets)).reshape(number_of_packets, self.packet_len)

        for i in range(0, number_of_packets):                       #sumowanie pakietow
            check_sum_int = 0
            packet = data[i]
            sub_num = int(self.packet_len/self.checksum_len) - 1
            packet = packet.reshape(sub_num, self.checksum_len)

            # print("SEN: " + str(data[i]))
            for j in range(0, sub_num):
                packet_str = ""
                for k in range(0, self.checksum_len):
                    packet_str = packet_str + str(packet[j][k])
                
                check_sum_int += int(packet_str, 2)

            check_sum_bin = bin(check_sum_int)                            #dodawanie przeniesienia
            
            # print(check_sum_bin)
            # print(len(check_sum_bin))
            # print(self.checksum_len)
            
            if len(check_sum_bin)-2 < self.checksum_len:
                check_sum_bin = check_sum_bin[2:]
            if len(check_sum_bin)-2 > self.checksum_len:
                x = len(check_sum_bin)-self.checksum_len
                check_sum_bin = bin(int(check_sum_bin[0:x], 2) + int(check_sum_bin[x:], 2))
                if len(check_sum_bin)-2 > self.checksum_len:
                    x = len(check_sum_bin)-self.checksum_len
                    check_sum_bin = bin(int(check_sum_bin[0:x], 2) + int(check_sum_bin[x:], 2))[2:]
                else:
                    check_sum_bin = check_sum_bin[2:]

            if len(check_sum_bin) < self.checksum_len:
                check_sum_bin = '0'*(self.checksum_len - len(check_sum_bin)) + check_sum_bin
            if len(check_sum_bin)-2 == self.checksum_len:
                check_sum_bin = check_sum_bin[2:]

            # print(check_sum_bin)

            check_sum = numpy.array(list(check_sum_bin), dtype=int)
            for x in range(0, len(check_sum)):        #zamiana bitów na przeciwne
                if check_sum[x] == 1:
                    check_sum[x] = 0
                else: check_sum[x] = 1

            packet = packet.flatten()
            packet = numpy.append(packet, check_sum)
            
            packets[i] = packet
            
        return packets

