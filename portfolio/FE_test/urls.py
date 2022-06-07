from django.urls import path
from . import views
app_name = 'test'
urlpatterns = [
	path('home', views.home,  name='index'),
	#path('aboutUs', views.aboutUs, name='index'),
	#path('knowledge', views.knowledge, name='index'),
	#path('login', views.login, name='index'),

	path('member/<int:user_id>/', views.member_detail, name='index'),
	#path('member/<str:username>/invest', views.member_invest, name='index'),
	#path('register', views.register, name='index'),
	

	path('pie', views.pie_chart, name='pie'),
	path('test', views.member_detail_test, name='member_detail')
]
