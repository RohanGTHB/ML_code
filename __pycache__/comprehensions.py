
# slicing of list
grocery = ['apple', 'banana', 'milk', 'honey']
print(grocery[1:4:-1])  # here we have increment as well

# COMPREHENSIONS
rohan = [1, 2, 3, 4]

# LIST COMPREHENSIONS

# if using with for  loop we have to use append

# append vs extend
# append is used to add elements to a list [1,2,3,[4,5,6]]
# extend simply adds all the elements of a list to a list [1,2,3,4,5,6]

my_list = []
for n in rohan:
    my_list.append(n * n)  # similarly for sets use 'add' for sets
print(my_list)

my_list = [n * n for n in rohan]  # to print squares of a num
print(my_list)

my_list = [n for n in rohan if n % 2 == 0]  # you can also use if statemnt
print(my_list)

# list comprehension with combination of iems


my_list = [(letter, num) for letter in 'abcd' for num in range(4)]  # instead of using nested loops
print(my_list)


# instead of using for loops
my_list = [n * n for n in rohan]
print(my_list)

v = tuple(map(lambda n: n * n, rohan))
print(v)

y = [n * n for n in rohan if n % 2 == 0]
print(y)
'''
x = tuple(filter(map(lambda n:n%2==0,rohan)) # used for filtering values
print(x)
'''

# DICTIONARY COMPREHENSIONS

list1 = ['rohan', 'vishal', 'chetan']
list2 = ['smart', 'gent', 'chupa']

my_dict = {name: char for name, char in zip(list1, list2)if name != 'chetan'}
print(my_dict)

# SETS COMPREHENSIONS
# same as lists

# SORTING

groceries = [1, 2, 3, 89, 16, 22]
gsort = sorted(groceries, reverse=True)  # descending sorting
print(gsort)

groceries.sort()  # .sort returns null
print(groceries)
#.sort() this method cant be applied to tuples and dictionaries

# sorting based on a key

list1 = [-5, -1, 3, 4, 6, -9]
sort_list = sorted(list1, key=abs)  # key is used to assign already defined abs function
print(sort_list)


# generator comprehension
my_list = (n * n for n in [1, 2, 3, 4, 5, 6])

for x in my_list:
    print(x)

# generator doesnot hold all the values, we have to ask for each value to print them out mainly by looping or using NEXT state.my_list
