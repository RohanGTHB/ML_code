# OS MODULE
import os
# os.path.dirname(git.__file__)


# print(dir(os))
# print(os.getcwd())  # current working dir
# os.chdir('dir') - change cwd

# print(os.listdir('/users/rohan/deskop/'))

# os.makedirs('/users/rohan/desktop/python1/subdir')
# os.mkdir('/users/rohan/desktop/python1') #cant make a subdir in this
# os.rmdir('/users/rohan/desktop/python1/subdir') #doenot remove the intermediate directory
# os.removedirs() #removes the interm dir also

# os.rename('/users/rohan/desktop/python1/subdir','/users/rohan/desktop/python1/bheem') #renaming
# print(os.stat('/users/rohan/desktop/python1')) #properties
'''
for dirpath,dirname, filename in os.walk('/users/rohan/desktop/python1'):
    print('dirpath' , dirname)
    print('dirname',dirname)
    print('filename', filename)

import os
print(os.environ.get('HOME'))

# creating a file

filepath = os.path.join('/users/rohan/desktop/python1','test.txt') #join takes care of joining of filepath
print(filepath)                                                    #without bothering about ///

# now to create the file you must write the file

# base+directory name
print(os.path.basename('/users/rohan/desktop/python1')) #only base
print(os.path.dirname('/users/rohan/desktop/python1'))  #only dir
print(os.path.split('/users/rohan/desktop/python1')) #both
print(os.path.splitext('/users/rohan/desktop/python1')) #splits filetype
# print(dir(os.path))
print(os.path.exists('/users/rohan/desktop/python1')) #to see if the path exist in file dir.file
print(os.path.isdir('/users/rohan/desktop/python1'))
print(os.path.isfile('/users/rohan/desktop/python1'))
'''


#------------------------------------------------------------------------------------------>
# MODULE IMPORT

import module_import as mi  # use * to import all
# or if we want to import only function
# from module_import import {function1} as xyz,.....## in this case we can directly call the function
# without the help of module name

lis = ['math', 'science', 'python', 'ruby', 'java']

print(mi.find_index(lis, 'python'))

'''
# default direct. that python looks for module in
import sys    # sys is a list where python looks for modules made in a certain preference order
# now to import a module thats not in ou cwd we have to append this list
# and pass in the directory location also in this
# as sys.path.append(/users/.......location of module)


print(sys.path)

# to test the location of the module
import os
print(os.__file__)
'''
