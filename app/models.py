from django.db import models


# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname


class Video(models.Model):
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.url


class Post(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    TARGET_TYPE_CHOICES = (
        (Post, 'P'),
        (Video, 'V')
    )
    target_type = models.CharField(max_length=1, choices=TARGET_TYPE_CHOICES)
    target_id = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.text

