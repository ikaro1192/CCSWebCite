# -*- coding: utf-8 -*-

import datetime
import locale 
import sqlite3
import cgi
import os

class Request(object):
	def __init__(self, environ=os.environ):
		self.form__=cgi.FieldStorage()
		self.environ__=environ

	def getreq(self,key):
		if self.form__.has_key(key) == False :
			raise KeyError
		return self.form[key].value
		

class TopicsData(object):
	def __init__(self, Title, Body, Date = datetime.datetime.today() ):
		self.__title = Title
		self.__body = Body
		self.__date = Date
		return

	def encodeJson(self):
		Param = {"title":self.__title, "date":self.__date.strftime("%Y-%m-%d"), "body":self.__body}
		return u'{"title":"%(title)s", "date":"%(date)s", "body":"%(body)s"}' % Param

		return 


if __name__ == '__main__':
	Data = TopicsData(u"タイトル",u"中身")

	print "Content-type: application/json;charset=utf-8\n"
	print Data.encodeJson() 

	try:
		req=Request()
		req.getreq("foo")
	except KeyError:
		print "bar"


	con=sqlite3.connect('./dbfile.db')
	cur=con.cursor()
	try:
		cur.execute("""create table Topics(
						id serial,
						title text,
						date text,
						body text);"""
					)

		cur.execute(u"""insert into table values  (id serial, title text, date text, body text);""")
	except:
		print "hoge"
		pass
	con.commit()
