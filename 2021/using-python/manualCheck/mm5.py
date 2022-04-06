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

    self.k = 5  # matrix size it should be square
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

    self.checkpi = str(math.pi)
    self.checkpi2 = str(math.pi**2)
    self.checkpi12 = str(math.pi**(1/2))

    self.bestpi = self.mp.bestpiValue()
    self.bestpi2 = self.mp.bestpi2Value()
    self.bestpi12 = self.mp.bestpi12Value()

    """how much calculated at present moment and not printed"""
    # self.globalCounter = self.mp.globalCounterValue()

  def runAll(self):

    #insert last succesfull calculated from flow
    self.globalCounter = 266693
    self.globalCounter += 1
    calcChecker = self.globalCounter

    # remastered to one matrix
    if True:


      try:
        mx = self.mg.generateMatrices(self.globalCounter)
        needprint = True
        for m in mx:
          print(m)
          man = multiprocessing.Manager()
          solution = man.list()
          lp = multiprocessing.Process(
              target=self.ms.solve_pi,
              name="Foo",
              args=(m[1], solution, False))
          lp.start()
          lp.join()
          lp.terminate()

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
              str(self.globalCounter) + " range")


    input("enter to close")


mbox = MGAS(mydir)
# mbox.mg.printMatrix(9)
mbox.runAll()
