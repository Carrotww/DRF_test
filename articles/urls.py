from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.articleAPI, name='index'),
    path("<int:article_id>/", views.articleDetailAPI, name="article_view"),
]
