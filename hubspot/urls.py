from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('home/', views.auth_home, name="auth_home"),
	path('home/upload/', views.upload_vid, name="upload_vid"),
	path('signup/', views.signup, name="signup"),
	path('signin/', views.signin, name="signin"),
	path('home/signout/', views.signout, name="signout"),
	path('no_such/', views.no_such, name="no_such"),
]