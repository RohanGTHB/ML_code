for _ in range(10):
    print('rohan')

    first_name = ('rohan', 'vishal', 'chetan')
last_name = ('sharma', 'sengar', 'garg')

name = zip(first_name, last_name)
print(name)

stocks = {'yahoo': 100, 'google': 200, 'facebook': 150, 'tesla': 50}

# print(min(stocks.values(),stocks.keys()))


print(list(map(lambda x: x * 2, {10, 30, 75})))

stocks = [
    {'mark': 'google', 'price': 123},
    {'mark': 'fb', 'price': 245},
    {'mark': 'tcs', 'price': 1223},
    {'mark': 'gant', 'price': 1323}
]


text = "To indicate short quotations four typed lines fewer of prose  three lines of verse  your text"\
    "enclose the quotation within double quotation marks Provide the author  specific page citation  the"\
    "case of verse, provide line numbers the text, include a complete reference on the Works Cited page."\
    "Punctuation marks such  periods, commas,  semicolons should appear after the parenthetical citation."\
    "Question marks  exclamation points should appear within the quotation marks they are a part of"\
    "the quoted passage but after the parenthetical citation  they are a part of your text"


words = text.split()
print(words)


def students(*args, **kwargs):
    print(args)
    print(kwargs)


students('rohan', 'sharma', 'vihsal', 'senagr', jade='dop', value='shop')

name = ('rohan', 'sharma', 'vishal')
dict = {'rohan': 'smart', 'vihsal': 'chupa'}

students(name, dict)
students(*name, **dict)

# video 22 conatain decimal/date/0 addition formatting


'''
# here i  am pssing a funciton(that takes arguments) as an argument to another function
# without using a decorator layering that was there
# ERROR
def wrapper_function(display_info,*args,**kwargs):
        print('Executed Before', display_info.__name__)
        result = display_info(*args, **kwargs)
        print('Executed After', display_info.__name__, '\n')
        return result

@wrapper_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('rohan',22)
'''


def fun(n):
    a = n * n

    def nuf():
        b = a * a
        print(b)
    return nuf()


fun(2)
# 1 here the output of the function is a funciton
# we can't write (print nuf) instead of (return nuf) coz we cant print functions, we (print,return) variable
# but when we retun a variable we dont get anything but the output in virtual memory till the time print the variable


def fun1(n):
    a = n * n

    def nuf1():
        b = a * a
        print(b)

    print(nuf1)


fun1(2)  # if we try to print the function without executing it (which is output of a function)
# we get it location,etc
# if we try to print the function with executing it (which is output of a function), we get none as output

#------------------------------------>
'''
def scope_test():

    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
'''
a = 10


def mun():
    a = 5

    def num():
        a = 3
        b = 4
        print(a)
        # return a
    print(a)
    num()
# print(a)


# print(a)---here a wont print coz a is defined in a function and has a lcoal namespace
 # variable scope is not here
 # the function has a local namespace
 # the main script has a global namespace
 # the modules have a diff. namespace
 # biultin namespace - class,def,.....(already there)

# namespace are stored as dict.(gloabal namespace)
# where a:key and 3:value ---bith of these will have same address(namespace)


import json


test_olly = '''
{
  "ecom" : {
    "classic" : {
      "names" : [ "flipkart", "snapdeal", "paytmmall", "zopper" ],
      "score" : 5
    },
    "premium" : {
      "names" : [ "amazonshopping", "amazonprime", "myntra", "netflix", "hotstar", "bookmyshow" ],
      "score" : 10
    }
  }
  }
'''

test1 = json.loads(test_olly)
print(type(test1))

for x in test1['ecom']['classic']:
    print(x)

#---------------------------->

# this is the same as corey's json since here ecom list has 2 obects, but here the objects are again nested with
# objects(dict) which does not allows us to call keys of each object


test_olly = '''
{
  "ecom" :[
  {
    "classic" : {
      "names" : [ "flipkart", "snapdeal", "paytmmall", "zopper" ],
      "score" : 5
    }
    },{
    "premium" : {
      "names" : [ "amazonshopping", "amazonprime", "myntra", "netflix", "hotstar", "bookmyshow" ],
      "score" : 10
    }
  }
  ]
}
'''

test1 = json.loads(test_olly)
print(type(test1))

for x in test1['ecom'][0]['classic']['names']:
    print(x)


import sys
print(sys.version)
print(sys.executable)
