import komm
import numpy
from Sender import Sender
from Receiver import Receiver
from Chanel import Chanel
from Generator import Generator

m = 40                       #dlugosc ciagu bitow
n = 8                            #dlugosc pakietu
p = 0.1

generator = Generator(m)
data = generator.generate_data()
print(data)

sender = Sender(n, m, data)
# packets = sender.coder_parity_bit()
packets = sender.coder_check_sum(m, data)
# packets = sender.coder_parity_bit_and_check_sum()
# print(sender.coder_parity_bit_and_check_sum())

chanel = Chanel(packets, p)
# chanel.data_transmission()
packets_with_noise = packets
for i in range(0, numpy.shape(chanel.packets)[0]):
    packets_with_noise[i] = chanel.BSC(chanel.p, chanel.packets[i])
    # packets_with_noise[i] = chanel.BEC(chanel.p, chanel.packets[i])

print(packets)
receiver = Receiver(packets, n)
# receiver.decoder_parity_bit()
receiver.decoder_check_sum()
