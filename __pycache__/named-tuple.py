# NAMED TUPLES


from collections import namedtuple

y = namedtuple('x', ['red', 'green', 'blue'])

x = y(55, 155, 255)
#white = Color(255,255,255)

print(x.blue)
# print(x['red']) #- dont know why not working
print(x[0])
