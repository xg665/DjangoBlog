from django.contrib import admin
from .models import Post, Feedback
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Post)
admin.site.register(Feedback)
