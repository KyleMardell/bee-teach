from django.shortcuts import render
from django.views import generic
from .models import Resource


# Create your views here.
class ResourceList(generic.ListView):
    queryset = Resource.objects.all()
    template_name = "resource_list.html"