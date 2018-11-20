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

from MMB.views import Start, MembersView, MemberView, BandsView, BandView, LogoutView, registration, login, TitlesView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', Start.as_view()),
    url(r'^member/$', MembersView.as_view()),
    url(r'^member/(?P<id>\d+)$', MemberView.as_view(), name='member_url'),
    url(r'^band/$', BandsView.as_view()),
    url(r'^band/(?P<id>\d+)$', BandView.as_view(), name='band_url'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', login),
    path('registration/', registration),
    path('start/', TitlesView.as_view())
]
