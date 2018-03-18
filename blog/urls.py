"""blog URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
import posts.views
import sitepages.views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', posts.views.home, name="home"),
    
    # url(r'^contact/', posts.views.contact, name="contact"),
    url(r'^posts/(?P<posts_id>[0-9]+)/$', posts.views.posts_detail, name="posts_detail"),
    url(r'^about/', sitepages.views.about, name="about"),
    url(r'^contact/', sitepages.views.contact, name="contact"),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
