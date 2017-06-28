#coding=utf8
import geocoder
import MySQLdb

db = MySQLdb.connect(host="localhost",user="root",passwd="ttmaker",db="opendata",charset='utf8')
sql = "select r.Location from 02_HardwareRetail r , 02_HardwareStore s where r.Location = s.Location  "
cursor = db.cursor()
cursor.execute(sql)
result = cursor.fetchall()

sum = 0

for i in result:
	I = str(i[0])
	sql = "Delete from 02_HardwareRetail where Location = " + "'" + I + "'"
	cursor.execute(sql)
	db.commit()
	sum = sum + 1
	print (sql)
print (sum)
db.close
