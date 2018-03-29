from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(User, User)
admin.site.register(Post, Post)
admin.site.register(Video, Video)
admin.site.register(Comment, Comment)