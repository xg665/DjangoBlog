from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Post(models.Model):
	
	pub_date = models.DateTimeField(default=timezone.now)

	title =  models.CharField(max_length=200)

	content = models.TextField()

	url = models.URLField(max_length=200,default='https://leetcode.com/problemset/all/')

	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blogs:post-detail',kwargs={'pk':self.pk})

