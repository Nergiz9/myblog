from django.db import models


# Create your models here.

class PostType(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    desc = models.TextField()


class Post(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=250)
    body = models.TextField()
    seem = models.IntegerField()
    publish = models.DateTimeField()
    type = models.ForeignKey(PostType, null=True)


class Comment(models.Model):
    def __str__(self):
        return self.author

    author = models.CharField(max_length=60)
    mail = models.EmailField()
    text = models.TextField()
    post = models.ForeignKey(Post, null=True)
