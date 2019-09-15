#STRINGS

a = ''' my name is rohan sharma
i am trying to learn python'''
print(a)  #similarly we can use double quotes as well for multi-line strings

print(a.upper())
print(a.lower())
print(a.count('rohan')) #this is counted as 1
print(a.count('t'))  # this is counted as 3 coz we have 3 't'
print(a.find('n'))  #this is instance where we find 't'
print(a[31])
print(a.find('john')) #returns -1 if the string doesnot exist
print(a.replace('rohan sharma', 'john don'))
a = 'rohan'
b = 'sharma'
print (a+' '+ b) #cumbersome for long strings
print('{} {}'.format(a,b))
print( f'{a}, {b}') #this is f string , available only for python>3.6
print(dir(a)) #gives us all the functions(methods,attributes) available for a variable
#print(help(str)) #help is only for predefined functions

emp_str_1 = 'John-Doe-70000'
first,last,name = emp_str_1.split('-') #split
print(first,last,name)

a = '   strip'
print(a.strip())

b = '****strip*'
print(b.strip('*'))

print('st' in a) #to check whether a substring is a part of a string or

#--------------------------------------------------------------------------------------------------->

#INTEGER/FLOATS

print(abs(-3))
print(round(2.501,2))
print(round(3.75,1))

print(3 == 2) # = is for assignment, == for comparison

num = '3'
print (num *2)
print(int(num)*2) #int just like str


#------------------------------------------------------------------------------------------------------>


#DICTIONARY

dict = {'rohan': 'smart', 'vishal': 'gent', 'chetan': 'chaman'}
print(dict['rohan'])
print(dict.get('rohan')) #allows to return none when we check for key which doesn exist instead of error

#changing values

dict['rohan'] = 'angry'
print(dict)

print(dict.keys())
print(dict.items())

for key,value in dict.items(): #looping in dictionary # key,value can be anything (x,y) for ex.
    print(key,value)

#-------------------------------------------------------------------------------------------------->

#LOOPS

for a in range(2, 10, 2):  #start,end,increment
    if a==6:
        print('continue/break')
        break
    print(a)

#break - in a range of 5 print 123
#continue- in a range of 5 print 1245

#sorting of list
bills = [1,45,3,415]
bills.sort()
print(bills)
bills.reverse()
print(bills)
bills.sort(reverse=True)
print(bills)

bills.pop(2) # deletes the element of the list with a particular index
print(bills)

#bills.remove(45) # deletes the element of the list with a particular value
#print(bills)


a = sorted (bills) #imp to use a container
print(a)

for x, y in enumerate(bills, start=1): # x is taken as index/ 'y' is taken as value
    print(x, y)

#tuples - list that can not be modified and has () instead of []

#--------------------------------------------------------------------------------------->

#sets have distinct values only with {}
groceries = {'milk', 'milk', 'lehom','almond'}
groc = {'milk', 'honey', 'milk', 'lehom'}

print('milk'in groceries) #same can be done with list
groceries.add('added') #add in sets
print(groceries)
print(groceries.intersection(groc))
print(groceries.difference(groc))
#similarly union can be dpne

#empty values

empty_list = [] #this cant be used to create empty tuples
emplty_list =list()

#similarly for tuples


#agruments with tuples and dictionaries
def students(*args,**kwargs):
    print(args)
    print(kwargs)

students('rohan','sharma','vihsal','senagr',jade='dop',value='shop')

name = ('rohan','sharma','vishal')
dict = {'rohan':'smart','vihsal':'chupa'}

students(name,dict)
students(*name,**dict)

#----------------------------------------------------------------------------------------------->

#SCOPE OF VARIABLE
#LEGB - LOCAL,ENCLOSED (FROM SOME OUTER),GLOBAL,BUILT IN

x='i am global'
def scope():
    global x  #global allows to set value of variable in gloabl scope('i am global') here is set as
                # x = 'i am local' and then whenever we  call print('x') in global scope it will take
                #set up values.
    x= 'i am local '
    print(x)

print(x) #taking valuues from global coz of LEGB rule
scope() #taking x locally from function coz of rule

y='i am global'
def scope_y():
    #y= 'i am local '
    print(y)

scope_y() #here it is taking values from global coz no value is in local domain

#builtin vs global
list = [1,2,3,5]

def min():
    pass

#print(min(list)) - here min function wont run coz preference is given to global functions before built in functions

# enclosed vs local vs global

#print(dir.(builtins)) --- contains all the predefned attributes of python

# Namespaces are created at different moments and have different lifetimes.
# The namespace containing the built-in names is created when the Python interpreter starts up,
#  and is never deleted. The global namespace for a module is created when the module definition is read in;
#  normally, module namespaces also last until the interpreter quits.
# The statements executed by the top-level invocation of the interpreter,
#  either read from a script file or interactively, are considered part of a module called __main__,
# so they have their own global namespace.
# (The built-in names actually also live in a module; this is called builtins.)

#The local namespace for a function is created when the function is called,
#  and deleted when the function returns or raises an exception that is not handled within the function.

a = 'global'
def outer():
    #global a
    a =  'outer'

    def middle():
        #nonlocal a
        #global a
        a= 'middle'
        print(a)


        def inner():
            #nonlocal a    # non local simply allows you to set value of variable outside local but inside
            #global a      #global scope in case of nested functions
            a = 'inner'    # here a in nonlocal(middle)  is set to inner
            print(a)

        inner()
    middle() #this will give us 'middle ' if no nonlocal is used in inner
    print(a)

outer()
print(a) # this will give us 'global' if no global is used in nested function

#------------------------------------------------------------------------------------------------->

#slicing of list
grocery = ['apple', 'banana', 'milk', 'honey']
print(grocery[1:4:-1]) # here we have increment as well

# COMPREHENSIONS
rohan =[1,2,3,4]

#LIST COMPREHENSIONS

#if using with for  loop we have to use append

# append vs extend
#append is used to add elements to a list [1,2,3,[4,5,6]]
#extend simply adds all the elements of a list to a list [1,2,3,4,5,6]

my_list =[]
for n in rohan:
    my_list.append(n*n) #similarly for sets use 'add' for sets
print(my_list)

my_list = [n*n for n in rohan] #to print squares of a num
print(my_list)

my_list = [n for n in rohan if n%2==0] #you can also use if statemnt
print(my_list)

#list comprehension with combination of iems


my_list = [ (letter,num) for letter in 'abcd' for num in range (4)] #instead of using nested loops
print(my_list)



#instead of using for loops
my_list = [n*n for n in rohan]
print(my_list)

v = tuple(map(lambda n:n*n,rohan))
print(v)

y = [n*n for n in rohan if n%2==0]
print(y)
'''
x = tuple(filter(map(lambda n:n%2==0,rohan)) # used for filtering values
print(x)
'''

# DICTIONARY COMPREHENSIONS

list1 = ['rohan','vishal','chetan']
list2 = ['smart','gent','chupa']

my_dict = {name:char for name,char in zip(list1,list2)if name != 'chetan'}
print(my_dict)

#SETS COMPREHENSIONS
#same as lists

#SORTING

groceries = [1,2,3,89,16,22]
gsort = sorted(groceries, reverse =True) #descending sorting
print(gsort)

groceries.sort() #.sort returns null
print(groceries)
#.sort() this method cant be applied to tuples and dictionaries

#sorting based on a key

list1= [-5,-1,3,4,6,-9]
sort_list = sorted(list1, key=abs) #key is used to assign already defined abs function
print(sort_list)


# sorting of dictionary
stocks = {'yahoo':100,'google':200,'facebook':150,'tesla':50}

print(sorted(zip(stocks.values(),stocks.keys())))  #here in this case priority is given to order of zipping
print(sorted(zip(stocks.keys(),stocks.values())))

#-------------------------------------------------------------------------------------------->

#example
#sorting in classes
'''
class Test():
    def __init__(self,name,age,salary):
        self.naam = name
        self.umar = age
        self.baiten = salary


    def fuk(self):
        return '{} {} {}'.format(self.naam,self.umar,self.baiten)

def kuf(emp):
    return emp.umar



emp1 = Test('rohan',22,20000)
emp2 = Test('sengar ',23,15000)
emp3 = Test('john',16,13114)

employ = [emp1,emp2,emp3]
print(emp1.fuk())

sort1 =sorted(employ,key = kuf)
print(sort1)
'''

#---------------------------------------------------------------------------------------------->

#STRINGS

str = {'name' :'rohan' , 'age' : 23}

#1
tup = 'my name is {0} and my age is {1} and my friend age is {1}'.format(str['name'], str['age'])
print(tup)

#2
tup ='my name is {0[name]} and my age is {1[age]} and my friend age is {1[age]}'.format(str,str)
print(tup) #here we have 0,1 because we have 2 references (str,str)

#3
tup ='my name is {0[name]} and my age is {0[age]} and my friend age is {0[age]}'.format(str)
print(tup)

#4 for a list
list1 = ['rohan ',23]
tup ='my name is {0[0]} and my age is {0[1]} and my friend age is {0[1]}'.format(list1)
print(tup)

#5 with classes

class rohan1():
    def __init__(self,name,age):
        self.naam  = name
        self.umar = age

p1  = rohan1('roh',22)

sen = 'my name is {0.naam} and age is {0.umar}'.format(p1)
print(sen)

#6 with keyword arguments
tup ='my name is {name} and my age is {age} and my friend age is {age}'.format(name = 'rohan',age = 22 )
print(tup)

#-------------------------------------------------------------------------------------------------->

#NAMED TUPLES



from collections import namedtuple

y = namedtuple('x', ['red', 'green', 'blue'])

x= y(55,155,255)
#white = Color(255,255,255)

print(x.blue)
#print(x['red']) #- dont know why not working
print(x[0])

#GENERATOR
list = []
for n in [1,2,3,4,5,6]:
    list.append(n*n)
print(list)

#GENERATOR
def square (num):
    for n in num:
        yield n*n

y  = square ([1,2,3,4,5])
for x in y:
    print(x)

#generator comprehension
my_list = (n*n for n in [1,2,3,4,5,6])

for x in my_list:
    print(x)

#generator doesnot hold all the values, we have to ask for each value to print them out mainly by looping or using NEXT state.my_list

#RANDOM

import random
value = random.random()
print(value) #prints a random value bw 0-1
value = random.uniform(1,10) #prints float
value =  random.randint(1,10) #prints integer



greet = ['hi','hey','yo']
value = random.choice(greet)
print(value + 'rohan')

greet = ['hi','hey','yo'] #same can be done with tuple
value = random.choices(greet,weights = [10,10,2], k =10) #gives the looping parameter and weight
print(value)


list=[]
list= tuple(range(1,50))
value = random.sample(list,k=5)
print(list)


#FIRST CLASS or HIGHER ORDER FUNCITON
#functions that can be assigned to a variable , can be entered as argument,can be returned as a result of a function

def cube(x):
       return x*x*x

f= cube
print(cube)  #fucn wont execute without closure
print(f)    #declaring funciton without closure means that function stays but does not execute
print(f(4))

#function as arg

def square1(x):
    return x*x

def first_class(fun,li):
    list1=[]
    for n in li:
        list1.append(fun(n))
    return list1

map_ = first_class(square1,[1,2,3,4] ) #here square1 has no closure coz that would make it run
print(map_)   #but that is not the purpose coz it will run only when it reaches list.append........



#CLOSURE
# function result of a funciton-----THIS IS A CLOSURE
# A CLOSURE IS AN INNER FUNCTION WHICH HAS ACCESS TO ITS VARIABLES IN ITS LOCAL SCOPE EVEN WHEN OUTER FUN HAS FINISHED OPERATING

def html_tag(tag): #this function returns another function as a return

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text  # HERE WE DONT HAVE () OHTER WISE WE WOULD HAVE had an error suggestung 1 missing agr[msg]


print_h1 = html_tag('h1') #as mentioned html funciton returns wrap_text
print(print_h1.__name__) #this shows that the var. has stored the function wrap_text
print(print_h1)    #here print_h1 is equivalent to wrap_text funnction (function result of a funciton)
print_h1('Test Headline!') #since this is wrap text, it still remembers tag value eneterd earlier in this
print_h1('Another Headline!')

#MUTABLE[LIST] AND IMMUTABLE[STRING] -


#DECORATER

def decorter_f(orig_f):
    def wrapper_f(*args,**kwargs):
        print('wrapper executed this before {}'.format(orig_f.__name__))
        return orig_f(*args,**kwargs) #we dont need a return here coz function has a print statement,so its already
    return wrapper_f                     #returning something #we can remove return

#def display():
 #   print('display func ran')

#decorated_display =decorter_f(display)
#print(decorated_display.__name__)
#decorated_display()

@decorter_f
def display(name,age):
    print('display func ran with args {} and {}'.format(name,age))

display('rohan',22) #now this diaplay function has been wrapped with wrapper function and now is immutable unless we remove the @dec......


#ARGUMENSTS IN DECORATER FUNCTIONS(difficult to undersatnd)

def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, 'Executed Before', original_function.__name__)
            result = original_function(*args, **kwargs) #we dont even need result var. to store the output, we can simply remove it as well
            print(prefix, 'Executed After', original_function.__name__, '\n')
            #return result #not neccessary since our orginal function is already getting executed
        return wrapper_function
    return decorator_function


@prefix_decorator('LOG:') #here display function is decorated on prefix function but still we get the same
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


print(display_info.__name__) #being a double layered decorator function, display function still = wrapper function
display_info('John', 25)

#------------------------------------------------------------------------------------------------------------------>

#CLASSES
'''
class employee:
    def __init__(self,first,last,pay):
        self.f_name=first
        self.l_name=last
        self.paid=pay
        print(self.f_name)
    def full_name(self):
        return '{} {}'.format(self.f_name,self.l_name)

emp1=employee('rohan','sharma',5000)
emp2=employee('vishal','senagr',13131)


print(emp1) #here we are printing the location of the object(which has now been passed to the class)
#print(emp1.__name__) this will return error since instance of a class has no __name__
#print(emp1.f_name.__name__) this returns error
emp1.full_name() # here emp1 is getting entered in self(used for instance or objects), this gives the details of return function
print(emp1.full_name.__name__) #this is equivalent to the function full_name with argument passed emp1 in self
print(emp1.full_name) #this gives the location of the function with instance in memory since we are not executing full_name

#self.fname = first
# {simply means
# fnmae is a container/variable which is dynamic and equal to first(argument)(which again is dynamic)
# and the dynamics is provided by self function used which makes them different for each instance
# emp1.fname = rohan
# emp2.fname = vishal
# and then we print them }

#self.f_name ,etc are var in init function but they are also accessible in inner functions(which has self as the only argument)
#or we can say since self.f_name = name, so name(argument entered) in outer function is also accessible in inner function
#now imp to know is whether it is (name) is available for inner fun as local or gloabl  variable

############
#VARIABLE CALLING IN A CLASS
#print(emp1.f_name)
#print('{} {}'.format(emp1.f_name,emp1.l_name))


#FUNCTION CALLING IN A CLASS
print(emp1.full_name()) #since the output of full_name is RETURN TYPE , thats why we have to print the function
print(employee.full_name(emp1))
 '''

#--------------------------------------------------------------------------------------------------------------->
#class and instance variable

class Employee:
    increm = 1.2

    def __init__(self,first,last,pay):
        self.f_name=first
        self.l_name=last
        self.paid=pay

    def full_name(self):
        return '{} {}'.format(self.f_name,self.l_name)


    def increment(self): #function used to assign new value to self.paid
        self.paid = int(self.paid*Employee.increm) #we can't use class variable(increm) without (class,self) references


emp1=Employee('rohan','sharma',5000)
emp2=Employee('vishal','senagr',1313)

#print(isinstance(man1,Employee)) #although in the later part we see that man1 is an instance of Employee class but still this throws an error
#print(man1.f_name)
print(emp1.paid)
emp1.increment()
print(emp1.paid)


                   #attribute assigned to the class.TRY[print(emp1.__dict__)] to check the attributes assigned to the instance

emp1.increm=2.5    #but here we have passed the increm attr for emp1,so now on it will seek the value from here
emp2.increm =3.6

print(Employee.increm) #we can access the class variable through all (class, instances)
print(emp1.increm)  #we have different increm vlaue for employees coz we can change the increm value based on the emp
print(emp2.increm) #coz of the self used

print(emp1.__dict__) #here it returns 'f_name' and not 'name' , because 'name' is not the attribute of emp1 but f_name
print(Employee.__dict__)

#emp1.increment()
#print(emp1.paid) #this is taking the factor to be 2.5 when used with self.paid but when used with Employee.paid the value is 1.2
#print(emp1.increm) #but this gets changed even with the Employee.paid coz increm is outside the scope of increment function


#--------------------------------------------------------------------------------------------------------------->
#CLASS METHODS , REGULAR METHODS(INSTANCES), STATIC METHODS


#class methods just like regular methods takes in classes(cls) as default and
#just like changes made to regular methods is acted upon the specific instances
#similarly changes made in a class method is reflected in throughout the class
#since we have only 1 class here(Employee1) the c method is default acted on Employees
# @STATIC METHOD AND @CLASS METHOD BOTH ARE CLASSES.USE  HELP()

class Employee1:
    increm = 1.2

    def __init__(self,first,last,pay):
        self.f_name=first
        self.l_name=last
        self.paid=pay

    def full_name(self):
        return '{} {}'.format(self.f_name,self.l_name)


    def increment(self):
        self.paid = int(self.paid*Employee1.increm)

    @classmethod
    def set_raise(cls,amount):
        cls.increm = amount    # here increm is not just a container for cls(we can't name 'increm' as anything coz
                                  #in case of self.f_name we could have named f_name as anyhting as it was just  a
                                  # conatiner(dynamic) but here the 'increm' is also a class variable naming
                                  # cls.xyz wont help in this case coz changes wont be redirected to increm variable )

    @classmethod
    def from_string(cls,emp_str):
        first,last,name = emp_str.split('-')
        return cls(first,last,name)

    @staticmethod   #this is static method which does not takes in any self/cls(instances/classes)
    def is_workday(day):
        if day.weekday == 6:
            print('weekend')
        else :
            print('weekday')


emp1=Employee1('rohan1','sharma1',5000)
emp2=Employee1('vishal1','senagr1',1313)


Employee1.set_raise(1.5) #here Employee1 is the class enterd in place of (cls) just like emp1 for (self)
                          #and 1.5 is the req. argument

emp1.set_raise(1.6) #we can also run the class method from the instance and that will change the variable for the whole
                    #class not just for the instance

print(Employee1.increm) # here we are just accessing the increm variable for which we have to tell the class it belongs to

#class methods as alternative constructors
#using class methods to provide objects

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first,last,name = emp_str_1.split('-')

emp_1 = Employee1(first,last,name) #passing object which has a string type info
print(emp_1.f_name)

#class methods as alternative constructors

emp_1 = Employee1.from_string(emp_str_1) #this is a complete function used to assign values to the object
print(emp_1.l_name)

#static method
import datetime
my_date =datetime.date(2016,7,10)

print(Employee1.is_workday(my_date))


#--------------------------------------------------------------------------------------------------------------------------------------->
#INHERITENCE , SUBCLASSES

class coders(Employee): #this is now a subclass
    increm = 1.05

    def __init__(self,first, last, pay,lang):
        super().__init__(first, last, pay)
                          #its imp to use this to get the remaining attributes since we are overwriting
        #Employee.__init__(first, last, pay) #em attribute,but still it gives some value,that's by accessing the
        self.lan = lang   #the already imported init funciton if we type in only 'lang' attribute and expect the init(developer)
                          #to get rest (name,pay) inherited then its not possible without this.


class manager(Employee):

    def __init__(self,first, last, pay,emp_list=None):
        super().__init__(first, last, pay)
        if emp_list is None:
            self.list= []
        else :
            self.list = emp_list


    def add_emp (self,emp):
        if emp not in self.list:
            self.list.append(emp)

    def  remove_emp (self,emp):
        if emp not in self.list:
            self.list.remove(emp)

    def print_emp(self): #here self is for 'man1' object and not for emp1 object,
        for emp in self.list:
            print(emp.f_name)   #important to note is that (emp= dev1,dev2) and f_name is their attribute.
                                #now here f_name for manager is 'don' but here since we are referring to f_name(attribute inherited)
                                # from Employee) but we are also getting the attributes of the object(dev1,2 -'dilpreet','chetan')
                                #now moreover ('dilpreet', 'chetan') are attributes of class (coders)(dev1,dev2) which we have not even inherited
                                # so just by calling dev1,2 we are also getting their (f_name,l_name,etc) also
                                #certainly since we are getting (dev1,2) attributes from (coders) without inheritence.
                                #that means the atributes of objects(even when they belong to different classes which we have not even inherited)
                                #gives us the access to the attributess
        print(emp.full_name())



dev1=coders('chetan','garg',5000,'python')
dev2=coders('dilpreet','singh',1313,'java')
man1 = manager('don','bon',12345,[dev1,dev2,emp1])

print(dev1.lan)
#print(help(coders)) # the class coders fetches data in method resolution order

print(dev1.increm) #we can adjust the class variable for a subclass without altering the value of the same for the
print(emp1.increm) #for parent class

man1.print_emp()

print(issubclass(manager,Employee))
print(isinstance(emp1,manager))  #objects/instances of the parent classes are not instances  of subclasses


print(isinstance(man1,Employee))  # but vice versa its true,although man1 is an instance of Employee class but when we print(man1.f_name) after
                                  #Employee class, it show Error
#print(issubclass(coders,Employee)


#------------------------------------------------------------------------------------------------------------------------------------------>

#DUNDER METHODS

class dunder(Employee):

    def __init__(self,first,last,pay):
        self.f_name=first
        self.l_name=last
        self.paid=pay

    def full_name(self):
        return '{} {}'.format(self.f_name,self.l_name)

    def __repr__(self): #its important to have (repr) coz even if call str(emp1), then str can fall back on repr for input
        return 'Employee( {} , {} , {} )'.format(self.f_name,self.l_name,self.paid)

    def __str__(self): #__str__ has no significanse here,we can simply rename it xyz without dunder and results wont change.
        return 'Employee( {} - {} - {} )'.format(self.f_name,self.l_name,self.paid) #priority when printing emp1(self) is given to str
                                                                                     #method over repr method

    def __add__(self,other): #using 2 instamces in a function simultaneosly
                                #here we are simply modifying the inbuilt def. of __add__ function
        return self.paid + other.paid


emp1 = dunder('rohan','shar',1526)
emp2 = dunder('dund2','er2',1526)


print(emp1.f_name)  #here this emp1 corresponds to last class it was used in(Employee1) and since our clss dunder has no object thus it shows that
                         # subclass does not inherit objects from parent class


print(emp1)
print(emp1.__repr__())
print(emp1.__str__())
#print(str(emp1))
print(repr(emp1))


#other special methods

print(1+2)
print(int.__add__(1,2)) #the functions(methods) working behind 1+2 and a+b
print('a'+'b')
#print(str.__add__('a','b'))

print(emp1 + emp2) #usnig __add__ we have used emp. names to calc sum of their salaries


#modifying __add__ function to get ...




#----------------------------------------------------------------------------------------------------------------------------------------->
#REPR VS STR

'''
import datetime


a = datetime.datetime.utcnow()

b = str(a)

print ('str(a): {}'.format(str(a))) #str() is used for representation , repr() is used for coder purpose(representation for debugers)
print ('str(b): {}'.format(str(b)))



print( 'repr(a): {}'.format(repr(a)))
print ('repr(b): {}'.format(repr(b)))

'''
#------------------------------------------------------------------------------------------------------------------------------------->

#PROPERTY DECORATER - SETTERS, GETTERS AND DELETERS

class setget():

    def __init__(self,first,last,pay):
        self.f_name=first
        self.l_name=last
        self.paid=pay
        #self.mail = self.f_name + self.l_name + '@gmail.com'

    @property  #property decorater to accesss a method as an attribute(variable) in object calling
    def mail(self):
        return self.f_name + self.l_name + '@gmail.com'

    @property
    def full_name(self):
        return '{} {} -return '.format(self.f_name,self.l_name)

    @full_name.setter #setter for setting the default values of method, which inturn also  changes the 'f_name','l_name'
    def x(self,name): # here x is the setter for full_name , althogh x is also a function but becoz we have used @property on full_name
                        # so we can simply use this as an attribute to (we can set the value of this...name)


        first, last = name.split(' ')
        self. f_name  = first
        self.l_name = last


    @full_name.deleter
    def y(self):
        print ('deletion here means default attributes gets deleted')
        self.f_name =None
        self.l_name = None



emp1 = setget('rohset','sharset',1255)

emp1.f_name = 'changed' # changing the first name does not change the email. to handle this:
                        # we can create new mail clss but then if this class is used as parent clss somewhere else, that will create problems
print(emp1.f_name)
print(emp1.mail) #since we have property decorater mail function works like variable
#print(emp1.full_name()) - once using @property in a method makes it a variable and we cant use it with ()


# SETTING THE DEFAULT FOR A FUNCTION
#emp1.fullname() = 'abcd xjsj'  this will throw us an error becoz we can not methods like this
                      #for that purpose we use setters

emp1.x ='corey sch' #this is function 'x' getting called and set, its working like an attribute
                        # moreover the way variable is being passed is something unique here


print(emp1.full_name) #setting up in function
print(emp1.mail)  # aslo changed the rest of the attribute



#DELETING
#del emp1.full_name - not working

#---------------------------------------------------------------------------------------------------------------------------------------->

#HOW TO READ AND WRITE TO A FILE

#f = open ('rohan.txt','r')
#print(f.name)
#f.close() #here its imp to close the file
#print(f.mode)

#opening files with context manager
#for a context manager, the file automatically gets close once we exit the block,although we would still
# have the access to the file(context) variable

with open ('rohan.txt','r') as f:
    #print(f.read())
    #fcont = f.read()
    #fcont2 =f.readlines()
    #fcont3 = f.readline #here we can use next , next(fcont) to get the next line

    #print(fcont)

    for x in f:
        print(x[0])

    #using while loop, looping in chunks
    #fcont = f.read(10) #if i dont put any(10) at the beginnig then first whole of file would be read then
    #while len(fcont) > 0:      #while loop would start and since there would be no values to iterate
    #    print(fcont,end = '*') #further,we would have * put and loop would end
    #    fcont = f.read(10)

    # f.read(100)
    #f.read(100) this means for the first command first 100 words would be returned and then for the 2 next
                   #100 would be returned , not that we will have the same 100 letters again
                   #but to do that


    #print(f.read(10))

    #f.seek(0) #this simply puts the cursor at position given in the index
    #print(f.read(10))


#print(f.closed) #since the file is closed u can access it but cant read the contents outside the block


#WRITING OF FILES
with open('roh.txt','w') as fw:
    fw.write('text')
    fw.write('sect')
    #seek #for write this is mostly used for overwriting
    fw.seek(0)
    fw.write('d')

#reading and writing both

#with open('rohan.txt','r') as fr1: #we might be writing in the read file coz for loop wont have lines to read
#    with open('rohan_copy.txt','w') as fw1: #in that case
#        for line in fr1:
#            fw1.write(line)

#-------------------------------------------------------------------------------------------------------->

#READING AND WRITING TO A CSV FILE

import csv #split can also be used but csv module makes parsing of files easier

with open('names.csv','r') as csv1:
    csv_read = csv.reader(csv1) #reader is a method that understands the csv files and iterates through the lines

    print(csv_read) #this is just an object in the memory

    next(csv_read) #lets you skip the first line coz we returned it here but did not print it.

    for line in csv_read:       #csv files should be seperated by comma's
        print(line[0:2])

#writing to files
#with open('names.csv','r') as csv1: #if i dont indent the write file in read file it will show me error
#    csv_read = csv.reader(csv1) # as i/o operation on closed file coz that would be out of scope of read file
#    with open('names_w.csv','w') as csv_w:
#        csv_write = csv.writer(csv_w,delimiter ='*')

#        for line in csv_read:
#            csv_write.writerow(line)


#reading/writitng csv using dictionary

#reader
with open('names.csv','r') as csv1:
    csv_read = csv.DictReader(csv1)

    for line in csv_read:
        print(line['email']) #more convieneient to parse out the info.

#writer

with open('names.csv','r') as csv1: #if i dont indent the write file in read file it will show me error
    csv_read = csv.DictReader(csv1) # as i/o operation on closed file coz that would be out of scope of read file


    with open('names_wd.csv','w') as csv_w:
        fiel_name = ['first_name','last_name'] #these field names should be same as headers passed in read file
        csv_write = csv.DictWriter(csv_w,fieldnames= fiel_name)

        csv_write.writeheader() #this is to print the headers(fieldnames) already passed in

        for line in csv_read:
            del line['email'] #this allows us to remove specified result in our write query
            csv_write.writerow(line)


#-------------------------------------------------------------------------------------------------------->

#OS MODULE
import os
#print(dir(os))
#print(os.getcwd()) #current working dir
#os.chdir('dir') - change cwd

#print(os.listdir('/users/rohan/deskop/'))

#os.makedirs('/users/rohan/desktop/python1/subdir')
#os.mkdir('/users/rohan/desktop/python1') #cant make a subdir in this
#os.rmdir('/users/rohan/desktop/python1/subdir') #doenot remove the intermediate directory
#os.removedirs() #removes the interm dir also

#os.rename('/users/rohan/desktop/python1/subdir','/users/rohan/desktop/python1/bheem') #renaming
#print(os.stat('/users/rohan/desktop/python1')) #properties
'''
for dirpath,dirname, filename in os.walk('/users/rohan/desktop/python1'):
    print('dirpath' , dirname)
    print('dirname',dirname)
    print('filename', filename)

import os
print(os.environ.get('HOME'))

#creating a file

filepath = os.path.join('/users/rohan/desktop/python1','test.txt') #join takes care of joining of filepath
print(filepath)                                                    #without bothering about ///

#now to create the file you must write the file

#base+directory name
print(os.path.basename('/users/rohan/desktop/python1')) #only base
print(os.path.dirname('/users/rohan/desktop/python1'))  #only dir
print(os.path.split('/users/rohan/desktop/python1')) #both
print(os.path.splitext('/users/rohan/desktop/python1')) #splits filetype
#print(dir(os.path))
print(os.path.exists('/users/rohan/desktop/python1')) #to see if the path exist in file dir.file
print(os.path.isdir('/users/rohan/desktop/python1'))
print(os.path.isfile('/users/rohan/desktop/python1'))
'''
#------------------------------------------------------------------------------------------------------->

#ELSE_IF

log = False #this simply tests the presence of the variable.
if not log: #this 'not' just takes the opposite of (and/or/true/false)
    print('yo')
else:
    print('false retuned')


# is vs ==

l1 = [1,2,3,4]
l2=[1,2,3,4]

if l1==l2:
    print('=')
elif l1 is l2:
    print('is')

l1 = l2
if l1 is l2:
    print('is')

# is simply means l1 and l2 being same variable in memory
# or same address for both in memory
# or address l1 = address l2. ie id(l1) = id(l2)
print(id(l1))

# true-false

condition = None    #none, 0 , false evaluates to be false
                    # any no. other than 0 evaluates to true
if condition:       # any empty entity evaluates tobe false( [],{},[],'', ,"")
    print('true')
else:
    print('false')

#------------------------------------------------------------------------------------------------>
#MODULE IMPORT

import module_import as mi # use * to import all
#or if we want to import only function
#from module_import import {function1} as xyz,.....## in this case we can directly call the function
# without the help of module name

lis = ['math','science','python','ruby','java']

print(mi.find_index(lis,'python'))

#default direct. that python looks for module in
import sys    # sys is a list where python looks for modules made in a certain preference order
              # now to import a module thats not in ou cwd we have to append this list
              # and pass in the directory location also in this
              # as sys.path.append(/users/.......location of module)


print(sys.path)

# to test the location of the module
import os
print(os.__file__)

#------------------------------------------------------------------------------------------------------>
#ELSE ON LOOPS

for x in range(5): # the same concept works with while loops too
    print(x)
    #if x==4: # if we had used break then else wont have worked.
    #    break


else:
    print('this works if we dont break out of loop')


#practical ex:-


def find_index(to_search, target):
  for i, value in enumerate(to_search):
    if value == target:
      break
  else:
    return -1
  return i


my_list = ['Corey', 'Rick', 'John']
index_location = find_index(my_list, 'Steve')

print ('Location of target is index: {}'.format(index_location))

#----------------------------------------------------------------------------------------------------->
# DUCK TYPING + EAFP

# Duck Typing and Easier to ask forgiveness than permission (EAFP)
# duck typing -  If an object has same attributes to a another object, although bith belong to different class,
#then even we treat them both to be same.

class Duck:

    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, Flap!')


class Person:

    def quack(self):
        print("I'm Quacking Like a Duck!")

    def fly(self):
        print("I'm Flapping my Arms!")


def quack_and_fly(thing):
    # Not Duck-Typed (Non-Pythonic)
     if isinstance(thing, Duck):   # if we remove this then bith the objects would yield result, but this
                                    # might be prone to error since we can throw in any type of object,
                                    # for that purpose checks are there and that's why we introduce
                                    #try and except mthod for making life easy with less coding and also
                                    # coz of Easier to ask forgiveness than permission (EAFP) rule.



         thing.quack()             ### another  imp thing here is quack and fly are funtions of class
         thing.fly()       # both with self for reference and quack_and_fly is another function but
     else:                # but here the agrument 'thing' is passed in as the instance, although values
         print('This has to be a Duck!')    # passed in thing are actually the objects of the class


d = Duck()
quack_and_fly(d)

p = Person()  # here person has same attr as duck but we are not taking it as a duck(non pythonic )
quack_and_fly(p)


# look before you leave- non pythonic

 #LBYL (Non-Pythonic)

def quack_and_fly1(thing):   # here we ask for permissions and have checks already in place
    if hasattr(thing, 'quack'):  # another thing to note is 'hasattr' function #
        if callable(thing.quack):
             thing.quack()

    if hasattr(thing, 'fly'):
        if callable(thing.fly):
         thing.fly()

d = Duck()
quack_and_fly1(d)

p = Person()  # here person has same attr as duck and we are taking both in but this is a non pythonic
quack_and_fly1(p) # way of doing thngs

# eafp - this can be used anywhere where we have to provide conditions(generally if statements) and where
            # we want to avoid error by keeping the domain of if() fixed...
def quack_and_fly2(thing):
        try:
            thing.quack() #instead of asking for permissions we are asking forgiveness in except blocks
            thing.fly()
            thing.bark()
        except AttributeError as e:
             print(e)
d = Duck()
quack_and_fly2(d)

p = Person()  # here person has same attr as duck and we are taking both in but this is a pythonic
quack_and_fly(p) # way of doing thngs


#---------------------------------------------------------------------------------------------------->

#TRY/EXCEPT/ELSE/FINALLY

try:
    f = open('rohan.txt') #if we put an error here and also in var then this being first gets executed first
    #var = badvar            #and error we get is filenot found

    #if f.name =='rohan.txt': #here we are manually raising an exception #type is 'Exception'#
    #    raise Exception
except FileNotFoundError:
    print('file not found error executed')

except Exception : #as e:    #used to print something against the default error msg that python throws
    print('general exception executed')#e)              # this prints the default error msg but a lower down version of that

else:
    print('this gets executed only when no exception is raised')

finally:
    print('this will always get executed no matter what try- except pair is raised')

# -------------------------------------------------------------------------------------------------------------------------------------->
