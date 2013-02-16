# -*- coding: utf-8 -*-

import datetime
import locale 
import sqlite3
import cgi
import os
from data_module import *

def getTopics():
	print "Content-type: text/javascript;charset=utf-8\n"

	try:
		req=Request()
		TopicID=int(req.getreq("id"))
	except KeyError:
		TopicID = 1
		pass

	con=sqlite3.connect('./dbfile.db')
	cur=con.cursor()

	#Select Topics Data
	cur.execute("""select count(id) from Topics;""")
	result = cur.fetchall()		
	TopicsNum = result[0][0]


	cur.execute(""" select title, date, body from Topics where id = %d;"""%(TopicsNum - TopicID + 1))
	result = cur.fetchall()		
	if (result != []):
		for res in result:
			DateData=TopicsData(res[0], res[2], datetime.datetime.strptime(res[1],"%Y-%m-%d"))
			print "callback("+DateData.encodeJson()+")"
	else:
		#return empty Json
		print "callback({})"


if __name__ == '__main__':
	getTopics()


