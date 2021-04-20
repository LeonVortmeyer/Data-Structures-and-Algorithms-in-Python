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

#--------------------------------R-3.8-----------------------------------------------

"""
From smallest asymptotic growth rate to largest:

1. 2 ** 10 (constant)

2. 2 ** log(n) = n (linear)

3. 3n + 100 * log(n) (linear, but steeper than 2.)

4. 4n (linear, but steeper than 3.)

5. n * log(n) (log * linear > linear)

6. 4 * n * log(n) + 2 * n (log * linear, but steeper than 5.)

7. n ** 2 + 10 * n (quadratic > log * linear)

8. n ** 3 (cubic > quadratic)

9. 2 ** n (exponential > cubic)
"""

#--------------------------------R-3.9-----------------------------------------------

"""
Suppose d(n) is O(f(n)), then there exists a constant c > 0 and an n' such that for all n > n',

d(n) < c * (f(n))

Then for any constant a > 0, let d = c*a. Then 

a * d(n) < d * f(n) for all n > n', so a * d(n) is in O(f(n))

"""

#--------------------------------R-3.10-----------------------------------------------
"""
Suppose d(n) is in O(f(n)) and e(n) is in O(g(n)), then there exists some constants a and b > 0 such that for all 
n > n':

i) d(n) < a * f(n)
ii) e(n) < b * g(n)

so d(n) * e(n) < a * b * f(n) * g(n)

so d(n) * e(n) is in O(f(n) * g(n))
"""


#--------------------------------R-3.11-----------------------------------------------
"""
Suppose d(n) is in O(f(n)) and e(n) is in O(g(n)), then there exists some constants a and b > 0 such that for all 
n > n':

i) d(n) < a * f(n)
ii) e(n) < b * g(n)

so d(n) + e(n) < a * f(n) + b * g(n) < max(a,b) * (f(n) + g(n))

so d(n) + e(n) is in O(f(n) * g(n))
"""

#--------------------------------R-3.12-----------------------------------------------
"""
Suppose d(n) is in O(f(n)) and e(n) is in O(g(n)), then there exists some constants a and b > 0 such that for all 
n > n':

i) d(n) < a * f(n)
ii) e(n) < b * g(n)

suppose f(n) = g(n) = n ** 2

d(n) = 2n

e(n) = n

d(n) - e(n) = n

f(n) - g(n) = 0

n is not in O(0)

proof by counter-example 

"""

#--------------------------------R-3.13-----------------------------------------------
"""
Suppose d(n) is in O(f(n)) and f(n) is in O(g(n)), then there exists some constants a and b > 0 such that for all 
n > n':

i) d(n) < a * f(n)
ii) f(n) < b * g(n)

so d(n) < a * f(n) < b * g(n)

so d(n) < b * g(n)

so d(n) is in O(g(n))
"""

#--------------------------------R-3.14-----------------------------------------------
"""
Suppose O(max{f(n), g(n)}) is not equal to O(f(n) + g(n)) - setting up proof by contradiction

then, there exists some function x(n) such that either:

i) x(n) > c * (f(n) + g(n)) for some constant c (asymptotically) AND x(n) < c * (max{f(n), g(n)}
ii) x(n) > c * (max{f(n), g(n)} AND x(n) < c * (f(n) + g(n))

if x(n) < c * max{f(n), g(n)}, then x(n) < c * (f(n) + g(n)) - contradiction 

"""

#--------------------------------R-3.15-----------------------------------------------
"""
Suppose g(n) is theta(f(n)), then there exists 2 constants c' and c'' > 0, such that for all n > n':

c' * f(n) < g(n) < c'' * f(n) 

therefore, f(n) < (1 / c') * (g(n)); therefore, f(n) is in O(g(n))

Now to prove iff, suppose g(n) is not theta(f(n)), then we must show f(n) is not O(g(n)):

then there does not exist a c' > 0, such that

c' * f(n) < g(n), and therefore f(n) is not O(g(n))

And such we prove f(n) is in O(g(n)) iff g(n) is theta(f(n))

"""

#--------------------------------R-3.16-----------------------------------------------

"""
Suppose p(n) is a polynomial in n, then log(p(n)) is O(log(n)):

Let's consider the highest order term of p(n) given that any lower-order terms are ancillary WLOG.

Let the highest order term of p(n) = a * n ** p

log(p(n)) = p * (log(a) + log(n))

note that let c be a constant greater than p * log(a) + p, then there exists an n', such that for all n > n',

p * (log(a) + log(n)) < c * log(n), so log(p(n)) is in O(log(n))

"""

#--------------------------------R-3.17-----------------------------------------------
"""
Similar to R-3.16:

Let's consider the highest order term of (n + 1) ** 5, which is n ** 5 WLOG

There exists a constant c such that for all n > some n':

(n + 1) ** 5 < c * n ** 5

Therefore (n + 1) ** 5 is in O(n ** 5)

"""

#--------------------------------R-3.18-----------------------------------------------
"""
2 ** (n + 1) = 2 * 2 ** n

for all n > 0, let c = 10,

2 ** (n + 1) = 2 * 2 ** n < 10 * 2 ** n

so 2 ** (n + 1) is in O(2 ** n)

"""

#--------------------------------R-3.19-----------------------------------------------
"""
First, n is O(n), given that for all n > 0, let c = 2, then

n < 2 * n

Since log(n) > 0 for all n > 0, it is also true that:

n < 2 * n * log(n),

so n is in O(n * log(n))

"""

#--------------------------------R-3.20-----------------------------------------------
"""
log(2) < 2

"""
