from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('root/', views.go_to_root, name="go-to-root"),
    path('register/', views.register, name="signup"),
    path('update-profile/', views.update_profile, name="updateprofile"),
    path('profile/<str:username>/', views.my_profile, name="myprofile"),
    path('view-profile/<int:pk>/', views.view_profile, name="viewprofile"),
    path('search-user/', views.find_user, name="search-user"),
]
