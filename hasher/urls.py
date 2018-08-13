"""hasher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from myapp.views import *
from .settings import MEDIA_ROOT, DEBUG
from django.views.static import serve
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main, name="home"),
    url(r'^profile/(?P<pk>\d+)/$', UserProfileView.as_view(), name="profile"),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^users/logout/$', auth_views.logout,
        kwargs={'next_page': 'home'},
        name='auth_logout'),

]

if DEBUG:
    # serve files from media folder
    urlpatterns += [
                    url(r'^media/(?P<path>.*)$', serve,
                    {'document_root': MEDIA_ROOT})]