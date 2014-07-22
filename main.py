__author__ = 'steve_w'

import csvkit
import os
import pyodbc  # pyodbc is great for accessing microsoft access databases.

tables = []
DBfile = os.getcwd() + '/maragua.mdb'  # Name of file here either .accdb or .mdb
cnxn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+DBfile)
cursor = cnxn.cursor()
# cursor.tables() is responsible for getting all the tables within the mdb so that we can query each table
for dbtable in cursor.tables():
    tables.append(dbtable.table_name)

cursor.close()

cursor = cnxn.cursor()
for table in tables:
    sql = 'SELECT * FROM ' + table
    cursor.execute(sql)
    row = cursor.fetchone()
    if row:
        print row  # Here shall be implemented to write to file. Manipulation of the output to look like a csv.
        savefile = table + '.csv'
        with open(savefile, 'wb') as f:
            writer = csvkit.writer(f)
            writer.writerows(row)

cursor.close()
cnxn.close()
