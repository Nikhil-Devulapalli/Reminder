from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<List_id>',views.delete,name='delete'),
    path('edit/<List_id>',views.edit,name='edit'),
]