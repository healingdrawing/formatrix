from mg import MG
from ms import MS
from mp import MP

import multiprocessing
import time
import sys
import os
import math

if getattr(sys, 'frozen', False):
    mydir = os.path.dirname(sys.executable)
elif __file__:
    mydir = os.path.dirname(os.path.abspath(__file__))

"""trying calculate all in one flow without preparing every partion of matrices"""


class MGAS:
    """matrix generator and solver"""

    def __init__(self, mydir) -> None:
        self.mydir = mydir
        """run.py script file path"""
        # names of parameters. first element target(old code recoding result) is will pi
        self.input_n = ["pi", "R", "S", "P", "PS", "N", "RN", "O", "C", "OC", "F", "A", "FA", "AC", "AS", "ACAS", "FAC", "RR", "SS", "PP", "PSPS", "NN", "RNRN", "OO", "CC", "OCOC", "FF", "AA", "FAFA",
                        "ACAC", "ASAS", "ACASACAS", "FACFAC", "NU", "XU", "XR", "o", "f", "r", "ac", "as", "Af", "Rr", "v", "NUNU", "XUXU", "XRXR", "oo", "ff", "rr", "acac", "asas", "AfAf", "RrRr", "vv"]

        self.k = 3  # matrix size it should be square
        # turn on ignore some number indices from parameters flow f.e.: n1 n2 n4
        self.ignoriism = True
        # which number/s of parameters indices will ignored 1...7 for my case
        self.iism0 = [5]

        # generated parameter indices from 2
        self.iism1 = 2
        # generated parameter indices to 7
        self.iism2 = 7  # for circle case, because infinity haven't good int value

        self.mg = MG(
            self.input_n,
            self.k,
            self.ignoriism,
            self.iism0,
            self.iism1,
            self.iism2
        )
        self.globalLimit = self.mg.globalLimit

        self.ms = MS()
        self.mp = MP(self.mydir, self.k)
        self.mp.checkDirsNeeded()

        self.checkpi = str(math.pi)
        self.checkpi2 = str(math.pi**2)
        self.checkpi12 = str(math.pi**(1/2))

        self.bestpi = self.mp.bestpiValue()
        self.bestpi2 = self.mp.bestpi2Value()
        self.bestpi12 = self.mp.bestpi12Value()

        """how much calculated at present moment and not printed"""
        self.globalCounter = self.mp.globalCounterValue()

    def runAll(self):

        self.globalCounter += 1
        calcChecker = self.globalCounter

        # calculation with pause between steps
        while calcChecker <= self.globalLimit:
            time.sleep(1)

            try:
                mx = self.mg.generateMatrices(self.globalCounter)
                needprint = False
                for m in mx:

                    #trying prefiltering long operations was detected
                    man = multiprocessing.Manager()
                    solution = man.list()
                    lp = multiprocessing.Process(
                        target=self.ms.solve_pi,
                        name="Foo",
                        args=(m[1], solution, False))
                    lp.start()
                    #timeout as join parameter must be increased x2, 120 is 61(60 is 31) finally, strange
                    lp.join()
                    lp.terminate()

                    if (len(solution) == 1 and solution[0]==None):
                        print("m \n",m)
                        print("solution \n", solution)
                        #write matrix to special list/file in folder "bad"
                        self.mp.printToFileLongCalculatedMatrices(m)
                    else:

                        # pi check
                        result = self.mp.findMax(
                            solution, self.checkpi, self.bestpi[0])
                        if (len(result) > len(self.bestpi[0])):
                            self.bestpi = [result, str(m[0])]
                            self.mp.refreshpiValue(result, m[0])
                            needprint = True
                        elif (len(result) == len(self.bestpi[0])):
                            self.bestpi = [
                                result, self.bestpi[1] + " " + str(m[0])]
                            self.mp.updatepiValue(result, self.bestpi[1])
                            needprint = True

                        # pi2 check
                        result = self.mp.findMax(
                            solution, self.checkpi2, self.bestpi2[0])
                        if (len(result) > len(self.bestpi2[0])):
                            self.bestpi2 = [result, str(m[0])]
                            self.mp.refreshpi2Value(result, m[0])
                            needprint = True
                        elif (len(result) == len(self.bestpi2[0])):
                            self.bestpi2 = [
                                result, self.bestpi2[1] + " " + str(m[0])]
                            self.mp.updatepi2Value(result, self.bestpi2[1])
                            needprint = True

                        # pi12 check
                        result = self.mp.findMax(
                            solution, self.checkpi12, self.bestpi12[0])
                        if (len(result) > len(self.bestpi12[0])):
                            self.bestpi12 = [result, str(m[0])]
                            self.mp.refreshpi12Value(result, m[0])
                            needprint = True
                        elif (len(result) == len(self.bestpi12[0])):
                            self.bestpi12 = [
                                result, self.bestpi12[1] + " " + str(m[0])]
                            self.mp.updatepi12Value(result, self.bestpi12[1])
                            needprint = True

                        # print to console screen
                        if needprint:
                            print(str(m[0])+" "+str(solution))
                            print(str(m[2]))
                            print(" -"*10)
                            needprint = False

                        calcChecker += 1
                self.mp.refreshGlobalCounterValue(m[0])

            except:
                theError = sys.exc_info()
                self.mp.printToFileAnyError(theError, self.globalCounter)
                print(theError)
                print("some fail with matrices " +
                      str(self.globalCounter) + " range")

            if calcChecker == self.globalLimit:
                break
            else:
                self.globalCounter += 1
        input("enter to close")


mbox = MGAS(mydir)
# uncomment next line and comment last line to just print matrix
# mbox.mg.printMatrix(9)
mbox.runAll()
