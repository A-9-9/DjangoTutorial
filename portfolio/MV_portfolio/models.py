from django.db import models

# Create your models here.
class User(models.Model):
	user_name = models.CharField(max_length=100)
	user_account = models.CharField(max_length=50)
	user_password = models.CharField(max_length=50)

class Department(models.Model):
	name = models.CharField(max_length=100)
class Company(models.Model):
	name = models.CharField(max_length=100)
	department = models.ForeignKey(Department, on_delete=models.CASCADE)
class Invest_combination(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	#weights = models
	#shares
	#conbination_id
class Member_invest(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	combination = models.ForeignKey(Invest_combination, on_delete=models.CASCADE)
	date = models.DateTimeField()
	total = models.IntegerField(default=0)




class Price(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	date = models.DateTimeField('Closing price')
	ROI = models.FloatField(default=0)
