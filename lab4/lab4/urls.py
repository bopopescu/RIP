"""lab4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from my_app.views import CoffeesView, CoffeeView, base, SyrupsView, SyrupView

urlpatterns = [
    url(r'^$', base),  # ВАЖНО
    url(r'^coffee/$', CoffeesView.as_view(), name="coffees_url"),
    url(r'^coffee/(?P<id>\d+)$', CoffeeView.as_view(), name="coffee_url"),
    url(r'^syrup/$', SyrupsView.as_view(), name="syrups_url"),
    url(r'^syrup/(?P<id>\d+)$', SyrupView.as_view(), name="syrup_url"),
    path('admin/', admin.site.urls),
]
