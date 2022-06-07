from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import User
# Create your views here.

def home(request):
	return render(request, 'FE_test/index.html', {})

def pie_chart(request):
	context = {
		'data': [
			['AMAZON.COM', 20], 
			['ABBOTT LABORATORIES', 30], 
			['AES', 15], 
			['ABIOMED', 35]], 
	}
	return render(request, 'FE_test/pie_chart.htm', context)

def member_detail_test(request):
	
	class User():	
		def __init__(self, id, name):
			self.id = id
			self.name = name
	user = User('U001', 'Ken')
	return render(request, 'FE_test/test.html', {'user': user})
	

def aboutUs(request):
	pass

def knowledge(request):
	pass

def login(requets):
	pass

def member_detail(request, user_id):
	user = get_object_or_404(User, pk=user_id)
	return render(request, 'FE_test/test.html', {'user': user})

def member_invest(request):
	pass

def register(request):
	pass
