"""DZ1 URL Configuration

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

from MMB.views import MembersView, MemberView, BandsView, BandView, registration, login, TitlesView, \
    logoutView, ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', login),
    url(r'^member/$', MembersView.as_view()),
    url(r'^member/(?P<id>\d+)$', MemberView.as_view(), name='member_url'),
    url(r'^band/page=(?P<page>\d+)', BandsView.as_view()),
    url(r'^band/(?P<id>\d+)$', BandView.as_view(), name='band_url'),
    url(r'^logout/', logoutView, name='logout'),
    url(r'^login/', login),
    url(r'^registration/', registration),
    url(r'^start/', TitlesView.as_view()),
    url(r'^profile/', ProfileView.as_view())
    # url(r'^me/', CustomerInDetail.as_view(), name='customers_detail')
]
