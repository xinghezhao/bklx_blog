# _*_ coding:utf-8 _*_
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
# from django.views.static import serve

from blog.views import get_blogs, blogs_detail, blogs_person, person_detail, timeline,aboutme

from django.conf import settings
from django.conf.urls.static import static
#用户处理静态文件
from django.views.generic import TemplateView

# from mysite.settings import MEDIA_ROOT


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_blogs, name='index'),
    url(r'^blogs/(\d+)/$', blogs_detail, name='blogs'),

    url(r'^person/$', blogs_person, name='person'),
    url(r'^person/(\d+)/$', person_detail, name='person_id'),
    url(r'^timeline/$', timeline, name='timeline'),
    url(r'^aboutme/$', aboutme, name='aboutme'),

    # # 配置上传文件的访问函数
    # url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),



]
