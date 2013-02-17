#!/usr/bin/python python
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
		return self.form__[key].value
		

class TopicsData(object):
	def __init__(self, Title, Body, Date = datetime.datetime.today() ):
		#Parameter sequence is't elegant...
		self.__title = Title
		self.__body = Body
		self.__date = Date
		return

	def encodeJson(self):
		"""TopicsData encode to Json Data"""
		Param = {"title":self.__title, "date":self.__date.strftime("%Y-%m-%d"), "body":self.__body}
		return u"{'title':'%(title)s', 'date':'%(date)s', 'body':'%(body)s'}" % Param



