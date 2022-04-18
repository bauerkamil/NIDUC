import numpy


class Receiver:

    def __init__(self, packets, n):
        self.packets = packets
        self.n = n

    def decoder_parity_bit(self):
        is_correct = True
        for i in range(0, numpy.shape(self.packets)[0]):
            parity_bit = self.packets[i][self.n - 1]
            packet_str = str(self.packets[i])
            packet_str = packet_str[:-1]
            if packet_str.count("1") % 2 != parity_bit:
                is_correct = False
        return is_correct

    def decoder_check_sum(self):
        check_sum_from_packets = self.packets[numpy.shape(self.packets)[0]-1]
        check_sum_int = 0

        for i in range(0, numpy.shape(self.packets)[0]-1):
            packet_str = ""
            for j in range(0, self.n):
                packet_str = packet_str + str(self.packets[i][j])
            check_sum_int += int(packet_str, 2)
            # print(bin(check_sum_int))

        check_sum_bin = bin(check_sum_int)
        if len(check_sum_bin) > self.n:
            x = len(check_sum_bin)-self.n
            check_sum_bin = bin(int(check_sum_bin[0:x], 2) + int(check_sum_bin[x:], 2))[2:]
        if len(check_sum_bin) < self.n:
            check_sum_bin = '0'*(self.n - len(check_sum_bin)) + check_sum_bin
        print(check_sum_bin)    #git

        check_sum_from_packets_str = ""
        for j in range(0, self.n):
            check_sum_from_packets_str = check_sum_from_packets_str + str(check_sum_from_packets[j])

        print(bin(int(check_sum_from_packets_str, 2)))   #git
        sum = int(check_sum_bin) + int(check_sum_from_packets_str, 2)

        print(bin(sum))

        # print(check_sum_from_packets)
        # print(check_sum)
        # if str(check_sum) != str(check_sum_bin):
        #     print("f")
        #     return False
        # else:
        #     return True
        #     print("t")


    def answer(self):
        pass