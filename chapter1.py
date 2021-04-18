import random
import math

#Reinforcement

#R - 1.1 - Write a short Python function, is_multiple(n, m), that takes two integer values and returns True
#if n is a multiple of m, that is, n=mi for some integer i, and Fale otherwise.

def is_multiple(n, m):
    if n % m == 0:
        return True
    return False

#R - 1.2 - Write a short Python function, is_even(k), that takes an integer value and return True if k is even,
# False otherwise. However your function cannot use the multiplication, modulo, or division operators.

def is_even(k):
    if (k ^ 1 == k + 1): #notice that the bitwise exclusive-or with 1 increments a number by 1 if odd, and decrements if even
        return True
    return False

#R - 1.3 - Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and
# returns the smallest and largest numbers, in the form of a tuple of length two. Do not use the built-in functions min
# max in implementing your solution.

def minmax(data):
    min = max = data[0]
    for item in data:
        if item > max:
            max = item
        if item < min:
            min = item
    return(min, max)

#R - 1.4 - Write a short Python function that takes a positive integer n and returns the sum of teh squares of all the
# positive integers smaller than n.

def sum_of_squares_up_to(n):
    return sum((k * k for k in range(1, n)))

#R - 1.5 - Do 1.4 with comprehension (already done)

#R - 1.6 - Write a short Python function that takes a positive integer n and returns the sum of the squares of all
# the odd positive integers smaller than n.

def sum_of_odd_squares_up_to(n):
    return sum((k * k for k in range(1, n, 2)))

#R - 1.7 - Do 1.6 with comprehension (already done)

#R - 1.8 - Python allows negative integers to be used as indeces into a sequence, such as a string. If string s has
# length n, and expression s[k] is used for index -n <= k <= 0, what is the equivalent index j >= 0 such that
# s[j] references the same element?

print('n + k')

#R - 1.9 - What paramaters shoudl be sent to the range constructor to produce a range with values 50, 60, 70, 80?
a = list(range(50, 90, 10))

print(a)

#R - 1.10 - What paramaters shoudl be sent to the range constructor to produce a range with values 8, 6, 4, 2, 0, -2, -4, -6, -8?
a = list(range(8, -10, -2))

print(a)

#R - 1.11 - Demonstrate how to use Python's list comprehension sytax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256]

list = [2 ** k for k in range(0,9)]
print(list)

#R - 1.12 - Python's random module includes a funciton choice(data) that returns a random element from a non-empty
# sequence. The random module includes a more basic function randrange, with parameterization similar ot the built-in
# range function, that return a random choice from teh given range. Using only the randrange function, implement your
# own version of the choice function.

def choice(data):
    return data[random.randrange(0, len(data))]

# Creativity

# C - 1.13 - Write a pseudo-code description of afunciton that reverses a uist of n integers, so that the numebrs are listed
# in the opposite order.

def reverse(list):
    new_list = []
    for i in range(len(list)-1, -1, -1):
        print(i)
        new_list.append(list[i])
    return new_list


# C - 1.14 - write a function that takes a sequence of integer valies and determines if there is a distinct pair of numbers
# in the sequence whose product is odd.

def is_odd_product(list):
    counter = 0
    for item in list:
        if not is_even(item):
            counter += 1
    if counter >= 2:
        return True
    else:
        return False



# C - 1.15 - write a function that takes a sequence of integers and determines if all the numbers are unqiue.

def all_items_unique(list):
    counter = 0
    for i in range(0, len(list)):
        for j in range(0, len(list)):
            if i != j and list[i] == list[j]:
                counter += 1
    if counter > 0:
        return False
    else:
        return True






# C - 1.16 - In our implementation of the scale function (page 25), the body of the loop executes the command data[j] *= factor
# We have discussed that numeric types ar immutable and that the use of the *= operator in this context causes the
# creation of a new instance (not the mutation of an existing instance). How is it then that our implementation of scale
#changes the actual parameter sent by the caller.

print("list types are mutable, even if they are a sequence of immutable types")

#C - 1.17 - Had we implemented the scale function with val *= factor, would it still work?

print("no because val is presumably an immutable type, so the *= operator would create a new instance of val")

# C - 1.18 - Demonstate how to use Python's list comprehension syntax to produce the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]

list = [k * (k + 1) for k in range(0,10)]
print(list)

# C - 1.19 - Demonstrate how to use Python's list comprehension syntax to generate a list of individual alphabet characters

list = [chr(k) for k in range (97, 123)]


# C - 1.20 - Python's random module includes a function shuffle(data) that accepts a list of elements and randomly reorders the elements
# so that each possible order occurs with equal probability. The random module includes a more basic function randint(a, b)
# that returns a uniformly random integer from a to b (including both endpoints). Using only the randint function,
# implement your own  version of the shuffle function.

list = [1,2,3,4,5]

def reorder_list(list):
    new_list = []
    for i in range(0, len(list)):
        place = random.randint(0, len(list)-1)
        new_list.append(list[place])
        list.pop(place)
    return new_list

print(reorder_list([1,2,3,4,5]))



# C - 1.21 - Write a python program that repeatedly reads lines from standard input until
# an EOFError is raised, and then outputs those lines in reverse order.

def reverse_lines(file):
    reverse_list = []
    fp = open(file)
    lines = fp.readlines()
    for i in range(len(lines) - 1, -1, -1):
        reverse_list.append(lines[i])
    print(reverse_list)

# C - 1.22 - Write a short Python program that takes two arrays a and b of length n int values, and returns
# the dot product of a and b. That is, it returns an array of c of length n such that c[i] = a[i] + b[i]

def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError('Input lists must be of same length')
    dot_product = []
    for i in range(0, len(a)):
        dot_product.append(a[i] * b[i])
    return dot_product

# C - 1.23 - Write a code fragment that attempts to write an element to a list based on an index
# that may be out of bounds.

#some procedure with list...
print("raise IndexError(Don't try buffer overflow attacks in Python)")

# C - 1.24 - Write a python function that counts the number fo vowels in a string

def count_vowels(string):
    counter = 0
    ascii_vowels = ['a', 'e', 'i', 'o', 'u']
    for char in string:
        if char in ascii_vowels:
            counter += 1
    return counter

# C - 1.25 - Write a python fucntion that takes a string resembling a sentence and removes all
# punctuation and returns the amended string.

def remove_punctuation(string):
    punctuation = ['"', "'", '.', ',', '?', "!", "-"]
    new_string_list = []
    for i in range(0, len(string)):
        if string[i] not in punctuation:
            new_string_list.append(string[i])
    return new_string_list

# C - 1.26 - Take 3 integers as arguments from the console and decide whether they meet some equation of your choice

def do_nums_fit_equation():
    reply = input("enter integrers a, b, c seperated by spaces")
    nums = reply.split()
    a = int(nums[0])
    b = int(nums[1])
    c = int(nums[2])
    if a + b == c:
        print("True")
        return True
    else:
        print("False")
        return False


# C - 1.27 - In section 1.8, we provided three different implementations of a
# generator that computes factors of a given integer. The third of those implementations
# from page 41, was the most efficient, but it noted that we did not yield the
# factors in increasing order. Modify the generator so that it reports the items in order.

def factors(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            if k > n // k:
                yield n // k
            else:
                yield k
        k += 1
    if k * k == n:
        yield k

    k = math.floor(math.sqrt(n)) - 1
    while k > 0:
        if n % k == 0:
            if k < n // k:
                yield n // k
            else:
                yield k
        k -= 1


# C - 1.28 - The p-norm of a vector v = (v1, v2, ..., vn) is n-dimensional space is defined as p-root of
# (v1 ** p + v2 ** p + ... + vn ** p). For the special case of p = 2, this results in the traditional Euclidean norm,
# which represents the length of a vector. Give an implementation of a function named norm such that norm(v, p) returns
# the p-norm value of v and norm(v) returns the Eucliden norm of v. You may assume v is a list of numbers.

def norm(v, p=2):
    sum = 0
    for i in range(0, len(v)):
        sum += v[i] ** p
    return sum ** (1/p)

print(norm([1,2]))