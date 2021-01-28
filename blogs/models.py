from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Post(models.Model):
	
	pub_date = models.DateTimeField(default=timezone.now)

	title =  models.CharField(max_length=200)

	problem_num = models.IntegerField(
		default=1,
		validators=[
            MaxValueValidator(2000),
            MinValueValidator(1)
        ]
    )

	description = models.TextField(default="")

	content = models.TextField(default=" ")

	url = models.URLField(max_length=200,default='https://leetcode.com/problemset/all/')

	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blogs:post-detail',kwargs={'pk':self.pk})

class Feedback(models.Model):

	pub_date = models.DateTimeField(default=timezone.now)

	title =  models.CharField(max_length=200)

	description = models.TextField()

	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return "Feedback:{title} by {user}".format(title = self.title, user = self.user)

	def get_absolute_url(self):
		return reverse('blogs:index')