import multiprocessing.managers

import sympy as s


class MS:
    """matrix solver"""

    def __init__(self) -> None:
        pass

    def pi_in_matrixDeterminant(self, d) -> bool:
        if "pi" in str(d):
            return True
        return False

    def solve_pi(self, m:s.ImmutableMatrix, solution:multiprocessing.managers.SyncManager.list, debug:bool=False)-> list:
        solution.append(None)
        mdet = m.det()

        if debug:
            print("debug mdet =\n",mdet)

        if self.pi_in_matrixDeterminant(mdet):
            solution.extend(s.solve(mdet, s.pi, dict=True, check=False, rational=None))
            # this is bad(fail, tested) way, because solution is special list,
            # and reassign make it usual, but if use the for loop then overflow happen
            # this why i tried extend(), but there is big chance it will fail too.
            # Old syntax in _ms.py, have no this fails, but can't be catched depend of calc time
            # for i in rez: solution.append(i)
        else:
            solution.append(mdet)
        solution.pop(0) #remove None from zero index, means calculation was completed
