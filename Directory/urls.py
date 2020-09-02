from django.urls import path
from . import views

urlpatterns = [
    path("<int:pid>/", views.view_directories, name="view-directories"),
    path("<int:pid>/create-directory/", views.create_directory, name="create-directory"),
    path("<int:pid>/send-directory/", views.send_directory, name="send-directory"),
    path("<int:pid>/delete-directory/", views.delete_directory, name="delete-directory"),
    path("<int:pid>/edit-directory/", views.update_directory, name="edit-directory"),
]