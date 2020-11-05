from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myfun(request):
	return HttpResponse("hello world")
def fun(request):
	return HttpResponse("2nd helloworld")
def ff(request):
	return render(request,'sample.html')