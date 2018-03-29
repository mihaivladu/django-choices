from django.db import models


# Lookups
class MyLookup(models.Lookup):
    lookup_name = 'lkp'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process.rhs(compiler, connection)
        params = lhs_params + rhs_params
        return '%s <> %s' % (lhs, rhs), params


# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname + ' ' + self.lastname


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
        ('P', 'Post'),
        ('V', 'Video')
    )
    target_type = models.CharField(max_length=1, choices=TARGET_TYPE_CHOICES)
    target_id = models.IntegerField()
    text = models.TextField(default='')

    def __str__(self):
        return self.text