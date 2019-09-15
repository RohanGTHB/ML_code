import sqlite3
from employee import Employee

conn= sqlite3.connect(':memory:') #( :memory:) to create an in memory db ('employee.db')
                                        #using employee.db when we want to store db in a file

c = conn.cursor()  #creating a cursor to execute some sql commands

c.execute (""" CREATE TABLE employee(firstdb TEXT
               ,lastdb TEXT
                ,paydb INTEGER
              )""")


emp1=Employee('chetu','sharma',5000) #if i print these instance it will happen but we want to store them in our db
emp2=Employee('bakchod','senagr',1313)

c.execute("INSERT INTO employee VALUES ('rdb1','sdb',10000)")
conn.commit()
c.execute("INSERT INTO employee VALUES ('{}','{}',{})".format(emp1.f_name,emp1.l_name,emp1.paid)) #this is prone to errors coz of its mutability
conn.commit()
c.execute("INSERT INTO employee VALUES (?,?,?)",(emp2.f_name,emp2.l_name,emp2.paid))
conn.commit()
c.execute("INSERT INTO employee VALUES (:firstdb,:lastdb,:paydb)",{'firstdb':emp1.f_name,'lastdb':emp1.l_name,'paydb':emp1.paid})
conn.commit()


c.execute("SELECT * FROM employee ")

#print(c.fetchone()) #fetchmany() , fetchall
#print(c.fetchall()) #result in a list

#c.execute("SELECT * FROM employee where lastdb =?",('sharma',))
print(c.fetchall())
#c.execute("SELECT * FROM employee where lastdb =:lastdb",{'lastdb':'senagr'})
print(c.fetchall())


conn.commit()
conn.close() #closing the connection to db




