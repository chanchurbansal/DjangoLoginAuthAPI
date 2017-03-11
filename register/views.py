from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random
import string
from register.models import Resume
from register.forms import resumeForm
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

def isValid():
	return True
def createUser(req):
	if req.method == 'POST':
		form=resumeForm(req.POST)
		print("Her")
		us = req.POST.get("username","")
		na = req.POST.get("name","")
		ag = req.POST.get("age","")
		co = req.POST.get("contactNum","")
		em = req.POST.get("email","")
		ar = req.POST.get("areaOfExpertise","")
		ad = req.POST.get("address","")
		ci = req.POST.get("city","")
		st = req.POST.get("state","")
		pr = req.POST.get("prefferedLocation","")
		qu = req.POST.get("qualification","")
		te = req.POST.get("teachingExperience","")
		cu = req.POST.get("currentSchool","")
		if isValid:
		
			try:
				q=Resume(username=us,name=na,age=ag,contactNum=co,email = em,areaOfExpertise = ar,address = ad,city = ci,state = st,prefferedLocation = pr,qualification = qu,teachingExperience = te,currentSchool =cu)
				q.save()
				return render(req, 'signUp.htm', {'user_obj': q,'is_registered':True })
			except:
				raise
				return HttpResponse("error")
	else:
		form = resumeForm()  # an unboundform
		return render(req,'signUp.htm', {'form': form})