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
