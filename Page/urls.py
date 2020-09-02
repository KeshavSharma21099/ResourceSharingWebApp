from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pid>/new-page/', views.new_page),
    path('<int:pid>/send-page/', views.send_page, name="send-page"),
    path('<int:pid>/delete-page/', views.delete_page, name="delete-page"),
    path('instant-share/', views.instant_share, name='instant-share'),
]