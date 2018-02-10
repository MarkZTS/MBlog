import markdown
from django.shortcuts import render
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic.base import View
from .models import Article, Catagory, AboutMe

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
        print(post)
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
        about = AboutMe.objects.get(id=1)
        print(about)
        # markdown格式
        about.desc = markdown.markdown(about.desc,
                                         extensions=[
                                             'markdown.extensions.extra',
                                             'markdown.extensions.codehilite',
                                             'markdown.extensions.toc',
                                         ])
        return render(request, "about.html", {"about":about})


class ArchiveView(View):
    """
    归档
    """
    def get(self, request):
        all_posts = Article.objects.all()
        all_posts_nums = all_posts.count()
        all_years = []
        for i in all_posts:
            all_years.append(i.date_publish.year)
        years = set(all_years)
        print(years)
        return render(request, 'archives.html', {
            "all_posts":all_posts,
            "all_posts_nums":all_posts_nums,
            "years":years

        })


class CategoryView(View):
    '''
    分类
    '''
    def get(self, request):
        categories = Catagory.objects.all()
        category_nums = categories.count()
        return render(request, 'catagory.html', {
            "category_nums":category_nums,
            "categories":categories,
        })


class CategoryPostView(View):
    '''
    同种分类文章
    '''
    def get(self, request, category_id):

        hot_posts = Article.objects.all().order_by("-click_count")[:5]
        categorys = Catagory.objects.all()

        posts = Article.objects.filter(category_id=category_id)

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(posts, 5, request=request)

        page_posts = p.page(page)

        print((posts.count() // 5))

        # 分页数
        pagination_num = posts.count() / 5
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
            elif page < (posts.count() // 5) - 1:
                show_num = range(page - 1, page + 4)
            else:
                show_num = range((posts.count() // 5) - 3, (posts.count() // 5) + 2)
        else:
            show_num = range(2, 7)

        return render(request, 'index.html', {
            "posts": posts,
            "hot_posts": hot_posts,
            "categorys": categorys,
            "page_posts": page_posts,
            "show_num": show_num,
        })

def page_not_found(request):
    # 全局404处理函数
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response

