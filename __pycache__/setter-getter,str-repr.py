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
