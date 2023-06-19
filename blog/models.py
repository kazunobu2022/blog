from django.db import models
from mdeditor.fields import MDTextField # 追加

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = MDTextField() 
