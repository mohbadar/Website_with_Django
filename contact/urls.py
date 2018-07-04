"""noc_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.urls import path , include

from . import views


urlpatterns = [
    path('', views.support, name='support'),
    path('support_save/', views.support, name='support_save'),
    path('members/', views.members , name = 'members'),
    path('about/', views.about , name = 'about'),
    path('archicture/', views.archicture , name = 'archicture'),


]
