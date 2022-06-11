import numpy


class Receiver:

    def __init__(self, packet_len, checksum_len):
        self.packets = []
        self.packet_len = packet_len
        self.checksum_len = checksum_len

    def decoder_parity_bit(self, packetNum):                       #bit parzystosci - dekodowanie
        is_correct = True

        parity_bit = self.packets[packetNum][self.packet_len - 1]
        packet_str = str(self.packets[packetNum])

        packet_str = packet_str[:-2]

        if packet_str.count("1") % 2 != parity_bit:
            is_correct = False

        return is_correct

    def decoder_check_sum(self, packetNum):                       #suma kontrolna - dekodowanie
        packet = self.packets[packetNum]
        
        sub_num = int(self.packet_len/self.checksum_len)
        
        packet = packet.reshape(sub_num, self.checksum_len)

        sub_num -= 1
        check_sum_from_packet = packet[sub_num]
        is_correct = True
        check_sum_int = 0

        for i in range(0, sub_num):      #sumowanie pakietow
            packet_str = ""
            # print("REC: " + str(self.packets[i]))
            for j in range(0, self.checksum_len):
                packet_str = packet_str + str(packet[i][j])
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
            check_sum_bin = '0'*(self.checksum_len - len(check_sum_bin)+2) + check_sum_bin

        if len(check_sum_bin)-2 == self.checksum_len:
            check_sum_bin = check_sum_bin[2:]

        # print(check_sum_bin)

        check_sum_from_packet_str = ""                         #sprawdzenie sumy obliczonej z otrzymana
        for j in range(0, self.checksum_len):
            check_sum_from_packet_str = check_sum_from_packet_str + str(check_sum_from_packet[j])

        check_sum_bin = check_sum_bin.replace('0', 'a')
        check_sum_bin = check_sum_bin.replace('1', '0')
        check_sum_bin = check_sum_bin.replace('a', '1')
        if check_sum_bin != check_sum_from_packet_str:
                is_correct = False

        packet = packet.flatten()
        return is_correct
