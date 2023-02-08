from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UploadVideoForm

def index(request):
	return render(request, "hubspot/index.html")

def auth_home(request):
	return render(request, "hubspot/auth_home.html")

def no_such(request):
	return render(request, "hubspot/no_such.html")

def signup(request):

	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		confirm_password = request.POST['confirm_password']

		my_user = User.objects.create_user(username, email, password)
		my_user.save()

		return redirect("auth_home")

	return render(request, "hubspot/signup.html")

def signin(request):

	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]

		user = authenticate(username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect("auth_home")
		else:
			return redirect("no_such")

	return render(request, "hubspot/signin.html")

def signout(request):
	logout(request)
	return redirect("index")

def upload_vid(request):
	form = UploadVideoForm()

	if request.method == "POST":
		form = UploadVideoForm(data=request.POST, files=request.FILES)
		if form.is_valid():
			form.save()
		return redirect("auth_home")

	context = {
		'form':form
	}
	return render(request, "hubspot/upload_vid.html", context)