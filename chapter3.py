import matplotlib.pyplot as plt
import pylab
import math
import numpy as np

"""credit here to wdlcameron! Still getting back into the swing with matplotlib"""
x = [10**i for i in range(10)]

funcs = [lambda x: 8*x,
        lambda x: 4*x*math.log(x),
        lambda x: 2*x**2,
        lambda x: x**3,
        #lambda x: 2**x    #Note, this is too time consuming to compute
        ]

ys = []

for func in funcs:
    ys.append(list(map(func, x)))

for y in ys:
    plt.plot(x, y)
plt.yscale('log')
plt.xscale('log')
plt.show()


#--------------------------------R-3.2-----------------------------------------------
"""
what is the smallest integer n for which it is true that:

8 * n * log(n) < 2 * n ** 2

This is equivalent to:

log(n) < n / 4

When n is 16, log(n) - (base 2) is 4, and n / 4 is 4. 

n = 17 is the least integer value of n such that algorithm A is better than B.
"""

#--------------------------------R-3.3-----------------------------------------------

"""
what is the smallest integer n for which it is true that:

40 * n ** 2 < 2 * n ** 3

This is equivalent to:

40 < n * 2 

n = 21 is the least integer value of n such that algorithm A is better than B.

"""

#--------------------------------R-3.4-----------------------------------------------

"""
y = 0
"""


#--------------------------------R-3.5-----------------------------------------------

"""
consider log(y) = log(n ** c)

This can be written: log(y) = c * log(n)

With the log scale in mind, this would graphically look like the linear equivalent: y = c*x, a simple linear
equation with an origin intercept and slope c.

"""

#--------------------------------R-3.6-----------------------------------------------

"""
The sum of numbers from 0 to n is n * (n+1) / 2

Replace n with 2n for the sum from 0 to 2n:

(2n) * (2n + 1) / 2 = n * (2n + 1) 

"""

#--------------------------------R-3.7-----------------------------------------------

"""
Let's denote the worst case running time of algorithm A as A'.

By statement b, A' is in the set O(f(n)). Since the runtime of A' > runtime of all other A cases (trivial by "worst case")
all other A cases must be in the set of O(f(n)). 
"""

#--------------------------------R-3.7-----------------------------------------------