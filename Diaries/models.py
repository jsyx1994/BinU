#coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.conf import settings
class Diary(models.Model):
	title=models.CharField(max_length=50)
	content=models.TextField()
	finished_time=models.DateTimeField()
	friendly=models.BooleanField(default=False)

	author=models.ForeignKey(settings.AUTH_USER_MODEL,default=None)
	def __unicode__(self):
		return self.title

	#set method
	def setTitle():
		pass
	def setContent():
		pass
	def setFinishedTime():
		pass
	def beFriendly():
		pass
	def deFriendly():
		pass

	#get method
	def getTitle():
		pass
	def getContent():
		pass
	def getFinishedTime():
		pass
	def isFriendly():
		pass
