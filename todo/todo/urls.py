
from django.contrib import admin
from django.urls import path
from main.views import *
from homework import views
from homework.views import  homepage,newf,homework,meeting,add_tomeet,habits,create
from django.conf import settings
from django.conf.urls.static import static

from homework.views import delete_tomeet, mark_tomeet, unmark_tomeet




urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/',homepage),
    path('test/',test,name='test'),
    path('newf/',newf,name='newf'),
    path('homepage/',homepage,name='homepage'),
    path('homework/',homework,name='homework'),
    path('meeting/',meeting,name='meeting'),
    path('add-todo/',add_todo,name='add-todo'),
    path('add-tomeet/',add_tomeet,name='add-tomeet'),
    path('', views.habits),
    path('create/', views.create),
    path("delete-todo/<id>/",delete_todo,name="delete-todo"),
    path("mark-todo/<id>/",mark_todo,name="mark-todo"),
    path("unmark-todo/<id>/",unmark_todo,name="unmark-todo"),
    path("delete-tomeet/<id>/",delete_tomeet,name="delete-tomeet"),
    path("mark-tomeet/<id>/", mark_tomeet,name="mark-tomeet"),
    path("unmark-tomeet/<id>/", unmark_tomeet,name="unmark-tomeet"),

    ] + static (settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
