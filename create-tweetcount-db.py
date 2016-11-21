# code to run to setup postgres dB, leverging psycopg example

#Connecting to a database
#Note: If the database does not exist, then this command will create the database


import psycopg2

from psycopg2 import connect

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE


# create database

#connect to the default system database postgres and then issue your query to create the new database.

con = connect(dbname='postgres', user="postgres", host='localhost', password="pass")

con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) # <-- ADD THIS LINE

#command to connect to specific dB
cur = con.cursor()
cur.execute("DROP DATABASE IF EXISTS %s ;" % 'tcount')
cur.execute("CREATE DATABASE %s  ;" % 'tcount')
con.close()

#Create a Table
#The first step is to create a cursor. 

#connect to new dB
con2 = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

cur = con2.cursor()

cur.execute('''DROP TABLE IF EXISTS tweetwordcount''')


cur.execute('''CREATE TABLE tweetwordcount
       (word TEXT PRIMARY KEY     NOT NULL,
       count INT     NOT NULL);''')
con2.commit()

# test
# cur.execute('''SELECT word, count FROM tweetwordcount;''')

con2.close()


