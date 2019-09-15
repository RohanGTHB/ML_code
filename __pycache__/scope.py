
# SCOPE OF VARIABLE
# LEGB - LOCAL,ENCLOSED (FROM SOME OUTER),GLOBAL,BUILT IN

x = 'i am global'


def scope():
    global x  # global allows to set value of variable in gloabl scope('i am global') here is set as
    # x = 'i am local' and then whenever we  call print('x') in global scope it will take
    # set up values.
    x = 'i am local '
    print(x)


print(x)  # taking valuues from global coz of LEGB rule
scope()  # taking x locally from function coz of rule

y = 'i am global'


def scope_y():
    #y= 'i am local '
    print(y)


scope_y()  # here it is taking values from global coz no value is in local domain

# builtin vs global
list = [1, 2, 3, 5]


def min():
    pass

# print(min(list)) - here min function wont run coz preference is given to global functions before built in functions

# enclosed vs local vs global

# print(dir.(builtins)) --- contains all the predefned attributes of python

# Namespaces are created at different moments and have different lifetimes.
# The namespace containing the built-in names is created when the Python interpreter starts up,
#  and is never deleted. The global namespace for a module is created when the module definition is read in;
#  normally, module namespaces also last until the interpreter quits.
# The statements executed by the top-level invocation of the interpreter,
#  either read from a script file or interactively, are considered part of a module called __main__,
# so they have their own global namespace.
# (The built-in names actually also live in a module; this is called builtins.)

# The local namespace for a function is created when the function is called,
#  and deleted when the function returns or raises an exception that is not handled within the function.


a = 'global'


def outer():
    #global a
    a = 'outer'

    def middle():
        # nonlocal a
        #global a
        a = 'middle'
        print(a)

        def inner():
            # nonlocal a    # non local simply allows you to set value of variable outside local but inside
            # global a      #global scope in case of nested functions
            a = 'inner'    # here a in nonlocal(middle)  is set to inner
            print(a)

        inner()
    middle()  # this will give us 'middle ' if no nonlocal is used in inner
    print(a)


outer()
print(a)  # this will give us 'global' if no global is used in nested function
