"""MBlog URL Configuration

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
import xadmin
from django.views.static import serve

from blog.views import IndexView, PostView, AboutView, ArchiveView, CategoryView, CategoryPostView
from .settings import MEDIA_ROOT, STATIC_ROOT

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', IndexView.as_view(), name="index"),
    # 文章详情页
    url(r'^post/(?P<post_id>\d+)/$', PostView.as_view(), name="post"),
    # 关于作者
    url(r'^about/$', AboutView.as_view(), name="about"),
    # 登陆
    url(r'^login/$', AboutView.as_view(), name="login"),
    # 注册
    url(r'^register/$', AboutView.as_view(), name="register"),
    # 归档
    url(r'^archives/$', ArchiveView.as_view(), name="archives"),
    # 分类
    url(r'^categories/$', CategoryView.as_view(), name="categories"),

    url(r'^static/(?P<path>.*)$', serve, {"document_root":STATIC_ROOT}),

    # 同种分类文章
    url(r'^category/(?P<category_id>\d+)/$', CategoryPostView.as_view(), name="category_post"),



    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),
]

# 全局404页面配置
handler404 = 'blog.views.page_not_found'
