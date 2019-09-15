# LOOPS

for a in range(2, 10, 2):  # start,end,increment
    print(a)

# break - in a range of 5 print 123
# continue- in a range of 5 print 1245

# sorting of list
bills = [1, 45, 3, 415]
bills.sort()
print(bills)
bills.reverse()
print(bills)
bills.sort(reverse=True)
print(bills)

bills.pop(2)  # deletes the element of the list with a particular index
print(bills)

# bills.remove(45) # deletes the element of the list with a particular value
# print(bills)


a = sorted(bills)  # imp to use a container
print(a)

for index, items in enumerate(bills, start=1):
    print(index, bills)

# tuples - list that can not be modified and has () instead of []


# sets have distinct values only with {}
groceries = {'milk', 'milk', 'lehom', 'almond'}
groc = {'milk', 'honey', 'milk', 'lehom'}

print('milk'in groceries)  # same can be done with list
groceries.add('added')  # add in sets
print(groceries)
print(groceries.intersection(groc))
print(groceries.difference(groc))
# similarly union can be dpne

# empty values

empty_list = []  # this cant be used to create empty tuples
emplty_list = list()

# similarly for tuples


# agruments with tuples and dictionaries
def students(*args, **kwargs):
    print(args)
    print(kwargs)


students('rohan', 'sharma', 'vihsal', 'senagr', jade='dop', value='shop')

name = ('rohan', 'sharma', 'vishal')
dict = {'rohan': 'smart', 'vihsal': 'chupa'}

students(name, dict)
students(*name, **dict)
