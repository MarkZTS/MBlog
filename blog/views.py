import markdown
from django.shortcuts import render
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic.base import View
from .models import Article, Catagory

# Create your views here.


class IndexView(View):
    '''
    首页
    '''
    def get(self, request):
        posts = Article.objects.all()
        hot_posts = Article.objects.all().order_by("-click_count")[:5]
        categorys = Catagory.objects.all()

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(posts, 5, request=request)

        page_posts = p.page(page)

        print((posts.count()//5))

        # 分页数
        pagination_num = posts.count()/5
        if pagination_num.is_integer():
            pagination_num = pagination_num
        else:
            pagination_num = int(pagination_num + 1)

        print("-", pagination_num)
        # 当前页
        page = int(page)
        if pagination_num > 5:
            if page < 4:
                show_num = range(2, 7)
            elif page < (posts.count()//5)-1:
                show_num = range(page-1, page+4)
            else:
                show_num = range((posts.count()//5)-3, (posts.count()//5)+2)
        else:
            show_num = range(2, 7)

        return render(request, 'index.html', {
            "posts": posts,
            "hot_posts": hot_posts,
            "categorys": categorys,
            "page_posts": page_posts,
            "show_num": show_num,
        })


class PostView(View):
    """
    文章
    """
    def get(self, request, post_id):

        post = Article.objects.get(id=int(post_id))
        # 增加点击量
        post.click_count += 1
        post.save()
        # 热门文章
        hot_posts = Article.objects.all().order_by("-click_count")[:5]
        # 分类
        categorys = Catagory.objects.all()

        # markdown格式
        post.content = markdown.markdown(post.content,
                                         extensions=[
                                             'markdown.extensions.extra',
                                             'markdown.extensions.codehilite',
                                             'markdown.extensions.toc',
                                         ])
        return render(request, 'post.html', {
            "post": post,
            "hot_posts": hot_posts,
            "categorys": categorys,
        })


class AboutView(View):
    """
    关于作者
    """
    def get(self, request):
        return render(request, "about.html", {})
