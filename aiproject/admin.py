from django.contrib import admin
from aiproject.models import *


class PostCatAdmin(admin.ModelAdmin):
    list_display = ('no', 'name')
admin.site.register(PostCat, PostCatAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'etitle', 'jtitle', 'editor', 'content', 'url')
admin.site.register(Post, PostAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Title', 'Expertise', 'Education']
admin.site.register(Member, MemberAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['Chi_title', 'Eng_title', 'Editor', 'Content','Data_url','pk']
admin.site.register(Article, ArticleAdmin)

class AI_ArticleAdmin(admin.ModelAdmin):
    list_display = ['Chi_title', 'Eng_title', 'Editor', 'Content','Data_url','pk']
admin.site.register(AI_Article, AI_ArticleAdmin)

class DH_ArticleAdmin(admin.ModelAdmin):
    list_display = ['Chi_title', 'Eng_title', 'Editor', 'Content','Data_url','pk']
admin.site.register(DH_Article, DH_ArticleAdmin)
# Register your models here.
