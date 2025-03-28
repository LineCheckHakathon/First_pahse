"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # User API endpoints
    path('api/users/', views.user_list, name='user_list'),             # GET all users
    path('api/users/<int:user_id>/', views.get_user, name='get_user'), # GET specific user
    path('api/users/create/', views.user_create, name='user_create'),   # POST create user
    path('api/users/<int:user_id>/update/', views.update_user, name='update_user'), # PUT update user
    path('api/users/<int:user_id>/patch/', views.patch_user, name='patch_user'),    # PATCH update user
    path('api/users/<int:user_id>/delete/', views.delete_user, name='delete_user'), # DELETE user
]