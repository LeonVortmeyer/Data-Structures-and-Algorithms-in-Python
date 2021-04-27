import math
import sys
import ctypes
import time
import pandas as pd
#--------------------------------R-5.1-----------------------------------------------

n = 51

data = []
for k in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes {1:4d}'.format(a,b))
    data.append(None)

"""
My system has the same capacity points but uses consistently fewer bytes.
"""

# --------------------------------R-5.2-----------------------------------------------

n = 51

data = []
for k in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    data.append(None)
    c = sys.getsizeof(data)

    if b != c:
        print(k)

# --------------------------------R-5.3-----------------------------------------------

n = 51

data = [None]*51
for k in range(n,0, -1):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes {1:4d}'.format(a,b))
    data.pop()

# --------------------------------R-5.4-----------------------------------------------

class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not -self._n <= k < self._n:
            raise IndexError('invalid index')
        if k >= 0:
            return self._A[k]
        else:
            return self._A[n+k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()


# --------------------------------R-5.5-----------------------------------------------

"""
Assuming the cost of growing an array from size k to size 2k costs 3k in run-time, 

The size of the array is represented by 2^i, so doubling the array will require 3*2^i in "cyber dollars".

This requires amortization in cells 2^(i - 1) to 2^i - 1.

Each append operation that does not require extension of the size of the array requires 1 "cyber dollar"
Extending the array requires 6 additional reserved "cyber dollars"

So the amortized portion of these "cyber dollars" requires 6 (as opposed to 2 when doubling required just k, not 3k).

"""

# --------------------------------R-5.6-----------------------------------------------

class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not -self._n <= k < self._n:
            raise IndexError('invalid index')
        if k >= 0:
            return self._A[k]
        else:
            return self._A[n+k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def insert(self, k, value):
        if self._n == self._capacity:
            B = self._make_array(2 * self._capacity)
            for i in range(self._n):
                if i < k:
                    B[i] = self._A[i]
                else:
                    B[i+1] = self._A[i]
                self._A = B
                self._capacity *= 2

        for j in range (self._n, k-1):
            self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1

# --------------------------------R-5.7-----------------------------------------------

def find_repeat(S):
    n = len(S)
    check = [None]*n #create an empty array of length S
    for item in S:
        if check[item]:    #check if the array at the item of S has a truthy value, if so this is our duplicate
            return item
        else:
            check[item] = 1 #if the array item is originally falsy, set it equal to 1

    return ('no duplicates')

print(find_repeat([1,2,3,4,4]))


# --------------------------------R-5.8-----------------------------------------------


N = [100, 1000, 10000]
results = pd.DataFrame()

for length in N:
    data = [None]*length
    start = time.time()
    for n in range(length):
        data.pop(0)
    end = time.time()

    results.loc["k = 0", N] = (end - start) / length

    data = [None] * length
    start = time.time()
    for n in range(length-1, 0, -1):
        data.pop(n // 2)
    end = time.time()

    results.loc["k = n // 2", N] = (end - start) / length

    data = [None] * length
    start = time.time()
    for n in range(length-1, 0, -1):
        data.pop(n)
    end = time.time()

    results.loc["k = 1", N] = (end - start) / length

print(results)


# --------------------------------R-5.9-----------------------------------------------

"""
The encoding and decoding list keys will have temp arrays of new length corresponding to the 
length of the respective alphabet used. The starting character, in the original case 'A' will be changed
to a starting reference character fo the given alphabet.
"""

# --------------------------------R-5.10-----------------------------------------------

class CaesarCipher:
    def __init__(self, shift):
        self._forward = [''.join(chr((k + shift) % 26 + ord('A'))) for k in range(26)]
        self._backward = [''.join(chr((k - shift) % 26 + ord('A'))) for k in range(26)]

# --------------------------------R-5.11-----------------------------------------------

def create_2d_list(array, rows):
    data = [array for j in range(rows)]
    return data

list_to_sum = create_2d_list([1,2,3], 3)

print(list_to_sum)

accumulator = 0
for i in range(len(list_to_sum)):
    for j in range(len(list_to_sum[0])):
       accumulator += list_to_sum[i][j]

print(sum)

# --------------------------------R-5.12-----------------------------------------------

"""
Use list comprehension to iterate through the minor lists upon which the built-in sum function can 
be invoked.
"""