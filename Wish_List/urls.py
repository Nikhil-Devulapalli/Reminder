from django.contrib import admin
from django.urls import path,include
from wis_list import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('wis_list.urls')),
]
