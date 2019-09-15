#GENERATOR
list = []
for n in [1,2,3,4,5,6]:
    list.append(n*n)
print(list)

#GENERATOR
def square (num):
    for n in num:
        yield n*n

y  = square ([1,2,3,4,5])
for x in y:
    print(x)


#generator comprehension
my_list = (n*n for n in [1,2,3,4,5,6])

for x in my_list:
    print(x)

#generator doesnot hold all the values, we have to ask for each value to print them out mainly by looping or using NEXT state.my_list
