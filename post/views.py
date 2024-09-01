from django.shortcuts import render
from django.views import generic
from .models import Resource


# Create your views here.
class ResourceList(generic.ListView):
    queryset = Resource.objects.filter(status=1)
    template_name = "post/index.html"
    paginate_by = 6