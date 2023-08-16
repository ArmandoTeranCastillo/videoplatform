from django.db import models


class User(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    user = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)


class Video(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    upload_date = models.DateField(auto_now_add=True)
    thumbnail = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    user_id = models.CharField(max_length=50)
