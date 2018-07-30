# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=50)
	username = models.CharField(max_length=50,blank="false")
	password = models.CharField(max_length=50,blank="false")
	phone_number = models.CharField(max_length=50)
	type_user_CHOICES=(
		('Librarian', 'Librarian'),
		('Student', 'student')
		)
	type_user = models.CharField(max_length=15, choices=type_user_CHOICES, default='student')
	
	def __str__(self): #to get name(s) on admin
		return self.username
	
class Books(models.Model):
	bookname = models.CharField(max_length=100)
	author = models.CharField(max_length=50)
	subject = models.CharField(max_length=50)
	copies = models.IntegerField(blank="false")
	summary = models.CharField(max_length=500,blank="true")

	def __str__(self):
		return self.bookname +" "+ self.author
book_status_CHECK = (
		('NoStatus','NOSTATUS'),
		('Booked','BOOKED'),
		('PickedUp','PICKEDUP'),
		('Returned','RETURNED')
		)
class IssueBook(models.Model):
	"""docstring for IssueBook"""
	bookname = models.CharField(max_length=100)
	author = models.CharField(max_length=50)
	subject = models.CharField(max_length=50)
	copies = models.IntegerField(blank="false")
	issueDate = models.DateField(null="true")

	book_status = models.CharField(max_length=20,choices=book_status_CHECK,default='NOSTATUS')
	
	def __str__(self):
		return self.bookname +" "+ self.copies
