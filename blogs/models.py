from django.db import models

# Create your models here.

class User(models.Model):

	username = models.CharField(max_length=200)

	password = models.CharField(max_length=200)

	created_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.username

class Post(models.Model):
	
	pub_date = models.DateTimeField(auto_now_add=True)

	title =  models.CharField(max_length=200)

	content = models.TextField()

	url = models.CharField(max_length=200,default='https://leetcode.com/problemset/all/')

	category = models.CharField(max_length=200, null=True)

	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)

	def __str__(self):
		return self.title


