print(2+5)
print('rohan'*5)
print('rohan'+str(60))
players = "rohan"
print(players)
print(players[2:5])
print(players[2])
print('roh\nan')
print('roh')
print(len('rohan'))

# list-5

kane = ['rohan','sharma','jai']
print(kane[1])

# if-elif expression:
age = 9
if age > 10:
    print('age moer than 10')
elif age < 10:
    print('i dont knoe')

name = 'vishal'
if name is 'rohan':
    print('smart')
else:
    print('he is chetan')

# loops=1-dimensional
food = [20, 30, 40, 500]

for f in food:
    print(f+12)
    print(len(str(f)))

for f in food[3:5]:
    print(f)

# how to delete terms in a list with loop??????

# for loop with initial,end and increment
for x in range(10, 19, 2):
    print(x)

for x in range(10):
    print('rohan')

for a in range(2, 10, 2):
    print(a)

# while loop with increment which works as a condition without which this would have been an infinite loop
rohan = 5
while rohan < 10:
    print(rohan)
    rohan += 1

# break statement-9
magic_no = 8
for n in range(50):
    if n is magic_no:
        print(n)
        break
    else:
        print(n)

# 10
for x in range(101):
    if x % 4 is 0:
        print(x)

# 11 continue
# doubt on indentation
n = [1, 2, 13, 15]
for i in range(20):
    if i in n:
        continue
    print(i)

# functions
def bitcoin(btc):
    amount = btc*527
    print(amount)

bitcoin(2)

# return
def girl_age_limit(my_age='i dont know'):
    girl_age = my_age/2+8
    return girl_age

#  girl_age_limit(20)-----return function just stores the value withot doing anything with it
rohan_age_limit = girl_age_limit(22)
print("rohan_age_limit", rohan_age_limit)

# default values

def gender(sex='i dont know'):
    if sex is "m":
        sex = "male"
    elif sex is 'f':
        sex = "female"
    print(sex)

gender()

# scope of a variable-15
a = 100

def fun():
    # IF a=100 would have been here then nuf() wouldnt have worked
    print(a)

def nuf():
    print(a)

fun()
nuf()

# keyword_arguments- changing the default values

def func(name='rohan', verb='ate', object='banana'):
    print(name, verb, object)

func()

func(name='sharma')
func(verb='sleeps', object='in bag')

# flexible no. of keyword_arguments

def add_no(*enter):
    total = 0
    for n in enter:
        total += n
    print(total)

add_no(3, 5, 246)

# 18 unpacking arguments

def health_indicator(age, apples, cigs):

    score = (age*3)+(apples*2)-(2.5*cigs)
    print(score)

rohan = (22, 7, 0)
# 1
health_indicator(rohan[0], rohan[1], rohan[2])

# 2,
health_indicator(age=1, apples=2, cigs=0)

# 3
health_indicator(*rohan)

# sets- non repeated-19
groceries = {'milk', 'honey', 'milk', 'lehom'}
print(groceries)

if'milk' in groceries:
    print('there is milk')
else:
    print('no milk')

# 20- dictionary:key:values

dict = {'rohan': 'smart', 'vishal': 'gent', 'chetan': 'chaman'}
print(dict['rohan'])

for k, v in dict.items():
    print(k+" "+v) #multiple variable declaration in a range

# import-modules21
import random

data = random.randrange(1, 1000)
print(data) #printing a random number

# web crawler

import random
import urllib.request

def down_img(url):
    name = random.randrange(1, 100)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

#down_img("https://upload.wikimedia.org/wikipedia/commons/b/b4/JPEG_example_JPG_RIP_100.jpg")

# read and write file-23
#fw = open('roh.txt', 'w+')
#fw.write = ('rohan')
#fw.close()

#fr= open('roh.txt','r')
#text=fr.read
#print(text)
#fr.close()

#28-error
#input function not working

#29class and objects
class Enemy:
    life = 3
    def attack(self):
        print('wtf')
        self.life-=1



    def life_left(self):
        if self.life<=0:
            print('dead')
        else:
            print('life left'+'='+ str(self.life))

enemy1= Enemy()
enemy2 =Enemy()

enemy1.attack()
enemy2.attack()
enemy1.attack()

enemy1.life_left()
enemy2.life_left()

#init function-30
class bheem:

    def __init__(self):
        print('this would always be there coz its init')

    def test(self):
        print('optional on calling')

object1=bheem()
object1.test()   #you can directly call function in a

#practical init ex
class Evil:

    def __init__(self,x):
        self.power=x

    def power_show(self):
        print(self.power)

evil1=Evil(5)    #here we have given 5,20 in function which directs to x in def
evil2=Evil(20)    # but what if we have multiple functions with multiple such vairable how would we enter then

evil1.power_show()
evil2.power_show()
print(evil1.power) #you can directly print the variable in a class and no need to write class with variable

#31-class variable vs instance variable
class girl:

    gender = 'female'  #class var(same for whole class)

    def __init__(self,name):         # what if we had 2 function each with something inside parenth.
        self.name=name               #---instance variable

r=girl('nobita') #here we have kept a value in pareth coz we have the same(name) function?
s=girl('ryan')   #what if we have a non init function and what if against self we'd have a different name
print(r.gender)
print(s.gender)
print(r.name)
print(s.name)

#32,33 inheritence,multiple inheritence,overpowering inheritence

class Mario():

    def walk(self):
        print('i can walk')

class Jmup():
    def jump(self):
        print('i can jump')

class Big_mario(Mario, Jmup):
    pass

class overpowering(Mario):
    def walk(self):
        print('i am overwriting')

mario= Big_mario()
mario.walk()
mario.jump()

mario1=overpowering()
mario1.walk()

#threading 34
import threading

class message(threading.Thread): #parenth-here its showing inheritence
    def run(self):               #run is a function triggered by start
        for _ in range(20):
            print(threading.current_thread().getName())

x=message(name='msg sent')
y=message(name='msg received')

x.start()
y.start()

#38-unpacking variables,tuples
date,name,place =['feb','rohan','delhi']
print(name)

def grades(grade):
    first,*middle,last=grade
    avg= sum(middle)/len(middle)
    print(avg)
grades([1,2,3322,4,5555])

#39- zip---------same as concatenate(works even when an entry is missing)
first_name= ('rohan','vishal','chetan')
last_name=('sharma','sengar','garg')

name=zip(first_name,last_name)

for a,b in name:
    print(a,b)

#40-lambda-is a mini function easy to use without making a new function, used for making buttons

answer = lambda x:7*x
print(answer(2))

#41 min/max/sort via zip in dictionaries
#we have taken vlaues first because sorting is done on first entity basis)
# we have to zip the dictionaries because we cant perform min/max on dictionaries

stocks = {'yahoo':100,'google':200,'facebook':150,'tesla':50}

print(min(zip(stocks.values(),stocks.keys())))   #by default while using min keys are taken for ordering
print(sorted(zip(stocks.values(),stocks.keys())))  #if we donot use zip



#struct-49

from struct import *

packed_data=pack('iif',6,12,4.3)  #packing of data
print(packed_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

#unpacking of data

unpack_data=unpack('iif',b'\x06\x00\x00\x00\x0c\x00\x00\x00\x9a\x99\x89@')
unpack_data=unpack('iif',packed_data)
print(unpack_data)

#50-map

listi = [12,1,12,35,16]

def double(dollars):
    double_num = dollars*2
    return double_num

pd=list(map(double,listi))
print(pd)

print(list(map(lambda x: x*2, listi))) #same thing using lamda



#52 binary-bitwise oprator

a = 16 & 50 #this is gates type and operator
print(a)

b = 16 or 17
print(b)

c = 20
d= c >> 2 #right shift (all functions happening in binary form)
print(d)

#53 - gratest and smallest
import heapq

grades = [20,30,1,56,4,61,62,12]

print(heapq.nlargest(3,grades))

#important example

stocks =[
{'mark':'google','price':123},
{'mark':'fb','price':245},
{'mark':'tcs','price':1223},
{'mark':'gant','price':1323}
]

print(heapq.nlargest(2,stocks,key=lambda stocks:stocks['price']))

#54 word frequency counter
from collections import Counter
text ="To indicate short quotations four typed lines fewer of prose  three lines of verse  your text"\
"enclose the quotation within double quotation marks Provide the author  specific page citation  the"\
"case of verse, provide line numbers the text, include a complete reference on the Works Cited page."\
"Punctuation marks such  periods, commas,  semicolons should appear after the parenthetical citation."\
"Question marks  exclamation points should appear within the quotation marks they are a part of"\
"the quoted passage but after the parenthetical citation  they are a part of your text"



words= text.split() #converts into list

Count=Counter(words)
amx=Count.most_common(3)

print(amx)

#55
