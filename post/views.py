from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Resource


# Create your views here.
class ResourceList(generic.ListView):
    queryset = Resource.objects.filter(status=1)
    template_name = "post/index.html"
    paginate_by = 6


def resource_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Resource.objects.filter(status=1)
    resource = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "post/resource_detail.html",
        {"resource": resource},
    )