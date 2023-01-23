import sympy as sp
from sympy import symbols, Eq, solve, cos, pi, tan, sin, atan
from mpmath import radians, degrees
from sympy.parsing.sympy_parser import parse_expr
from equMain import *

 


class equclass:

    def __init__(self, leftside, rightside, variableList=[]):
        self.eq = Eq(leftside, rightside)
        self.variableList = list(self.eq.free_symbols)

    def eqsolve(self, what):
        ret = solve(self.eq, what)
        print(self.eq, what, ret)
        if len(ret) == 2:
            ret = ret[1]
        else:
            ret = ret[0]

        rets = ret.evalf(3, subs=globalsvar)
        return rets

 

eq = equclass(p**2+q**2+2*p*q*cos(radians(theta)), r**2)
eq2 = equclass((p*sin(radians(theta))) /
               (q+p*cos(radians(theta))), tan(radians(alpha)))
eq3 = equclass(r*cos(radians(theta)), x)
eq4 = equclass(u*t+0.5*a*t**2, s)
eq5 = equclass(v**2, u**2+2*a*s)
eq6 = equclass(a, (v-u)/2)
