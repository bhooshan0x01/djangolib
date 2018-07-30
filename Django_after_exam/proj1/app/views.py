# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import User,Books
from django.db.models import Q

# Create your views here.


def index(request):
	return HttpResponse("<h1>Welcome to the XYZ Library</h1>")


@csrf_exempt
def register(request):
	if request.method == 'GET':

		return render(request,'register.html',{})
	elif request.method == 'POST':
		context = {} #to show on UI
		#print request.POST
		name = request.POST['name']
		username = request.POST['username']
		password = request.POST['password']
		phone_number = request.POST['phone_number']
		type_user = request.POST['type_user']
		#Data Received 
		context['name'] = name
		context['password'] = username
		context['password'] = password
		context['phone_number'] = phone_number
		context['type_user'] = type_user
		if User.objects.filter(username=username).exists():
			print 'User exists'
		
		else:
			aa=User(name=name,username=username,password=password,phone_number=phone_number,type_user=type_user)
			aa.save()
		return redirect("/login")
	
	

@csrf_exempt
def login(request):
	if 'username' in request.session:
		user_obj=User.objects.get(username=request.session['username'])
		if user_obj.type_user =='Librarian':
			return redirect('/Librarian')
		elif user_obj.type_user == 'student':
			return redirect('/student')
	else:
		if request.method == 'GET':
		   	return render(request,'login.html',{})
		elif request.method == 'POST':
			context = {}
			message = ''
			#print request.POST
			username = request.POST['username']
			password = request.POST['password']
			
			#Data Received 
			if User.objects.filter(username=username).exists():
				user_obj=User.objects.get(username=username)
				if user_obj.password == password:
					request.session['username']=username
					if user_obj.type_user=='Librarian':
						return redirect("/Librarian")
					elif user_obj.type_user=='student':
						return redirect("/student")
			else:
				message = 'User not exists'
				return redirect("/register")


			

@csrf_exempt
def LogOut(request):
	if 'username' in request.session:
		del request.session['username']
	return redirect('/login')	

@csrf_exempt
def book_details(request):
	context={}
	id = request.GET['b_id']
	#print id
	book_obj = Books.objects.get(id=id)
	#print book_obj.summary
	context['book_details']=book_obj.summary
	return render(request,'details.html',context)

@csrf_exempt
def view_profile(request):

	context = {}
	context['user'] = User.objects.all()
	return render(request,'profile.html',context)

@csrf_exempt
def search_by_name(request):
	context={}
	search_by_name = request.POST['search_name']
	if Books.objects.filter(Q(bookname=search_by_name)|Q(author=search_by_name)|Q(subject=search_by_name)):
		search_=Books.objects.filter(Q(bookname=search_by_name)|Q(author=search_by_name)|Q(subject=search_by_name))
		context['search_by']=search_
		return render(request,'result.html',context)
	else:
		return redirect('/student')

def Librarian(request):
	if 'username' in request.session:
		user_obj=User.objects.get(username=request.session['username'])
		if user_obj.type_user == 'Librarian':
			context = {}
			return render(request,'Librarian.html',{})
		else:
			return redirect('/login')
	else:
		return redirect('/login')

def student(request):
	if 'username' in request.session:
		user_obj=User.objects.get(username=request.session['username'])
		if user_obj.type_user == 'student':
			context = {}
			context['book'] = Books.objects.all()
			return render(request,'student.html',context)
	else:
		return redirect('/login')

def  BookIssue(request):
	