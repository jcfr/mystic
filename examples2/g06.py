#!/usr/bin/env python
#
# Problem definition:
# A-R Hedar and M Fukushima, "Derivative-Free Filter Simulated Annealing
# Method for Constrained Continuous Global Optimization", Journal of
# Global Optimization, 35(4), 521-549 (2006).
# 
# Original Matlab code written by A. Hedar (Nov. 23, 2005)
# http://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/go.htm
# and ported to Python by Mike McKerns (December 2014)
#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Copyright (c) 1997-2015 California Institute of Technology.
# License: 3-clause BSD.  The full license text is available at:
#  - http://trac.mystic.cacr.caltech.edu/project/mystic/browser/mystic/LICENSE

def objective(x):
    x0,x1 = x
    return (x0 - 10)**3 + (x1 - 20)**3

bounds = [(13,100),(0,100)]
# with penalty='penalty' applied, solution is:
xs = [14.095, 0.84296079]
ys = -6961.81387628

from mystic.symbolic import generate_constraint, generate_solvers, solve
from mystic.symbolic import generate_penalty, generate_conditions

equations = """
(x0 - 5)**2 + (x1 - 5)**2 - 100 >= 0.0
(x0 - 6)**2 + (x1 - 5)**2 - 82.81 <= 0.0
"""
#cf = generate_constraint(generate_solvers(solve(equations))) #XXX: inequalities
pf = generate_penalty(generate_conditions(equations), k=1e12)

from mystic.constraints import as_constraint

cf = as_constraint(pf)



if __name__ == '__main__':
    x = [0]*len(xs)

    from mystic.solvers import fmin_powell
    from mystic.math import almostEqual

    result = fmin_powell(objective, x0=x, bounds=bounds, penalty=pf, disp=False, full_output=True)

    assert almostEqual(result[0], xs, tol=1e-2)
    assert almostEqual(result[1], ys, rel=1e-2)



# EOF
