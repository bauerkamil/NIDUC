import numpy
import csv


class ResultsToFile:

    def __init__(self, codeChoice, channel, msgLen, packetLen, probability, numOfIter):
        self.fileName = "results.csv"
        self.originalPackets = []
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
        # print("Approved with:")
        # print(self.sentPackets)
        # print(approvedPackets)

        mistakesApproved = 0
        for i in range(0, numpy.shape(self.originalPackets)[0]):
            for j in range(0, self.packetLen):
                if self.originalPackets[i][j] != approvedPackets[i][j]:
                    mistakesApproved = mistakesApproved+1

        ber = mistakesApproved/self.msgLen
        row = [self.codeChoice, self.channel, self.msgLen, self.packetLen,
               self.probability, self.numOfIter, self.resendNum, mistakesApproved, ber, numpy.array_equal(self.originalPackets,approvedPackets)]


        with open(self.fileName, 'a') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)

            # writing the data rows
            csvwriter.writerow(row)
            
        self.resendNum = 0
