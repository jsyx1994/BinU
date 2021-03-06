#coding:utf-8
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
class Message(models.Model):
	title = models.CharField(
		max_length = 50,
		)
	message = models.CharField(
		max_length = 200,
		)
	sended_time = models.DateTimeField()
	readed = models.BooleanField(
		default = False,
		)
	sender = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		default = None,
		related_name = 'sender',
		)
	receiver = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		default = None,
		related_name = 'receiver',
		)
	def __unicode__(self):
		return self.title

	def get_title(self):
		pass
	def get_message(self):
		pass
	def get_sended_time(self):
		pass
	def is_readed(self):
		pass

