#----------------------------------------------------------------------------------------------------------------

# Anjana Vakil
# "Using and abusing Python's double-underscore methods and attributes"
# EuroPython 2016
#
# License: Don't use this code for anything, ever! :)
# (But if you do, give credit where credit is due.)


# A dunder-ful class!
class StringyInt:

    # Basic dunders
    def __init__(self, value):
        '''The beloved constructor method!'''
        self.value = value

    def __str__(self):
        '''Returns a "user-friendly" string representation
        of the object, for e.g. printing.
        '''
        return "ZOMG it's {} y'all!!!".format(self.value)

    def __repr__(self):
        '''Returns a representation of self "as code",
        usually as something that Python
        could understand and evaluate.
        '''
        return str(self.value)

    # Operator overloading dunders
    def __add__(self, other):
        '''Called by the + operator on the left-hand object.'''
        new_value = int(str(self.value) + str(other.value))
        return StringyInt(new_value)

    def __mul__(self, other):
        '''Called by the * operator on the left-hand object.'''
        return StringyInt(int(str(self.value) * other.value))

    def __radd__(self, other):
        '''Called by the + operator on the right-hand object,
        if __add__ is not supported (for the given types)
        for the left-hand obj.
        '''
        return StringyInt(other).__add__(self)

    def __eq__(self, other):
        '''Called by ==, and also used for hashing
        keys into a dict (see __hash__ below).'''
        try:
            return self.value == other.value
        except AttributeError:
            return self.value == int(other)

    # Hashability dunder
    def __hash__(self):
        '''In combination with __eq__,
        makes the object hashable,
        e.g. for use as a key in a dict.
        Only for immutables!
        '''
        return self.value

    # Prevents creation of __dict__, saves time & space
    __slots__ = ('value')


# Some old dunder friends:
if __name__ == "__main__":
    # This block is executed only if the module is run
    # (not if it's imported)

    # Setting up some fun new objects to play with:
    one = StringyInt(1)
    two = StringyInt(2)
    three = StringyInt(3)

    # Run this module in interactive mode and play around!
# ________________________________________________________________________________________________________________________

print(one)  # we are able to print a customized string here because of the __str__ method present
# which gets called automatically. Just like __init__

print(two + one)  # we are able to use + in a customized way coz of the '__add__' method being there

print(two * one)  # we are able to use * in a customized way coz of the '__mul__' method being there

print(1 + one)  # we are able to use + in a customized way coz of the '__radd__' method being there
# radd allows us to add objects from 2 different classes.

print(1 == one)  # we are able to use = in a customized way coz of the '__eq__' method being there

dic = {'k1': one}  # we are able to create a key:value pair by using an object coz of the '__hash__' method being there
print(dic)
# ________________________________________________________________________________________________________________________
# ________________________________________________________________________________________________________________________

import random


def coin_flip():
    '''A little craziness helper.'''
    return random.random() > 0.5


class CrazyList:

    # Some basic dunders, again
    def __init__(self):
        self.values = []

    def __repr__(self):
        return str(self.values)

    # The craziness begins:
    def append(self, val):
        self.values.insert(random.randint(0, len(self.values)), val)

    # Dunders for length and truthiness
    def __len__(self):
        '''Called by `len()`, and can also be called
        by `if obj` if `__bool__` isn't defined.
        '''
        return random.randint(0, 2 * len(self.values))

    def __bool__(self):
        '''Called for e.g. `if obj: ...`'''
        return coin_flip()

    # Dunders for iterables
    def __iter__(self):
        '''Used for `for` loops, and can be used
        for membership tests (e.g. `if x in obj: ...`).
        '''
        print("__iter__ got called!")
        for _ in range(len(self)):
            yield random.choice(self.values) if coin_flip() else '?'

    def __str__(self):
        '''Our old friend for `print()` etc.'''
        # the `for` loop here uses `__iter__`
        return str([v for v in self])

    # Dunders for indexed/keyed objects
    def __getitem__(self, i):
        '''Called for obj[i] or obj[key],
        and can also be called by `for` loops
        or to test for membership (`x in obj`)
        if the object doesn't have
         `__iter__` and/or `__contains__`.
        '''
        return random.choice(self.values)

    def __setitem__(self, i, value):
        '''Used for obj[i] = x or obj[key] = value'''
        new_i = random.randint(0, len(self.values) - 1)
        self.values[new_i] = value

    # Dunder for membership
    def __contains__(self, item):
        '''Called by `x in obj`. Can be faster
        than the `__iter__`/`__getitem__` fallback.
        '''
        truth = item in self.values
        return truth if coin_flip() else not truth


if __name__ == "__main__":
    # A crazy little list for you to play with:
    l = CrazyList()
    for v in range(5):
        l.append(v)
# ________________________________________________________________________________________________________________________
print(l)  # this is happening coz we have tweaked the append function using random

print(len(l))  # we are able to call len() method coz we have defined a custom built __len__ method in the class

for x in l:  # we are able to iterate an object coz we have a cutomized build __iter__ in the method call
    print(x)


print(l[2])  # we are here able to get the indexed item coz __getitem__ method is in place


# similarly for contains you can do the same
print(2 in l)
