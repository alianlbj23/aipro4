from django.contrib import admin
from django.urls import path
from aiproject import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('mdtest/', views.mdtest), #markdown語法測試用網頁
    path('upload/', views.upload), #上傳文章用照片
    path('imagedel/<int:id>/', views.imagedel), #刪除上傳的檔案記錄資料
    path('article_list/<int:mod>/', views.article_list),
    #path('article_list_tag/<str:tag>/', views.article_list_tag),
    path('article_read/<int:mod>/<int:id>/', views.article_read),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG: #在debug模式啟動時
    #django原本不支援靜態檔，所以要加上這行之後在網頁http://127.0.0.1:8000/media/image/~~~~~.jpg 可直接在網頁上顯示該資料夾底下的圖片
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    
