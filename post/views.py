from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Resource, Media


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

    template_name = "post/resource_list.html"
    
    return render(
        request,
        template_name,
        {"resources": resources, "features": features},
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

    return render(
        request,
        "post/resource_detail.html",
        {"resource": resource, "images": images},
    )