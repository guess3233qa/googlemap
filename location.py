#coding=utf8
import geocoder
import MySQLdb

db = MySQLdb.connect(host="localhost",user="root",passwd="ttmaker",db="opendata",charset='utf8')
sql = "select Location from 01_Hospital where Lat = 0 or Lng = 0 "
cursor = db.cursor()
cursor.execute(sql)
result = cursor.fetchall()

for i in result:
	g = geocoder.google(i[0])

	lat = str(g.lat)
	lng = str(g.lng)
	sql = "UPDATE 01_Hospital SET Lat = " + lat + " , Lng = " + lng + " WHERE Location = " + '"' + i[0] + '"'

	if lat != 'None' and lng != 'None':
		cursor.execute(sql)
		db.commit()

	print (sql)

db.close
