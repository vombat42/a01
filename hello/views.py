from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import fNameAge, fUpFile
#from .functions import handle_uploaded_file

app_name = 'hello'

def index(request):
	host = request.META["HTTP_HOST"] # получаем адрес сервера
	user_agent = request.META["HTTP_USER_AGENT"]    # получаем данные бразера
	path = request.path     # получаем запрошенный путь
	userform = fNameAge()
	if request.method == "POST":
		age = request.POST.get("age")
		name = request.POST.get("name")
	else:
		age = 0
		name = 'Empty'
	data={"rm":request.method,"form": userform, "name":name, "age":age, "user_agent" : user_agent, "hst":host, "path":path}
	return render (request, "hello/index.html", context=data)

def about(request):
	return render(request, "hello/about.html")

def contacts(request):
    return render(request, "hello/contacts.html")

def textanalysis(request):
	ff=1
	form = fUpFile(request.POST, request.FILES)
	if request.method == 'POST' and request.FILES:
		form = fUpFile(request.POST, request.FILES)
		ff=request.FILES["textfile"].read()
		if form.is_valid():
			form.save()
			#return redirect('textanalysis')
	#else:
	data={"form": fUpFile(), "rf": request.FILES, "rp":form.Meta.fields, "ff":ff}
	return render(request, "hello/text_analysis.html",context=data)
	#if request.method == "POST" and request.FILES:
	#	handle_uploaded_file(request.FILES["textfile"])
	#	return HttpResponse("<div>File uploaded successfuly" \
	#						"</div><div><a href=/textanalysis>Назад</a></div>")
	#else:
	#	userform = fUpFile()
	#	data={"form": userform}
	#	return render(request, "text_analysis.html",context=data)
