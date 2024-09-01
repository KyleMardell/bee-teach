from django.contrib import admin
from .models import Resource, Feature, Comment, Media
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Resource)
class ResourceAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'key_stage',)
    search_fields = ['title']
    list_filter = ('status', 'key_stage',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


admin.site.register(Feature)
admin.site.register(Comment)
admin.site.register(Media)