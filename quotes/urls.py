from django.urls import path
from . import views

app_name = "quotes"

urlpatterns = [
    path('', views.main, name="root"),
    path('<int:page>', views.main, name="root_paginate"),
    path('author/<int:author_id>', views.author, name="about_author"),
    path('tag/<str:tag_name>/', views.by_tag, name="by_tag"),
    path('add_quote/', views.upload, name="add_quote"),
    path('add_author/', views.load_author, name="add_author"),
]
