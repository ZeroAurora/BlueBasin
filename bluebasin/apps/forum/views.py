from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from bluebasin.apps.identity.models import Identity
from bluebasin.apps.admin.models import Report

from .forms import CreatePostForm, ReplyPostForm, ReportPostForm
from .models import Post


def index(request: HttpRequest):
    page = request.GET.get("page", 1)
    size = request.GET.get("size", 10)
    order_by = request.GET.get("order_by", "-last_replied_at")
    posts = Paginator(Post.get_index_posts(order_by), size).get_page(page)

    return render(request, "forum/index.html", {"posts": posts})


def posts_index(request: HttpRequest):
    return redirect("forum_index")


@login_required
def posts_create(request: HttpRequest):
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid() and (author := request.session.get("identity")):
            post = Post(
                author=Identity.objects.get(pk=author),
                title=form.cleaned_data["title"],
                content=form.cleaned_data["content"],
            )
            post.save()
            return redirect("forum_posts_view", post_id=post.id)
        else:
            return HttpResponseBadRequest()

    return render(request, "forum/posts_create.html")


def posts_view(request: HttpRequest, post_id: int):
    if request.method == "POST":
        form = ReplyPostForm(request.POST)
        if form.is_valid() and (author := request.session.get("identity")):
            post = Post(
                author=Identity.objects.get(pk=author),
                content=form.cleaned_data["content"],
                parent=Post.objects.get(pk=post_id),
            )
            post.save()
        else:
            return HttpResponseBadRequest()

    post = Post.objects.get(pk=post_id)
    page = request.GET.get("page", 0)
    size = request.GET.get("size", 10)
    replies = Paginator(Post.get_replies(post_id), size).get_page(page)
    return render(request, "forum/posts_view.html", {"post": post, "replies": replies})

@login_required
def posts_report(request: HttpRequest, post_id: int):
    if request.method == "POST":
        form = ReportPostForm(request.POST)
        if form.is_valid():
            report = Report(
                author=request.user,
                type=form.cleaned_data["type"],
                detail=form.cleaned_data["detail"],
                origin=Post.objects.get(pk=post_id),
            )
            report.save()
            messages.info(request, "report:success")
        else:
            return HttpResponseBadRequest()

    post = Post.objects.get(pk=post_id)
    return render(request, "forum/posts_report.html", {"post": post})
