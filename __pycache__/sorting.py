# SORTING

groceries = [1, 2, 3, 89, 16, 22]
gsort = sorted(groceries, reverse=True)  # descending sorting
print(gsort)

groceries.sort()  # .sort returns null
print(groceries)
#.sort() this method cant be applied to tuples and dictionaries

# sorting based on a key

list1 = [-5, -1, 3, 4, 6, -9]
sort_list = sorted(list1, key=abs)  # key is used to assign already defined abs function
print(sort_list)


# sorting of dictionary
stocks = {'yahoo': 100, 'google': 200, 'facebook': 150, 'tesla': 50}

print(sorted(zip(stocks.values(), stocks.keys())))  # here in this case priority is given to order of zipping
print(sorted(zip(stocks.keys(), stocks.values())))


#sorting in classes

class Test():
    def __init__(self, name, age, salary):
        self.naam = name
        self.umar = age
        self.baiten = salary

    def fuk(self):
        return '{} {} {}'.format(self.naam, self.umar, self.baiten)


def kuf(emp):
    return emp.umar


emp1 = Test('rohan', 22, 20000)
emp2 = Test('sengar ', 23, 15000)
emp3 = Test('john', 16, 13114)

employ = [emp1, emp2, emp3]
print(emp1.fuk())

sort1 = sorted(employ, key=kuf)
print(sort1)
