from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random
import string
from login.models import User

# Create your views here.
def index(req):
	data=req.POST.get('Name','')
	return HttpResponse(data)


def createUser(req):
	un = req.GET['un']
	p = req.GET['p']
	n=req.GET['n']
	
	try:
		z=User.objects.raw('SELECT * from login_user where username = "'+un+'"')[0].name

	except:
		q=User(username=un,password=p,name=n,auth12="aa")
		q.save()
		return JsonResponse({"Status":"Success"})
	return JsonResponse({"Status":"Fail"})


def loginUser(req): 
	un = req.GET['un']
	p = req.GET['p']
	a=''.join(random.choice(string.ascii_uppercase + string.digits+ string.ascii_lowercase) for _ in range(16))
	q="error"
	try:
		q=User.objects.raw('SELECT * from login_user where username = "'+un+'" and password = "'+p+'"')[0].name
		a=User.objects.raw('SELECT * from login_user where username = "'+un+'" and password = "'+p+'"')[0].auth12
	except:
		return JsonResponse({"Error":"UserNotFound"})
	trying=False	
	if len(a)<=5 :
		trying=True
	while(trying):
		a=''.join(random.choice(string.ascii_uppercase + string.digits+ string.ascii_lowercase) for _ in range(16))
		try:
			x=User.objects.raw('SELECT * from login_user where auth12 = "'+a+'"')[0].name
		except:
			trying = False
	w=User(username=un,password=p,name=q,auth12=a)
	w.save()
	return JsonResponse({"Authentication":a,"Name":q})


def verifyUser(req): 
	un = req.GET['un']
	a = req.GET['a']
	
	try:
		q=User.objects.raw('SELECT * from login_user where username = "'+un+'" and auth12 = "'+a+'"')[0].name
		
	except:
		return JsonResponse({"Error":"UserNotVerified"})
	
	return JsonResponse({"Success":"Authentication Successfull"})

def logoutUser(req): 
	un = req.GET['un']
	
	try:
		q=User.objects.raw('SELECT * from login_user where username = "'+un+'"')[0].name
		p=User.objects.raw('SELECT * from login_user where username = "'+un+'"')[0].password
		
	except:
		return JsonResponse({"Error":"UserNotFound"})
	w=User(username=un,password=p,name=q,auth12='NA')
	w.save()
	return JsonResponse({"Success":"Logout Successfull"})


