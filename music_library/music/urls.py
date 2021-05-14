from django.urls import path
from . import views

urlpatterns = [
    path('music/', views.SongList.as_view()),
    path('music/<int:pk>', views.SongDetails.as_view()),
    path('music/add_like/<int:pk>', views.SongAddLike.as_view())
]