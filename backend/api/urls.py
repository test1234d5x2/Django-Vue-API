"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/stable/topics/http/urls/
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
from django.urls import path
from .views import get_data, delete_data, add_data, update_data


urlpatterns = [
    # API entry points should be defined here
    path("allElements", get_data, name="Get Data"),
    path("addData/<str:type>", add_data, name="Add Data"),
    path("deleteData/<str:type>/<int:id>", delete_data, name="Delete Data"),
    path("updateData<str:type>/<int:id>", update_data, name="Update Data"),
]
