__author__ = 'steve_w'

import subprocess, os

name_of_file = "maragua.mdb"
DBfile = os.getcwd() + '/' + name_of_file  # Name of file here either .accdb or .mdb
table_names = subprocess.Popen(["mdb-tables", "-1", DBfile], stdout=subprocess.PIPE).communicate()[0]
tables = table_names.split('\n')
folder_name = name_of_file.split('.')
# This will be for saving the files into a certain folder.
if os.path.exists(folder_name[0]):
    print("file already exists.")
else:
    os.makedirs(folder_name[0])
    os.chdir(folder_name[0])
# Dump each table as a CSV file using "mdb-export",
# converting " " in table names to "_" for the CSV filenames.
for table in tables:
    if table != '':
        filename = table.replace(" ", "_") + ".csv"
        access_file = open(filename, 'w')
        print("Dumping " + table)
        contents = subprocess.Popen(["mdb-export", DBfile, table], stdout=subprocess.PIPE).communicate()[0]
        access_file.write(contents)
        access_file.close()

