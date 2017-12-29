from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
	#return HttpResponse("hello world!")
	context = {}
	context['hello'] = "hello world" #hello对应模板hello.html里面{{hello}}
	return render(request,"hello.html",context)
