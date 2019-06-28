from django.urls import path
from . import views

urlpatterns = [
  path('', views.entry_list, name='entry_list'),
  path('entry/<int:pk>/', views.entry_detail, name='entry_detail'),
  path('entry/new/', views.post_new, name='post_new'),
  path('entry/<int:pk>/edit/', views.post_edit, name='post_edit'),
  path('entry/<int:pk>/remove/', views.post_remove, name='post_remove'),
  path('accounts/singup/', views.signup, name='signup'),
]
