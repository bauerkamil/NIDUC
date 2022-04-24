import komm
import numpy
from Sender import Sender
from Receiver import Receiver
from Chanel import Chanel
from Generator import Generator
from menu import Menu

menu = Menu(42,8,0.1,100)
# m = 42                       #dlugosc ciagu bitow
# n = 8                         #dlugosc pakietu
# p = 0.5                          #prawdopodobieństwo


# generator = Generator(m)            #generowanie ciągu 0 i 1
# data = generator.generate_data()

# # print(' 1.Bit parzystosci\n 2.Suma kontrolna\n 3.Bit parzystosci i suma kontrolna\n')
# # choice = int(input("Wprowadz swoj wybor: "))
# # print(' 1.BSC\n 2.BEC\n 3.BSC i BEC\n')
# # choice2 = int(input("Wprowadz swoj wybor: "))

# sender = Sender(n, m, data)             #kodowanie
# packets = sender.coder_parity_bit()
# # packets = sender.coder_check_sum(m, data)
# # packets = sender.coder_parity_bit_and_check_sum()

# print("Wyslany:")
# print(packets)

# chanel = Chanel(packets, p)             #zaklocenia
# for i in range(0, numpy.shape(chanel.packets)[0]):
#     packets[i] = chanel.BSC(chanel.p, chanel.packets[i])
#     # packets[i] = chanel.BEC(chanel.p, chanel.packets[i])

# print("Otrzymany:")
# print(packets)

# receiver = Receiver(packets, n)         #dekodowanie
# answer = receiver.decoder_parity_bit()
# # answer = receiver.decoder_check_sum()
# # answer = receiver.decoder_parity_bit_and_check_sum()


# if answer: print("Odpowiedz: Zaakceptowano")
# else: print("Odpowiedz: Odrzucono")