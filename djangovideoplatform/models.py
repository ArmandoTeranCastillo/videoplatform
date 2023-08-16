from django.db import models


class User(models.Model):
    user = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    profile_picture = models.CharField(max_length=100)



class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    upload_date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Tag(models.Model):
    tag = models.CharField(max_length=100)
    video = models.ManyToManyField(Video)


class Comment(models.Model):
    comment = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)


class Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    reaction = models.BooleanField()


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(User, on_delete=models.CASCADE, related_name='channel_id')

