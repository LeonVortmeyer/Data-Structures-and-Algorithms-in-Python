from abc import ABCMeta, abstractmethod


# ------------------------R2-1----------------------------
"""
1) Self-driving cars

2) Water filtration

3) Life-sustaining medical devices

"""


# ------------------------R2-2----------------------------
"""
Software that relies on integration with web browsers (like extensions). Functionality must be supported
by a diversity of browsers and must be adaptable to upcoming changes in its environment.
"""

# ------------------------R2-3----------------------------
"""
Save As:
- Check if file already exits
- Handle user confirmation to override a file if it already exists
- Write data to the file
"""

# ------------------------R2-4----------------------------

class Flower:
    def __init__(self, name = None, petals = None, price = None):
        self._name = name
        self._num_petals = petals
        self._price = price

    def get_name(self):
        return self._name

    def get_num_petals(self):
        return self._num_petals

    def get_price(self):
        return self._price

    def set_name(self, name):
        self._name = str(name)

    def set_petals(self, petals):
        self._name = int(petals)

    def set_name(self, price):
        self._name = float(price)

Sun = Flower('Sunflower', 25, 8.50)

print(Sun.get_name(), Sun.get_num_petals(), Sun.get_price())

# ------------------------R2-5----------------------------

class CreditCard():
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def set_balance(self, value):
        self._balance = value

    def charge(self, charge):
        try:
            charge = float(charge)
        except:
            print('price argument must be an integer, float, or string representing an int / float')
            return False
        if charge + self._balance > self._limit:
            print(f'Your deposit of {charge} exceeds your remaining balance: {self.get_limit() - self.get_balance()}')
            return False
        else:
            self._balance += charge
            return True

    def make_payment(self, payment):
        try:
            payment = float(payment)  # This will accept an int, float or string that can be converted to a float
        except:
            print('price argument must be an integer, float, or string representing an int / float')
            return False
        self._balance -= payment
        return True

# ------------------------R2-6----------------------------

class CreditCard():
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def set_balance(self, value):
        self._balance = value

    def charge(self, charge):
        try:
            charge = float(charge)
        except:
            print('price argument must be an integer, float, or string representing an int / float')
            return False
        if charge + self._balance > self._limit:
            print(f'Your deposit of {charge} exceeds your remaining balance: {self.get_limit() - self.get_balance()}')
            return False
        else:
            self._balance += charge
            return True

    def make_payment(self, payment):
        try:
            payment = float(payment)  # This will accept an int, float or string that can be converted to a float
        except:
            print('price argument must be an integer, float, or string representing an int / float')
            return False

        if payment < 0:
            raise ValueError('Payments must be positive in value')

        self._balance -= payment
        return True

# ------------------------R2-7----------------------------
class CreditCard():
    def __init__(self, customer, bank, acnt, limit, bal=0):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = bal # we add bal as an optional 5th parameter for the CreditCard instance w default value = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def set_balance(self, value):
        self._balance = value

    def charge(self, charge):
        try:
            charge = float(charge)
        except:
            print('price argument must be an integer, float, or string representing an int / float')
            return False
        if charge + self._balance > self._limit:
            print(f'Your deposit of {charge} exceeds your remaining balance: {self.get_limit() - self.get_balance()}')
            return False
        else:
            self._balance += charge
            return True

    def make_payment(self, payment):
        try:
            payment = float(payment)  # This will accept an int, float or string that can be converted to a float
        except:
            print('price argument must be an integer, float, or string representing an int / float')
            return False

        if payment < 0:
            raise ValueError('Payments must be positive in value')

        self._balance -= payment
        return True

# ------------------------R2-8----------------------------


wallet = []
wallet.append(CreditCard('John Bowman', 'California Savings', '56 5391 0375 9387 5309', 2500))
wallet.append(CreditCard('John Bowman', 'California Federal', '3485 0399 3395 1954', 3500))
wallet.append(CreditCard('John Bowman', 'California Finance', '5391 0375 9387 5309', 5000))


for val in range(1, 59): #extended range to 59 to bring credit card 3 over its limit.
    wallet[0].charge(val)
    wallet[1].charge(2 * val)
    wallet[2].charge(3 * val)

for c in range(3):
    print('Customer = ', wallet[c].get_customer())
    print('Bank = ', wallet[c].get_bank())
    print('Account = ', wallet[c].get_account())
    print('Limit = ', wallet[c].get_limit())
    print('Balance = ', wallet[c].get_balance())

    while wallet[c].get_balance() > 100:
        wallet[c].make_payment(100)
        print('New Balance = ', wallet[c].get_balance())
    print()

# ------------------------R2-9----------------------------
class Vector:
    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        try:
            self._coords[j] = val
            return True
        except:
            print('Invalid input or index')
            return False

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must match')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must match') #same implementation as add here to confirm vector dimension
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

v1 = Vector(5)
v2 = Vector(5)

for i in range(5):
    v1[i] = 6
    v2[i] = 3

print(v1 - v2)

# ------------------------R2-10----------------------------
class Vector:
    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        try:
            self._coords[j] = val
            return True
        except:
            print('Invalid input or index')
            return False

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must match')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must match') #same implementation as add here to confirm vector dimension
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * -1
        return result

v1 = Vector(5)

for i in range(5):
    v1[i] = 6

print(-v1)

# ------------------------R2-11----------------------------
"""
A method __radd__(self, other) must be added to the class definition.
"""

# ------------------------R2-12----------------------------
class Vector:
    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        try:
            self._coords[j] = val
            return True
        except:
            print('Invalid input or index')
            return False

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must match')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must match') #same implementation as add here to confirm vector dimension
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * -1
        return result

    def __mul__(self, factor):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * factor
        return result


v1 = Vector(5)

for i in range(5):
    v1[i] = 6

print(v1 * 3)

# ------------------------R2-13----------------------------
class Vector:
    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        try:
            self._coords[j] = val
            return True
        except:
            print('Invalid input or index')
            return False

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must match')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must match') #same implementation as add here to confirm vector dimension
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * -1
        return result

    def __mul__(self, factor):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * factor
        return result

    def __rmul__(self, factor):
        return (self * factor)

v1 = Vector(5)

for i in range(5):
    v1[i] = 6

print(3 * v1)


# ------------------------R2-14----------------------------
class Vector:
    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        try:
            self._coords[j] = val
            return True
        except:
            print('Invalid input or index')
            return False

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must match')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must match') #same implementation as add here to confirm vector dimension
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * -1
        return result

    def __mul__(self, factor):
        if type(factor) == int or type(factor) == float:
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * factor
            return result
        else:
            if len(factor) != len(self):
                raise ValueError('Vectors must be of same length to apply dot product')
            dot_product = 0
            for i in range(len(self)):
                dot_product += self[i] * factor[i]
            return dot_product

    def __rmul__(self, factor):
        return (self * factor)

v1 = Vector(5)
v2 = Vector(5)

for i in range(5):
    v1[i] = 2
    v2[i] = 3


print(v1 * 3)
print(v1 * v2)

# ------------------------R2-15----------------------------
class Vector:
    def __init__(self, d):
        if type(d) == int:
            self._coords = [0] * d
        else:
            self._coords = d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        try:
            self._coords[j] = val
            return True
        except:
            print('Invalid input or index')
            return False

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must match')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must match') #same implementation as add here to confirm vector dimension
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * -1
        return result

    def __mul__(self, factor):
        if type(factor) == int or type(factor) == float:
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * factor
            return result
        else:
            if len(factor) != len(self):
                raise ValueError('Vectors must be of same length to apply dot product')
            dot_product = 0
            for i in range(len(self)):
                dot_product += self[i] * factor[i]
            return dot_product

    def __rmul__(self, factor):
        return (self * factor)

v1 = Vector(5)
v2 = Vector([1,2,3,4,5])

for i in range(5):
    v1[i] = 2


print(v1 * 3)
print(v1 * v2)

# ------------------------R2-16----------------------------
"""
To first give a couple of examples, range(1,5,1) = [1, 2, 3, 4]

5 - 1 + 1 - 1 // 1 = 4

If step = 1, the formula just reduces to stop - start.

Now consider the same range, but step = 2; range(1,5,1) = [1, 3]

5 - 1 + 2 - 1 // 2 = 2

Here, we remove 1 from step to assure that we don't traverse over stop. Without removing 1 from step, the range length
will be overestimated by 1.

"""

# ------------------------R2-17----------------------------

""" 
a)

Class Object:

Class Goat (extends Object):
Fields: _tail
Behaviors: milk(), jump()

b)

Class Object:

Class Pig (extends Object):
Fields: _nose
Behaviors: eat(food), wallow()

c)

Class Object:

Class Horse (extends Object):
Fields: _height, _color
Behaviors: run(), jump()

d)

Class Object:

Class Racer (extends Horse):
Fields:
Behaviors: race()

e)

Class Object:

Class Equestrian (extends Horse):
Fields: _weight
Behaviors: trot(), is_trained()


"""

# ------------------------R2-18----------------------------
class Progression():

    def __init__(self, start=0):
        self._current = start


    def _advance(self):
        self._current += 1


    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer


    def __iter__(self):
        return self


    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))


class Fibonacci(Progression):
    def __init__(self, first=0, second=1):
        self._current = first
        self._prev = second - first

    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current

fib = Fibonacci(2,2)
fib.print_progression(8)

# ------------------------R2-19----------------------------
class Progression():

    def __init__(self, start=0):
        self._current = start


    def _advance(self):
        self._current += 1


    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer


    def __iter__(self):
        return self


    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression):
    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment


    def _advance(self):
        self._current += self._increment

p = ArithmeticProgression(128, 0)

counter = 0
while p._current < 2 ** 63:
    p._advance()
    counter += 1
print(counter)

# ------------------------R2-20----------------------------
"""
Primarily namespace conflicts in nested classes overriding methods of parent classes.
"""

# ------------------------R2-21----------------------------

"""
Any changes to the Z class will spread to all of its subclasses. 
"""

# ------------------------R2-22----------------------------

class Sequence(metaclass = ABCMeta):
    @abstractmethod
    def __len__(self):
        pass
    @abstractmethod
    def __getitem__(self, j):
        pass

    def __contains__(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return True
            return False

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for j in range(len(self)):
            if self[j] == other[j]:
                return False
            return True

    def index(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('value not in sequence')

    def count(self, val):
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
            return k


# ------------------------R2-23----------------------------
class Sequence(metaclass=ABCMeta):
    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __getitem__(self, j):
        pass

    def __contains__(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return True
            return False

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for j in range(len(self)):
            if self[j] == other[j]:
                return False
            return True

    def __lt__(self, other):
        for j in range(len(self)):
            if self[j] < other[j]:
                return True
            return False

    def index(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('value not in sequence')

    def count(self, val):
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
            return k

# ------------------------C2-24----------------------------

