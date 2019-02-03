from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('property-grid.html/', views.post_list_all_categories, name='post_list_all_categories'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('category/<int:category>/', views.post_list_category, name='post_list_category'),
    path('judge/<int:judge>/', views.post_list_judge, name='post_list_judge'),
    path('club/<int:club>/', views.post_list_club, name='post_list_club'),
    path('dog/<int:dog>/', views.post_list_dog, name='post_list_dog'),
    path('search/', views.search, name='search'),

]
