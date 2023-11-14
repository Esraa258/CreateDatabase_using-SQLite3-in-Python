# create a database called STAFF and load the contents of the CSV file as a table called INSTRUCTORS, for a dataset of employee records that is available with an HR team in a CSV file

# install pandas to read the CSV and interact with the database
# pip install pandas

########################################   Database initiation   ########################################
# database for storing data would be created on a server to which the other team members would have access, I'm going to create the database on a dummy server using SQLite3 library
# SQLite3 is an in-process Python library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine
import sqlite3
import pandas as pd

# use SQLite3 to create and connect the process to a new database STAFF
conn = sqlite3.connect('STAFF.db')


########################################   Create and Load the table   ########################################
table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE'] #Attributes are columns of the table

# Reading the CSV file
file_path = r'C:\Users\esraa\Desktop\Python_Projects\Database\INSTRUCTOR.csv'
df = pd.read_csv(file_path, names = attribute_list)

# Loading the data to the table
df.to_sql(table_name, conn, if_exists = 'replace', index =False)
print('Table is ready')
# if_exists = 'fail' --> Default, The command doesn't work if a table with the same name exists in the database
# if_exists = 'replace' --> The command replaces the existing table in the database with the same name
# if_exists = 'append' --> The command appends the new data to the existing table with the same name


########################################   Running basic queries on data   ########################################
# Now the data is uploaded to the table in the database, anyone with access to the database can retrieve this data by executing SQL queries

# Viewing all the data in the table
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn) #read_sql function in pandas: to execute SQL queries on the data
print(query_statement)
print(query_output)

# Viewing only FNAME column of data
query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Viewing the total number of entries in the table
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# appending some data to the table
data_dict = {'ID' : [100],
            'FNAME' : ['John'],
            'LNAME' : ['Doe'],
            'CITY' : ['Paris'],
            'CCODE' : ['FR']}
data_append = pd.DataFrame(data_dict)
data_append.to_sql(table_name, conn, if_exists = 'append', index =False)
print('Data appended successfully')


# check the count after appending
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# close the connection to the database.
conn.close()