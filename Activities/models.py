#coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone
class Activity(models.Model):
	#各种类型的活动，一级活动下可以再分二级。。。。。。
	CATEGORY_LIST=(
		('BL','球类'),
		('KT','KTV'),
		('TR','旅行'),
	)
	title = models.CharField(max_length=50)
	category = models.CharField(max_length=2,choices=CATEGORY_LIST)

        #用户所设定的开始时间
	start_time = models.DateTimeField()

        #用户所设定的结束时间
	due_time = models.DateTimeField()

        #自动设定的发布时间，用于检查新旧，默认为对象被创建的时间
        pub_time = models.DateTimeField(
                default = timezone.now,
                )

        #人数限制
	person_num_limit = models.PositiveSmallIntegerField(

                )
        #当前人数
        person_count = models.PositiveSmallIntegerField(
                default = 0,
                )
	#place=models.
	active=models.NullBooleanField()

	person_joined=models.ManyToManyField(
                settings.AUTH_USER_MODEL,
                default = None,
                blank = True,
                )
	def __unicode__(self):
		return self.title

	#set method
	def set_title(self,title):
            self.title = title

	def set_category(self,category):
	    self.category = category

	def set_start_time(self,start_time):
	    self.start_time = start_time

	def set_due_time(self,duetime):
	    self.start_time = due_time

	def set_place():
            pass

    	def be_active(self):
            self.active = True

	def de_active():
	    self.active = False

	#get method
	def get_time_last(self):
            time_last = self.get_due_time() - self.get_start_time()
	    return self.time_last

	def get_start_time(self):
	    return self.start_time

	def get_due_time(self):
	    return self.due_time

        def get_person_num(self):
            return self.person_num_limit

        def get_person_count(self):
            return self.person_count

	def is_active(self):
	    return self.active

	def is_full(self):
            return self.get_person_num() == self.get_person_count()

        def is_due(self):
            return timezone.now() - self.get_start_time() < self.get_tiem_last()
