from .models import Comment, Resource, Media
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ('title', 'key_stage', 'content', 'links', 'status',)

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ('featured_media',)