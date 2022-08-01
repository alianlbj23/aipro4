import pathlib
import os
import django
import docx
import jieba
import jieba.analyse
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()
from aiproject.models import *
doc = docx.Document(
    "C://Users//User//new_ai_lastest//aiproject//mysite//aiproject//dh_word_read//"+
    "課堂裡的Voyant Tools練習"+
    ".docx"
)
content = ""
for para in doc.paragraphs:
    content+=str(para.text)
content = str(content)
tags = jieba.analyse.extract_tags(content, topK=20, withWeight=True)
key_list = list()
for tag in tags:
    key_list.append(tag[0])
print(key_list)