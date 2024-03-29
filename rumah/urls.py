"""rumah URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

urlpatterns = [
    path('', include('apps.base.urls', namespace='base')),
    path('office/', include('apps.office.urls', namespace='office')),
    path('office/categories/', include('apps.backoffice.categories.urls', namespace='categories')),
    path('office/location/', include('apps.backoffice.location.urls', namespace='location')),
    path('office/listing/', include('apps.backoffice.listing.urls', namespace='listing')),
    path('admin/', admin.site.urls),
]
