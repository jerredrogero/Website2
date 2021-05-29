from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, "blog/home.html", {"title": "Home"})


def projects(request):
    return render(request, "blog/projects.html", {"title": "Projects"})


def bookshelf(request):
    return render(request, "blog/bookshelf.html", {"title": "Bookshelf"})


def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts, "title": "Blog"})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect("post_detail", slug=post.slug)
    else:
        form = CommentForm()

    return render(request, "blog/post_detail.html", {"post": post, "form": form})


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(
        request,
        "blog/category.html",
        {"cats": cats.title(), "category_posts": category_posts},
    )

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(CategoryView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
