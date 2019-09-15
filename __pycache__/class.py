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



