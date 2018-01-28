import markdown
from django.shortcuts import render

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
        print(categorys)
        return render(request, 'index.html', {
            "posts": posts,
            "hot_posts": hot_posts,
            "categorys": categorys,
        })


class PostView(View):
    """
    文章
    """
    def get(self, request, post_id):
        post = Article.objects.get(id=int(post_id))
        post.click_count += 1
        post.save()


        # markdown格式
        post.content = markdown.markdown(post.content,
                                         extensions=[
                                             'markdown.extensions.extra',
                                             'markdown.extensions.codehilite',
                                             'markdown.extensions.toc',
                                         ])
        return render(request, 'post.html', {
            "post": post,
        })


class AboutView(View):
    """
    关于作者
    """
    def get(self, request):
        return render(request, "about.html", {})
