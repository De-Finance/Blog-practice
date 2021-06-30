from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
    # (기존 CBV 방법)
    # path('', views.index),
    # path('<int:pk>/', views.single_post_page),
]