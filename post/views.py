from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils.text import slugify
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Resource, Media, Feature, Comment
from .forms import CommentForm, ResourceForm, MediaForm


def home_page(request):
    queryset = Resource.objects.filter(status=1).order_by("-created_on")
    resources = queryset[:4]
    images = Media.objects.filter(resource__in=resources)

    return render(
        request,
        "post/index.html",
        {"resources": resources, "images": images}
    )


@login_required
def resource_list(request):
    resources = Resource.objects.filter(status=1)
    features = Feature.objects.all()

    paginator = Paginator(resources, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if page_number:
        return render(request, 'post/partials/resource_list.html', {'page_obj': page_obj})

    return render(
        request,
        "post/resource_list.html",
        {"page_obj": page_obj, "features": features},
    )


@login_required
def resource_detail(request, slug):
    """
    Display an individual :model:`post.Resource`.

    **Context**

    ``resource``
        An instance of :model:`post.Resource`.

    **Template:**

    :template:`post/resource_detail.html`
    """

    queryset = Resource.objects.filter(status=1)
    resource = get_object_or_404(queryset, slug=slug)
    images = Media.objects.filter(resource=resource.id)
    comments = resource.comments.all().order_by("-created_on")
    comment_count = comments.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.resource = resource
            comment.save()
            
            messages.success(request, "Comment Added")

    comment_form = CommentForm()

    return render(
        request,
        "post/resource_detail.html",
        {
            "resource": resource,
            "images": images,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


@login_required
def resource_preview(request, slug):
    queryset = Resource.objects.filter(author=request.user)
    resource = get_object_or_404(queryset, slug=slug)
    images = Media.objects.filter(resource=resource.id)

    return render(
        request,
        "post/resource_preview.html",
        {
            "resource": resource,
            "images": images,
        },
    )


@login_required
def resource_create(request):

    if request.method == 'POST':
        resource_form = ResourceForm(request.POST)
        media_files = request.FILES.getlist('featured_media')
        
        if resource_form.is_valid():
            resource = resource_form.save(commit=False)
            resource.slug = slugify(resource.title)
            resource.author = request.user
            resource.save()
            
            for media_file in media_files:
                Media.objects.create(resource=resource, featured_media=media_file)

            if resource.status == 1:
                messages.success(request, "Resource Posted")
                return redirect('resource_detail', slug=resource.slug)
            else:
                messages.success(request, "Resource Draft Created (Publish your post from the 'My Resources' Page)")
                return redirect('user_posts_list')

    resource_form = ResourceForm()
    media_form = MediaForm()

    return render(
        request,
        "post/resource_create.html",
        {
            "resource_form": resource_form,
            "media_form": media_form,
        },
    )

@login_required
def comment_edit(request, slug, comment_id):
    if request.method == "POST":

        queryset = Resource.objects.filter(status=1)
        resource = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.resource = resource
            comment.save()
            messages.success(request, "Comment updated")
        else:
            messages.error(request, "Error updating")

    return HttpResponseRedirect(reverse('resource_detail', args=[slug]))


@login_required
def user_posts_list(request):

    user_resources = Resource.objects.filter(author=request.user)
    resource_form = ResourceForm()

    return render(
        request,
        "post/user_posts_list.html",
        {
            "user_resources": user_resources,
            "resource_form": resource_form,
        },
    )


@login_required
def resource_edit(request, slug, resource_id):
    if request.method == "POST":

        resource = get_object_or_404(Resource, pk=resource_id)
        media_files = request.FILES.getlist('featured_media')

        if resource.author == request.user:
            resource_form = ResourceForm(data=request.POST, instance=resource)

        if resource_form.is_valid() and resource.author == request.user:
            resource = resource_form.save(commit=False)
            resource.slug = slugify(resource.title)
            resource.save()
            
            for media_file in media_files:
                Media.objects.create(resource=resource, featured_media=media_file)

            messages.success(request, "Resource Updated")
            return redirect('user_posts_list')

        else:
            messages.error(request, "Error updating")
            
            
