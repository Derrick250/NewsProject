from __future__ import unicode_literals

from django.db import models
import datetime
# Create your models here.


LEXERS = []
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)



class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    gender = models.IntegerField()
    password = models.TextField()
    eduLevel = models.IntegerField()

    class Meta:
        ordering = ('name', )


class Articles(models.Model):
    title = models.TextField(max_length=100)
    url = models.TextField()
    paper = models.TextField()
    author = models.TextField()
    date = models.DateField(default=datetime.datetime.now().strftime("%Y-%m-%d"))
    time = models.TimeField(default=datetime.datetime.now().strftime("%H:%M:%S"))
    description = models.TextField()

    class Meta:
        ordering = ('title', )




class Comments(models.Model):
    text = models.TextField(max_length=1000)
    articleID = models.TextField()
    userID = models.TextField()
    date = models.DateField(default=datetime.datetime.now().strftime("%Y-%m-%d"))
    time = models.TimeField(default=datetime.datetime.now().strftime("%H:%M:%S"))

    class Meta:
        ordering = ('text', )


class UserTags(models.Model):
    tag = models.TextField(max_length=100)
    frequency = models.IntegerField(default=0)
    userID = models.TextField()


    class Meta:
        ordering = ('tag', )

class ArticleTags(models.Model):
    tag = models.TextField(max_length=100)
    articleID = models.TextField()

    class Meta:
        ordering = ('tag', )