# STRINGS

# upper/count/find are the attributes of 'str' class and 'a' is a string object

a = ''' my name is rohan sharma
i am trying to learn python'''
print(a)  # similarly we can use double quotes as well for multi-line strings

# print(a.size())
print(a.upper())
# print(help(a))
print(a.lower())
print(a.count('rohan'))  # this is counted as 1
print(a.count('t'))  # this is counted as 3 coz we have 3 't'
print(a.find('n'))  # this is instance where we find 't'
print(a[31])
print(a.find('john'))  # returns -1 if the string doesnot exist
print(a.replace('rohan sharma', 'john don'))
a = 'rohan'
b = 'sharma'
print (a + ' ' + b)  # cumbersome for long strings
print('{} {}'.format(a, b))
print(f'{a}, {b}')  # this is f string , available only for python>3.6
print(dir(a))  # gives us all the functions(methods,attributes) available for a variable
# print(help(str)) #help is only for predefined functions or maybe classes
                    #wont work with upper()/lower() because they are functions of object(a)[a is object of str class]

emp_str_1 = 'John-Doe-70000'
first, last, name = emp_str_1.split('-')  # split
print(first, last, name)

a = '   strip'
print(a.strip())

b = '****strip*'
print(b.strip('*'))

print('st' in a)  # to check whether a substring is a part of a string or


# INTEGER/FLOATS

print(abs(-3))
print(round(2.501, 2))
print(round(3.75, 1))

print(3 == 2)  # = is for assignment, == for comparison

num = '3'
print (num * 2) # since num is a string object
print(int(num) * 2)  # int just like str

#-------------------------------------------------------------------------------------->>>>>>>>>>>>.

# STRINGS

str = {'name': 'rohan', 'age': 23}

# 1
tup = 'my name is {0} and my age is {1} and my friend age is {1}'.format(str['name'], str['age'])
print(tup)

# 2
tup = 'my name is {0[name]} and my age is {1[age]} and my friend age is {1[age]}'.format(str, str)
print(tup)  # here we have 0,1 because we have 2 references (str,str)

# 3
tup = 'my name is {0[name]} and my age is {0[age]} and my friend age is {0[age]}'.format(str)
print(tup)

# 4 for a list
list1 = ['rohan ', 23]
tup = 'my name is {0[0]} and my age is {0[1]} and my friend age is {0[1]}'.format(list1)
print(tup)

# 5 with classes


class rohan1():
    def __init__(self, name, age):
        self.naam = name
        self.umar = age


p1 = rohan1('roh', 22)

sen = 'my name is {0.naam} and age is {0.umar}'.format(p1)
print(sen)

# 6 with keyword arguments
tup = 'my name is {name} and my age is {age} and my friend age is {age}'.format(name='rohan', age=22)
print(tup)
