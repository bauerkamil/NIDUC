import numpy


class ResultsToFile:

    def __init__(self):
        self.fileName = "results.csv"
        self.sentPackets = [0]
        self.resendNum = 0

    def _addRep_(self):
        self.resendNum = self.resendNum+1
