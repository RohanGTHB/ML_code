#list and dictionaries
'''
grocery = ['apple', 'banana', 'milk', 'honey']
print(grocery[1])
grocery[1] = 'shaih'
print(grocery)


bills = ['elect', 'water', 'light', 'rent']

# combination of list within a list

combine = [bills, grocery]
print(combine)

# selecting nested list items
print(combine[0][1])


# append,insert,sort,desort list
grocery.append('cake')  # isertion
print(combine)

grocery.insert(1, 'cake')  # insertion at a specified instance

print(grocery.extend(combine))  # extend

# grocery.sort()
grocery.reverse()
del grocery[2]  # delete

print(grocery)

combine2 = grocery + bills
print(combine2)
print(len(combine2))
# print(min(combine2))

# tuples
# almost a list but with non changing elements

tup = (1, 2, 3, 4)
list_of_tup = list(tup)
print(list_of_tup)

# similarly one can convert a list back to a tuple

new_tup = tuple(list_of_tup)
print(new_tup)

# dictionaries

# similar to a list but we can not add a dicitonary with a +
#  sign moreover it has a fixed key:value syntax

dict = {'rohan': 'smart', 'vishal': 'gent', 'chetan': 'chaman'}


print(dict['rohan'])  # 2 diff ways of doing things
print(dict.get('rohan'))

dict['rohan'] = 'clever'
# delete ,length etc

#usp-key and values
print(dict.keys())
dict.values()


# use of end in loops
for x in range(10):
    print(x, '', end="sv")

# while

i = 0

while(i <= 20):
    if i % 2 == 0:
        print(i)
    elif(i == 9):
        break
    else:
        i += 1
        continue
    i += 1

# handling strings
sent = "i am rohan sharma , i work in olly moreover i am learning to code"
print(sent[2:10])
print(sent[-10:])
print(sent.find("rohan"))
print(sent.replace("rohan", "sharma"))

print(list(sent))  # conversion into a list
print(sent.split(" "))
'''
'''
import json
from json import JSONEncoder

f = '{"fname": "/foo/bar"}'


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


MyEncoder().encode(f)
json.dumps(cls=MyEncoder)

'''

import pickle


class Animal:
    def __init__(self, number_of_paws, color):
        self.number_of_paws = number_of_paws
        self.color = color


class Sheep(Animal):
    def __init__(self, color):
        Animal.__init__(self, 4, color)


mary = Sheep("white")

print (str.format("My sheep mary is {0} and has {1} paws", mary.color, mary.number_of_paws))

my_pickled_mary = pickle.dumps(mary)

print ("Would you like to see her pickled? Here she is!")
print (my_pickled_mary)
