# FIRST CLASS or HIGHER ORDER FUNCITON
# functions that can be assigned to a variable , can be entered as argument,can be returned as a result of a function


def cube(x):
    return x * x * x


f = cube
print(cube)  # fucn wont execute without closure
print(f)  # declaring funciton without closure means that function stays but does not execute
print(f(4))

# function as arg


def square1(x):
    return x * x


def first_class(fun, li):
    list1 = []
    for n in li:
        list1.append(fun(n))
    return list1


map_ = first_class(square1, [1, 2, 3, 4])  # here square1 has no closure coz that would make it run
print(map_)  # but that is not the purpose coz it will run only when it reaches list.append........


# CLOSURE
# function result of a funciton-----THIS IS A CLOSURE
# A CLOSURE IS AN INNER FUNCTION WHICH HAS ACCESS TO ITS VARIABLES IN ITS LOCAL SCOPE EVEN WHEN OUTER FUN HAS FINISHED OPERATING

def html_tag(tag):  # this function returns another function as a return

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text  # HERE WE DONT HAVE () OHTER WISE WE WOULD HAVE had an error suggestung 1 missing agr[msg]


print_h1 = html_tag('h1')  # as mentioned html funciton returns wrap_text
print(print_h1.__name__)  # this shows that the var. has stored the function wrap_text
print(print_h1)  # here print_h1 is equivalent to wrap_text funnction (function result of a funciton)
print_h1('Test Headline!')  # since this is wrap text, it still remembers tag value eneterd earlier in this
print_h1('Another Headline!')

# MUTABLE[LIST] AND IMMUTABLE[STRING] -


# DECORATER

def decorter_f(orig_f):
    def wrapper_f(*args, **kwargs):
        print('wrapper executed this before {}'.format(orig_f.__name__))
        return orig_f(*args, **kwargs)  # we dont need a return here coz function has a print statement,so its already
    return wrapper_f  # returning something #we can remove return

# def display():
 #   print('display func ran')

#decorated_display =decorter_f(display)
# print(decorated_display.__name__)
# decorated_display()


@decorter_f
def display(name, age):
    print('display func ran with args {} and {}'.format(name, age))


display('rohan', 22)  # now this diaplay function has been wrapped with wrapper function and now is immutable unless we remove the @dec......


# ARGUMENSTS IN DECORATER FUNCTIONS(difficult to undersatnd)

def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, 'Executed Before', original_function.__name__)
            result = original_function(*args, **kwargs)  # we dont even need result var. to store the output, we can simply remove it as well
            print(prefix, 'Executed After', original_function.__name__, '\n')
            # return result #not neccessary since our orginal function is already getting executed
        return wrapper_function
    return decorator_function


@prefix_decorator('LOG:')  # here display function is decorated on prefix function but still we get the same
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


print(display_info.__name__)  # being a double layered decorator function, display function still = wrapper function
display_info('John', 25)
