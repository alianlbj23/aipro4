import pathlib
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()
from aiproject.models import *

tmp = Article.objects.filter(pk=46).update(Eng_title=" ")
