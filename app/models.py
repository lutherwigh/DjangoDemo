from django.db import models
import uuid

# Create your models here.
class Article(models.Model):
    title = models.CharField(u'标题',max_length = 256)
    content = models.TextField(u'内容')
    time = models.DateTimeField()

class Person(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid1,editable = False,null = False)
    name = models.CharField(max_length = 6,null = False)
    age = models.IntegerField()
    time = models.DateTimeField(auto_now = True,null = False)    