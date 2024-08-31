from django.contrib import admin
from .models import Resource, Feature, Comment, Media

# Register your models here.
admin.site.register(Resource)
admin.site.register(Feature)
admin.site.register(Comment)
admin.site.register(Media)