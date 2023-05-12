from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('games/', views.GameList.as_view(), name='games_index'),
    path('games/create/', views.GameCreate.as_view(), name='games_create'),
    path('games/<int:pk>/', views.GameDetail.as_view(), name='games_detail'),
    path('games/<int:pk>/update', views.GameUpdate.as_view(), name= 'games_update'),
    path('games/<int:pk>/delete', views.GameDelete.as_view(), name= 'games_delete'),
    path('games/<int:pk>/add_review/', views.add_review, name='add_review'),
    path('games/<int:game_id>/assoc_publisher/<int:publisher_id>/', views.assoc_publisher, name='assoc_publisher'),
    path('games/<int:game_id>/remove_publisher/<int:publisher_id>/', views.remove_publisher, name='remove_publisher'),
    path('publishers/', views.PublisherList.as_view(), name='publishers_index'),
    path('publishers/<int:pk>/', views.PublisherDetail.as_view(), name='publishers_detail'),
    path('publishers/create/', views.PublisherCreate.as_view(), name='publishers_create'),
    path('publishers/<int:pk>/update/', views.PublisherUpdate.as_view(), name='publishers_update'),
    path('publishers/<int:pk>/delete/', views.PublisherDelete.as_view(), name='publishers_delete'),
]