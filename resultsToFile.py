import numpy
import csv


class ResultsToFile:

    def __init__(self, codeChoice, channel, msgLen, packetLen, probability, numOfIter):
        self.fileName = "results.csv"
        self.sentPackets = []
        self.resendNum = 0
        self.codeChoice = codeChoice
        self.channel = channel
        self.msgLen = msgLen  # bit message length
        self.packetLen = packetLen  # packet length
        self.probability = probability  # probability
        self.numOfIter = numOfIter  # number of iterations

    def _addRep_(self):
        self.resendNum = self.resendNum+1

    def _printToCsv_(self, approvedPackets):
        mistakesApproved = 0
        # for i in range(0, numpy.shape(self.sentPackets)[0]):
        #     if self.sentPackets[i] != approvedPackets[i]:
        #         mistakesApproved = mistakesApproved+1

        row = [self.codeChoice, self.channel, self.msgLen, self.packetLen,
               self.probability, self.numOfIter, self.resendNum, mistakesApproved]

        with open(self.fileName, 'a') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)

            # writing the data rows
            csvwriter.writerow(row)
