from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Resource, Media, Feature
from .forms import CommentForm, ResourceForm, MediaForm


def home_page(request):
    queryset = Resource.objects.filter(status=1).order_by("-created_on")
    resources = queryset[:4]
    images = Media.objects.filter(resource__in=resources)
    template_name = "post/index.html"

    return render(
        request,
        template_name,
        {"resources": resources, "images": images}
    )


@login_required
def resource_list(request):
    resources = Resource.objects.filter(status=1)
    features = Feature.objects.all()

    paginator = Paginator(resources, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if page_number:
        return render(request, 'post/partials/resource_list.html', {'page_obj': page_obj})

    template_name = "post/resource_list.html"
    return render(
        request,
        template_name,
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
def resource_create(request):

    if request.method == 'POST':
        resource_form = ResourceForm(request.POST)
        media_form = MediaForm(request.POST, request.FILES)
        
        if resource_form.is_valid() and media_form.is_valid():
            resource = resource_form.save(commit=False)
            resource.slug = slugify(resource.title)
            resource.author = request.user
            resource.save()

            media = media_form.save(commit=False)
            media.resource = resource
            media.save()

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