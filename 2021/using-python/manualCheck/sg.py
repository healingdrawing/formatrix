import sympy as s


class SG:
    """symbols generator

    R,S,P,PS,N,RN,O,C,OC,
    F,A,FA,AC,AS,ACAS,FAC,
    RR,SS,PP,PSPS,NN,RNRN,OO,CC,OCOC,
    FF,AA,FAFA,ACAC,ASAS,ACASACAS,FACFAC,

    NU,XU,XR,o,f,r,ac,as,Af,Rr,v
    NUNU,XUXU,XRXR,oo,ff,rr,acac,asas,AfAf,RrRr,vv

    linear values:
    R - radius of circle outside polygon, one for all.
    S - side of polygon
    P - perimeter of polygon
    PS - perimeter minus side
    N - normal (perpendicular) from side center to circle center
    RN - radius minus normal
    O - circle length
    C - circle arc length between two polygon vertex
    OC - full circle length minus C

    NU - normal from polygon side to circle center , to intersection with polygon oposite direction
    perimeter
    XU - sum of NU for each polygon side
    XR - sum of RN for each polygon side
    o - internal circle length

    Rr - R minus r, ring width
    v - "vertex -> center -> side" length

    squared values:
    F - full circle area
    A - area of polygon
    FA - full circle area minus polygon area
    AC - area of  circle sector
    AS - area of polygon sector
    ACAS - AC minus AS
    FAC - full circle area minus AC

    f - internal circle area
    r - ring area, F minus f
    ac - area of internal circle section
    as - area AS minus ac
    Af - area A minus f

    repeating is power of two

    """
    sv = dict()
    """symbol values"""
    R = s.Integer(1)
    O = 2 * s.pi * R
    F = s.pi * R ** 2
    RR = R * R
    OO = O * O
    FF = F * F

    def __init__(self, sn: list, R=1) -> None:
        print("sg init")
        self.sn = ["pi", "R", "S", "P", "PS", "N", "RN", "O", "C", "OC", "F", "A", "FA", "AC", "AS", "ACAS", "FAC", "RR", "SS", "PP", "PSPS", "NN", "RNRN", "OO", "CC", "OCOC", "FF", "AA", "FAFA",
                   "ACAC", "ASAS", "ACASACAS", "FACFAC", "NU", "XU", "XR", "o", "f", "r", "ac", "as", "Af", "Rr", "v", "NUNU", "XUXU", "XRXR", "oo", "ff", "rr", "acac", "asas", "AfAf", "RrRr", "vv"]
        """symbol names"""

        self.R = s.Rational(R)
        self.O = 2 * s.pi * self.R
        self.F = s.pi * self.R ** 2
        self.RR = self.R * self.R
        self.OO = self.O * self.O
        self.FF = self.F * self.F

        self.sv = {
            "pi": s.pi,
            "R2": self.R, "R3": self.R, "R4": self.R, "R6": self.R, "R7": self.R,
            "O2": self.O, "O3": self.O, "O4": self.O, "O6": self.O, "O7": self.O,
            "F2": self.F, "F3": self.F, "F4": self.F, "F6": self.F, "F7": self.F,
            "RR2": self.RR, "RR3": self.RR, "RR4": self.RR, "RR6": self.RR, "RR7": self.RR,
            "OO2": self.OO, "OO3": self.OO, "OO4": self.OO, "OO6": self.OO, "OO7": self.OO,
            "FF2": self.FF, "FF3": self.FF, "FF4": self.FF, "FF6": self.FF, "FF7": self.FF
        }

        # n2 polygon values
        self.sv["S2"] = 2*self.R
        self.sv["P2"] = 4*self.R
        self.sv["PS2"] = self.sv["P2"]-self.sv["S2"]
        self.sv["N2"] = s.Rational(0)
        self.sv["RN2"] = self.sv["R2"]-self.sv["N2"]
        self.sv["C2"] = self.sv["O2"]/2
        self.sv["OC2"] = self.sv["O2"]-self.sv["C2"]
        self.sv["A2"] = s.Rational(0)
        self.sv["FA2"] = self.sv["F2"]-self.sv["A2"]
        self.sv["AC2"] = self.sv["F2"]/2
        self.sv["AS2"] = self.sv["A2"]/2
        self.sv["ACAS2"] = self.sv["AC2"]-self.sv["AS2"]
        self.sv["FAC2"] = self.sv["F2"]-self.sv["AC2"]
        self.sv["NU2"] = s.Rational(0)
        self.sv["XU2"] = s.Rational(0)
        self.sv["XR2"] = self.sv["RN2"]*2
        self.sv["o2"] = 2*s.pi*self.sv["N2"]
        self.sv["f2"] = s.pi*self.sv["N2"]**2
        self.sv["r2"] = self.sv["F2"]-self.sv["f2"]
        self.sv["ac2"] = self.sv["f2"]/2
        self.sv["as2"] = self.sv["AS2"]-self.sv["ac2"]
        self.sv["Af2"] = self.sv["A2"]-self.sv["f2"]
        self.sv["Rr2"] = self.sv["R2"]-self.sv["N2"]
        self.sv["v2"] = self.sv["R2"]*2

        self.sv["SS2"] = self.sv["S2"] ** 2
        self.sv["PP2"] = self.sv["P2"] ** 2
        self.sv["PSPS2"] = self.sv["PS2"] ** 2
        self.sv["NN2"] = self.sv["N2"] ** 2
        self.sv["RNRN2"] = self.sv["RN2"] ** 2
        self.sv["CC2"] = self.sv["C2"] ** 2
        self.sv["OCOC2"] = self.sv["OC2"] ** 2
        self.sv["AA2"] = self.sv["A2"] ** 2
        self.sv["FAFA2"] = self.sv["FA2"] ** 2
        self.sv["ACAC2"] = self.sv["AC2"] ** 2
        self.sv["ASAS2"] = self.sv["AS2"] ** 2
        self.sv["ACASACAS2"] = self.sv["ACAS2"] ** 2
        self.sv["FACFAC2"] = self.sv["FAC2"] ** 2
        self.sv["NUNU2"] = self.sv["NU2"] ** 2
        self.sv["XUXU2"] = self.sv["XU2"] ** 2
        self.sv["XRXR2"] = self.sv["XR2"] ** 2
        self.sv["oo2"] = self.sv["o2"] ** 2
        self.sv["ff2"] = self.sv["f2"] ** 2
        self.sv["rr2"] = self.sv["r2"] ** 2
        self.sv["acac2"] = self.sv["ac2"] ** 2
        self.sv["asas2"] = self.sv["as2"] ** 2
        self.sv["AfAf2"] = self.sv["Af2"] ** 2
        self.sv["RrRr2"] = self.sv["Rr2"] ** 2
        self.sv["vv2"] = self.sv["v2"] ** 2

        # n3 polygon values
        self.sv["S3"] = 3**(1/2) * self.sv["R3"]
        self.sv["P3"] = 3 * self.sv["S3"]
        self.sv["PS3"] = self.sv["P3"]-self.sv["S3"]
        self.sv["N3"] = 3 ** (1/2)/6 * self.sv["S3"]
        self.sv["RN3"] = self.sv["R3"] - self.sv["N3"]
        self.sv["C3"] = self.sv["O3"]/3
        self.sv["OC3"] = self.sv["O3"] - self.sv["C3"]
        self.sv["A3"] = 3**(1/2)/4 * self.sv["S3"]**2
        self.sv["FA3"] = self.sv["F3"] - self.sv["A3"]
        self.sv["AC3"] = self.sv["F3"]/3
        self.sv["AS3"] = self.sv["A3"]/3
        self.sv["ACAS3"] = self.sv["AC3"] - self.sv["AS3"]
        self.sv["FAC3"] = self.sv["F3"] - self.sv["AC3"]
        self.sv["NU3"] = self.sv["N3"] + self.sv["R3"]
        self.sv["XU3"] = self.sv["NU3"]*3
        self.sv["XR3"] = self.sv["RN3"]*3
        self.sv["o3"] = 2*s.pi * self.sv["N3"]
        self.sv["f3"] = s.pi * self.sv["N3"] ** 2
        self.sv["r3"] = self.sv["F3"] - self.sv["f3"]
        self.sv["ac3"] = self.sv["f3"]/3
        self.sv["as3"] = self.sv["AS3"] - self.sv["ac3"]
        self.sv["Af3"] = self.sv["A3"] - self.sv["f3"]
        self.sv["Rr3"] = self.sv["R3"] - self.sv["N3"]
        self.sv["v3"] = self.sv["R3"] + self.sv["N3"]

        self.sv["SS3"] = self.sv["S3"] ** 2
        self.sv["PP3"] = self.sv["P3"] ** 2
        self.sv["PSPS3"] = self.sv["PS3"] ** 2
        self.sv["NN3"] = self.sv["N3"] ** 2
        self.sv["RNRN3"] = self.sv["RN3"] ** 2
        self.sv["CC3"] = self.sv["C3"] ** 2
        self.sv["OCOC3"] = self.sv["OC3"] ** 2
        self.sv["AA3"] = self.sv["A3"] ** 2
        self.sv["FAFA3"] = self.sv["FA3"] ** 2
        self.sv["ACAC3"] = self.sv["AC3"] ** 2
        self.sv["ASAS3"] = self.sv["AS3"] ** 2
        self.sv["ACASACAS3"] = self.sv["ACAS3"] ** 2
        self.sv["FACFAC3"] = self.sv["FAC3"] ** 2
        self.sv["NUNU3"] = self.sv["NU3"] ** 2
        self.sv["XUXU3"] = self.sv["XU3"] ** 2
        self.sv["XRXR3"] = self.sv["XR3"] ** 2
        self.sv["oo3"] = self.sv["o3"] ** 2
        self.sv["ff3"] = self.sv["f3"] ** 2
        self.sv["rr3"] = self.sv["r3"] ** 2
        self.sv["acac3"] = self.sv["ac3"] ** 2
        self.sv["asas3"] = self.sv["as3"] ** 2
        self.sv["AfAf3"] = self.sv["Af3"] ** 2
        self.sv["RrRr3"] = self.sv["Rr3"] ** 2
        self.sv["vv3"] = self.sv["v3"] ** 2

        # n4 polygon values
        self.sv["S4"] = 2**(1/2) * self.sv["R4"]
        self.sv["P4"] = 4 * self.sv["S4"]
        self.sv["PS4"] = self.sv["P4"]-self.sv["S4"]
        self.sv["N4"] = self.sv["S4"]/2
        self.sv["RN4"] = self.sv["R4"] - self.sv["N4"]
        self.sv["C4"] = self.sv["O4"]/4
        self.sv["OC4"] = self.sv["O4"] - self.sv["C4"]
        self.sv["A4"] = self.sv["S4"]**2
        self.sv["FA4"] = self.sv["F4"] - self.sv["A4"]
        self.sv["AC4"] = self.sv["F4"]/4
        self.sv["AS4"] = self.sv["A4"]/4
        self.sv["ACAS4"] = self.sv["AC4"] - self.sv["AS4"]
        self.sv["FAC4"] = self.sv["F4"] - self.sv["AC4"]
        self.sv["NU4"] = self.sv["N4"]*2
        self.sv["XU4"] = self.sv["NU4"]*4
        self.sv["XR4"] = self.sv["RN4"]*4
        self.sv["o4"] = 2*s.pi * self.sv["N4"]
        self.sv["f4"] = s.pi * self.sv["N4"]**2
        self.sv["r4"] = self.sv["F4"] - self.sv["f4"]
        self.sv["ac4"] = self.sv["f4"]/4
        self.sv["as4"] = self.sv["AS4"] - self.sv["ac4"]
        self.sv["Af4"] = self.sv["A4"] - self.sv["f4"]
        self.sv["Rr4"] = self.sv["R4"] - self.sv["N4"]
        self.sv["v4"] = self.sv["R4"]*2

        self.sv["SS4"] = self.sv["S4"] ** 2
        self.sv["PP4"] = self.sv["P4"] ** 2
        self.sv["PSPS4"] = self.sv["PS4"] ** 2
        self.sv["NN4"] = self.sv["N4"] ** 2
        self.sv["RNRN4"] = self.sv["RN4"] ** 2
        self.sv["CC4"] = self.sv["C4"] ** 2
        self.sv["OCOC4"] = self.sv["OC4"] ** 2
        self.sv["AA4"] = self.sv["A4"] ** 2
        self.sv["FAFA4"] = self.sv["FA4"] ** 2
        self.sv["ACAC4"] = self.sv["AC4"] ** 2
        self.sv["ASAS4"] = self.sv["AS4"] ** 2
        self.sv["ACASACAS4"] = self.sv["ACAS4"] ** 2
        self.sv["FACFAC4"] = self.sv["FAC4"] ** 2
        self.sv["NUNU4"] = self.sv["NU4"] ** 2
        self.sv["XUXU4"] = self.sv["XU4"] ** 2
        self.sv["XRXR4"] = self.sv["XR4"] ** 2
        self.sv["oo4"] = self.sv["o4"] ** 2
        self.sv["ff4"] = self.sv["f4"] ** 2
        self.sv["rr4"] = self.sv["r4"] ** 2
        self.sv["acac4"] = self.sv["ac4"] ** 2
        self.sv["asas4"] = self.sv["as4"] ** 2
        self.sv["AfAf4"] = self.sv["Af4"] ** 2
        self.sv["RrRr4"] = self.sv["Rr4"] ** 2
        self.sv["vv4"] = self.sv["v4"] ** 2

        # n6 polygon values
        self.sv["S6"] = self.sv["R6"]
        self.sv["P6"] = 6 * self.sv["R6"]
        self.sv["PS6"] = self.sv["P6"] - self.sv["S6"]
        self.sv["N6"] = 3**(1/2)/2 * self.sv["R6"]
        self.sv["RN6"] = self.sv["R6"] - self.sv["N6"]
        self.sv["C6"] = self.sv["O6"]/6
        self.sv["OC6"] = self.sv["O6"] - self.sv["C6"]
        self.sv["A6"] = 3*3**(1/2)/2 * self.sv["R6"]**2
        self.sv["FA6"] = self.sv["F6"] - self.sv["A6"]
        self.sv["AC6"] = self.sv["F6"]/6
        self.sv["AS6"] = self.sv["A6"]/6
        self.sv["ACAS6"] = self.sv["AC6"] - self.sv["AS6"]
        self.sv["FAC6"] = self.sv["F6"] - self.sv["AC6"]
        self.sv["NU6"] = self.sv["N6"]*2
        self.sv["XU6"] = self.sv["NU6"]*6
        self.sv["XR6"] = self.sv["RN6"]*6
        self.sv["o6"] = 2*s.pi * self.sv["N6"]
        self.sv["f6"] = s.pi * self.sv["N6"] ** 2
        self.sv["r6"] = self.sv["F6"] - self.sv["f6"]
        self.sv["ac6"] = self.sv["f6"]/6
        self.sv["as6"] = self.sv["AS6"] - self.sv["ac6"]
        self.sv["Af6"] = self.sv["A6"] - self.sv["f6"]
        self.sv["Rr6"] = self.sv["R6"] - self.sv["N6"]
        self.sv["v6"] = self.sv["R6"]*2

        self.sv["SS6"] = self.sv["S6"] ** 2
        self.sv["PP6"] = self.sv["P6"] ** 2
        self.sv["PSPS6"] = self.sv["PS6"] ** 2
        self.sv["NN6"] = self.sv["N6"] ** 2
        self.sv["RNRN6"] = self.sv["RN6"] ** 2
        self.sv["CC6"] = self.sv["C6"] ** 2
        self.sv["OCOC6"] = self.sv["OC6"] ** 2
        self.sv["AA6"] = self.sv["A6"] ** 2
        self.sv["FAFA6"] = self.sv["FA6"] ** 2
        self.sv["ACAC6"] = self.sv["AC6"] ** 2
        self.sv["ASAS6"] = self.sv["AS6"] ** 2
        self.sv["ACASACAS6"] = self.sv["ACAS6"] ** 2
        self.sv["FACFAC6"] = self.sv["FAC6"] ** 2
        self.sv["NUNU6"] = self.sv["NU6"] ** 2
        self.sv["XUXU6"] = self.sv["XU6"] ** 2
        self.sv["XRXR6"] = self.sv["XR6"] ** 2
        self.sv["oo6"] = self.sv["o6"] ** 2
        self.sv["ff6"] = self.sv["f6"] ** 2
        self.sv["rr6"] = self.sv["r6"] ** 2
        self.sv["acac6"] = self.sv["ac6"] ** 2
        self.sv["asas6"] = self.sv["as6"] ** 2
        self.sv["AfAf6"] = self.sv["Af6"] ** 2
        self.sv["RrRr6"] = self.sv["Rr6"] ** 2
        self.sv["vv6"] = self.sv["v6"] ** 2

        # n7 polygon values circle
        self.sv["S7"] = s.Rational(0)
        self.sv["P7"] = 2*s.pi*self.sv["R7"]
        self.sv["PS7"] = self.sv["P7"] - self.sv["S7"]
        self.sv["N7"] = self.sv["R7"]
        self.sv["RN7"] = self.sv["R7"] - self.sv["N7"]
        self.sv["C7"] = s.Rational(0)
        self.sv["OC7"] = self.sv["O7"]
        self.sv["A7"] = s.pi * self.sv["R7"]**2
        self.sv["FA7"] = self.sv["F7"] - self.sv["A7"]
        self.sv["AC7"] = s.Rational(0)
        self.sv["AS7"] = s.Rational(0)
        self.sv["ACAS7"] = self.sv["AC7"] - self.sv["AS7"]
        self.sv["FAC7"] = self.sv["F7"] - self.sv["AC7"]
        self.sv["NU7"] = self.sv["N7"]*2
        self.sv["XU7"] = 2 * self.sv["R7"]
        self.sv["XR7"] = s.Rational(0)
        self.sv["o7"] = 2*s.pi * self.sv["N7"]
        self.sv["f7"] = s.pi * self.sv["N7"]**2
        self.sv["r7"] = self.sv["F7"] - self.sv["f7"]
        self.sv["ac7"] = s.Rational(0)
        self.sv["as7"] = self.sv["AS7"] - self.sv["ac7"]
        self.sv["Af7"] = self.sv["A7"] - self.sv["f7"]
        self.sv["Rr7"] = self.sv["R7"] - self.sv["N7"]
        self.sv["v7"] = self.sv["R7"]*2

        self.sv["SS7"] = self.sv["S7"] ** 2
        self.sv["PP7"] = self.sv["P7"] ** 2
        self.sv["PSPS7"] = self.sv["PS7"] ** 2
        self.sv["NN7"] = self.sv["N7"] ** 2
        self.sv["RNRN7"] = self.sv["RN7"] ** 2
        self.sv["CC7"] = self.sv["C7"] ** 2
        self.sv["OCOC7"] = self.sv["OC7"] ** 2
        self.sv["AA7"] = self.sv["A7"] ** 2
        self.sv["FAFA7"] = self.sv["FA7"] ** 2
        self.sv["ACAC7"] = self.sv["AC7"] ** 2
        self.sv["ASAS7"] = self.sv["AS7"] ** 2
        self.sv["ACASACAS7"] = self.sv["ACAS7"] ** 2
        self.sv["FACFAC7"] = self.sv["FAC7"] ** 2
        self.sv["NUNU7"] = self.sv["NU7"] ** 2
        self.sv["XUXU7"] = self.sv["XU7"] ** 2
        self.sv["XRXR7"] = self.sv["XR7"] ** 2
        self.sv["oo7"] = self.sv["o7"] ** 2
        self.sv["ff7"] = self.sv["f7"] ** 2
        self.sv["rr7"] = self.sv["r7"] ** 2
        self.sv["acac7"] = self.sv["ac7"] ** 2
        self.sv["asas7"] = self.sv["as7"] ** 2
        self.sv["AfAf7"] = self.sv["Af7"] ** 2
        self.sv["RrRr7"] = self.sv["Rr7"] ** 2
        self.sv["vv7"] = self.sv["v7"] ** 2
