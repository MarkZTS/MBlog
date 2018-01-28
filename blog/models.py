from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    '''用户模型'''
    avatar = models.ImageField(upload_to="avatar/%Y/%m", default='avatar/defaule.png', max_length=200, verbose_name="用户头像")
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name="QQ号码")
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name="手机号")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Tag(models.Model):
    '''标签'''
    name = models.CharField(max_length=30, verbose_name="标签名称")
    # add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Catagory(models.Model):
    name = models.CharField(max_length=30, verbose_name="分类名称")
    index = models.IntegerField(default=999, verbose_name="分类的排序")
    # add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def get_post_nums(self):
        return self.article_set.all().count()

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 自定义一个文章Model的管理器
# 1、新加一个数据处理的方法
# 2、改变原有的queryset
class ArticleManager(models.Manager):
    def distinct_date(self):
        distinct_date_list = []
        date_list = self.values('date_publish')
        for date in date_list:
            date = date['date_publish'].strftime('%Y/%m文章存档')
            if date not in distinct_date_list:
                distinct_date_list.append(date)
        return distinct_date_list


class Article(models.Model):
    '''文章模型'''
    title = models.CharField(max_length=50, verbose_name="文章标题")
    desc = models.CharField(max_length=128, verbose_name="文章描述")
    content = models.TextField(verbose_name='文章内容')
    image = models.ImageField(upload_to="post/%Y/%m", max_length=200, default="post/default.png", verbose_name="封面图")
    click_count = models.IntegerField(default=0, verbose_name="点击次数")
    is_recommend = models.BooleanField(default=False, verbose_name="是否推荐")
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    category = models.ForeignKey(Catagory, on_delete=models.CASCADE, blank=True, null=True, verbose_name="分类")
    tag = models.ManyToManyField(Tag, verbose_name="标签")

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __str__(self):
        return self.title


# 评论模型
class Comment(models.Model):
    content = models.TextField(verbose_name='评论内容')
    username = models.CharField(max_length=30, blank=True, null=True, verbose_name='用户名')
    email = models.EmailField(max_length=50, blank=True, null=True, verbose_name='邮箱地址')
    url = models.URLField(max_length=100, blank=True, null=True, verbose_name='个人网页地址')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='用户')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, blank=True, null=True, verbose_name='文章')
    pid = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='父级评论')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)

# 友情链接
class Links(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    description = models.CharField(max_length=200, verbose_name='友情链接描述')
    callback_url = models.URLField(verbose_name='url地址')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    index = models.IntegerField(default=999, verbose_name='排列顺序(从小到大)')

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.title

# 广告
class Ad(models.Model):
    title = models.CharField(max_length=50, verbose_name='广告标题')
    description = models.CharField(max_length=200,  verbose_name='广告描述')
    image_url = models.ImageField(upload_to='ad/%Y/%m', verbose_name='图片路径')
    callback_url = models.URLField(null=True, blank=True, verbose_name='回调url')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    index = models.IntegerField(default=999, verbose_name='排列顺序(从小到大)')

    class Meta:
        verbose_name = '广告'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.title