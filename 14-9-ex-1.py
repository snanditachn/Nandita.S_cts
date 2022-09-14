#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install mysql-connector-python


# In[3]:


import mysql.connector


# In[4]:


mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "password")


# In[5]:


mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")


# In[6]:


for i in mycursor:
    print(i)


# In[7]:


#Taking one database
mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "password",
database="sakila")


# In[8]:


mycursor = mydb.cursor()
mycursor.execute("select*from actor")


# In[9]:


for i in mycursor:
    print(i)


# In[10]:


mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE actorinfo (name VARCHAR(255),age INT(3), address VARCHAR(500))")


# In[11]:


mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")

for i in mycursor:
    print(i)


# In[12]:


mycursor = mydb.cursor()
mycursor.execute("ALTER TABLE actor ADD COLUMN new varchar(10)")


# In[13]:


mycursor = mydb.cursor()
mycursor.execute("DESCRIBE actor")
for i in mycursor:
    print(i)


# In[14]:


#deleting table
mycursor = mydb.cursor()
mycursor.execute("DROP TABLE actorinfo")


# In[15]:


mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")


# In[16]:


for i in mycursor:
    print(i)

