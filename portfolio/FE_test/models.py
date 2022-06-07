from django.db import models

# Create your models here.
class User(models.Model):
	user_account = models.CharField(max_length=30)
	user_name = models.CharField(max_length=15)
	user_password = models.CharField(max_length=20)
	user_career = models.CharField(max_length=15)
	user_age = models.IntegerField(default=20)
	user_income = models.IntegerField(default=0)


		
		 

	def __str__(self):
		return 'User: Account: %s, Name: %s' % (self.user_account, self.user_name)
	def get_id(self):
		return self.id

