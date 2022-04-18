import random

import numpy


class Generator:

    def __init__(self, m):
        self.m = m

    def generate_data(self):                        #generowanie ciagu bitow o zadanej dlugosci m
        data = numpy.arange(self.m)
        for i in range(self.m):
            data[i] = (random.randint(0, 1))
        return data
