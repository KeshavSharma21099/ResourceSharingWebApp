"""gluepost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Profile import views as profile_views
from Page import views as page_views
from Directory import views as directory_views

router = routers.DefaultRouter()
router.register('api-profile', profile_views.ProfileViewSet)
router.register('api-page', page_views.PageViewSet)
router.register('api-directory', directory_views.DirectoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("django.contrib.auth.urls")),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include("Profile.urls")),
    path('', include("Directory.urls")),
    path('', include("Page.urls")),
]
