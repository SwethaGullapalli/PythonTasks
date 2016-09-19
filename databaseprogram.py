# Programs for database
import csv
import sqlite3
import pdb
connection=sqlite3.connect(r"D:\python\samples\Modelprograms.db")
with open('C:\Users\Swetha\Desktop\student.csv','r') as csvfile:
	read_file=csv.reader(csvfile,delimiter='|')
	print (read_file)
	for row in read_file:
		InsertQueryString="insert into CSVFileData values('%s','%s','%s','%s','%s','%s','%s')"%(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
		#pdb.set_trace()
		connection.execute(InsertQueryString)
		#print "insert into CSVFileData values('%s','%s','%s','%s','%s','%s')"%(row[0],row[1],row[2],row[3],row[4],row[5])
		print InsertQueryString
connection.commit()
connection.close()
