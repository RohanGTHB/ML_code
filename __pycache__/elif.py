# ELSE_IF

log = False  # this simply tests the presence of the variable.
if not log:  # this 'not' just takes the opposite of (and/or/true/false)
    print('yo')
else:
    print('false retuned')


# is vs ==

l1 = [1, 2, 3, 4]
l2 = [1, 2, 3, 4]

if l1 == l2:
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

condition = None  # none, 0 , false evaluates to be false
# any no. other than 0 evaluates to true
if condition:       # any empty entity evaluates tobe false( [],{},[],'', ,"")
    print('true')
else:
    print('false')
