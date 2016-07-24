from django.contrib import admin

# Register your models here.
from demo.models import Post, PostType, Comment

admin.site.register([Post, PostType, Comment])
