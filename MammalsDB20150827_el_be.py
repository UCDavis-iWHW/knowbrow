import json
import collections
import MySQLdb
import json as simplejson
 
db = MySQLdb.connect(host="localhost", user="root", passwd="langeresearch123", db="MammalsDB20150827_el_be")
cursor = db.cursor()

#get tables from MySQL
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

#put tables into array
table_nm = []
for (table_name,) in cursor:
    if table_name != 'Paste Errors':
        table_nm.append(table_name)

cursor.close()


#create wrap to put the data table name in json
wrap = {}

#create array to put the columns/rows in the tables
rowarray_list = []

#go through each table in the database
for name in table_nm:
	rowarray_list = []
	cursor = db.cursor()
	cursor.execute("SELECT * FROM " + name)
	rows = cursor.fetchall()
	columns = [desc[0] for desc in cursor.description]
	
	#query the array
	for row in rows:
		t = dict(zip(columns, row))
		rowarray_list.append(t)
		wrap[name] = rowarray_list

j = json.dumps(wrap, sort_keys=True, indent=4)

#store into json file 
rowarrays_file = 'json/milkdata.json'
f = open(rowarrays_file,'w')
print >> f, j

cursor.close()
