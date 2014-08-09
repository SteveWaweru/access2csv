__author__ = 'steve_w'

import sys, subprocess, os

DBfile = os.getcwd() + '/maragua.mdb'  # Name of file here either .accdb or .mdb
table_names = subprocess.Popen(["mdb-tables", "-1", DBfile],
                               stdout=subprocess.PIPE).communicate()[0]
tables = table_names.split('\n')

# Dump each table as a CSV file using "mdb-export",
# converting " " in table names to "_" for the CSV filenames.
for table in tables:
    if table != '':
        filename = table.replace(" ", "_") + ".csv"
        file = open(filename, 'w')
        print("Dumping " + table)
        contents = subprocess.Popen(["mdb-export", DBfile, table],
                                    stdout=subprocess.PIPE).communicate()[0]
        file.write(contents)
        file.close()

