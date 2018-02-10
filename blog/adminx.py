#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  : 2018/1/26 10:46
# @Author : ZTS
# @Software: PyCharm

import xadmin
from xadmin import views

from .models import Article, Tag, Comment, Catagory, Links, Ad, AboutMe


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = "ZTSong's Blog 后台管理"
    site_footer = "ZTSong"
    menu_style = "accordion"


class ArticleAdmin(object):
    list_display = ['title', 'desc', 'content', 'click_count', 'is_recommend', 'user', 'category', 'tag', 'date_publish']
    search_fields = ['title', 'desc', 'content', 'click_count', 'is_recommend', 'user', 'category', 'tag']
    list_filter = ['title', 'desc', 'content', 'click_count', 'is_recommend', 'user', 'category', 'tag', 'date_publish']


class TagAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name',]
    list_filter = ['name', 'add_time']


class CommentAdmin(object):
    list_display = ['content', 'username', 'email', 'url', 'user', 'article', 'pid', 'date_publish']
    search_fields = ['content', 'username', 'email', 'url', 'user', 'article', 'pid']
    list_filter = ['content', 'username', 'email', 'url', 'user', 'article', 'pid', 'date_publish']


class CatagoryAdmin(object):
    list_display = ['name', 'index', 'add_time']
    search_fields = ['name', 'index']
    list_filter = ['name', 'index', 'add_time']


class LinksAdmin(object):
    list_display = ['title', 'description', 'callback_url', 'index', 'date_publish']
    search_fields = ['title', 'description', 'callback_url', 'index']
    list_filter = ['title', 'description', 'callback_url', 'index', 'date_publish']


class AdAdmin(object):
    list_display = ['title', 'description', 'image_url', 'callback_url', 'index', 'date_publish']
    search_fields = ['title', 'description', 'image_url', 'callback_url', 'index']
    list_filter = ['title', 'description', 'image_url', 'callback_url', 'index', 'date_publish']


class AboutMeAdmin(object):
    list_display = ['desc', 'date_publish']
    search_fields = ['desc']
    list_filter = ['desc', 'date_publish']


xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Tag)
xadmin.site.register(Catagory)
xadmin.site.register(Comment, CommentAdmin)
xadmin.site.register(Ad, AdAdmin)
xadmin.site.register(Links, LinksAdmin)
xadmin.site.register(AboutMe, AboutMeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)