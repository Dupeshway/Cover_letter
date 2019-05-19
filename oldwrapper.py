#!/usr/bin/env python3

#basic python wrapper for SQL queries
'''
Program:
File:

Version:
Date:
Function: to wrap SQL queries in python language

Author: Yobi Livingstone
Address: Biological Sciences, Birkbeck ...

--------------------------------------------------------------------------
Description:


--------------------------------------------------------------------------
Usage:

--------------------------------------------------------------------------
Revision History:


--------------------------------------------------------------------------
Import libraries'''

import pymysql.cursors
'''--------------------------------------------------------------------------
'''


# Set parameters
dbname   = "ly001"
dbhost   = "hope"
dbuser   = "ly001"   # Ask a demonstrator
dbpass   = "xxxx"   # Ask a demonstrator
port     = 3306

# Create SQL statement to find number of human protein entries
sql      = "select * from CDS"

# Connect to the database
db = pymysql.connect(host=dbhost, port=port, user=dbuser, passwd=dbpass, db=dbname)

# Create a cursor and execute the SQL on it
cursor = db.cursor()
nrows  = cursor.execute(sql)

# We know there is only one row returned to fetch it and print the data
data   = cursor.fetchone()
print ("There were ", data[0], " rows")

def query():
    '''placing SQL queries in a python wrapper to be sent to the business layer
    input:
    output
    '''

    import sqlite3

    
    sql = ('select field1, field2, field3, field4 '
       'from table '
       'where condition1=1 '
       'and condition2=2 ')



