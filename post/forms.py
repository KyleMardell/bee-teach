from .models import Comment, Resource, Media
from django import forms
from django_summernote.widgets import SummernoteWidget


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

    def clean_featured_media(self):
        media = self.cleaned_data.get('featured_media')
        
        if media and not media.content_type.startswith('image'):
            raise forms.ValidationError("Only image files are allowed.")

        return media