from mg import MG
from ms import MS
from mp import MP

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

        self.k = 5  # matrix size it should be square
        # turn on ignore some number indices from parameters flow f.e.: n1 n2 n4
        self.ignoriism = True
        # which number/s of parameters indices will ignored
        self.iism0 = [5]

        # generated parameter indices from 2
        self.iism1 = 2
        # generated parameter indices to 7
        self.iism2 = 7

        # generate matrices from 1
        self.out1 = 1
        # generate matrices to 3
        self.out2 = 3

        self.mg = MG(
            self.input_n,
            self.k,
            self.ignoriism,
            self.iism0,
            self.iism1,
            self.iism2
        )
        self.globalLimit = self.mg.summcount()

        self.ms = MS()
        self.mp = MP(self.mydir, self.k)

        self.checkpi = str(math.pi)
        self.checkpi2 = str(math.pi**2)
        self.checkpi12 = str(math.pi**(1/2))

        self.bestpi = self.mp.bestpiValue()
        self.bestpi2 = self.mp.bestpi2Value()
        self.bestpi12 = self.mp.bestpi12Value()

        self.calcSize = 1
        """how much matrices will calculated before time sleep, must be < saveSize"""
        self.sessionSize = 0
        """how much calculated at present moment and not printed"""
        self.globalCounter = self.mp.globalCounterValue()

    def runAll(self):

        self.globalCounter += 1
        calcChecker = self.globalCounter
        self.out1 = self.globalCounter
        self.out2 = self.globalCounter + self.calcSize - 1
        # calculation with pause between steps
        while calcChecker <= self.globalLimit:
            time.sleep(1)

            try:
                mx = self.mg.generateMatrices(
                    self.input_n, self.k, self.ignoriism, self.iism0, self.iism1, self.iism2, self.out1, self.out2
                )
                needprint = False
                for m in mx:
                    solution = self.ms.solve_pi(m[1])
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
                print(sys.exc_info())
                print("some fail with matrices " +
                      str(self.out1)+" "+str(self.out2)+" range")

            if calcChecker == self.globalLimit:
                break
            elif self.globalCounter + self.calcSize > self.globalLimit:
                self.calcSize = self.globalLimit - self.globalCounter

            self.globalCounter += self.calcSize
            self.out1 = self.globalCounter
            self.out2 = self.globalCounter + self.calcSize - 1

        input("enter to close")


mbox = MGAS(mydir)
mbox.runAll()
