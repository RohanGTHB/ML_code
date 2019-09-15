
# DICTIONARY

dict = {'rohan': 'smart', 'vishal': 'gent', 'chetan': 'chaman'}
print(dict['rohan'])
print(dict.get('rohan'))

# changing values

dict['rohan'] = 'angry'
print(dict)

print(dict.keys())
print(dict.items())

for key, value in dict.items():  # looping in dictionary
    print(key, value)


# LOOPS

for a in range(2, 10, 2):  # start,end,increment
    print(a)

# break - in a range of 5 print 123
# continue- in a range of 5 print 1245

# sorting of dictionary
stocks = {'yahoo': 100, 'google': 200, 'facebook': 150, 'tesla': 50}

print(sorted(zip(stocks.values(), stocks.keys())))  # here in this case priority is given to order of zipping
print(sorted(zip(stocks.keys(), stocks.values())))
