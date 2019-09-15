


#Namespaces are created at different moments and have different lifetimes. 
# The namespace containing the built-in names is created when the Python interpreter starts up,
#  and is never deleted. The global namespace for a module is created when the module definition is read in;
#  normally, module namespaces also last until the interpreter quits. 
# The statements executed by the top-level invocation of the interpreter,
#  either read from a script file or interactively, are considered part of a module called __main__, 
# so they have their own global namespace. 
# (The built-in names actually also live in a module; this is called builtins.)

#The local namespace for a function is created when the function is called,
#  and deleted when the function returns or raises an exception that is not handled within the function.

from contextlib import contextmanager
@contextmanager
def open_file(file, mode):
    f = open(file, mode)
    yield f 
    f.close()


with open_file('sample.txt', 'w') as m:
    m.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

print(m.closed)

