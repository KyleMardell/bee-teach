from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Resource, Media


# Create your views here.
class ResourceList(generic.ListView):
    queryset = Resource.objects.filter(status=1)
    template_name = "post/index.html"
    paginate_by = 6


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