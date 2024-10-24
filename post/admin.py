from django.contrib import admin
from .models import Resource, Feature, Comment, Media
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Resource)
class ResourceAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'key_stage', 'created_on')
    search_fields = ['title', 'content', ]
    list_filter = ('status', 'key_stage', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

@admin.register(Feature)
class FeatureAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Comment)
admin.site.register(Media)
