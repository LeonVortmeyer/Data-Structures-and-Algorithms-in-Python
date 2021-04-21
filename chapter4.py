import math

#--------------------------------R-4.1-----------------------------------------------

def find_max(s):
    n = len(s)
    if n == 1:
        return s[0]
    return max(s[n-1], find_max(s[0:n-1]))

A = [1,2,3,4,5]

"""
Each recursion takes O(1) time with n calls to recursion, therefore runtime is O(n).

Since there are n activations, space too is O(n).
"""


#--------------------------------R-4.2-----------------------------------------------

def power(x, n):
    if n == 0:
        return 1
    else: return x * power(x, n-1)

"""
Recursion trace of power(2, 5):

power(2, 5)     returns 16 * 2 = 32
    power(2, 4)     returns 8 * 2 = 16
        power(2, 3)     returns 4 * 2 = 8
            power(2, 2)     returns 2 * 2 = 4 
                power(2, 1)   returns 2 * 1 = 2
                    power(2, 0) returns 1

"""

#--------------------------------R-4.3-----------------------------------------------

def power(x, n):
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)
        result = partial * partial

    if n % 2 == 1:
        return result * x
    return result

"""
Recursion trace of power(2, 18)

power(2, 18)    returns 512 * 512 = 262,144
    power(2, 9)     returns 16 * 16 * 2 = 512
        power(2, 4)     returns 4 * 4 = 16
            power(2, 2)     returns 2 * 2 = 4
                power(2, 1)     returns 2 * 1 = 2
                    power(2, 0)     returns 1
"""


# --------------------------------R-4.4-----------------------------------------------

def reverse(S, start, stop):
    if start < stop - 1:
        S[start], S[stop-1] = S[stop-1], S[start]
        reverse(S, start+1, stop-1)


"""
Recursion trace of reverse([4, 3, 6, 2, 6], 0, 5):

power(2, 18)    
"""

# --------------------------------R-4.5-----------------------------------------------

"""
Recursion trace of PuzzleSolve(3, [], {a, b, c, d})

PuzzleSolve(3, [], {a, b, c, d}
                PuzzleSolve(2, a, {b, c, d}) 
                    PuzzleSolve(1, ab, {c, d}
                    PuzzleSolve(1, ac, {b, d}
                    PuzzleSolve(1, ad, {b, c}
                PuzzleSolve(2, b, {a, c, d})
                    PuzzleSolve(1, ba, {c, d}
                    PuzzleSolve(1, bc, {a, d}
                    PuzzleSolve(1, bd, {a, c}
                PuzzleSolve(2, c, {a, b, d})
                    PuzzleSolve(1, ca, {b, d}
                    PuzzleSolve(1, cb, {a, d}
                    PuzzleSolve(1, cd, {a, b}
                PuzzleSolve(2, d, {a, b, c})
                    PuzzleSolve(1, da, {b, c}
                    PuzzleSolve(1, db, {a, c}
                    PuzzleSolve(1, dc, {a, b}
"""

# --------------------------------R-4.6-----------------------------------------------

def harmonic_number(n):
    if n == 1:
        return 1

    else:
        return 1 / n + harmonic_number(n-1)

"""
This function requires linear recursion and is executed in O(n) time and requires O(n) space with n activations.
"""

# --------------------------------R-4.7-----------------------------------------------

def int_from_string(str, index=0):
    n = len(str)
    if index == n - 1:
        return int(str[index])

    else:
        return int(str[index]) * 10 ** (n - index - 1) + int_from_string(str, index + 1)

"""
This function requires linear recursion and is executed in O(n) time and requires O(n) space with n activations.
"""

# --------------------------------R-4.7-----------------------------------------------

def isabel_sum(S):
    if not math.log(len(S),2) % 1 == 0:
        raise ValueError('Sequence must have length equal to power of 2')
    if len(S) == 1:
        return S[0]
    else:
        B = [None] * (len(S) // 2)
        for i in range(B):
            B[i] = S[2 * i] + A[2 * i - 1]
        return isabel_sum(B)

"""
Through each iteration the array is shortened by a factor of 1/2. As discussed in the binary search algorithm,
this yields log(n) number of times the recursive function will be called.

For each recursive call, the elements of the array are accessed: n, then n / 2, then n / 4, then n / 8 elements.

Is runtime here O(n) or O(n * log(n))?
"""