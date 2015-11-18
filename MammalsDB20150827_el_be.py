import json
import collections
import MySQLdb
 
db = MySQLdb.connect(host="localhost", user="root", passwd="ilbaloney.", db="MammalsDB20150827_el_be")
cursor = db.cursor()

#get tables from MySQL
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

#put tables into array
table_nm = []
for (table_name,) in cursor:
    if table_name != 'Paste Errors':
        table_nm.append(table_name)

print table_nm

cursor.close()

#get attributes in each table in database
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

	#create json for data
	j = json.dumps(rowarray_list)

	#put json data into a file
	rowarrays_file = 'json/'+name + '.json'
	f = open(rowarrays_file,'w')
	print >> f, j

	cursor.close()
