from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class User(models.Model):
	user_name = models.CharField(max_length=100)
	user_account = models.CharField(max_length=50)
	user_password = models.CharField(max_length=50)

	def __str__(self):
		return self.user_name

class Department(models.Model):
	name = models.CharField(max_length=100)



class Company(models.Model):
	name = models.CharField(max_length=100)
	department = models.ForeignKey(Department, on_delete=models.CASCADE)


class Member_invest(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	combination = models.ForeignKey(Information, on_delete=models.CASCADE)
	date = models.DateTimeField()
	total = models.IntegerField(default=0)



class Information(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	date = models.DateTimeField('Closing price')
	ROI = models.FloatField(default=0)
	weights = models.ArrayField(CharField(max_length=50))
	shares = models.ArrayFailed(CharField(max_length=50))
