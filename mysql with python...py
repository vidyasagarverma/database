#!/usr/bin/env python
# coding: utf-8

# In[51]:


import mysql.connector as mysql 
connection=mysql.connect(host="127.0.0.1",
  user="root",
  password="Igs@1234",
 
                  )
cursor=connection.cursor()
cursor.execute("CREATE DATABASE customer_detail")


# In[68]:


import mysql.connector as mysql 
connection=mysql.connect(host="127.0.0.1",
  user="root",
  password="Igs@1234",
 
                  )
cursor=connection.cursor()
cursor.execute("SHOW DATABASES")
for x in cursor:
    print(x)


# In[69]:


#create a table 
import mysql.connector as mysql 
connection=mysql.connect(host="127.0.0.1",
  user="root",
  password="Igs@1234",
  database="customer_detail"
                  )
cursor=connection.cursor()
cursor.execute("CREATE TABLE customer(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),address VARCHAR(255))")


# In[70]:


cursor=connection.cursor()
cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)


# In[71]:


#insert the values into table
cursor=connection.cursor()
sql = "INSERT INTO customer (name, address) VALUES (%s, %s)"
val=("vidya sagar","delhi")
cursor.execute(sql,val)
print(cursor.rowcount, "record inserted.")


# In[72]:


#insert the multiple dataset into table
cursor=connection.cursor()
sql="INSERT INTO customer (name, address) VALUES (%s, %s)"
val=[
    ("vidya","delhi"),
    ("sagar","New Delhi"),
    ("Raj","Gurgaon")
    ]
cursor.executemany(sql,val)
print(cursor.rowcount,"recorded inserted")


# In[73]:


cursor = connection.cursor()

sql = "INSERT INTO customer (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
cursor.execute(sql, val)

connection.commit()

print("1 record inserted, ID:", cursor.lastrowid)


# In[74]:



import mysql.connector as mysql 
connection=mysql.connect(host="127.0.0.1",
  user="root",
  password="Igs@1234",
  database="customer_detail"
                  )
#select all records from the "customers" table, and display the result:
cursor=connection.cursor()
sql="SELECT * FROM customer"
cursor.execute(sql)
cursor.fetchall()


# In[75]:


#select distinct records from the "customers" table, and display the result:
cursor=connection.cursor()
sql="SELECT DISTINCT name FROM customer"
cursor.execute(sql)
cursor.fetchall()


# In[76]:


#Select only address columns:
cursor=connection.cursor()
sql="SELECT address FROM customer"
cursor.execute(sql)
cursor.fetchall()


# In[77]:


import mysql.connector as mysql 
connection=mysql.connect(host="127.0.0.1",
  user="root",
  password="Igs@1234",
  database="customer_detail"
                  )
#Select record(s) where the address is "delhi"
cursor=connection.cursor()
sql="SELECT name FROM customer WHERE address='delhi'"
cursor.execute(sql)
cursor.fetchall()


# In[78]:


#Wildcard Characters
#Select records where the address contains the word "delhi"
sql = "SELECT * FROM customer WHERE address LIKE '%delhi%'"
cursor.execute(sql)
cursor.fetchall()


# In[79]:


#Prevent SQL Injection
#Escape query values by using the placholder %s method:
sql="SELECT * FROM customer WHERE address=%s"
add=('delhi',)
cursor.execute(sql,add)
cursor.fetchall()


# In[80]:


#order the customer by their name
sql="SELECT * FROM customer ORDER BY name"
cursor.execute(sql)
cursor.fetchall()


# In[81]:


cursor=connection.cursor(buffered=True)
#Delete any record where the address is "New Delhi:
sql="DELETE FROM customer WHERE address='New Delhi'"
cursor.execute(sql)
connection.commit()

print(cursor.rowcount, "record(s) deleted")


# In[66]:


#drop the table 
sql="DROP TABLE customer"
cursor.execute(sql)


# In[82]:


cursor=connection.cursor(buffered=True)
sql = "UPDATE customer SET address = 'Canyon 123' WHERE address = 'delhi'"
cursor.execute(sql)
print(cursor.rowcount,"record(s) affected")


# In[ ]:




