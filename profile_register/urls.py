from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('profiles/', views.form, name = 'profile_insert'),
    path('<int:id>/', views.form, name = 'profile_update'),
    path('delete/<int:id>/', views.delete, name = 'profile_delete'),
    path('', views.home, name = 'home'),
    path('list/', views.list, name = 'profile_list')
]