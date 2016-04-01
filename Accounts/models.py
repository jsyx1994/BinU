#coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import(
	BaseUserManager,AbstractBaseUser
	)
class MyUserManager(BaseUserManager):
    def create_user(self, email,nick_name,real_name,password=None):
        """
        Creates and saves a User with the given email, and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            nick_name=nick_name,
			real_name=real_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,nick_name,real_name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            nick_name=nick_name,
	    real_name=real_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
	USER_SEX = (
		('M','男'),
		('F','女'),
   		)
	email = models.EmailField(
		verbose_name='email address',
		max_length=255,
		unique=True,
		)
	sex = models.CharField(
		max_length = 1,
		choices = USER_SEX,
		default = 'M',
		)
	nick_name = models.CharField(
		#primary_key = True,
		unique = True,
                max_length = 100,
		)
	work = models.CharField(
		max_length = 20,
		blank = True,
    		)
	phone_num = models.CharField(
		max_length = 15,
               # unique = True,通过后台来验证
		blank = True,
                null = True,
		)
	height = models.PositiveSmallIntegerField(
		blank=True,
		null = True,
		)
	weight = models.PositiveSmallIntegerField(
		blank=True,
		null =True,
		)
	birthday = models.DateField(
		blank=True,
		null = True,
		)
	real_name = models.CharField(
		unique = True,
		max_length = 100,
		)
        online = models.NullBooleanField()

	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = MyUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = [
		#'email',
		'nick_name',
		'real_name',
		]
	friends=models.ManyToManyField(
		'self',
		related_name = 'friShip',
		through = 'FriendShip',
		through_fields = ('subject','friend'),
		symmetrical=False,
		)

        #blow are the basic mehtods
	def get_full_name(self):
		# The user is identified by their email address
	    return self.real_name
	def get_short_name(self):
		# The user is identified by their email address
	    return self.nick_name
	def __unicode__(self):              # __unicode__ on Python 2
	    return self.email
	def has_perm(self, perm, obj=None):
	    "Does the user have a specific permission?"
	    # Simplest possible answer: Yes, always
	    return True
	def has_module_perms(self, app_label):
	    return True
	@property
	def is_staff(self):
	    # Simplest possible answer: All admins are staff
	    return self.is_admin
        #above are the basic methods


#Set method
	def set_real_name(self,real_name):
	    self.real_name = real_name

	def set_nick_name(self,nick_name):
	    self.nick_name = nick_name

	def set_sex(self,choice):
	    self.sex = unicode(choice)

	def set_birthday(self,birthday):
	    self.birthday = birthday

	def set_work(self,work):
	    self.work = work

	def set_email(self,email):
	    self.email = email

        def set_pswd(self,raw_password):
            self.set_password(raw_password)

	def set_profile(self):
	    pass

	def set_phone_num(self,phone_num):
	    self.phone_num = phone_num

	def set_height(self,height):
	    self.height = height

	def set_weight(self,weight):
            self.weight = weight

	def set_online(self):
	    self.online = True

	def set_offline(self):
	    self.online = False
#Get method

	def get_real_name(self):
	    return self.real_name

	def get_nick_name(self):
	    return self.nick_name

	def get_sex(self):
            return self.get_sex_display()

	def get_age(self):
            date_of_birth=self.get_birthday()
            if date_of_birth :
                now = timezone.now()
                age = now.year - date_of_birth.year
                delta = now.month - date_of_birth.month
                if delta <0:
                    age -= 1
	        return age
            else:
                pass

	def get_birthday(self):
            if self.birthday :
	        return self.birthday
            else:
                pass

	def get_work(self):
	    return self.work

	def get_email(self):
	    return self.email

        #见密码管理http://python.usyiyi.cn/django_182/topics/auth/passwords.html
	def get_pswd():
            pass

	def get_profile():
	    pass

	def get_phone_num(self):
            if self.phone_num:
	        return self.phone_num
            else:
                return ''
	def get_height(self):
	    return self.height

	def get_weight(self):
	    return self.weight

	def is_online(self):
	    return self.online

        #通过昵称来添加好友
        def add_friend(self,nick_name):
            obj = MyUser.objects.get(nick_name = nick_name)
            fri = FriendShip(
                subject = self,
                friend = obj,
                    )
            fri.save()

        def del_friend(self,nick_name):
            fri = FriendShip.objects.get(friend__nick_name = nick_name)
            fri.delete()

class FriendShip(models.Model):
	subject = models.ForeignKey(
		MyUser,
		related_name = 'subject',
		)
	friend = models.ForeignKey(
		MyUser,
		related_name = 'friend',
		)
	friend_each_other = models.BooleanField(
		default = False,
		)
	level = models.PositiveSmallIntegerField(
		default = 0
		)
	def __unicode__(self):
		return self.subject.nick_name+u'\'s friend'

