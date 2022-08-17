from django.shortcuts import render
from mysite import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from aiproject.models import Member
from .models import *
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm

import os
import sys
sys.path.append('aiproject')
import tool
from markdown import markdown


def home(request):
    members = Member.objects.all()
    articles = Article.objects.all()
    return render(request, 'index.html', locals())

def mdtest(request):
    return render(request, 'mdtest.html', locals())

@login_required(login_url='/admin/login/?next=/')
def upload(request):
    if request.method=="POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                uploaded_file = request.FILES['file']
                fss = FileSystemStorage()
                file = fss.save(uploaded_file.name, uploaded_file)
                filerec = PostImage()
                filerec.title = request.POST.get("title").strip()
                filerec.image = fss.url(file)
                filerec.save()
                return redirect('/upload/')
            except Exception as e:
                print(e)
    else:
        form = UploadFileForm()
    images = PostImage.objects.all()
    domain = request.build_absolute_uri('/')[:-1]
    return render(request, "upload.html", locals())

def imagedel(request, id):
    target = PostImage.objects.get(id=id)
    target_file = str(target.image)
    try:
        target.delete()
        os.remove(target_file[1:])
    except Exception as e:
        print(e)
    return redirect("/upload/")
    
def article_list(request,mod):
    postcat = PostCat.objects.get(no=mod)
    articles = Post.objects.filter(category = postcat)
    keywords = Keyword.objects.all()
    return render(request, 'article_list.html', locals())

def article_list_tag(request, tag):
    tag_list = list()
    tag_list.append(tag)
    tag_list = set(tag_list)
    slide_pk = slide_article_pk(tag_list)
    #articles = Article.objects.filter(pk__in=slide_pk[0])
    #ai_articles = AI_Article.objects.filter(pk__in=slide_pk[1])
    articles = Post.objects.filter(content__icontains=tag)
    keywords = Keyword.objects.all()
    return render(request, 'article_list_tag.html', locals())
    
from pydocx import PyDocX
import pathlib
def dataOutput(information,range1, range2):
    left = information.find(range1)
    information = information[left+len(range1):]
    right = information.find(range2)
    target = information[:right]
    target = target.strip()
    Updateinformation = information[right:]
    return target,Updateinformation


def slide_article_pk(target_set):
    target_set = set(target_set)
    articles = Article.objects.all()
    ai_articles = AI_Article.objects.all()
    dh_articles = DH_Article.objects.all()
    pk_list = list()
    ai_pk_list = list()
    dh_pk_list = list()
    # pk_list = tool.GetPkList(articles,target_set,"articles")
    # ai_pk_list = tool.GetPkList(ai_articles,target_set,"ai_articles")
    # dh_pk_list = tool.GetPkList(dh_articles,target_set,"dh_articles")

    for j in articles:
        tmp = Article.objects.filter(pk=j.pk)
        article_title = str(list(tmp.values('Chi_title'))[0]['Chi_title'])
        article_tag = set(tool.key_find("word_read",article_title))
        if len(list(article_tag & target_set)) != 0:
            pk_list.append(j.pk)

    for j in ai_articles:
        tmp = AI_Article.objects.filter(pk=j.pk)
        article_title = str(list(tmp.values('Chi_title'))[0]['Chi_title'])
        article_tag = set(tool.key_find("ai_word_read",article_title))
        if len(list(article_tag & target_set)) != 0:
            ai_pk_list.append(j.pk)

    for j in dh_articles:
        tmp = DH_Article.objects.filter(pk=j.pk)
        article_title = str(list(tmp.values('Chi_title'))[0]['Chi_title'])
        article_tag = set(tool.key_find("dh_word_read",article_title))
        if len(list(article_tag & target_set)) != 0:
            dh_pk_list.append(j.pk)

    return [pk_list,ai_pk_list,dh_pk_list]

from django.utils.safestring import mark_safe
# def article_read(request,mod,pk):
#     print("mod: ", mod)
#     if mod == 0:
#         article_tmp = Article.objects.filter(pk=pk)
#         file_name = "word_read"
#         # articles = Article.objects.all()
#     elif mod == 1:
#         article_tmp = AI_Article.objects.filter(pk=pk)
#         file_name = "ai_word_read"
#         # ai_articles = AI_Article.objects.all()
#     elif mod == 2:
#         article_tmp = DH_Article.objects.filter(pk=pk)
#         file_name = "dh_word_read"
#         # ai_articles = AI_Article.objects.all()
#     article_title = str(list(article_tmp.values('Chi_title'))[0]['Chi_title'])
#     article_title_eng = str(list(article_tmp.values('Eng_title'))[0]['Eng_title'])
#     article_editor = str(list(article_tmp.values('Editor'))[0]['Editor'])
#     article_url = str(list(article_tmp.values('Data_url'))[0]['Data_url'])
#     path = str(pathlib.Path(__file__).parent.absolute()).replace('\\','/')
#     path = path+"/"+file_name+"/"+str(article_title)+".docx"
#     print("path: ",path)
#     html = PyDocX.to_html(path)
#     with open("test.html", 'w', encoding="utf-8") as f:
#         f.write(html)
#     with open("test.html", 'r', encoding="utf-8") as f:
#         html_data = f.read()
#     body_html, html_data = dataOutput(html_data,"<body>", "</body>")
#     print("!!!!!!!!!!!",article_url)
#     body_html = mark_safe(body_html)
#     all_keys = set(tool.key_word())
#     article_tag = set(tool.key_find(file_name,article_title))
#     tags = list(all_keys & article_tag)
#     slide_pk = slide_article_pk(tags)
#     articles = Article.objects.filter(pk__in=slide_pk[0])
#     ai_articles = AI_Article.objects.filter(pk__in=slide_pk[1])
#     dh_articles = DH_Article.objects.filter(pk__in=slide_pk[2])
#     return render(request, 'tool.html', locals())

def article_read(request, mod, id):
    article = Post.objects.get(id=id)
    try:
        pcat = PostCat.objects.get(no=mod)
    except:
        pcat = PostCat.objects.get(no=0)
    related_posts = Post.objects.filter(category=pcat)
    categories = PostCat.objects.all()
    mcontent = markdown(article.content, extensions=['markdown.extensions.extra', 
                                                     'markdown.extensions.codehilite',
                                                     'tables'])
    return render(request, "article_read.html", locals())