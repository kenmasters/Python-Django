from django.urls import path
from pdb_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item/<int:id>/', views.detail, name='detail'),
    path('categories/', views.categories, name='categories'),
]


