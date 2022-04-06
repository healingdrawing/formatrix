from __future__ import division
import itertools as ite
from sympy import Matrix, ImmutableMatrix
from sg import SG


class MG:
    """matrix generator"""

    def __init__(self, n: list, k: int,
                 ignoriism: bool,
                 iism0: list, iism1: int, iism2: int
                 ) -> None:
        self.nmassiv = n  # array of symbolic names of parameters
        self.n = len(n)-1  # follow js way, to exclude "pi" from list
        self.k = k  # square matrix size
        self.ignoriism = ignoriism  # boolean ingnor indices from iism0 list
        self.iism0 = iism0  # list of ingored indices for polygons inside circle
        self.iism1 = iism1  # value 2
        self.iism2 = iism2  # value 7 used for circle as base polygon with infinity
        self.sg = SG(self.n, 1)

        self.globalLimit, self.uniColGroups, self.uniRowGroups, self.colsNumber, self.rowsNumber = self.summcount()

    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)

    def summcount(self):
        # unique names/symbols group . columns
        # first pi cutted
        uniColGroups = list(ite.combinations(self.nmassiv[1:], self.k))

        rowsList = []
        for i in [i for i in range(self.iism1, self.iism2+1) if i not in self.iism0]:
            rowsList.append(str(i))
        # unique groups of rows, which is numeric indices for polygons
        uniRowGroups = list(ite.combinations(rowsList, self.k))
        cn = len(uniColGroups)
        rn = len(uniRowGroups)
        # unique matrixes masked by size from global big table
        sumFinal = cn * rn
        print("original matrices number "+str(int(sumFinal)))
        return sumFinal, uniColGroups, uniRowGroups, cn, rn

    def generateMatrix(self, crIndices: list) -> list:

        mdata = []
        """number matrix data"""
        sdata = []
        """symbolic matrix data"""
        cindices, rindices = crIndices
        for rind in self.uniRowGroups[rindices]:
            mrow = []
            srow = []
            for cind in self.uniColGroups[cindices]:
                mSymbol = cind+rind
                mrow.append(self.sg.sv[mSymbol])
                srow.append(mSymbol)
            mdata.append(mrow)
            sdata.append(srow)

        m = Matrix(mdata)
        im = ImmutableMatrix(m)
        msym = Matrix(sdata)
        imsym = ImmutableMatrix(msym)
        # return [m, msym]
        return [im, imsym]

    def generateMatrixColsRowsNumericIndicesList(self, globalCounter: int):
        rind = int(globalCounter / self.colsNumber)
        cind = globalCounter % self.colsNumber
        return [cind, rind]

    def generateMatrices(self, globalCounter: int) -> list:
        matrices = []
        """each element is [number, matrix, symbol matrix]"""
        crIndices = self.generateMatrixColsRowsNumericIndicesList(
            globalCounter)
        bothMatrix = self.generateMatrix(crIndices)
        mxd = []
        mxd.append(globalCounter)
        mxd.append(bothMatrix[0])
        mxd.append(bothMatrix[1])
        matrices.append(mxd)

        return matrices

    def printMatrix(self, number: int):
        m = self.generateMatrices(number)
        print(m[0][2])
        input("press enter to continue calculation")
