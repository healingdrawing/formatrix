import os
import math
import datetime

class MP:
    """matrix printer"""

    def __init__(self, mydir, k) -> None:
        self.mydir = mydir
        self.resultDir = self.mydir + os.sep + "resultFolder"+str(k)+"x"+str(k)
        self.resultSubDir = self.resultDir + os.sep + "result"
        self.resultBadDir = self.resultDir + os.sep + "bad"

    def checkDirsNeeded(self):
        # check if no previous completed inkrement of calculated matrices
        if not os.path.exists(self.resultDir):
            os.makedirs(self.resultDir)
        if not os.path.exists(self.resultSubDir):
            os.makedirs(self.resultSubDir)
        if not os.path.exists(self.resultBadDir):
            os.makedirs(self.resultBadDir)

    def printMatrix(self, m, solution):
        print("----"+str(m[0]))  # matrix number
        print(m[2])  # symbolic matrix
        print(solution)

    def printToFile(self, solutionBox):
        """print result to file with matrix index"""
        # last calculated matrix index in this group
        fileName = str(solutionBox[-1][0])+".txt"
        rfDir = self.resultSubDir + os.sep + fileName
        resultFile = open(rfDir, mode="wt", encoding="utf-8")
        slines = []
        for one in solutionBox:
            sline = str(one[0])+"  "+str(one[-1])+"\n"
            slines.append(sline)
        resultFile.writelines(slines)
        resultFile.close()

        # refresh globalCounterValue
        gcfDir = self.resultDir + os.sep + "globalCounter.txt"
        gcv = str(solutionBox[-1][0])
        gcFile = open(gcfDir, mode="wt", encoding="utf-8")
        gcFile.write(gcv)
        gcFile.close()

        print("printed "+str(solutionBox[0][0])+" "+str(solutionBox[-1][0]))

    def refreshGlobalCounterValue(self, value):
        # refresh globalCounterValue
        gcfDir = self.resultDir + os.sep + "globalCounter.txt"
        gcv = str(value)
        gcFile = open(gcfDir, mode="wt", encoding="utf-8")
        gcFile.write(gcv)
        gcFile.close()

    def globalCounterValue(self) -> int:

        gcfDir = self.resultDir + os.sep + "globalCounter.txt"

        if not os.path.exists(gcfDir):
            gcFile = open(gcfDir, mode="wt", encoding="utf-8")
            gcFile.write("0")
            gcFile.close()

        gcFile = open(gcfDir, mode="rt", encoding="utf-8")
        gcv = int(gcFile.readline())
        gcFile.close()
        print("mp.py calculated "+str(gcv))
        return gcv

    def bestpiValue(self) -> list:
        gcfDir = self.resultDir + os.sep + "bestpi.txt"

        # check if no previous completed inkrement of calculated matrices
        if not os.path.exists(self.resultDir):
            os.makedirs(self.resultDir)
        if not os.path.exists(self.resultSubDir):
            os.makedirs(self.resultSubDir)

        if not os.path.exists(gcfDir):
            gcFile = open(gcfDir, mode="wt", encoding="utf-8")
            gcFile.write(str(math.pi)[0:2]+" 0")
            gcFile.close()

        gcFile = open(gcfDir, mode="rt", encoding="utf-8")
        gcv, mnumber = gcFile.readline().split(" ", 1)
        gcFile.close()
        print("mp.py best pi "+str(gcv))
        return [gcv, mnumber]

    def bestpi2Value(self) -> list:
        gcfDir = self.resultDir + os.sep + "bestpi2.txt"

        # check if no previous completed inkrement of calculated matrices
        if not os.path.exists(self.resultDir):
            os.makedirs(self.resultDir)
        if not os.path.exists(self.resultSubDir):
            os.makedirs(self.resultSubDir)

        if not os.path.exists(gcfDir):
            gcFile = open(gcfDir, mode="wt", encoding="utf-8")
            gcFile.write(str(math.pi**2)[0:2]+" 0")
            gcFile.close()

        gcFile = open(gcfDir, mode="rt", encoding="utf-8")
        gcv, mnumber = gcFile.readline().split(" ", 1)
        gcFile.close()
        print("mp.py best pi*pi "+str(gcv))
        return [gcv, mnumber]

    def bestpi12Value(self) -> list:
        gcfDir = self.resultDir + os.sep + "bestpi12.txt"

        # check if no previous completed inkrement of calculated matrices
        if not os.path.exists(self.resultDir):
            os.makedirs(self.resultDir)
        if not os.path.exists(self.resultSubDir):
            os.makedirs(self.resultSubDir)

        if not os.path.exists(gcfDir):
            gcFile = open(gcfDir, mode="wt", encoding="utf-8")
            gcFile.write(str(math.pi**(1/2))[0:2]+" 0")
            gcFile.close()

        gcFile = open(gcfDir, mode="rt", encoding="utf-8")
        gcv, mnumber = gcFile.readline().split(" ", 1)
        gcFile.close()
        print("mp.py best pi**1/2 "+str(gcv))
        return [gcv, mnumber]

    def refreshpiValue(self, value, mnumber):
        # refresh globalCounterValue
        gcfDir = self.resultDir + os.sep + "bestpi.txt"
        gcv = str(value)
        mnumber = str(mnumber)
        gcFile = open(gcfDir, mode="wt", encoding="utf-8")
        gcFile.write(gcv + " " + mnumber)
        gcFile.close()

        print("refreshed bestpi "+gcv+" "+mnumber)

    def refreshpi2Value(self, value, mnumber):
        # refresh globalCounterValue
        gcfDir = self.resultDir + os.sep + "bestpi2.txt"
        gcv = str(value)
        mnumber = str(mnumber)
        gcFile = open(gcfDir, mode="wt", encoding="utf-8")
        gcFile.write(gcv + " " + mnumber)
        gcFile.close()

        print("refreshed bestpi2 "+gcv+" "+mnumber)

    def refreshpi12Value(self, value, mnumber):
        # refresh globalCounterValue
        gcfDir = self.resultDir + os.sep + "bestpi12.txt"
        gcv = str(value)
        mnumber = str(mnumber)
        gcFile = open(gcfDir, mode="wt", encoding="utf-8")
        gcFile.write(gcv + " " + mnumber)
        gcFile.close()

        print("refreshed bestpi12 "+gcv+" "+mnumber)

    def updatepiValue(self, value, mnumber):
        # update globalCounterValue
        gcfDir = self.resultDir + os.sep + "bestpi.txt"
        gcv = str(value)
        mnumber = str(mnumber)
        gcFile = open(gcfDir, mode="wt", encoding="utf-8")
        gcFile.write(gcv + " " + mnumber)
        gcFile.close()

        print("updated bestpi "+gcv+" "+mnumber)

    def updatepi2Value(self, value, mnumber):
        # update globalCounterValue
        gcfDir = self.resultDir + os.sep + "bestpi2.txt"
        gcv = str(value)
        mnumber = str(mnumber)
        gcFile = open(gcfDir, mode="wt", encoding="utf-8")
        gcFile.write(gcv + " " + mnumber)
        gcFile.close()

        print("updated bestpi2 "+gcv+" "+mnumber)

    def updatepi12Value(self, value, mnumber):
        # update globalCounterValue
        gcfDir = self.resultDir + os.sep + "bestpi12.txt"
        gcv = str(value)
        mnumber = str(mnumber)
        gcFile = open(gcfDir, mode="wt", encoding="utf-8")
        gcFile.write(gcv + " " + mnumber)
        gcFile.close()

        print("updated bestpi12 "+gcv+" "+mnumber)

    def findMax(self, solution: list, whatNeed: str, maxVal: str):
        """whatNeed is pi form for compare"""
        result = ""
        for fline in solution:
            line = str(fline)
            if maxVal in line:
                whatWant = whatNeed.split(maxVal, 1)[1]
                for point in whatWant:
                    if maxVal+point in line:
                        maxVal += point
                        result = maxVal
                    else:
                        result = maxVal
                        break
        return result

    def printToFileLongCalculatedMatrices(self, m:list):
        """
        print matrices with long calculation,
        not completed in time, to file for later continue
        the process if possible
        """
        print("*"*33)
        print("*long calculated matrix detected*")
        print("*"*33)
        fileName = str(m[0])+".txt"
        rfDir = self.resultBadDir + os.sep + fileName
        resultFile = open(rfDir, mode="wt", encoding="utf-8")
        slines = []
        for one in m:
            sline = str(one)+"\n\n"
            slines.append(sline)
        resultFile.writelines(slines)
        resultFile.close()

    def printToFileAnyError(self, error, globalCounter):
        """
        print matrices with long calculation,
        not completed in time, to file for later continue
        the process if possible
        """
        print("*"*20)
        print("*some fail happened*")
        print("*"*20)
        fileName = str("error-"+str(datetime.datetime.now()))+".txt"
        rfDir = self.resultBadDir + os.sep + fileName
        resultFile = open(rfDir, mode="at", encoding="utf-8")
        slines = []
        slines.append(str(error)+"\n")
        slines.append("globalCounter "+str(globalCounter)+"\n")
        slines.append("*"*50+"\n\n")
        resultFile.writelines(slines)
        resultFile.close()
