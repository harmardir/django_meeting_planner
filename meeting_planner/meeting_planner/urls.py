from django.contrib import admin
from django.urls import path

from website.views import welcome , date , about
from meetings.views import detail, rooms_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', welcome , name = 'welcome'),
    path('date/', date),
    path('about/', about),
    path('meetings/<int:id>',detail , name='detail'),
    path('rooms', rooms_list, name='rooms'),
]
