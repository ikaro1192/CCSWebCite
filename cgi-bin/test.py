# -*- coding: utf-8 -*-

import datetime
import locale 
import sqlite3
import cgi
import os
from data_module import *


def addTopics():
	Data = TopicsData(u"タイトル",u"中身")
	print Data.encodeJson() 
	con=sqlite3.connect('./dbfile.db')
	cur=con.cursor()
	try:
		cur.execute("""create table Topics(
						id INTEGER PRIMARY KEY,
						title text,
						date text,
						body text);"""
					)

		cur.execute(u"""insert into Topics ( title, date, body)
						values  ("hogefoobar","2012-11-17", "this is text");""")
	except:
		print "hoge"
		pass

	con.commit()

	return


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
	cur.execute(""" select title, date, body from Topics where id = %d;"""%TopicID)
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


