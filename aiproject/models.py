from django.db import models
from django.db.models.base import Model

class Member(models.Model):
    Name = models.CharField(max_length=50) 
    Title = models.CharField(max_length=50) 
    Expertise = models.CharField(max_length=50) 
    Education = models.CharField(max_length=50) 
    def __str__(self):
        return self.Name

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



