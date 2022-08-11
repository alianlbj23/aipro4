from django.db import models
from django.db.models.base import Model

class Member(models.Model):
    Name = models.CharField(max_length=50) 
    Title = models.CharField(max_length=50) 
    Expertise = models.CharField(max_length=50) 
    Education = models.CharField(max_length=50) 
    def __str__(self):
        return self.Name

class PostCat(models.Model):
    no = models.PositiveSmallIntegerField(default=0)
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
class Post(models.Model):
    category = models.ForeignKey(PostCat, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="中文標題")
    etitle = models.CharField(max_length=200, verbose_name="英文標題", default="", null=True, blank=True)
    jtitle = models.CharField(max_length=200, verbose_name="日文標題", default="", null=True, blank=True)
    editor = models.CharField(max_length=200, verbose_name="編輯")
    content = models.TextField(verbose_name="內容")
    url = models.CharField(max_length=200, verbose_name="來源網址")
    def __str__(self):
        return self.title


class Article(models.Model):
    Chi_title = models.CharField(max_length=500) 
    Eng_title = models.CharField(max_length=500)
    Editor = models.CharField(max_length=500)
    Content = models.CharField(max_length=2000) 
    Data_url = models.CharField(max_length=500) 
    def __str__(self):
        return self.Chi_title
        
class AI_Article(models.Model):
    Chi_title = models.CharField(max_length=500) 
    Eng_title = models.CharField(max_length=500)
    Editor = models.CharField(max_length=500)
    Content = models.CharField(max_length=2000) 
    Data_url = models.CharField(max_length=500) 
    def __str__(self):
        return self.Chi_title
    
class DH_Article(models.Model):
    Chi_title = models.CharField(max_length=500) 
    Eng_title = models.CharField(max_length=500)
    Editor = models.CharField(max_length=500)
    Content = models.CharField(max_length=2000) 
    Data_url = models.CharField(max_length=500) 
    def __str__(self):
        return self.Chi_title



